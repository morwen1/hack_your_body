package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/go-redis/redis"

	"github.com/gorilla/mux"

	"github.com/gorilla/websocket"
)

var clients = make(map[*websocket.Conn]bool) //clients

var upgrader = websocket.Upgrader{
	ReadBufferSize:  1024,
	WriteBufferSize: 1024,
}

//modelos del mensaje message {request : {posclient , route} , response :{posclient  , point  }
type PosClient struct {
	Lat float64 `json:"lat"`
	Lng float64 `json:"lng"`
}
type Response struct {
	PosRacers    []redis.GeoLocation `json:"posclient"`
	Point        float64             `json:"point"`
	CloseRunners int                 `json:"closerunners"`
}
type Request struct {
	PosClient PosClient `json:"posclient"`
	RouteName string    `json:"route"`
}

type Message struct {
	ID              string   `json:"id"`
	RequestMessage  Request  `json:"request"`
	ResponseMessage Response `json:"response"`
}

var message = make(chan Message)

func HandleConnections(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)

	//connect with redis and obtain all the tokens
	idRace := vars["id_race"]
	token := vars["token"]
	clientredis := GetRedisClient()
	racers := clientredis.GetRunners(idRace)

	//verify the tokens in the request
	found := false
	for _, i := range racers {
		if i == token {
			found = true
		}

	}

	ws, err := upgrader.Upgrade(w, r, nil)
	//log.Println(found, token, idRace, racers)
	if found == false {
		ws.Close()
	}

	log.Println(" WS connection")
	if err != nil {
		log.Println("error while try to read request , error:", err)
	}
	defer ws.Close()

	clients[ws] = true
	for {
		var msg Message
		err := ws.ReadJSON(&msg)
		if err != nil {
			log.Println("error while read json request %v", err)
			delete(clients, ws)
			break
		}
		clientredis.AddRacersLocation(idRace, msg.RequestMessage.PosClient.Lat, msg.RequestMessage.PosClient.Lng)
		racers := clientredis.GetRacers(idRace, msg.RequestMessage.PosClient.Lat, msg.RequestMessage.PosClient.Lng)
		msg.ResponseMessage.PosRacers = racers
		msg.ResponseMessage.CloseRunners = len(racers)
		fmt.Println(msg)
		message <- msg
	}

}

func HandleMessage() {

	for {
		msg := <-message

		for client := range clients {

			err := client.WriteJSON(msg)

			if err != nil {
				log.Println("error sendig msg %v", err)
				client.Close()
				delete(clients, client)
			}

		}
	}
}
