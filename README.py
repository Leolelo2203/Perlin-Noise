from modul import noise_2d
#/\
#||
#||
#||
#Just a Noise-Function:
#def noise_2d(x, y, seed):
#    x *= x
#    y *= y
#    x *= s
#    y *= s
#    x = x%127
#    y = y%127
#    return x + y
"""
Steuerung:
n: aktuellen Seed angeben(und mit e dann die Karte sehen)
w: alles löschen
s oder klicken: Inseln selber malen
h: aktuellen seed printen
Hashtag und s: aktuelle Karte speichern
Hashtag und l: gespeicherte Karte laden

Bei Fragen zum Code oder zum Programm einfach in die Kommentare posten :-)
"""
import pygame

from random import randint


willkommen = 100
pygame.init()
screen = pygame.display.set_mode((800, 800))
running = True
feld = []
drawer = None
save_path = '/Users/beispielname/Folder/Dateienname.txt' #Irgendeine Text Datei in einem belibiegen Ordner anlegen
def refresh(lis):
    new = []
    list = lis
    for i in range(0, 80):
        for e in range(0, 80):
            new.append(0)
            
    for i in range(3):    
        for i in range(0, len(new)):
            if 0 < i - 80:
                new[i] += list[i - 80]
                
            if 0 < i - 1:
                new[i] += list[i - 1]
                
            if len(list) > i + 1:
                new[i] += list[i + 1]
                
            if len(list) > i + 80:
                new[i] += list[i + 80]
            
            """
            if i + 81 < len(list):
                new[i] += list[i + 81]
            if i + 79 < len(list):
                new[i] += list[i + 79]
            if i - 81 >= 0:
                new[i] += list[i - 81]
            if i - 79 >= 0:
                new[i] += list[i - 79]
            """
            new[i] = new[i]/4
            new[i] = int(new[i])
            if new[i] > 255:
                new[i] = 254
            



            new[i] = int(new[i])
                    
        list = new
        
    
    
    return new
    """
    for i in range(2):    
        for i in range(0, len(new)):
            if 0 < i - 80:
                if list[i - 80] > new[i]/4:
                    new[i] += list[i - 80]
            
            if 0 < i - 1:
                if list[i - 1] > new[i]/4:
                    new[i] += list[i - 1]
            
            if len(list) > i + 1:
                if list[i + 1] > new[i]/4:
                    new[i] += list[i + 1]
            
            if len(list) > i + 80:
                if list[i + 80] > new[i]/4:
                    new[i] += list[i + 80]
            new[i] = new[i] / 4
            new[i] = int(new[i])
            if new[i] > 255:
                new[i] = 254
                
        list = new
        
    """
    
active_color = 255
def draw(feld):
    screen.fill((0, 0, 100))
    for i in range(0, 80):
        for e in range(0, 80):
            
            c = feld[(i*80) + e]
            color = None
            if c > 250:
                color = (0, 80, 0)
            #Farben
            elif c > 249:
               color = (0, 100, 0)
            elif c > 200:
                #color = (c * 0.3, 0, 0)
                color = (150, 150, 70)
            elif c > 150:
                #color = (c, 0, 0)
                color = (130, 130, 50)
            elif c > 100:
                color = (120, 120, 40)
            elif c > 50:
                #color = ((c*2)%255, (c*2)%255, 0)
                color = (0, 0, 110)
            elif c > 0:
                #color = ((c*4)%255, (c*4)%255, 0)
                color = (0, 0, 100)
        
            elif c < 0:
                color = (70, 70, 70)
            if c != 0:
                pygame.draw.rect(screen, color, [e * 10, i * 10, 10, 10])

    pygame.display.flip()
seed = 123
#118
#106
"""
def noise(zahl):
    seed = zahl
    seed *= 20
    seed = seed % 250

    return seed
"""

for i in range(0, 80):
    for e in range(0, 80):
        feld.append(0)
color = None
key = None
pos = None
click = None

while running:
        
    key = pygame.key.get_pressed()
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (key[pygame.K_z]):
        click = [1]
        pos = (400, 700)
    if (key[pygame.K_HASH]) and (key[pygame.K_r]):
        feld = refresh(feld)
        draw(feld)
    if (key[pygame.K_p]):
        draw(feld)
    if (key[pygame.K_o]):
        for i in range(0, len(feld)):
            feld[i] = active_color
        screen.fill((active_color, active_color, active_color))
        pygame.display.flip()
    if (key[pygame.K_w]):
        for i in range(0, len(feld)):
            feld[i] = 0
        screen.fill((0, 0, 0))
        pygame.display.flip()
    if (key[pygame.K_e]):
        drawer = refresh(feld)

        drawer = refresh(drawer)
        draw(drawer)
    if click[0] == 1 or (key[pygame.K_s]) and not (key[pygame.K_HASH]):
        feld[(int(pos[1]/10) * 80) + int(pos[0]/10)] += active_color
        drawer = refresh(feld)
        for i in range(1):
            drawer = refresh(drawer)
        
        #feld = refresh(feld)


        #Malen
        
        """screen.fill((0, 0, 0))
        for i in range(0, 80):
            for e in range(0, 80):
                
                c = feld[(i*80) + e]
                if c > 255:
                    c = 255
                if c < 0:
                    c = 0
                color = (c, c , c)
                if c > 0:
                    pygame.draw.rect(screen, color, [e * 10, i * 10, 10, 10])

        pygame.display.flip()"""
        if not (key[pygame.K_p]):
            draw(drawer)
        else:
            draw(feld)
        
    #Farben ändern
    if (key[pygame.K_1]):
        active_color = 50
    elif (key[pygame.K_0]):
        active_color = -50
    elif (key[pygame.K_2]):
        active_color = 100
    elif (key[pygame.K_3]):
        active_color = 150
    elif (key[pygame.K_4]):
        active_color = 200
    elif (key[pygame.K_5]):
        
        active_color = 255
  
    if (key[pygame.K_RIGHT]):
        seed += 1
        for i in range(0, 80):
            for e in range(0, 80):
                c = noise_2d(e, i, seed)
                if c < 200:
                    c = 0
                feld[i*80 + e] = c

        draw(feld)
        pygame.time.delay(500)
    if (key[pygame.K_LEFT]):
        seed -= 1
        for i in range(0, 80):
            for e in range(0, 80):
                c = noise_2d(e, i, seed)
                if c < 200:
                    c = 0
                feld[i*80 + e] = c

        draw(feld)
        pygame.time.delay(500)
    if (key[pygame.K_h]):
        print(seed)
        pygame.time.delay(1000)
    if (key[pygame.K_n]):
        for i in range(0, len(feld)):
            feld[i] = 0
        for i in range(0, 80):
            for e in range(0, 80):
                c = noise_2d(e, i, seed)
                if c < 200:
                    c = 0
                feld[i*80 + e] = c

        draw(feld)
        pygame.time.delay(500)
    if (key[pygame.K_HASH]) and (key[pygame.K_s]):
        file = open(save_path, 'w')
        file.write("")
        file = open(save_path, 'a')
        file.write("feld = [")
        
        for i in range(0, len(feld)):
            file.write("{}".format(feld[i]))
            if i < len(feld) - 1:
                file.write(", ")
            if i%40 == 1:
                file.write("\n")
        file.write("]")
        for i in range(0, len(feld)):
            feld[i] = 0
        pygame.time.delay(1000)
        draw(feld)
    

    
        
    if (key[pygame.K_HASH]) and (key[pygame.K_l]):
        file = open(save_path, "r")
        exec(file.read())
        drawer = refresh(feld)
        drawer = refresh(drawer)
        draw(drawer)
    

        
            

        

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            running = False
    
        

