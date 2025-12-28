package com.example.api.config;

import org.springframework.amqp.core.*;
import org.springframework.amqp.support.converter.Jackson2JsonMessageConverter;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class RabbitMQConfig {

    public static final String WEATHER_EXCHANGE = "weather.exchange";
    public static final String REQUEST_QUEUE = "weather.requests";
    public static final String REQUEST_ROUTING_KEY = "weather.request.key";

    @Bean
    public TopicExchange weatherExchange() {
        return new TopicExchange(WEATHER_EXCHANGE);
    }

    @Bean
    public Queue requestQueue() {
        return QueueBuilder.durable(REQUEST_QUEUE).build();
    }

    @Bean
    public Binding requestBinding(Queue requestQueue, TopicExchange weatherExchange) {
        return BindingBuilder.bind(requestQueue).to(weatherExchange).with(REQUEST_ROUTING_KEY);
    }

    // Конвертер для автоматического преобразования объектов в JSON
    @Bean
    public Jackson2JsonMessageConverter jsonMessageConverter() {
        return new Jackson2JsonMessageConverter();
    }
}