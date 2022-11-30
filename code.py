from globals import Globals
import pygame
import random


class Consts:
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
    SIZE = 30
    SIZE_1 = 15
    size = [600, 600]
    record_size = 10
    min_coord = 75
    max_coord = 525


def exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


def fill_records_array():
    for i in range(Consts.record_size):
        Globals.high_score.append([j for j in (Globals.f.readline().split())])


def print_main_screen():
    screen.blit(background, (0, 0))
    game_name = Big_titles.render(f'Игра Змейка', 1, pygame.Color('red'))
    title = [0] * 10
    title[9] = small_titles.render(f'выберите раздел соответствующей цифрой на клавиатуре', 1, pygame.Color('red'))
    title[1] = small_titles.render(f'1. Уровень 1 (easy, vanila)', 1, pygame.Color('red'))
    title[2] = small_titles.render(f'2. Уровень 2 (easy)', 1, pygame.Color('red'))
    title[3] = small_titles.render(f'3. Уровень 3 (medium)', 1, pygame.Color('red'))
    title[4] = small_titles.render(f'4. Уровень 4 (hard)', 1, pygame.Color('red'))
    title[5] = small_titles.render(f'5. Уровень 5 (very hard)', 1, pygame.Color('red'))
    title[6] = small_titles.render(f'6. Таблица рекордов', 1, pygame.Color('red'))
    title[7] = small_titles.render(f'7. Настройка цвета змеи', 1, pygame.Color('red'))
    title[8] = small_titles.render(f'8. Ввод имени для таблицы рекордов', 1, pygame.Color('red'))
    screen.blit(game_name, (130, 50))
    for i in range(1, 10):
        screen.blit(title[i], (90, 140 + i * 40))
    pygame.display.flip()


def run_app():
    global screen
    screen = pygame.display.set_mode(Consts.size)
    pygame.display.set_caption("Змейка")
    global background
    background = pygame.image.load("background.jpg").convert()
    pygame.init()
    global clock
    clock = pygame.time.Clock()
    global titles
    titles = pygame.font.SysFont('Arial', 26)
    global Big_titles
    Big_titles = pygame.font.SysFont('Arial', 72)
    global small_titles
    small_titles = pygame.font.SysFont('Arial', 20)
    fill_records_array()
    print_main_screen()
    block_choice()


def name_change_block():
    Name = ''
    flag = True
    while flag:
        screen.blit(background, (0, 0))
        name_title = Big_titles.render(f' {Name}', 1, pygame.Color('red'))
        screen.blit(name_title, (100, 300))
        title_K_8 = titles.render(f' клавишу escape для выхода', 1, pygame.Color('red'))
        screen.blit(title_K_8, (100, 150))
        title_K_8 = titles.render(f' Введите ваше имя, затем нажмите', 1, pygame.Color('red'))
        screen.blit(title_K_8, (100, 100))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    flag = False
                Name += event.unicode
        exit()
        clock.tick(Globals.FPS)


def block_color_set_description():
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


def set_color(key):
    if key[pygame.K_1]:
        Globals.snake_color = Consts.YELLOW
    if key[pygame.K_2]:
        Globals.snake_color = Consts.GREEN
    if key[pygame.K_3]:
        Globals.snake_color = Consts.BLUE
    if key[pygame.K_4]:
        Globals.snake_color = Consts.PURPLE
    if key[pygame.K_5]:
        Globals.snake_color = Consts.WHITE
    if key[pygame.K_6]:
        Globals.snake_color = Consts.BLACK


def block_set_color():
    while True:
        block_color_set_description()
        key = pygame.key.get_pressed()
        clock.tick(Globals.FPS)
        exit()
        set_color(key)
        if key[pygame.K_ESCAPE]:
            break


def record_table_block():
    while True:
        screen.blit(background, (0, 0))
        record = Big_titles.render(f'Таблица рекордов', 1, pygame.Color('red'))
        screen.blit(record, (50, 10))
        for count in range(10):
            cur_record = titles.render(
                f'{count + 1}. {Globals.high_score[Consts.record_size - 1 - count][0]} {Globals.high_score[Consts.record_size - 1 - count][1]}',
                1, pygame.Color('red'))
            screen.blit(cur_record, (100, 100 + 40 * count))
        exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            break
        clock.tick(Globals.FPS)
        pygame.display.flip()


def levels_block(key):
    if key[pygame.K_1]:
        level_1()
    if key[pygame.K_2]:
        level_2()
    if key[pygame.K_3]:
        level_3()
    if key[pygame.K_4]:
        level_4()
    if key[pygame.K_5]:
        level_5()


def block_choice():
    while True:
        print_main_screen()
        exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_8]:
            name_change_block()
        if key[pygame.K_7]:
            block_set_color()
        if key[pygame.K_6]:
            record_table_block()
        levels_block(key)


def refill_high_score():
    idx = 0
    while idx < 10 and int(Globals.high_score[idx][0]) < Globals.score:
        if idx == 0:
            Globals.high_score[0] = [Globals.score, Globals.Name]
        else:
            Globals.high_score[idx - 1] = Globals.high_score[idx]
            Globals.high_score[idx] = [Globals.score, Globals.Name]
        idx += 1
    if idx > 0:
        Globals.f.seek(0)
        for i in range(Consts.record_size):
            Globals.f.write(str(Globals.high_score[i][0]) + ' ' + Globals.high_score[i][1] + '\n')


def draw_snake_and_apple():
    for row in range(Consts.SIZE):
        for columns in range(Consts.SIZE):
            if (row + columns) % 2 == 0:
                color = Consts.LIGHT_BLUE_1
            else:
                color = Consts.LIGHT_BLUE_2
            pygame.draw.rect(screen, color,
                             [Consts.min_coord + row * Consts.SIZE_1, Consts.min_coord + columns * Consts.SIZE_1,
                              Consts.SIZE_1, Consts.SIZE_1])
    for i, j in Globals.snake:
        pygame.draw.rect(screen, Globals.snake_color,
                         [i, j, Consts.SIZE_1, Consts.SIZE_1])
    pygame.draw.rect(screen, Globals.apple_color, (*Globals.apple, Consts.SIZE_1, Consts.SIZE_1))


def initiall_point_wo_walls(FPS):
    Globals.score = 0
    Globals.FPS = FPS
    Globals.dx, Globals.dy = 0, 0
    Globals.permissions = {'W': True, 'A': True, 'S': True, 'D': True}
    Globals.x, Globals.y = random.randrange(Consts.min_coord, Consts.max_coord, Consts.SIZE_1), random.randrange(
        Consts.min_coord, Consts.max_coord, Consts.SIZE_1)
    Globals.snake = [(Globals.x, Globals.y)]
    Globals.apple = (random.randrange(Consts.min_coord, Consts.max_coord, Consts.SIZE_1),
                     random.randrange(Consts.min_coord, Consts.max_coord, Consts.SIZE_1))
    Globals.length = 1


def change_direction(key):
    if key[pygame.K_w] and Globals.permissions['W']:
        Globals.dx, Globals.dy = 0, -1
        Globals.permissions = {'W': True, 'A': True, 'S': False, 'D': True}
    if key[pygame.K_a] and Globals.permissions['A']:
        Globals.dx, Globals.dy = -1, 0
        Globals.permissions = {'W': True, 'A': True, 'S': True, 'D': False}
    if key[pygame.K_s] and Globals.permissions['S']:
        Globals.dx, Globals.dy = 0, 1
        Globals.permissions = {'W': False, 'A': True, 'S': False, 'D': True}
    if key[pygame.K_d] and Globals.permissions['D']:
        Globals.dx, Globals.dy = 1, 0
        Globals.permissions = {'W': True, 'A': False, 'S': True, 'D': False}


def move_snake():
    if Globals.count == 0:
        Globals.x += Globals.dx * Consts.SIZE_1
        Globals.y += Globals.dy * Consts.SIZE_1
        Globals.snake.append((Globals.x, Globals.y))
        Globals.snake = Globals.snake[-Globals.length:]
        if Globals.snake[-1] == Globals.apple:
            Globals.length += 1
            Globals.score += Globals.length - 1
            Globals.apple = (random.randrange(Consts.min_coord, Consts.max_coord, Consts.SIZE_1),
                             random.randrange(Consts.min_coord, Consts.max_coord, Consts.SIZE_1))
            Globals.FPS += 1
        Globals.count = 100
    else:
        Globals.count -= 1
        clock.tick(Globals.FPS)


def move_snake_w_bon_apple(mltp):
    if Globals.count == 0:
        Globals.x += Globals.dx * Consts.SIZE_1
        Globals.y += Globals.dy * Consts.SIZE_1
        Globals.snake.append((Globals.x, Globals.y))
        if Globals.bonus_flag == 0:
            Globals.snake = Globals.snake[-Globals.length:]
        else:
            Globals.bonus_flag -= 1
            Globals.length += 1
        is_apple_eaten(mltp)
        Globals.count = 100
    else:
        Globals.count -= 1
        clock.tick(Globals.FPS)


def is_apple_eaten(mltp):
    if Globals.snake[-1] == Globals.apple:
        Globals.length += 1
        Globals.score += mltp * Globals.length - 1
        if Globals.apple_color == Consts.YELLOW:
            Globals.score += Globals.length - 1
        if Globals.apple_color == Consts.BLUE:
            Globals.walls_flag = 40
        Globals.apple = (random.randrange(Consts.min_coord, Consts.max_coord, Consts.SIZE_1),
                         random.randrange(Consts.min_coord, Consts.max_coord, Consts.SIZE_1))
        if random.randint(1, 5) == 3:
            Globals.apple_color = Consts.YELLOW
        elif random.randint(1, 5) == 4:
            Globals.apple_color = Consts.BLUE
        else:
            Globals.apple_color = Consts.RED
        if random.randint(1, 5) == 2:
            bonus_length()
        Globals.FPS += 1


def draw_screen():
    screen.blit(background, (0, 0))
    render_score = titles.render(f'SCORE: {Globals.score}', 1, pygame.Color('red'))
    screen.blit(render_score, (10, 10))
    Globals.count = 0
    draw_snake_and_apple()


def bonus_length():
    Globals.bonus_flag = 3
    Globals.score += 5


def level_1():
    FPS_1 = 10
    initiall_point_wo_walls(FPS_1)
    while True:
        draw_screen()
        flag_1 = Globals.x < Consts.min_coord or Globals.x >= Consts.max_coord
        flag_2 = Globals.y < Consts.min_coord or Globals.y >= Consts.max_coord
        flag_3 = len(Globals.snake) != len(set(Globals.snake))
        if flag_3 or flag_2 or flag_1:
            refill_high_score()
            break
        move_snake()
        pygame.display.flip()
        exit()
        clock.tick(Globals.FPS)
        key = pygame.key.get_pressed()
        change_direction(key)


def level_2():
    FPS_2 = 15
    initiall_point_wo_walls(FPS_2)
    while True:
        draw_screen()
        flag_1 = Globals.x < Consts.min_coord or Globals.x >= Consts.max_coord
        flag_2 = Globals.y < Consts.min_coord or Globals.y >= Consts.max_coord
        flag_3 = len(Globals.snake) != len(set(Globals.snake))
        if flag_3 or flag_2 or flag_1:
            refill_high_score()
            break
        move_snake_w_bon_apple(1)
        pygame.display.flip()
        exit()
        clock.tick(Globals.FPS)
        key = pygame.key.get_pressed()
        change_direction(key)


def is_apple_and_snake_in_wall(walls):
    flag = (Globals.x, Globals.y) in walls
    while flag:
        Globals.x, Globals.y = random.randrange(Consts.min_coord, Consts.max_coord, Consts.SIZE_1), random.randrange(
            Consts.min_coord, Consts.max_coord, Consts.SIZE_1)
        flag = (Globals.x, Globals.y) in walls
    Globals.snake = [(Globals.x, Globals.y)]
    flag = Globals.apple in walls
    while flag:
        Globals.apple = (random.randrange(Consts.min_coord, Consts.max_coord, Consts.SIZE_1),
                         random.randrange(Consts.min_coord, Consts.max_coord, Consts.SIZE_1))
        flag = Globals.apple in walls


def set_walls_3():
    walls = []
    min_wall_3 = 10
    max_wall_3 = 20
    for counter in range(min_wall_3, max_wall_3):
        walls.append((Consts.min_coord + min_wall_3 * Consts.SIZE_1, Consts.min_coord + counter * Consts.SIZE_1))
        walls.append((Consts.min_coord + counter * Consts.SIZE_1, Consts.min_coord + min_wall_3 * Consts.SIZE_1))
    return walls


def draw_walls(walls):
    for u, v in walls:
        pygame.draw.rect(screen, Consts.BLACK, [u, v, Consts.SIZE_1, Consts.SIZE_1])


def draw(walls_flag):
    walls_counter = titles.render(f'Ходов до конца бонуса: {walls_flag}', 1, pygame.Color('red'))
    screen.blit(walls_counter, (300, 10))


def level_3():
    FPS_3 = 15
    walls = set_walls_3()
    initiall_point_wo_walls(FPS_3)
    is_apple_and_snake_in_wall(walls)
    while True:
        draw_screen()
        draw_walls(walls)
        flag_1 = Globals.x < Consts.min_coord or Globals.x >= Consts.max_coord
        flag_2 = Globals.y < Consts.min_coord or Globals.y >= Consts.max_coord
        flag_3 = len(Globals.snake) != len(set(Globals.snake))
        if flag_3 or flag_2 or flag_1 or (((Globals.x, Globals.y) in walls) and Globals.walls_flag == 0):
            refill_high_score()
            break
        if Globals.walls_flag > 0:
            Globals.walls_flag -= 1
            draw(Globals.walls_flag)
        move_snake_w_bon_apple(3)
        pygame.display.flip()
        clock.tick(Globals.FPS)
        exit()
        key = pygame.key.get_pressed()
        change_direction(key)


def set_walls_4():
    walls = []
    min_wall_4 = 10
    max_wall_4 = 21
    gap = 15
    for counter in range(min_wall_4, max_wall_4):
        if counter != gap:
            walls.append((Consts.min_coord + min_wall_4 * Consts.SIZE_1, Consts.min_coord + counter * Consts.SIZE_1))
            walls.append(
                (Consts.min_coord + (max_wall_4 - 1) * Consts.SIZE_1, Consts.min_coord + counter * Consts.SIZE_1))
            walls.append((Consts.min_coord + counter * Consts.SIZE_1, Consts.min_coord + min_wall_4 * Consts.SIZE_1))
            walls.append(
                (Consts.min_coord + counter * Consts.SIZE_1, Consts.min_coord + (max_wall_4 - 1) * Consts.SIZE_1))
    return walls


def level_4():
    FPS_4 = 15
    walls = set_walls_4()
    initiall_point_wo_walls(FPS_4)
    is_apple_and_snake_in_wall(walls)
    while True:
        draw_screen()
        draw_walls(walls)
        flag_1 = Globals.x < Consts.min_coord or Globals.x >= Consts.max_coord
        flag_2 = Globals.y < Consts.min_coord or Globals.y >= Consts.max_coord
        flag_3 = len(Globals.snake) != len(set(Globals.snake))
        if flag_3 or flag_2 or flag_1 or (((Globals.x, Globals.y) in walls) and Globals.walls_flag == 0):
            refill_high_score()
            break
        if Globals.walls_flag > 0:
            Globals.walls_flag -= 1
            draw(Globals.walls_flag)
        move_snake_w_bon_apple(3)
        pygame.display.flip()
        clock.tick(Globals.FPS)
        exit()
        key = pygame.key.get_pressed()
        change_direction(key)


def set_walls_5():
    walls = []
    gap_1 = 10
    gap_2 = 19
    max_wall_5 = 29
    for counter in range(max_wall_5 + 1):
        if counter != gap_1 and counter != gap_2:
            walls.append(
                (Consts.min_coord + (max_wall_5 - counter) * Consts.SIZE_1, Consts.min_coord + counter * Consts.SIZE_1))
            walls.append((Consts.min_coord + counter * Consts.SIZE_1, Consts.min_coord + counter * Consts.SIZE_1))
    return walls


def level_5():
    FPS_5 = 15
    walls = set_walls_5()
    initiall_point_wo_walls(FPS_5)
    is_apple_and_snake_in_wall(walls)
    while True:
        draw_screen()
        draw_walls(walls)
        flag_1 = Globals.x < Consts.min_coord or Globals.x >= Consts.max_coord
        flag_2 = Globals.y < Consts.min_coord or Globals.y >= Consts.max_coord
        flag_3 = len(Globals.snake) != len(set(Globals.snake))
        if flag_3 or flag_2 or flag_1 or (((Globals.x, Globals.y) in walls) and Globals.walls_flag == 0):
            refill_high_score()
            break
        if Globals.walls_flag > 0:
            Globals.walls_flag -= 1
            draw(Globals.walls_flag)
        move_snake_w_bon_apple(4)
        pygame.display.flip()
        clock.tick(Globals.FPS)
        exit()
        key = pygame.key.get_pressed()
        change_direction(key)
