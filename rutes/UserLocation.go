package main

import (
	"github.com/go-redis/redis"
)

const key = "Users"

func (c *RedisClient) AddUserLocation(id string, lat, lng float64) {
	c.GeoAdd(
		key,
		&redis.GeoLocation{
			Latitude:  lat,
			Longitude: lng,
			Name:      id},
	)

}

func (c *RedisClient) DeleteUserLocation(id string) {

	c.ZRem(key, id)

}

func (c *RedisClient) SearchUsers(limit int, lat, lng float64, radius float64) []redis.GeoLocation {
	//search all close users
	res, _ := c.GeoRadius(key, lat, lng, &redis.GeoRadiusQuery{
		Radius:      radius,
		Unit:        "km",
		WithGeoHash: true,
		WithCoord:   true,
		Count:       limit,
		Sort:        "ASC",
	}).Result()

	return res

}

func (c *RedisClient) Tracking(id string) []*redis.GeoPos {
	res, _ := c.GeoPos(key, id).Result()
	return res
}
