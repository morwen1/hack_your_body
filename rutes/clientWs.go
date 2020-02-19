package main

import (
	"net/url"

	"github.com/gorilla/websocket"
)

//structure between websocket and urls
// for best control of messages
type CLientTemp struct {
	wsClient  *websocket.Conn
	urlClient *url.URL
	IdRace    string
	TokenUSer string
}
