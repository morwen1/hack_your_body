package main

import (
	"log"
	"time"
)

func main() {

	clientredis := GetRedisClient()
	clientpsql := ClientPsql()
	if clientredis != nil && clientpsql != nil {
		log.Println("client redis up")
		log.Println("client psql up")
	} else {
		log.Panic("databases not available")
	}
	r := Router()
	server := Server(r, "0.0.0.0:8010")

	go server.ListenAndServe()
	log.Println("running server....")
	go HandleMessage()
	logsCmd := "listening"
	for {
		log.Println(logsCmd)
		time.Sleep(3 * time.Minute)
		if logsCmd == "listening......" {
			logsCmd = "listening"
		} else {
			logsCmd = logsCmd + "."
		}

	}

}
