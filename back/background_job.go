/*
#portfolio
#Handle: _MUMINUL__ISLAM___
*/
package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"
	"time"
)

type Response struct {
	Input  int `json:"input"`
	Result int `json:"result"`
}

func counterHandler(w http.ResponseWriter, r *http.Request) {
	n_query := r.URL.Query().Get("n")
	if n_query == "" {
		http.Error(w, "Missing parameter", http.StatusBadRequest)
		return
	}
	n, err := strconv.Atoi(n_query)
	if err != nil {
		http.Error(w, "Invalid Number", http.StatusBadRequest)
	}
	counter := 0
	sum := 0

	for i := 0; i < n; i++ {
		time.Sleep(1 * time.Second)
		counter++
		sum += counter
		fmt.Println("Current count: ", counter)
	}
	counter = sum

	response := Response{
		Input:  n,
		Result: counter,
	}
	w.Header().Set("Content-Type", "application/json")
	err = json.NewEncoder(w).Encode(response)
	if err != nil {
		http.Error(w, "Failed to encode JSON", http.StatusInternalServerError)
	}
}

func main() {

	http.HandleFunc("/count", counterHandler)
	fmt.Println("Server Running on http://localhost:6000")
	http.ListenAndServe(":6000", nil)

}
