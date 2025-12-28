package com.example.frontend;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class WeatherFrontendApplication {
    public static void main(String[] args) {
        // Этот сервис будет работать на порту 8081, 
        // чтобы не конфликтовать с api-service (8080)
        SpringApplication.run(WeatherFrontendApplication.class, args);
    }
}