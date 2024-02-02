import pygame

cols = 20
margin = 100
tile_size = 40
screen_width = tile_size * cols
screen_height = (tile_size * cols) + margin
screen = pygame.display.set_mode((screen_width, screen_height))


def txt(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
