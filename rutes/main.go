package main

import (
	"fmt"
	"log"
	"time"
)

func main() {

	client := GetRedisClient()
	fmt.Println(client, "client redis up")
	clientpsql := ClientPsql()
	fmt.Println(clientpsql, "client psql up")
	r := Router()
	server := Server(r, "0.0.0.0:8010")

	go server.ListenAndServe()
	log.Println("running server....")
	go HandleMessage()
	for {
		logsCmd := "listening"

		log.Println(logsCmd)
		time.Sleep(1 * time.Minute)
		if logsCmd == "listening......" {
			logsCmd = "listening"
		} else {
			logsCmd = logsCmd + "."
		}

	}

}
