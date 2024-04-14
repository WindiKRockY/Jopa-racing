from pygame import *

#створи вікно гри
window = display.set_mode((700,500))
FPS = 90
clock= time.Clock()
#задай фон сцени
bg= image.load('background.png')
sprite1= image.load('sprite1.png')
sprite2= image.load('sprite2.png')

bg= transform.scale(bg ,(700,500))

#створи 2 спрайти та розмісти їх на сцені

#оброби подію «клік за кнопкою "Закрити вікно"»
run = True
class Player(sprite.Sprite):
    def __init__(self,srite_img,width,height,x,y):
        self.image = transform.scale(srite_img,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


npc_1 = Player(sprite1,70,70,150,250)
npc_2 = Player(sprite2,70,70,400,250)


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    window.blit(bg,(0,0))
    window.blit(npc_1.image,npc_1.rect)
    window.blit(npc_2.image,npc_2.rect)

    

    display.update()
    clock.tick(FPS)