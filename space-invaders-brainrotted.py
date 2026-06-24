import math
import random
import pygame

# 1. Initialize Pygame FIRST
pygame.init()
pygame.joystick.init()

# Create a clock object to control the framerate
clock = pygame.time.Clock()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 3  # Adjusted slightly for 60 FPS pacing
ENEMY_SPEED_Y = 20
BULLET_SPEED_Y = 15  # Adjusted slightly for 60 FPS pacing
COLLISION_DISTANCE = 27

# Dead Zone Configuration
DEAD_ZONE = 0.15  
TRIGGER_THRESHOLD = 0.30  

# Initialize Joysticks list
joysticks = []

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.image.load('67kid.jpg')

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('gun.jpg')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('rock.jpg'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))  
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Bullet
bulletImg = pygame.image.load('bullet.jpg')
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

# Track discrete controller states
dpad_active = False
bumper_active = False

# Game loop
running = True
while running:
    # Force the loop to run at exactly 60 frames per second
    clock.tick(60)

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    # 2. Joystick/Analog Stick & Trigger Reading
    if len(joysticks) > 0:
        axis_0_value = joysticks[0].get_axis(0)  
        axis_2_value = joysticks[0].get_axis(2)  
        
        rt_value = joysticks[0].get_axis(5)
        rt_normalized = (rt_value + 1) / 2
        
        # Check if Right Trigger is pulled past threshold
        if rt_normalized >= TRIGGER_THRESHOLD and bullet_state == "ready":
            bulletX = playerX
            fire_bullet(bulletX, bulletY)

        # Handle movement vectors if discrete buttons aren't driving the ship
        if not dpad_active and not bumper_active:
            if abs(axis_0_value) > DEAD_ZONE:
                playerX_change = axis_0_value * 8  # Snappy speed scaling for 60fps
            elif abs(axis_2_value) > DEAD_ZONE:
                playerX_change = axis_2_value * 8
            else:
                keys = pygame.key.get_pressed()
                if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                    playerX_change = 0

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)
            
        # Controller Button Down Controls
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0 and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
                
            if event.button == 1:
                running = False
                
            if event.button == 4:
                playerX_change = -8
                bumper_active = True
                
            if event.button == 5:
                playerX_change = 8
                bumper_active = True

        # Controller Button Up Controls
        if event.type == pygame.JOYBUTTONUP:
            if event.button in [4, 5]:
                playerX_change = 0
                bumper_active = False

        # Controller D-pad (Hat) Controls
        if event.type == pygame.JOYHATMOTION:
            dpad_x = event.value[0] 
            dpad_y = event.value[1]
            
            if dpad_y == 1 and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
                
            if dpad_x == -1:    
                playerX_change = -8
                dpad_active = True
            elif dpad_x == 1:   
                playerX_change = 8
                dpad_active = True
            elif dpad_x == 0:   
                playerX_change = 0
                dpad_active = False

        # Keyboard controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -8
            if event.key == pygame.K_RIGHT:
                playerX_change = 8
                
            if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
                
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            if len(joysticks) == 0:
                playerX_change = 0

    # Player Movement & boundaries
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))  

    # Enemy Movement
    for i in range(num_of_enemies):
        if enemyY[i] > 340:  
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        # Collision Check
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY) and bullet_state == "fire":
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i], i)

    # Cleaned up Bullet Movement & Rendering
    if bullet_state == "fire":
        screen.blit(bulletImg, (bulletX + 16, bulletY + 10))
        bulletY -= bulletY_change
        if bulletY <= 0:
            bulletY = PLAYER_START_Y
            bullet_state = "ready"

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()

pygame.quit()