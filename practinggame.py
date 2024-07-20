import math 
import random
import time
import pygame 
pygame.init()

#variables
WIDTH, HEIGHT = 800, 600
APPLE_EVENT = pygame.USEREVENT
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
LABEL_FONT = pygame.font.SysFont("pixelfy sans", 50) #creates font object
COLORS = ["fuchsia", "cyan", "springgreen", "yellow", "orange",  "white", "blue", "magenta", "violet", "palegreen", "gold", "pink" ]
USER_COLOR = random.randint(0, len(COLORS)-1)
KILLER_COLOR = random.randint(0,len(COLORS)-1)
BACKGROUND = "darkblue"
BORDER_PADDING = 30


class Square:
    LENGTH = 30 

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.LENGTH, self.LENGTH)

    def drawSquare(self, window):
        pygame.draw.rect(window, COLORS[USER_COLOR], self.rect)

class Apple:
    LENGTH = 30
    STEM_LEGNTH = 5

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x,self.y,self.LENGTH,self.LENGTH)
    
    def drawApple(self, window):
        pygame.draw.rect(window, "red", (self.x-5,self.y+5,self.LENGTH,20))
        pygame.draw.rect(window, "red", (self.x + 5 ,self.y+5,self.LENGTH,20))
        pygame.draw.rect(window, "red", self.rect)
        pygame.draw.rect(window, "saddlebrown", (self.x + 12.5 ,self.y - 8 ,5,10))
        pygame.draw.rect(window, "green", (self.x + 17.5,self.y - 5,5,5))
        pygame.draw.rect(window, "green", (self.x + 21.5,self.y-10,5,5))

class Killer:
    LENGTH = 30 

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.LENGTH, self.LENGTH)
    
    def drawKiller(self, window):
        pygame.draw.rect(window, COLORS[KILLER_COLOR] ,self.rect)


def drawK(window, killer):
    killer.drawKiller(window)

def drawS(window, square):
    square.drawSquare(window)

def drawA(window, apples):
    for obj in apples:
        obj.drawApple(window)

def format_time(secs):
    milli = math.floor(int(secs * 1000 % 1000) / 100) 
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60) 
    return f"{minutes:02d}:{seconds:02d}:{milli: 02d}"

def get_middle(surface):
    return WIDTH / 2 - surface.get_width()/2

def end_screen(window, elapsed_time, collected, arraylen):
    window.fill("blue")
    time_label = LABEL_FONT.render(f"You survived for: {format_time(elapsed_time)}", 1, "white") #render font obj
    collected_label = LABEL_FONT.render(f"You collected: {collected} apples!", 1, "white") #render font obj
    if(arraylen >= 10):
        failed_label = LABEL_FONT.render(f"Oh no! You left too many apples out to rot.", 1, "white") #render font obj
        window.blit(failed_label, (get_middle(failed_label),150))

    window.blit(time_label, (get_middle(time_label),225))
    window.blit(collected_label, (get_middle(collected_label),325))

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

def main():
    run = True
    increment = 10
    apples=[]
    collected = 0
    start_time = time.time()

    x, y = random.randint(BORDER_PADDING, WIDTH-BORDER_PADDING), random.randint(BORDER_PADDING, HEIGHT-BORDER_PADDING)
    i, j = random.randint(BORDER_PADDING, WIDTH-BORDER_PADDING),random.randint(BORDER_PADDING, HEIGHT-BORDER_PADDING) 

    clock = pygame.time.Clock() #clock object from time module
    pygame.time.set_timer(APPLE_EVENT, 1500)
    
    while run:
        WINDOW.fill(BACKGROUND)
        clock.tick(30)
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == APPLE_EVENT:
                a, b =random.randint(BORDER_PADDING, WIDTH - BORDER_PADDING),random.randint(BORDER_PADDING, HEIGHT - BORDER_PADDING)
                ap = Apple(a,b)
                apples.append(ap)


        keys = pygame.key.get_pressed()
        if pygame.KEYDOWN:
            a, b = random.choice([-30,30]), random.choice([-30, 30])
            if a + i >= WIDTH or b + j >= HEIGHT or a + i <= 0 or b + j <= 0:
                i -= a
                j -= b
            else: 
                i += a
                j += b

        if keys[pygame.K_LEFT]:
            x -= increment
        if keys[pygame.K_RIGHT]:
            x += increment
        if keys[pygame.K_UP]:
            y -= increment
        if keys[pygame.K_DOWN]:
            y += increment

        for obj in apples:
            if pygame.Rect.colliderect(obj.rect, user.rect):
                apples.remove(obj)
                collected += 1 
            if pygame.Rect.colliderect(killer.rect, user.rect) or len(apples) >= 10:
                end_screen(WINDOW, elapsed_time, collected, len(apples)) 

        user = Square(x,y)
        killer = Killer(i,j)        
        drawS(WINDOW,user)
        drawK(WINDOW, killer)
        drawA(WINDOW, apples)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main() 