package main

import (
	"fmt"
	"log"
	"net/http"
	"sync"

	"github.com/gorilla/mux"

	"github.com/gorilla/websocket"
)

var clients = make(map[*CLientTemp]bool) //clients
var pool sync.Pool

var upgrader = websocket.Upgrader{
	ReadBufferSize:  1024,
	WriteBufferSize: 1024,
	WriteBufferPool: &pool,
}

//modelos del mensaje message {request : {posclient , route} , response :{posclient  , point  }

var message = make(chan Message)

func HandleConnections(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	log.Println(r.URL)

	//connect with redis and obtain all the tokens and the users
	idRace := vars["id_race"]
	token := vars["token"]
	clientredis := GetRedisClient()
	event := clientredis.GetEvent(idRace)

	racers := clientredis.GetRunners(idRace)

	//verify the users tokens in the request
	found := false
	for _, i := range racers {
		if i == token {
			found = true
		}

	}

	//creating the upgrader
	ws, err := upgrader.Upgrade(w, r, nil)
	urlClient := r.URL
	clientConn := &CLientTemp{wsClient: ws, urlClient: urlClient, IdRace: idRace, TokenUSer: token}
	// verify the user token and event
	if found == false || event != "Event Active" {
		ws.Close()
	}

	if err != nil {
		log.Println("error while try to read request , error:", err)
	}
	defer ws.Close()

	log.Println(" WS connection succesfull")

	clients[clientConn] = true //add to map clients new client

	for {

		var msg Message
		err := ws.ReadJSON(&msg)
		if err != nil {
			log.Println("error while read json request %v", err)
			delete(clients, clientConn)
			break
		}
		clientredis.AddRacersLocation(idRace, msg.RequestMessage.PosClient.Lat, msg.RequestMessage.PosClient.Lng)
		racers := clientredis.GetRacersLocation(idRace, msg.RequestMessage.PosClient.Lat, msg.RequestMessage.PosClient.Lng)
		msg.ResponseMessage.PosRacers = racers
		msg.ResponseMessage.CloseRunners = len(racers)
		fmt.Println("message request ", msg)
		message <- msg //sending the mesage to the handler message
	}

}

//handler manage messages between clients and evita
func HandleMessage() {

	for {
		msg := <-message

		for client := range clients {
			if msg.ID == client.IdRace {
				err := client.wsClient.WriteJSON(msg)
				if err != nil {
					log.Println("error sendig msg %v", err)
					client.wsClient.Close()
					delete(clients, client)
				}

			}

		}
	}
}
