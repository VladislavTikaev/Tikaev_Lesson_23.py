import random
import time

import pygame
pygame.init()

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
dis = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Змейка')
game_over = False

window_size = pygame.display.get_window_size()
snake_block = 10
snake_speed = 15
# Координаты змейки
x_1 = 100
y_1 = 400
x_1_change = 0
y_1_change = 0

snake_List = [] # длина змейки
Length_snake = 1
# Координаты яблока
apple_x = random.randrange(0, window_size[0], 10)
apple_y = random.randrange(0, window_size[1], 10)

# Координаты стен
obj_1_x = 200
obj_1_y = 30
obj_2_x = 350
obj_2_y = 40
obj_3_x = 500
obj_3_y = 20
obj_4_x = 650
obj_4_y = 20


# Объявляем переменную clock, через которую отслеживается время в игре
clock = pygame.time.Clock()
# Объявляем переменные, в которых будут находится звуки
eating_sound = pygame.mixer.Sound('apple.mp3')
game_over_sound = pygame.mixer.Sound('game_over.mp3')
score = 0
font = pygame.font.Font(None, 36)

def our_snake(snake_block, snake_List):
   for x in snake_List:
       pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])

def message(msg,color):
    mesg=font.render(msg, True, color)
    dis.blit(mesg, [700/2, 500/2])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_1_change = -10
                y_1_change = 0
            if event.key == pygame.K_RIGHT:
                x_1_change = 10
                y_1_change = 0
            if event.key == pygame.K_UP:
                y_1_change = -10
                x_1_change = 0
            if event.key == pygame.K_DOWN:
                y_1_change = 10
                x_1_change = 0

    if x_1 >= window_size[0] or y_1 >= window_size[1] or x_1 <= 0 or y_1 <= 0:
        game_over = True
    x_1 += x_1_change
    y_1 += y_1_change
    dis.fill(white)
    nadpis = font.render('Очки: ' + str(score), True, red)
    dis.blit(nadpis, (10, 10))

    pygame.draw.rect(dis, blue, [x_1, y_1, 10, 10])
    pygame.draw.rect(dis, red, [apple_x, apple_y, 10, 10])
    pygame.draw.rect(dis,black, [obj_1_x, obj_1_y, 10, 410])
    pygame.draw.rect(dis, black, [obj_2_x, obj_2_y, 10, 350])
    pygame.draw.rect(dis, black, [obj_3_x, obj_3_y, 10, 320])
    pygame.draw.rect(dis, black, [obj_4_x, obj_4_y, 10, 380])
    pygame.display.update()
    snake_Head = []
    snake_Head.append(x_1)
    snake_Head.append(y_1)
    snake_List.append(snake_Head)
    if x_1 == obj_1_x and y_1 >= obj_1_y and y_1 <= obj_1_y +410:
        game_over = True
    if x_1 == obj_2_x and y_1 >= obj_2_y and y_1 <= obj_2_y +350:
        game_over = True
    if x_1 == obj_3_x and y_1 >= obj_3_y and y_1 <= obj_3_y +320:
        game_over = True
    if x_1 == obj_4_x and y_1 >= obj_4_y and y_1 <= obj_4_y +380:
        game_over = True
    if len(snake_List) > Length_snake:
        del snake_List[0]
    for x in snake_List[:-1]:
        if x == snake_Head:
            game_over = True
        our_snake(snake_block, snake_List)
        pygame.display.update()
    if x_1 == apple_x and y_1 == apple_y:
        eating_sound.play()
        print('Съел!')
        apple_x = random.randrange(0, window_size[0], 10)
        apple_y = random.randrange(0, window_size[1], 10)
        Length_snake += 1
        score += 1
        snake_speed += 3
    clock.tick(snake_speed)


message('Game over', red)
game_over_sound.play()
pygame.display.update()
time.sleep(2)

pygame = quit()
quit()
