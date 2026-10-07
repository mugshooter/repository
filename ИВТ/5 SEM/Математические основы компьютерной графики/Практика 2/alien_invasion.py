import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from save_load import save_game, load_game
import pickle

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Инопланетное вторжение")

        # Загрузка фонового изображения
        self.bg_image = pygame.image.load('resources/images/background.jpg')

        # Инициализация звуков
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound("resources/sounds/laser.mp3")
        self.alien_explosion_sound = pygame.mixer.Sound("resources/sounds/alien_explosion.mp3")
        self.life_lost_sound = pygame.mixer.Sound("resources/sounds/life_lost.mp3")
        self.game_over_sound = pygame.mixer.Sound("resources/sounds/game_over.mp3")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Добавляем атрибут для счёта и жизней
        self.score = 0
        self.lives = 3  # Начальные жизни
        self.font = pygame.font.SysFont(None, 48)  # Шрифт для отображения счёта и "Game Over"

        # Уровень игры
        self.level = 1

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_s:  # Сохранение игры
            self._save_game()
        elif event.key == pygame.K_l:  # Загрузка игры
            self._load_game()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.laser_sound.play()  # Воспроизведение звука выстрела

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            # Добавляем 10 очков за каждого уничтоженного инопланетянина
            self.score += 10 * len(collisions)
            self.alien_explosion_sound.play()  # Воспроизведение звука взрыва инопланетянина
        if not self.aliens:
            self.bullets.empty()
            self.settings.increase_speed()  # Увеличиваем скорость
            self.level += 1  # Увеличиваем уровень
            self._create_fleet()

    def _update_aliens(self):
        self.aliens.update()
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._take_life()  # Потеря жизни при столкновении с инопланетянином
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._take_life()  # Потеря жизни, если инопланетянин дошёл до низа экрана

    def _take_life(self):
        """Уменьшение жизней игрока и проверка на конец игры."""
        self.lives -= 1
        self.life_lost_sound.play()  # Воспроизведение звука потери жизни
        if self.lives <= 0:
            self._game_over()  # Если жизни закончились, конец игры
        else:
            # Перемещаем корабль обратно в стартовую позицию и возобновляем игру
            self.ship.center_ship()
            self.aliens.empty()
            self._create_fleet()
            self.bullets.empty()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        # Отображаем фоновое изображение
        self.screen.blit(self.bg_image, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Отображаем счёт и количество жизней
        self._display_score()
        self._display_lives()
        self._display_level()  # Отображаем уровень

        pygame.display.flip()

    def _display_score(self):
        """Отображает текущий счёт в углу экрана."""
        score_str = f"Score: {self.score}"
        score_image = self.font.render(score_str, True, (255, 255, 255))
        self.screen.blit(score_image, (20, 20))

    def _display_lives(self):
        """Отображает количество оставшихся жизней."""
        lives_str = f"Lives: {self.lives}"
        lives_image = self.font.render(lives_str, True, (255, 255, 255))
        self.screen.blit(lives_image, (self.settings.screen_width - 150, 20))

    def _display_level(self):
        """Отображает текущий уровень игры."""
        level_str = f"Level: {self.level}"
        level_image = self.font.render(level_str, True, (255, 255, 255))
        self.screen.blit(level_image, (self.settings.screen_width // 2 - 50, 20))

    def _game_over(self):
        """Отображение сообщения 'Game Over' с финальным счётом и завершение игры."""
        self.screen.blit(self.bg_image, (0, 0))  # Перерисовываем фон
        game_over_str = f"Game Over! Final Score: {self.score}"
        game_over_image = self.font.render(game_over_str, True, (255, 0, 0))
        self.screen.blit(game_over_image, (self.settings.screen_width // 2 - 150, self.settings.screen_height // 2))

        pygame.display.flip()
        self.game_over_sound.play()  # Воспроизведение звука конца игры
        pygame.time.wait(2000)  # Пауза на 2 секунды, чтобы игрок увидел счёт
        sys.exit()  # Завершаем игру

    def _save_game(self):
        """Сохранение текущего прогресса игры."""
        game_data = {
            "level": self.level,
            "score": self.score,
            "lives": self.lives
        }
        save_game(game_data)

    def _load_game(self):
        """Загрузка сохранённого прогресса игры."""
        game_data = load_game()
        if game_data:
            self.level = game_data["level"]
            self.score = game_data["score"]
            self.lives = game_data["lives"]

            # Очистить старые объекты игры перед загрузкой
            self.bullets.empty()
            self.aliens.empty()
            self.ship.center_ship()

            # Пересоздаём флот с учётом уровня
            self._create_fleet()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
