
import sys
import pygame
from pygame.locals import Color, KEYUP, K_ESCAPE, K_RETURN
import sprite

surface = pygame.display.set_mode((300,300))
FPS = 120
frames = FPS / 12
x = 576 / 9
y = 256 / 4
strips = [
    sprite.SpriteStripAnim('demo1.png', (0,0,x,y), 9, -1, True, frames=15),
    sprite.SpriteStripAnim('demo1.png', (0,y,x,y), 9, -1, True, frames=15),
    sprite.SpriteStripAnim('demo1.png', (0,2*y,x,y), 9, -1, True, frames=15),
    sprite.SpriteStripAnim('demo1.png', (0,3*y,x,y), 9, -1, True, frames=15)
]
black = Color('black')
clock = pygame.time.Clock()
n = 0
strips[n].iter()
image = strips[n].next()
while True:
    for e in pygame.event.get():
        if e.type == KEYUP:
            if e.key == K_ESCAPE:
                sys.exit()
            elif e.key == K_RETURN:
                n += 1
                if n >= len(strips):
                    n = 0
                strips[n].iter()
    surface.fill(black)
    surface.blit(image, (0,0))
    pygame.display.flip()
    image = strips[n].next()
    image = pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))
    clock.tick(FPS)