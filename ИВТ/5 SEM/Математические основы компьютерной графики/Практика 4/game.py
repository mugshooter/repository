import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Настройки экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Простая игра")

# Персонаж
player = pygame.Rect(100, 100, 50, 50)  # Начальная позиция 
player_speed = 5

# Гравитация и прыжки
velocity_y = 0
gravity = 0.5
jump_strength = -10
on_ground = False

# Ловушки (черного цвета и маленького размера)
trap = pygame.Rect(400, 350, 20, 20)  # Прямоугольник ловушки 

# Враги (красного цвета)
enemies = [pygame.Rect(600, 250, 50, 50), pygame.Rect(700, 150, 50, 50)]  # Враги 
# Платформы (препятствия)
platforms = [pygame.Rect(0, 350, 800, 50), pygame.Rect(300, 200, 150, 20), pygame.Rect(500, 100, 150, 20)]  # Платформы 
# Камера
camera = pygame.Rect(0, 0, WIDTH, HEIGHT)

# Локация (конец уровня)
level_end = pygame.Rect(750, 250, 50, 50)  # Конечная точка уровня 

# Зона атаки
attack_zone = pygame.Rect(player.x + 50, player.y - 30, 110, 110)  # зона атаки перед игроком
attack = False

# Переменные для жизней
lives = 3
score = 0

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)  # Очистка экрана

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Активировать атаку
                attack = True
            if event.key == pygame.K_UP and on_ground:  # Прыжок
                velocity_y = jump_strength
                on_ground = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                attack = False  # Деактивировать атаку

    # Управление персонажем
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    # Логика гравитации и прыжков
    on_ground = False
    for plat in platforms:
        if player.colliderect(plat) and velocity_y > 0:
            velocity_y = 0
            player.y = plat.top - player.height
            on_ground = True

    if not on_ground:
        velocity_y += gravity
    player.y += velocity_y

    # Камера следит за игроком
    camera.x = player.x - WIDTH // 2
    camera.y = player.y - HEIGHT // 2
    camera.x = max(0, min(camera.x, 1000 - WIDTH))  # Ограничение камеры по горизонтали
    camera.y = max(0, min(camera.y, 1000 - HEIGHT))  # Ограничение камеры по вертикали

    # Отображение платформ, ловушек, врагов, конечной точки
    for plat in platforms:
        pygame.draw.rect(screen, GREEN, plat)

    pygame.draw.rect(screen, BLACK, trap)  # Ловушка
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)  # Враги
    pygame.draw.rect(screen, (0, 0, 255), level_end)  # Конечная точка

    # Проверка активации ловушки
    if player.colliderect(trap):
        print("Ловушка активирована!")
        lives -= 2  # Уменьшаем жизни на 2
        trap = pygame.Rect(-100, -100, 20, 20)  # Уничтожить ловушку

    # Проверка столкновений с врагами
    for enemy in enemies[:]:
        if player.colliderect(enemy):
            print("Вы столкнулись с врагом!")
            lives -= 1  # Уменьшаем жизни на 1
            player.x = 100  # Сброс позиции персонажа
            player.y = 100  # Сброс позиции персонажа
            if lives <= 0:
                print("Игра окончена!")
                running = False  # Конец игры

    # Проверка попадания в врага атакой
    if attack:
        for enemy in enemies[:]:
            if attack_zone.colliderect(enemy):
                print("Враг уничтожен!")
                enemies.remove(enemy)  # Уничтожение врага

    # Проверка достижения конца уровня
    if player.colliderect(level_end):
        print("Вы прошли уровень!")
        running = False  # Конец игры после прохождения уровня

    # Нарисовать персонажа
    pygame.draw.rect(screen, BLUE, player)

    # Нарисовать зону атаки
    if attack:
        attack_zone = pygame.Rect(player.x + 50, player.y - 30, 110, 110)  # Обновляем зону атаки
        pygame.draw.rect(screen, RED, attack_zone)

    # Отображение счётчика жизней
    font = pygame.font.SysFont('Arial', 30)
    lives_text = font.render(f'Lives: {lives}', True, (0, 0, 0))
    screen.blit(lives_text, (10, 10))

    # Применение камеры
    screen.blit(screen, (0, 0), camera)

    pygame.display.flip()  # Обновление экрана
    clock.tick(FPS)  # Поддержание FPS

pygame.quit()
sys.exit()
