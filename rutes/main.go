package main

import "fmt"

func main() {

	client := GetRedisClient()
	fmt.Println(client)
	r := Router()
	server := Server(r, "0.0.0.0:8010")

	go server.ListenAndServe()

}
