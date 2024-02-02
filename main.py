import pygame
import pickle
from os import path

pygame.init()

clock = pygame.time.Clock()
fps = 60

# game window
tile_size = 40
cols = 20
margin = 100
level = 1
screen_width = tile_size * cols
screen_height = (tile_size * cols) + margin
white = (255, 255, 255)
green = (144, 201, 120)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Level Editor')

# load images
sun_img = pygame.image.load('images/sun.png')
sun_img = pygame.transform.scale(sun_img, (tile_size, tile_size))
bg_img = pygame.image.load('images/sky.png')
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height - margin))
save_img = pygame.image.load('images/save_btn.png')
load_img = pygame.image.load('images/load_btn.png')

world_data = [[0] * 20 for i in range(20)]


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


save_button = Button(screen_width // 2 - 150, screen_height - 80, save_img)
load_button = Button(screen_width // 2 + 50, screen_height - 80, load_img)

run = True
while run:

    clock.tick(fps)

    screen.fill(green)
    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, (tile_size * 2, tile_size * 2))

    if save_button.draw():
        pickle_out = open(f'level{level}_data', 'wb')
        pickle.dump(world_data, pickle_out)
        pickle_out.close()
    if load_button.draw():
        if path.exists(f'level{level}_data'):
            pickle_in = open(f'level{level}_data', 'rb')
            world_data = pickle.load(pickle_in)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
