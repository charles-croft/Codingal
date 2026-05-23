import ctypes
import pygame

try:
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        "mycompany.mygame.version1"
    )
except AttributeError:
    pass

pygame.init()
icon_image = pygame.image.load("controller.png")
pygame.display.set_icon(icon_image)
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")
image = pygame.image.load("no-gaming.png")
image = pygame.transform.scale(image, (300, 300))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((6, 148, 148))
    screen.blit(image, (100, 100))
    pygame.display.flip()
pygame.quit()