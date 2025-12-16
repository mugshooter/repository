import pygame
import random

class Bonus(pygame.sprite.Sprite):
    """Класс, представляющий бонус."""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Загружаем изображение бонуса
        self.image = pygame.image.load('resources/images/bonus.png')
        self.image = pygame.transform.scale(self.image, (50, 50))  # Масштабируем до 50x50
        self.rect = self.image.get_rect()
        
        # Устанавливаем начальную позицию бонуса (по координатам уничтоженного инопланетянина)
        self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)
        self.rect.y = 0  # Начальная позиция сверху
        self.y = float(self.rect.y)  # Позиция с плавающей точкой для плавного движения
        
        self.speed = self.settings.bonus_speed  # Скорость движения бонуса вниз

    def update(self):
        """Перемещает бонус вниз."""
        self.y += self.speed
        self.rect.y = self.y

    def draw(self):
        """Отображает бонус на экране."""
        self.screen.blit(self.image, self.rect)
