package com.example.aggregator;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling // Нужно для очистки устаревших данных
public class WeatherAggregatorApplication {
    public static void main(String[] args) {
        SpringApplication.run(WeatherAggregatorApplication.class, args);
    }
}