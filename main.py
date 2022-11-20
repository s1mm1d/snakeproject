import pygame
import random

f = open("high_score.txt", 'r+')
high_score = []
for i in range(10):
    high_score.append([j for j in (f.readline().split())])
size = [600, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Змейка")
BLUE = (0, 0, 100)
DARK_YELLOW = (100, 100, 0)
RED = (100, 0, 0)
GREEN = (0, 100, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE_1 = (12, 235, 220)
LIGHT_BLUE_2 = (167, 235, 230)
apple_color = RED
snake_color = GREEN
SIZE = 30
SIZE_1 = 15
background = pygame.image.load("background.jpg").convert()
FPS = 10
Name = 'UNKNOWN'

pygame.init()
clock = pygame.time.Clock()
titles = pygame.font.SysFont('Arial', 26)
Big_titles = pygame.font.SysFont('Arial', 72)
small_titles = pygame.font.SysFont('Arial', 20)

while True:
    screen.blit(background, (0, 0))
    game_name = Big_titles.render(f'Игра Змейка', 1, pygame.Color('red'))
    title_1 = small_titles.render(f'выберите раздел соответствующей цифрой на клавиатуре', 1, pygame.Color('red'))
    title_2 = small_titles.render(f'1. Уровень 1 (easy, vanila)', 1, pygame.Color('red'))
    title_3 = small_titles.render(f'2. Уровень 2 (easy)', 1, pygame.Color('red'))
    title_4 = small_titles.render(f'3. Уровень 3 (medium)', 1, pygame.Color('red'))
    title_5 = small_titles.render(f'4. Уровень 4 (hard)', 1, pygame.Color('red'))
    title_6 = small_titles.render(f'5. Уровень 5 (very hard)', 1, pygame.Color('red'))
    title_7 = small_titles.render(f'6. Таблица рекордов', 1, pygame.Color('red'))
    title_8 = small_titles.render(f'7. Настройка цвета змеи', 1, pygame.Color('red'))
    title_9 = small_titles.render(f'8. Ввод имени для таблицы рекордов', 1, pygame.Color('red'))
    screen.blit(game_name, (130, 50))
    screen.blit(title_1, (90, 500))
    screen.blit(title_2, (90, 180))
    screen.blit(title_3, (90, 220))
    screen.blit(title_4, (90, 260))
    screen.blit(title_5, (90, 300))
    screen.blit(title_6, (90, 340))
    screen.blit(title_7, (90, 380))
    screen.blit(title_8, (90, 420))
    screen.blit(title_9, (90, 460))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    key = pygame.key.get_pressed()
    score = 0

    if key[pygame.K_8]:
        Name = ''
        flag = True
        while True:
            if flag == False:
                break
            screen.blit(background, (0, 0))
            name_title = Big_titles.render(f' {Name}', 1, pygame.Color('red'))
            screen.blit(name_title, (100, 300))
            title_K_8 = titles.render(f' клавишу escape для выхода', 1,
                                      pygame.Color('red'))
            screen.blit(title_K_8, (100, 150))
            title_K_8 = titles.render(f' Введите ваше имя, затем нажмите', 1,
                                      pygame.Color('red'))
            screen.blit(title_K_8, (100, 100))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        flag = False
                        break
                    Name += event.unicode
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            clock.tick(FPS)

    if key[pygame.K_7]:
        while True:
            screen.blit(background, (0, 0))
            color_change = Big_titles.render(f'Игра Змейка', 1, pygame.Color('red'))
            color_2 = small_titles.render(f'1. Желтый', 1, pygame.Color('yellow'))
            color_3 = small_titles.render(f'2. Зеленый', 1, pygame.Color('green'))
            color_4 = small_titles.render(f'3. Синий', 1, pygame.Color('blue'))
            color_5 = small_titles.render(f'4. Фиолетовый', 1, pygame.Color('purple'))
            color_6 = small_titles.render(f'5. Белый', 1, pygame.Color('white'))
            color_7 = small_titles.render(f'6. Чёрный', 1, pygame.Color('black'))
            title = small_titles.render(f'Выберите цвет, для выхода в главное меню нажмите esc', 1,
                                        pygame.Color('black'))
            screen.blit(color_2, (90, 180))
            screen.blit(color_3, (90, 220))
            screen.blit(color_4, (90, 260))
            screen.blit(color_5, (90, 300))
            screen.blit(color_6, (90, 340))
            screen.blit(color_7, (90, 380))
            screen.blit(title, (90, 100))
            pygame.display.flip()
            key = pygame.key.get_pressed()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            if key[pygame.K_1]:
                snake_color = YELLOW
            if key[pygame.K_2]:
                snake_color = GREEN
            if key[pygame.K_3]:
                snake_color = BLUE
            if key[pygame.K_4]:
                snake_color = PURPLE
            if key[pygame.K_5]:
                snake_color = WHITE
            if key[pygame.K_6]:
                snake_color = BLACK
            if key[pygame.K_ESCAPE]:
                break

    if key[pygame.K_6]:
        while True:
            screen.blit(background, (0, 0))
            record = Big_titles.render(f'Таблица рекордов', 1, pygame.Color('red'))
            screen.blit(record, (50, 10))
            for count in range(10):
                cur_record = color_7 = titles.render(
                    f'{count + 1}. {high_score[9 - count][0]} {high_score[9 - count][1]}', 1, pygame.Color('red'))
                screen.blit(cur_record, (100, 100 + 40 * count))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                break
            clock.tick(FPS)
            pygame.display.flip()


    def RefillHighScore():
        idx = 0
        while idx < 10 and int(high_score[idx][0]) < score:
            if idx == 0:
                high_score[0] = [score, Name]
            else:
                high_score[idx - 1] = high_score[idx]
                high_score[idx] = [score, Name]
            idx += 1
        if idx > 0:
            f.seek(0)
            for i in range(10):
                f.write(str(high_score[i][0]) + ' ' + high_score[i][1] + '\n')


    def DrawSnakeAndApple():
        for row in range(SIZE):
            for columns in range(SIZE):
                if (row + columns) % 2 == 0:
                    color = LIGHT_BLUE_1
                else:
                    color = LIGHT_BLUE_2
                pygame.draw.rect(screen, color,
                                 [75 + row * SIZE_1, 75 + columns * SIZE_1, SIZE_1, SIZE_1])
        for i, j in snake:
            pygame.draw.rect(screen, snake_color,
                             [i, j, SIZE_1, SIZE_1])
        pygame.draw.rect(screen, apple_color, (*apple, SIZE_1, SIZE_1))


    if key[pygame.K_1]:
        FPS = 10
        dx = 0
        dy = 0
        permissions = {'W': True, 'A': True, 'S': True, 'D': True}
        x, y = random.randrange(75, 525, SIZE_1), random.randrange(75, 525, SIZE_1)
        snake = [(x, y)]
        apple = (random.randrange(75, 525, SIZE_1), random.randrange(75, 525, SIZE_1))
        length = 1

        while True:
            screen.blit(background, (0, 0))
            render_score = titles.render(f'SCORE: {score}', 1, pygame.Color('red'))
            screen.blit(render_score, (10, 10))
            count = 0
            DrawSnakeAndApple()
            if x < 75 or x >= 525 or y < 75 or y >= 525 or (len(snake) != len(set(snake))):
                RefillHighScore()
                break
            if count == 0:
                x += dx * SIZE_1
                y += dy * SIZE_1
                snake.append((x, y))
                snake = snake[-length:]
                if snake[-1] == apple:
                    length += 1
                    score += length - 1
                    apple = (random.randrange(75, 525, SIZE_1), random.randrange(75, 525, SIZE_1))
                    FPS += 1
                count = 100
            else:
                count -= 1
                clock.tick(FPS)

            pygame.display.flip()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            key = pygame.key.get_pressed()
            if key[pygame.K_w] and permissions['W']:
                dx, dy = 0, -1
                permissions = {'W': True, 'A': True, 'S': False, 'D': True}
            if key[pygame.K_a] and permissions['A']:
                dx, dy = -1, 0
                permissions = {'W': True, 'A': True, 'S': True, 'D': False}
            if key[pygame.K_s] and permissions['S']:
                dx, dy = 0, 1
                permissions = {'W': False, 'A': True, 'S': False, 'D': True}
            if key[pygame.K_d] and permissions['D']:
                dx, dy = 1, 0
                permissions = {'W': True, 'A': False, 'S': True, 'D': False}

    if key[pygame.K_2]:
        FPS = 15
        dx = 0
        dy = 0
        permissions = {'W': True, 'A': True, 'S': True, 'D': True}
        x, y = random.randrange(75, 525, SIZE_1), random.randrange(75, 525, SIZE_1)
        snake = [(x, y)]
        apple = (random.randrange(75, 525, SIZE_1), random.randrange(75, 525, SIZE_1))
        length = 1

        while True:
            screen.blit(background, (0, 0))
            render_score = titles.render(f'SCORE: {score}', 1, pygame.Color('red'))
            screen.blit(render_score, (10, 10))
            count = 0
            DrawSnakeAndApple()
            if x < 75 or x >= 525 or y < 75 or y >= 525 or (len(snake) != len(set(snake))):
                RefillHighScore()
                break
            if count == 0:
                x += dx * SIZE_1
                y += dy * SIZE_1
                snake.append((x, y))
                snake = snake[-length:]
                if snake[-1] == apple:
                    length += 1
                    score += length - 1
                    if apple_color == YELLOW:
                        score += length - 1
                    apple = (random.randrange(75, 525, SIZE_1), random.randrange(75, 525, SIZE_1))
                    if random.randint(1, 5) == 3:
                        apple_color = YELLOW
                    else:
                        apple_color = RED
                    FPS += 1
                count = 100
            else:
                count -= 1
                clock.tick(FPS)

            pygame.display.flip()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            key = pygame.key.get_pressed()
            if key[pygame.K_w] and permissions['W']:
                dx, dy = 0, -1
                permissions = {'W': True, 'A': True, 'S': False, 'D': True}
            if key[pygame.K_a] and permissions['A']:
                dx, dy = -1, 0
                permissions = {'W': True, 'A': True, 'S': True, 'D': False}
            if key[pygame.K_s] and permissions['S']:
                dx, dy = 0, 1
                permissions = {'W': False, 'A': True, 'S': False, 'D': True}
            if key[pygame.K_d] and permissions['D']:
                dx, dy = 1, 0
                permissions = {'W': True, 'A': False, 'S': True, 'D': False}

    if key[pygame.K_3]:
        walls = []
        for counter in range(10, 20):
            walls.append((75 + 10 * SIZE_1, 75 + counter * SIZE_1))
            walls.append((75 + counter * SIZE_1, 75 + 10 * SIZE_1))
        FPS = 15
        dx = 0
        dy = 0
        permissions = {'W': True, 'A': True, 'S': True, 'D': True}
        x = 225
        y = 225
        flag = (x, y) in walls
        while flag:
            x, y = random.randrange(75, 525, SIZE_1), random.randrange(75, 525, SIZE_1)
            flag = (x, y) in walls
        snake = [(x, y)]
        apple = (random.randrange(75, 525, SIZE_1), random.randrange(75, 525, SIZE_1))
        flag = apple in walls
        while flag:
            apple = (random.randrange(75, 525, SIZE_1), random.randrange(75, 525, SIZE_1))
            flag = apple in walls

        length = 1

        while True:
            screen.blit(background, (0, 0))
            render_score = titles.render(f'SCORE: {score}', 1, pygame.Color('red'))
            screen.blit(render_score, (10, 10))
            count = 0
            DrawSnakeAndApple()
            for u, v in walls:
                pygame.draw.rect(screen, BLACK, [u, v, SIZE_1, SIZE_1])
            if x < 75 or x >= 525 or y < 75 or y >= 525 or (len(snake) != len(set(snake))) or (x, y) in walls:
                RefillHighScore()
                break
            if count == 0:
                x += dx * SIZE_1
                y += dy * SIZE_1
                snake.append((x, y))
                snake = snake[-length:]
                if snake[-1] == apple:
                    length += 1
                    score += 2 * length - 1
                    if apple_color == YELLOW:
                        score += length - 1
                    apple = (random.randrange(75, 525, SIZE_1), random.randrange(75, 525, SIZE_1))
                    if random.randint(1, 5) == 3:
                        apple_color = YELLOW
                    else:
                        apple_color = RED
                    FPS += 1
                count = 100
            else:
                count -= 1
                clock.tick(FPS)

            pygame.display.flip()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            key = pygame.key.get_pressed()
            if key[pygame.K_w] and permissions['W']:
                dx, dy = 0, -1
                permissions = {'W': True, 'A': True, 'S': False, 'D': True}
            if key[pygame.K_a] and permissions['A']:
                dx, dy = -1, 0
                permissions = {'W': True, 'A': True, 'S': True, 'D': False}
            if key[pygame.K_s] and permissions['S']:
                dx, dy = 0, 1
                permissions = {'W': False, 'A': True, 'S': False, 'D': True}
            if key[pygame.K_d] and permissions['D']:
                dx, dy = 1, 0
                permissions = {'W': True, 'A': False, 'S': True, 'D': False}

    if key[pygame.K_4]:
        walls = []
        for counter in range(10, 21):
            if counter != 15:
                walls.append((75 + 10 * SIZE_1, 75 + counter * SIZE_1))
                walls.append((75 + 20 * SIZE_1, 75 + counter * SIZE_1))
                walls.append((75 + counter * SIZE_1, 75 + 10 * SIZE_1))
                walls.append((75 + counter * SIZE_1, 75 + 20 * SIZE_1))
        FPS = 15
        dx = 0
        dy = 0
        permissions = {'W': True, 'A': True, 'S': True, 'D': True}
        x = 225
        y = 225
        flag = (x, y) in walls
        while flag:
            x, y = random.randrange(75, 525, SIZE_1), random.randrange(75, 525, SIZE_1)
            flag = (x, y) in walls
        snake = [(x, y)]
        apple = (random.randrange(75, 525, SIZE_1), random.randrange(75, 525, SIZE_1))
        flag = apple in walls
        while flag:
            apple = (random.randrange(75, 525, SIZE_1), random.randrange(75, 525, SIZE_1))
            flag = apple in walls

        length = 1

        while True:
            screen.blit(background, (0, 0))
            render_score = titles.render(f'SCORE: {score}', 1, pygame.Color('red'))
            screen.blit(render_score, (10, 10))
            count = 0
            DrawSnakeAndApple()
            for u, v in walls:
                pygame.draw.rect(screen, BLACK, [u, v, SIZE_1, SIZE_1])
            if x < 75 or x >= 525 or y < 75 or y >= 525 or (len(snake) != len(set(snake))) or (x, y) in walls:
                RefillHighScore()
                break
            if count == 0:
                x += dx * SIZE_1
                y += dy * SIZE_1
                snake.append((x, y))
                snake = snake[-length:]
                if snake[-1] == apple:
                    length += 1
                    score += length - 1
                    if apple_color == YELLOW:
                        score += 4 * length - 1
                    a, b = random.randrange(75, 525, SIZE_1), random.randrange(75, 525, SIZE_1)
                    apple = (a, b)
                    if random.randint(1, 5) == 3 or ((225 < a) and (375 > a) and (b > 225) and (b < 375)):
                        apple_color = YELLOW
                    else:
                        apple_color = RED
                    FPS += 1
                count = 100
            else:
                count -= 1
                clock.tick(FPS)

            pygame.display.flip()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            key = pygame.key.get_pressed()
            if key[pygame.K_w] and permissions['W']:
                dx, dy = 0, -1
                permissions = {'W': True, 'A': True, 'S': False, 'D': True}
            if key[pygame.K_a] and permissions['A']:
                dx, dy = -1, 0
                permissions = {'W': True, 'A': True, 'S': True, 'D': False}
            if key[pygame.K_s] and permissions['S']:
                dx, dy = 0, 1
                permissions = {'W': False, 'A': True, 'S': False, 'D': True}
            if key[pygame.K_d] and permissions['D']:
                dx, dy = 1, 0
                permissions = {'W': True, 'A': False, 'S': True, 'D': False}

    if key[pygame.K_5]:
        walls = []
        for counter in range(30):
            if counter != 10 and counter != 19:
                walls.append((75 + (29 - counter) * SIZE_1, 75 + counter * SIZE_1))
                walls.append((75 + counter * SIZE_1, 75 + counter * SIZE_1))
        FPS = 15
        dx = 0
        dy = 0
        permissions = {'W': True, 'A': True, 'S': True, 'D': True}
        x = 225
        y = 225
        flag = (x, y) in walls
        while flag:
            x, y = random.randrange(75, 525, SIZE_1), random.randrange(75, 525, SIZE_1)
            flag = (x, y) in walls
        snake = [(x, y)]
        apple = (random.randrange(120, 480, SIZE_1), random.randrange(120, 480, SIZE_1))
        flag = apple in walls
        while flag:
            apple = (random.randrange(120, 480, SIZE_1), random.randrange(120, 480, SIZE_1))
            flag = apple in walls

        length = 1

        while True:
            screen.blit(background, (0, 0))
            render_score = titles.render(f'SCORE: {score}', 1, pygame.Color('red'))
            screen.blit(render_score, (10, 10))
            count = 0
            DrawSnakeAndApple()
            for u, v in walls:
                pygame.draw.rect(screen, BLACK, [u, v, SIZE_1, SIZE_1])
            if x < 75 or x >= 525 or y < 75 or y >= 525 or (len(snake) != len(set(snake))) or (x, y) in walls:
                RefillHighScore()
                break
            if count == 0:
                x += dx * SIZE_1
                y += dy * SIZE_1
                snake.append((x, y))
                snake = snake[-length:]
                if snake[-1] == apple:
                    length += 1
                    score += 5 * length - 1
                    if apple_color == YELLOW:
                        score += length - 1
                    apple = (random.randrange(75, 525, SIZE_1), random.randrange(75, 525, SIZE_1))
                    if random.randint(1, 5) == 3:
                        apple_color = YELLOW
                    else:
                        apple_color = RED
                    FPS += 1
                count = 100
            else:
                count -= 1
                clock.tick(FPS)

            pygame.display.flip()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            key = pygame.key.get_pressed()
            if key[pygame.K_w] and permissions['W']:
                dx, dy = 0, -1
                permissions = {'W': True, 'A': True, 'S': False, 'D': True}
            if key[pygame.K_a] and permissions['A']:
                dx, dy = -1, 0
                permissions = {'W': True, 'A': True, 'S': True, 'D': False}
            if key[pygame.K_s] and permissions['S']:
                dx, dy = 0, 1
                permissions = {'W': False, 'A': True, 'S': False, 'D': True}
            if key[pygame.K_d] and permissions['D']:
                dx, dy = 1, 0
                permissions = {'W': True, 'A': False, 'S': True, 'D': False}
