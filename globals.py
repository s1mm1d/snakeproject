import pygame

class Globals:
    apple_color = (100, 0, 0)
    snake_color = (0, 100, 0)
    FPS = 10
    Name = 'UNKNOWN'
    high_score = []
    f = open("high_score.txt", 'r+')
    permissions = {'W': True, 'A': True, 'S': True, 'D': True}
    dx = 0
    dy = 0
    x = 0
    y = 0
    snake = []
    apple = (0, 0)
    length = 0
    count = 0
    score = 0
    bonus_flag = 0
    walls_flag = 0