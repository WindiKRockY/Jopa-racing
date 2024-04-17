from pygame import * #імпортування бібліотеки пайгейм

#створи вікно гри

window = display.set_mode((700,500)) #створення дисплею 
FPS = 90 #змінна,яка відровідає за частоту кадрів
clock= time.Clock() #змінна часу

sprite1= image.load('sprite1.png')  #імпортування першого спрайту
sprite2= image.load('sprite2.png')  #імпортування другого спрайту

bg= transform.scale(bg ,(700,500)) #зміна розширення вікна

#створи 2 спрайти та розмісти їх на сцені

npc_1 = Player(sprite1,70,70,150,250) #розміщення першого спрайту
npc_2 = Player(sprite2,70,70,400,250) #розміщення другого спрайту

#оброби подію «клік за кнопкою "Закрити вікно"»

run = True #присвоєння зміній run активного статусу

#створення класу

class Player(sprite.Sprite): #назва класу
    def __init__(self,sprite_img,width,height,x,y): #властивості 
        self.image = transform.scale(sprite_img,(width,height)) #розширення спрайтів
        self.rect = self.image.get_rect() #отримання значення
        self.rect.x = x #присвоєння значення x
        self.rect.y = y #присвоєння значення y


#закриття програми при кліці

while run: #поки відбувається цикл
    for e in event.get(): #отримання значення 
        if e.type == QUIT: #якщо відбувається вихід
            run = False #цикл закінчується
            
#загрузка елементів
    
    window.blit(bg,(0,0)) #загрузка заднього фону
    window.blit(npc_1.image,npc_1.rect) #загрузка першого спрайту
    window.blit(npc_2.image,npc_2.rect) #загрузка другого спрайту

#встановлення частоти
    
    display.update() #обновлення події дисплею
    clock.tick(FPS) #встановлення частоти кадрів