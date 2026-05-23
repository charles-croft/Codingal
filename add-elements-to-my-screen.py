import ctypes
import pygame

try:
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        "mycompany.mygame.version1"
    )
except AttributeError:
    pass

pygame.init()
icon_image = pygame.image.load("fire.png")
pygame.display.set_icon(icon_image)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")
rect_width, rect_height = 200, 100
rect_x = (640 - rect_width) // 2
rect_y = (480 - rect_height) // 2
font = pygame.font.SysFont("comicsansms", 24)
text_surface = font.render("Hello Pygame", True, (255, 255, 255))
text_rect = text_surface.get_rect(center=(320, 240))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (6, 148, 148), (rect_x, rect_y, rect_width, rect_height))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
pygame.quit()