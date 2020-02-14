package main

import (
	"encoding/json"
	"log"
	"net/http"
	"time"

	"github.com/go-redis/redis"
)

type Runners struct {
	ID    string `json:"id"`
	Token string `json:"token"`
	Email string `json:"email"`
}
type Race struct {
	ID          string    `json:"id"`
	Ruta        string    `json:"ruta"`
	CreatedOf   string    `json:"created_of"`
	RunnersRace []Runners `json:"runners"`
	//conf the date dateOf       `json :"date_of"`
}

func (c *RedisClient) AddRacers(key string, runners []Runners) {
	key = key + ":" + "racers"
	for i := 0; i < len(runners); i++ {
		c.SAdd(
			key,
			runners[i].Email,
			runners[i].Token,
		)
	}
}

func (c *RedisClient) EventRaceAndRute(keyRace string, routeId string, duration time.Duration) {
	vars := []string{":route", ":event"}
	c.Set(keyRace+vars[0], routeId, duration)
	c.Set(keyRace+vars[1], "Event Active", duration)
}
func (c *RedisClient) GetEvent(keyRace string) string {
	race := keyRace + ":event"
	event, err := c.Get(race).Result()
	log.Println(race, event, err)
	return event
}

func (c *RedisClient) GetRunners(idRace string) []string {
	idRace = idRace + ":" + "racers"

	x, _ := c.SMembers(idRace).Result()
	return x
}

func (c *RedisClient) AddRacersLocation(idRace string, lat float64, lng float64) {
	idRace = idRace + ":racerslocation"
	c.AddUserLocation(idRace, lat, lng)
}

func (c *RedisClient) GetRacers(idRace string, lat float64, lng float64) []redis.GeoLocation {
	idRace = idRace + ":racerslocation"
	racers := c.SearchUsers(600, lat, lng, 20.0)
	log.Println("get racers ", racers)

	return racers

}

func NewRace(w http.ResponseWriter, r *http.Request) {
	var RaceData Race
	clientpsql := ClientPsql()

	if err := json.NewDecoder(r.Body).Decode(&RaceData); err != nil {
		log.Println("error decoding json into racedata '%v'", err)
	}
	//verification of users and creation
	var racer = struct {
		IsActive bool   `sql:"is_active"`
		Token    string `sql:"token"`
	}{}

	for i := 0; i < len(RaceData.RunnersRace); i++ {
		racer.IsActive = false
		clientpsql.Raw("select users_user.is_active  , authtoken_token.key as token from users_user inner join authtoken_token  on users_user.id = authtoken_token.user_id where  users_user.email = ?;  ",
			RaceData.RunnersRace[i].Email).Scan(&racer)

		if racer.IsActive == false {
			log.Println("runner is not active or not exist")
			w.Header().Set("Content-Type", "aplication/json")
			w.WriteHeader(http.StatusBadRequest)
			break
		}

		RaceData.RunnersRace[i].Token = racer.Token

	}

	clientredis := GetRedisClient()

	//add racers in redis db

	clientredis.AddRacers(RaceData.ID, RaceData.RunnersRace)
	durationRace, _ := time.ParseDuration("20m")                           //duration of the race in redis
	clientredis.EventRaceAndRute(RaceData.ID, RaceData.Ruta, durationRace) //create event race
	w.Header().Set("Content-Type", "aplication/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(&RaceData)

}
