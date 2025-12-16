package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	port := "6980"

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Пока от Артема %s", port)
	})

	log.Printf("Сервер запущен на порту %s\n", port)
	if err := http.ListenAndServe(":"+port, nil); err != nil {
		log.Fatalf("Ошибка запуска БИМБО: %v", err)
	}
}
