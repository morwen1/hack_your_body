package main

import (
	"encoding/json"
	"log"
	"net/http"
)

func AddLocationUser(w http.ResponseWriter, r *http.Request) {
	var user = struct {
		ID  string  `json:"id"`
		Lat float64 `json:"lat"`
		Lng float64 `json:"lng"`
	}{}

	if err := json.NewDecoder(r.Body).Decode(&user); err != nil {
		log.Println("can not decode that request %v", err)
		http.Error(w, "mano no puedo lee esa vaina", http.StatusBadRequest)
		return

	}
	rClient := GetRedisClient()
	rClient.AddUserLocation(user.ID, user.Lat, user.Lng)
	return
	data, err := json.Marshal(user)
	if err != nil {
		http.Error(w, "mano mala mia pero el json ta caido XD", http.StatusInternalServerError)
		log.Println("mano mala mia pero el json ta caido XD")
		return
	}
	w.WriteHeader(http.StatusCreated)
	w.Header().Set("Content-Type", "aplication/json")
	w.Write(data)
	return
}

func DeleteLocationUser(w http.ResponseWriter, r *http.Request) {
	var body = struct {
		ID string `json:"id"`
	}{}
	rClient := GetRedisClient()

	if err := json.NewDecoder(r.Body).Decode(&body); err != nil {
		log.Println("can not decode that request %v", err)
		http.Error(w, "can not decode that request", http.StatusBadRequest)
		return
	}
	rClient.DeleteUserLocation(body.ID)
	w.WriteHeader(http.StatusOK)
	w.Header().Set("Content-Type", "aplication/json")
	json.NewEncoder(w).Encode(body)

}

func SearchUserLocation(w http.ResponseWriter, r *http.Request) {
	var body = struct {
		Limit int     `json : "limit"`
		Lat   float64 `json:"lat"`
		Lng   float64 `json:"lng"`
	}{}
	rClient := GetRedisClient()

	if err := json.NewDecoder(r.Body).Decode(&body); err != nil {
		log.Println("can not decode that request %v", err)
		http.Error(w, "can not decode that request", http.StatusBadRequest)
		return

	}
	datausers := rClient.SearchUsers(body.Limit, body.Lat, body.Lng, 15000)
	data, err := json.Marshal(datausers)
	if err != nil {
		http.Error(w, "mano mala mia pero el json ta caido XD", http.StatusInternalServerError)
		log.Println("mano mala mia pero el json ta caido XD")
		return
	}

	w.Header().Set("Content-Type", "aplication/json")
	w.WriteHeader(http.StatusOK)
	w.Write(data)
	return

}

func TrackingLocation(w http.ResponseWriter, r *http.Request) {
	var body = struct {
		ID string `json : "id"`
	}{}
	rClient := GetRedisClient()

	if err := json.NewDecoder(r.Body).Decode(&body); err != nil {
		log.Println("can not decode that request %v", err)
		http.Error(w, "can not decode that request", http.StatusBadRequest)
		return

	}
	datausers := rClient.Tracking(body.ID)

	data, err := json.Marshal(datausers)

	if err != nil {
		http.Error(w, "mano mala mia pero el json ta caido XD", http.StatusInternalServerError)
		log.Println("mano mala mia pero el json ta caido XD")
		return
	}

	w.Header().Set("Content-Type", "aplication/json")
	w.WriteHeader(http.StatusOK)
	w.Write(data)
	return

}
