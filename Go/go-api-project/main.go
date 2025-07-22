package main

import (
    "log"
    "net/http"
    "go-api-project/handlers"
    "github.com/gorilla/mux"
)

func main() {
    router := mux.NewRouter()
    router.HandleFunc("/items", handlers.GetItems).Methods("GET")
    router.HandleFunc("/items", handlers.CreateItem).Methods("POST")

    log.Println("Servidor corriendo en http://localhost:8080")
    log.Fatal(http.ListenAndServe(":8080", router))
}

// para ir al link de la pagina es: http://localhost:8080/items