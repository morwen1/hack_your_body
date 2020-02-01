package main

import (
	"log"
	"net/http"

	"github.com/gorilla/websocket"
)

var clients = make(map[*websocket.Conn]bool) //clients

var upgrader = websocket.Upgrader{
	ReadBufferSize:  1024,
	WriteBufferSize: 1024,
}

//modelos del mensaje message {request : {posclient , route} , response :{posclient  , point  }
type Response struct {
	PosClient    float64 `json:"posclient"`
	Point        float64 `json:"point"`
	CloseRunners int     `json:"closerunners"`
}
type Request struct {
	PosClient float64 `json:"posclient"`
	RouteName string  `json:"route"`
}

type Message struct {
	ID              string   `json:"id"`
	RequestMessage  Request  `json:"request"`
	ResponseMessage Response `json:"response"`
}

var message = make(chan Message)

func HandleConnections(w http.ResponseWriter, r *http.Request) {
	ws, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		log.Println("error while try to read request %v", err)
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
		message <- msg
	}
}
