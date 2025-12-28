package com.example.api.service;

import com.example.api.controller.WeatherController.WeatherMessage;
import com.example.api.config.RabbitMQConfig;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.UUID;

@Service
public class WeatherService {

    @Autowired
    private RabbitTemplate rabbitTemplate;

    /**
     * Обрабатывает список городов, генерирует ID и отправляет в RabbitMQ
     */
    public String processWeatherRequest(List<String> cities) {
        // Генерируем уникальный Correlation ID для всей пачки городов
        String correlationId = UUID.randomUUID().toString();
        int totalCities = cities.size();

        for (String city : cities) {
            // Создаем объект сообщения
            WeatherMessage message = new WeatherMessage(
                correlationId, 
                city.trim(), 
                totalCities
            );

            // Отправляем в Exchange с конкретным Routing Key
            rabbitTemplate.convertAndSend(
                RabbitMQConfig.WEATHER_EXCHANGE,
                RabbitMQConfig.REQUEST_ROUTING_KEY,
                message
            );
        }

        return correlationId;
    }
}