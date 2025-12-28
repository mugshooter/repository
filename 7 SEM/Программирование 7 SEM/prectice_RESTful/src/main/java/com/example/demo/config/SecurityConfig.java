package com.example.demo.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.Customizer;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.config.annotation.web.configurers.AbstractHttpConfigurer;
import org.springframework.security.config.annotation.web.configurers.HeadersConfigurer;

@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            // Отключаем CSRF, так как это REST API и мы используем H2 Console
            .csrf(AbstractHttpConfigurer::disable)
            
            // Настройка доступа к эндпоинтам
            .authorizeHttpRequests(auth -> auth
                // Разрешаем доступ к консоли H2 без авторизации (для отладки)
                .requestMatchers("/h2-console/**").permitAll()
                // Все остальные запросы к API требуют аутентификации
                .anyRequest().authenticated()
            )
            
            // Включаем Basic Authentication (логин/пароль в заголовках)
            .httpBasic(Customizer.withDefaults())
            
            // Разрешаем отображение фреймов (нужно для работы интерфейса H2 Console)
            .headers(headers -> headers.frameOptions(HeadersConfigurer.FrameOptionsConfig::sameOrigin));

        return http.build();
    }
}