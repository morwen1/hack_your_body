package main

import (
	"github.com/go-redis/redis"
)

type Route struct {
	Name   string  `json:"id"`
	Points []Point `json:"points"`
}

type Point struct {
	ID  string  `json:"id"`
	Lat float64 `json:"lat"`
	Lng float64 `json:"lng"`
}

func (c *RedisClient) CreateRute(route Route) {
	//creating route in redis
	for i := 0; i < len(route.Points); i++ {
		c.GeoAdd(
			route.Name,
			&redis.GeoLocation{
				Latitude:  route.Points[i].Lat,
				Longitude: route.Points[i].Lng,
				Name:      route.Points[i].ID,
			},
		)
	}
}
