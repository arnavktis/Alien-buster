# main
import pygame
import random
import math

#initialise pygame
pygame.init()

# to create a screen
screen = pygame.display.set_mode((800,600))             #size of screen
screen.fill((0, 0, 0))

#background
background = pygame.image.load("background1.png")
background2 = pygame.image.load("background21.png")
#Title and Icon
arrow = pygame.image.load("up-arrow.png")
pygame.display.set_caption("Alien Buster")
img = pygame.image.load("ironman.jpg")
pygame.display.set_icon(img)

#Player

playerimg=pygame.image.load("spaceship.png")
playerx = 370
playery = 480
playerx_change = 0
playery_change = 0

def player(x,y):
    screen.blit(playerimg,(x,y))                               #blit= drawing
    
#Enemy
enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 5

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("alien.png"))  
    enemyx.append(random.randint(0,736)) 
    enemyy.append(random.randint(50,150)) 
    enemyx_change.append(5)  
    enemyy_change.append(40)

enemyimg2 = []
enemy2x = []
enemy2y = []
enemy2x_change = []
enemy2y_change = []
num_of_enemies2 = 4
    
for j in range(num_of_enemies2):
    enemyimg2.append(pygame.image.load("alien2.png"))  
    enemy2x.append(random.randint(1,735)) 
    enemy2y.append(random.randint(49,151)) 
    enemy2x_change.append(5)  
    enemy2y_change.append(40)

#Bullet
bulletimg = pygame.image.load("rectangle.png")
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 10
bullet_state = "ready"

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',45)
textx = 10
texty = 10

# Game over text
over_text = pygame.font.Font('freesansbold.ttf',90)

# Victory text
victory_text = pygame.font.Font('freesansbold.ttf',140)

def show_score(x,y):
    score = font.render('score :' + str(score_value),True, (0,255,209))
    screen.blit(score,(x,y))
      
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))                              #blit= drawing
def enemy2(x,y,j):
    screen.blit(enemyimg2[j],(x,y)) 
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x+31,y+10))

def iscollision(enemyx,enemyy,bulletx,bullety):
    distance = (math.sqrt(math.pow(enemyx - bulletx,2)) + (math.pow(enemyy - bullety,2)))
    if distance < 40:
        return True
    else:
        return False

def iscollision2(enemy2x,enemy2y,bulletx,bullety):
    distance2 = (math.sqrt(math.pow(enemy2x - bulletx,2)) + (math.pow(enemy2y - bullety,2)))
    if distance2 < 40:
        return True
    else:
        return False
    
#game loop
victory = True
running= True
playeron = True
lvlup = False
lvl1 = True
lvl2 = False
while running:
    screen.fill((0, 0, 0))
    #background image
    if lvl1:
        screen.blit(background,(0,0))
    if lvl2:
        bg2 = pygame.transform.scale(background2, (800, 600))
        screen.blit(bg2,(0,0))
    for event in pygame.event.get():                             #To close the game
        if event.type == pygame.QUIT:
            running = False
        #if keystroke is being pressed to check wether its right or left
        #keydown is pressing the key and keyup is lifting up the key
        if playeron :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerx_change = -5
                if event.key == pygame.K_RIGHT:
                    playerx_change = 5
                if lvlup and not lvl2:
                    if event.key == pygame.K_UP:
                        playery_change = -2
                    if event.key == pygame.K_DOWN:
                        playery_change = 2
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletx = playerx
                        fire_bullet(bulletx,bullety)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerx_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playery_change = 0
#restriction of player
    if victory:
        if playery < 0:
            lvlup = False       
            num_of_enemies = 4
            num_of_enemies2 = 4
            enemyimg = []
            enemyimg2 = []
            for i in range(num_of_enemies) :
                enemyimg.append(pygame.image.load("alien.png"))
            screen.blit(background2,(0,0))
            for i in range(num_of_enemies2) :
                enemyimg2.append(pygame.image.load("alien2.png"))
            screen.blit(background2,(0,0))
            lvl1 = False
            lvl2 = True
            playery = 480
        if playerx <= 0:
            playerx = 0
        elif playerx >= 736:
            playerx = 736
        if lvl1 and score_value == 15:
            screen.blit(arrow,(400,300))

#restrictions of the enemy
    for i in range(num_of_enemies):
        if enemyy[i] > 440:                    #Game over
            for J in range(num_of_enemies):
                enemyy[i] = 300
                playeron = False
        if playeron and victory:
            enemyx[i] += enemyx_change[i]
            if enemyx[i] <= 0:
                enemyx_change[i] = 3
                enemyy[i] += enemyy_change[i]
            elif enemyx[i] >= 736:
                enemyx_change[i] = -3
                enemyy[i] += enemyy_change[i]
                
    for i in range(num_of_enemies2):
        if enemy2y[i] > 440:                    #Game over
            for J in range(num_of_enemies2):
                enemy2y[i] = 300
                playeron = False
        if playeron and victory:
            enemy2x[i] += enemy2x_change[i]
            if enemy2x[i] <= 0:
                enemy2x_change[i] = 3
                enemy2y[i] += enemy2y_change[i]
            elif enemy2x[i] >= 736:
                enemy2x_change[i] = -3
                enemy2y[i] += enemy2y_change[i]


#collision
        collision = iscollision(enemyx[i],enemyy[i],bulletx,bullety)
        if collision:
             bullety = 480
             bullet_state = "ready"
             score_value += 1
             enemyx[i] = random.randint(0,736)
             enemyy[i] = random.randint(50,150)
        if num_of_enemies > 0:
                 if lvlup:
                     num_of_enemies -=1
        enemy(enemyx[i],enemyy[i],i)
        
        collision2 = iscollision2(enemy2x[j],enemy2y[j],bulletx,bullety)
        if collision2:
             bullety = 480
             bullet_state = "ready"
             score_value += 1
             enemy2x[j] = random.randint(0,736)
             enemy2y[j] = random.randint(50,150)
             if num_of_enemies2 > 0:
                 if lvlup:
                     num_of_enemies2 -=1
        enemy2(enemy2x[j],enemy2y[j],j)
    player(playerx,playery)
            

#bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletx,bullety)
        bullety -= bullety_change
    if bullety <= 0:
        bullety = 480
        bullet_state = "ready"
    playerx += playerx_change 
    playery += playery_change
    show_score(textx,texty)                           

#updates display
    if not playeron:
        over_text = font.render('GAME OVER',True, (0,255,209))
        screen.blit(over_text,(250,260))    
    pygame.display.update() 
    if score_value == 7:
        lvlup = True
    if victory:
        if score_value == 30:
            victory = False
    if not victory:
        if score_value == 30:
            victory_text = font.render('VICTORY',True, (0,255,209))
            screen.blit(victory_text,(250,260))
    pygame.display.update()
            
pygame.quit()                                               #ends program
