package main

import (
	"net/http"
	"fmt"
	"time"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		time.Sleep(time.Second * 1)
		fmt.Fprintf(w, "Hello world")
	})

	http.ListenAndServe(":3000", nil)

}
