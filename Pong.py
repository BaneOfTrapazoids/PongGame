import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((800,500))
font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 100)

direction = "UL"
point = [375, 225]
left = [0, 150]
right = [775, 150]

clock = pygame.time.Clock()

left_score = 0
right_score = 0

right_up = False
right_down = False
left_up = False
left_down = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                right_up = True
            
            elif event.key == pygame.K_DOWN:
                right_down = True

            elif event.key == pygame.K_w:
                left_up = True

            elif event.key == pygame.K_s:
                left_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                right_up = False

            elif event.key == pygame.K_DOWN:
                right_down = False

            elif event.key == pygame.K_w:
                left_up = False

            elif event.key == pygame.K_s:
                left_down = False

    if left_up and left[1] > 0:
        left[1] -= 1

    elif left_down and left[1] < 300:
        left[1] += 1

    elif right_down and right[1] < 300:
        right[1] += 1

    elif right_up and right[1] > 0:
        right[1] -= 1

    left_score_value = font.render(str(left_score), True, (255,255,255))
    right_score_value = font.render(str(right_score), True, (255,255,255))

    screen.fill((0,0,0))

    left_rect = pygame.draw.rect(screen, (255,255,255), (left[0], left[1], 25, 200))
    right_rect = pygame.draw.rect(screen, (255,255,255), (right[0], right[1], 25, 200))
    point_rect = pygame.draw.rect(screen, (255,255,255), (point[0], point[1], 50, 50))

    if point_rect.colliderect(right_rect):
        if direction == "UR":
            direction = "UL"

        elif direction == "DR":
            direction = "DL"

    if point_rect.colliderect(left_rect):
        if direction == "UL":
            direction = "UR"

        elif direction == "DL":
            direction = "DR"

    if point[1] <= 0:
        if direction == "UR":
            direction = "DR"

        elif direction == "UL":
            direction = "DL"

    if point[1] >= 450:
        if direction == "DR":
            direction = "UR"

        elif direction == "DL":
            direction = "UL"

    if point[0] >= 750:
        left_score += 1
        point = [375, 225]

    if point[0] <= 0:
        right_score += 1
        point = [375, 225]

    direction_dict = {
        "UR":(1, -1),
        "UL":(-1, -1),
        "DR":(1, 1),
        "DL":(-1, 1)
    }

    point[0] += direction_dict[direction][0]
    point[1] += direction_dict[direction][1]

    screen.blit(left_score_value, (150,25))
    screen.blit(right_score_value, (600, 25))

    pygame.display.update()
    clock.tick(150)