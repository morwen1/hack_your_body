package main

import (
	"log"
	"sync"

	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"

	"github.com/go-redis/redis"
)

type RedisClient struct{ *redis.Client }

var once sync.Once
var redisClient *RedisClient

func GetRedisClient() *RedisClient {
	once.Do(func() {
		client := redis.NewClient(&redis.Options{
			Addr:     "localhost:6379",
			Password: "",
			DB:       7,
		})
		redisClient = &RedisClient{client}

	})
	_, err := redisClient.Ping().Result()

	if err != nil {
		log.Fatalf("Could not connect to redis %v", err)
	}
	return redisClient

}

func ClientPsql() *gorm.DB {

	db, err := gorm.Open("postgres", "host=0.0.0.0 port=6500 user=debug dbname=hyk password=debug sslmode=disable")
	if err != nil {
		log.Println("error to connect to postgres db :", err)

	}
	db.SingularTable(true)
	db.LogMode(true)
	return db

}
