package main

import (
	"github.com/gorilla/mux"
)

func Router() *mux.Router {

	r := mux.NewRouter().StrictSlash(false)
	r.HandleFunc("/addloc", AddLocationUser).Methods("POST", "PUT")
	r.HandleFunc("/routes", AddRoutes).Methods("POST", "PUT")
	r.HandleFunc("/tracking_id", TrackingLocation).Methods("POST")
	r.HandleFunc("/searchusers", SearchUserLocation).Methods("POST")
	r.HandleFunc("/deleteloc", DeleteLocationUser).Methods("DELETE")
	r.HandleFunc("/newrace", NewRace).Methods("Post")
	r.HandleFunc("/ws/{id_race}/{token}", HandleConnections) //websocket endpoint
	return r
}
