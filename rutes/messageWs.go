package main

import "github.com/go-redis/redis"

//Structures to Wsendpoint

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

//example of message
//{"id": "carrera1","request": {"posclient": {"lat":36.176544,"lng" :36.176544} ,"route": "ruta1"},"response": {}}

//example of message with response
//{"id":"carrera1","request":{"posclient":{"lat":36.176544,"lng":36.176544},"route":"ruta1"},"response":{"posclient":[{"Name":"carrera1:racerslocation","Longitude":36.17654353380203,"Latitude":36.17654286830403,"Dist":0,"GeoHash":3511195763862117}}
