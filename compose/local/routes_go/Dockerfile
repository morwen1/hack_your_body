#traerse go
FROM Golang

RUN go get -u github.com/go-redis/redis
RUN go get -u github.com/gorilla/mux
RUN go get -u github.com/gorilla/websocket
RUN go get -u github.com/jinzhu/gorm
RUN go get -u github.com/jinzhu/gorm/dialects/postgres

COPY ./start /start
RUN chmod +x /start
WORKDIR /app


#yml
routes : &routes
    build :
      context: . 
      dockerfile : ./compose/local/routes_go/Dockerfile
    image: hyk_local_routes
    ports : 
      - 8002:8002
    depends_on : 
      - postgres
      - redis
    volumes:
      - ./routes_go:/app
    command : /start
