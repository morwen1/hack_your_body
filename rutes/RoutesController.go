package main

import (
	"encoding/json"
	"log"
	"net/http"
)

func AddRoutes(w http.ResponseWriter, r *http.Request) {
	var routes Route
	//fmt.Println(r.Body, "body")
	//		  | this is for decode the request       |
	if err := json.NewDecoder(r.Body).Decode(&routes); err != nil {
		log.Println("error decoding %v", err)
		http.Error(w, "mano no puedo lee esa vaina", http.StatusBadRequest)

	}
	//create route
	rClient := GetRedisClient()
	rClient.CreateRute(routes)

	//response
	w.Header().Set("Content-Type", "aplication/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(&routes) //Response de data created

	return

}
