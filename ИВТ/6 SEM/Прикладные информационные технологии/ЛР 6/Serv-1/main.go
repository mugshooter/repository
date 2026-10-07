package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	port := "8069"

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Привет от Артема %s", port)
	})

	log.Printf("Сервер запущен на порту %s\n", port)
	if err := http.ListenAndServe(":"+port, nil); err != nil {
		log.Fatalf("Ошибка запуска БИМБО: %v", err)
	}
}
