import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы для окна и цветов
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Создание окна
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Игровые объекты
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
player = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 70, 10, 140)
opponent = pygame.Rect(10, HEIGHT // 2 - 70, 10, 140)

# Начальные скорости мяча
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

# Скорость игрока и оппонента
player_speed = 0
opponent_speed = 7

# Счет
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)

# Функция обновления экрана
def draw_objects():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, WHITE, player)
    pygame.draw.rect(win, WHITE, opponent)
    pygame.draw.ellipse(win, BLUE, ball)
    pygame.draw.aaline(win, WHITE, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    player_text = font.render(f"Player: {player_score}", True, WHITE)
    opponent_text = font.render(f"Opponent: {opponent_score}", True, WHITE)
    win.blit(player_text, (WIDTH - player_text.get_width() - 10, 10))
    win.blit(opponent_text, (10, 10))
    pygame.display.update()

# Главный цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_speed = -7
    elif keys[pygame.K_DOWN]:
        player_speed = 7
    else:
        player_speed = 0

    # Движение игрока
    player.y += player_speed

    # Движение оппонента
    if ball.y > opponent.y + opponent.height // 2:
        opponent.y += opponent_speed
    elif ball.y < opponent.y + opponent.height // 2:
        opponent.y -= opponent_speed

    # Движение мяча
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Отскок мяча от верхней и нижней границ поля
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Проверка на столкновение мяча с игроком
    if ball.colliderect(player) and ball_speed_x > 0:
        ball_speed_x *= -1
        player_score += 1

    # Проверка на столкновение мяча с оппонентом
    if ball.colliderect(opponent) and ball_speed_x < 0:
        ball_speed_x *= -1
        opponent_score += 1

    # Проверка на выход мяча за границы экрана (проигрыш)
    if ball.left <= 0 or ball.right >= WIDTH:
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    draw_objects()

pygame.quit()
