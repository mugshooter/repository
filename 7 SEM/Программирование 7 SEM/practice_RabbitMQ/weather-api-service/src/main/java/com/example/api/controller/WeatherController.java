package com.example.api.controller;

import com.example.api.service.WeatherService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/weather")
public class WeatherController {

    @Autowired
    private WeatherService weatherService;

    @PostMapping("/query")
    public String queryWeather(@RequestBody List<String> cities) {
        String correlationId = weatherService.processWeatherRequest(cities);
        return "Запрос принят. Ваш Correlation ID: " + correlationId;
    }
}