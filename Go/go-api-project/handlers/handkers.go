package handlers

import (
    "encoding/json"
    "net/http"
)

type Item struct {
    ID   int    `json:"id"`
    Name string `json:"name"`
}

var items = []Item{
    {ID: 1, Name: "Item 1"},
    {ID: 2, Name: "Item 2"},
	{ID: 3, Name: "Item 3"},
}

func GetItems(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(items)
}

func CreateItem(w http.ResponseWriter, r *http.Request) {
    var newItem Item
    json.NewDecoder(r.Body).Decode(&newItem)
    items = append(items, newItem)
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(newItem)
}

