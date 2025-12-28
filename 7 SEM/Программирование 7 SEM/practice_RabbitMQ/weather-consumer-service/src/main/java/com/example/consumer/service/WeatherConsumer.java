package com.example.consumer.service;

import com.example.api.controller.WeatherController.WeatherMessage; // В реальном проекте это общий DTO
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class WeatherConsumer {

    @Autowired
    private RestTemplate restTemplate;

    @Autowired
    private RabbitTemplate rabbitTemplate;

    private final String API_KEY = "ВАШ_API_KEY_OPENWEATHER";
    private final String API_URL = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric";

    @RabbitListener(queues = "weather.requests")
    public void consumeWeatherRequest(WeatherMessage request) {
        try {
            // 1. Запрос к внешнему API
            String url = API_URL.replace("{city}", request.getCity()).replace("{key}", API_KEY);
            Object response = restTemplate.getForObject(url, Object.class);

            // 2. Формирование ответа для агрегатора
            WeatherResponse weatherResponse = new WeatherResponse(
                request.getCorrelationId(),
                request.getCity(),
                response,
                request.getTotalCities(),
                "SUCCESS"
            );

            // 3. Отправка в очередь ответов
            rabbitTemplate.convertAndSend("weather.exchange", "weather.response.key", weatherResponse);
            
        } catch (Exception e) {
            // В случае ошибки отправляем статус ERROR
            WeatherResponse errorResponse = new WeatherResponse(
                request.getCorrelationId(),
                request.getCity(),
                null,
                request.getTotalCities(),
                "ERROR: " + e.getMessage()
            );
            rabbitTemplate.convertAndSend("weather.exchange", "weather.response.key", errorResponse);
        }
    }

    @Data
    @AllArgsConstructor
    @NoArgsConstructor
    public static class WeatherResponse {
        private String correlationId;
        private String city;
        private Object data;
        private int totalCities;
        private String status;
    }
}