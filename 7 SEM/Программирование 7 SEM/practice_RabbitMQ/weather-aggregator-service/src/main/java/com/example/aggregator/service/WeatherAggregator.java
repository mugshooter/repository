package com.example.aggregator.service;

import com.example.consumer.service.WeatherConsumer.WeatherResponse;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

@Service
public class WeatherAggregator {

    // Хранилище: CorrelationId -> Список полученных ответов
    private final Map<String, List<WeatherResponse>> aggregateMap = new ConcurrentHashMap<>();

    @RabbitListener(queues = "weather.responses") // Очередь должна быть создана в RabbitMQConfig
    public void aggregate(WeatherResponse response) {
        String id = response.getCorrelationId();
        
        // 1. Добавляем полученный ответ в список
        aggregateMap.computeIfAbsent(id, k -> Collections.synchronizedList(new ArrayList<>()))
                    .add(response);

        List<WeatherResponse> receivedResponses = aggregateMap.get(id);

        // 2. Completion Strategy: Проверяем, всё ли собрали
        if (receivedResponses.size() >= response.getTotalCities()) {
            finalizeReport(id, receivedResponses);
        }
    }

    private void finalizeReport(String correlationId, List<WeatherResponse> results) {
        System.out.println("--- ОТЧЕТ СФОРМИРОВАН (" + correlationId + ") ---");
        results.forEach(r -> 
            System.out.println("Город: " + r.getCity() + " | Статус: " + r.getStatus())
        );
        
        // В реальной системе здесь была бы отправка в БД или обратно в API Service через RabbitMQ
        aggregateMap.remove(correlationId); // Очищаем память
    }

    // Задание 6: Очистка старых данных (если воркер упал и отчет не дособрался)
    @Scheduled(fixedRate = 60000)
    public void cleanup() {
        // Логика удаления записей старше 5 минут
    }
}