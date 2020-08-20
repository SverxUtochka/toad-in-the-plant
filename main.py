import pygame

pygame.init()

win = pygame.display.set_mode((640,360))

pygame.display.update()
pygame.display.set_caption("Toad in the plant")

#спрайты персонажа
Down = pygame.image.load('playerDown.png')
Right = pygame.image.load('playerRight.png')
Up = pygame.image.load('PlayerUp.png')
Lift = pygame.image.load('PlayerLeft.png')

#дополнительные предметы
Thanck = pygame.image.load('thanckyou.png')
car = pygame.image.load('car.png')
text = pygame.image.load('text.png')
scrap = pygame.image.load('scrap.png')
box = pygame.image.load('box.png')
bg = pygame.image.load('background.png')

#координаты спавна персонажа
x = 320
y = 180
#ширина и высота персонажа
width = 64
height = 64
#скорость персонажа
speed = 1
#координаты коробки
x_box = 30
y_box = 180

#вспомогательные True и False
ThanckYou = False
ScrapActive = False
start = True
Spawn_scrap = False
left = False
right = False
up = False
down = False
animate = 0

#функция по рисовке мира
def PaintPlayer():
    global animate
    win.blit(bg, (0, 0))
    win.blit(box, (x_box, y_box))
    win.blit(car, (400, 140))
    #спавн лома
    if Spawn_scrap == True:
        win.blit(scrap, (30, 250))
    if ThanckYou == True:
        win.blit(Thanck, (50, 50))
    #анимация спрайтов
    if left == True:
        win.blit(Lift, (x, y))
    if right == True:
        win.blit(Right, (x, y))
    if up == True:
        win.blit(Up, (x, y))
    if down == True:
        win.blit(Down, (x, y))
    if start == True:
       win.blit(text, (200, 30))
    pygame.display.update()

#запуск игры
game_end = False

while not game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True

    #кнопки
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > -10:
        x -= speed
        left = True
        right = False
        up = False
        down = False
        start = False
    if keys[pygame.K_RIGHT] and x < 590:
        x += speed
        left = False
        right = True
        up = False
        down = False
        start = False
    if keys[pygame.K_UP] and y > 180:
        y -= speed
        up = True
        left = False
        right = False
        down = False
        start = False
    if keys[pygame.K_DOWN] and y < 295:
        y += speed
        down = True
        right = False
        up = False
        left = False
        start = False
    #кнопка для спавна лома
    if keys[pygame.K_SPACE]:
        Spawn_scrap = True
    #взять лом
    if keys[pygame.K_RSHIFT]:
        Spawn_scrap = False
        ScrapActive = True
    if ScrapActive == True:
        if keys[pygame.K_TAB]:
            ThanckYou = True
    PaintPlayer()

#закрытие игры
pygame.quit()
quit()
