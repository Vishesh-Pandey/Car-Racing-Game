# Developed By Vishesh Pandey
import pygame
import random

x = pygame.init()

white = (255 , 255 , 255 ) # Road
black = ( 0 , 0 , 0 ) # Road
red = (255 , 0 , 0 ) # opposite car
green = (0 , 255 , 0) # grass
silver = (192 , 192 , 192) # boundry
gray = (137 , 137 , 137)
darkGreen = ( 20 , 128 , 8 )
yellow = (247 , 247 , 11)
blue = ( 0 , 0 , 255 ) # this is users car
orange = (255,165,0) # this is fuel to increase the score

# orange - fuel

screen_width = 900
screen_height = 600

score = 0

clock = pygame.time.Clock()

gameWindow = pygame.display.set_mode(( screen_width , screen_height ))

pygame.display.set_caption("Car-Racing")

font = pygame.font.SysFont(None,55)

def textScreen(text,color,x,y):
    screen_text = font.render(text ,True,color)
    gameWindow.blit(screen_text, [x,y])

developerFont = pygame.font.SysFont(None,20)

def devScreen(text,color,x,y):
    dev_text = developerFont.render(text,True,color)
    gameWindow.blit(dev_text , [x,y])

class Zebra:
    def __init__(self , y ):
        self.y = y
        
    def moveZebra(self):
        self.y += 10
        
        if self.y > 700 :
            self.y = -100
        
    def plotZebra(self):
        pygame.draw.rect(gameWindow , "white" , [ 445 , self.y , 10 , 100 ])
        
zebra1 = Zebra(-100)        
zebra2 = Zebra(100)        
zebra3 = Zebra(300)        
zebra4 = Zebra(500)  

zebra = [zebra1 , zebra2 , zebra3 , zebra4]   

class Car:
    def __init__(self , color , x , y , height , width , speed):
        self.color = color 
        self.x = x 
        self.y = y
        self.height = height
        self.width = width
        self.speed = speed 
    
    def draw(self):
        pygame.draw.rect(gameWindow , self.color , [ self.x , self.y , self.height , self.width ])

    def move(self):
        if self.speed < 0 :
            return 
        
        self.y += self.speed
        
        if self.y > 700 :
            self.y = -150 
            self.x = random.randint(225 , 625)
            self.y += self.speed

car = Car(blue , 425 , 500 , 50 , 100 , -20)
car1 = Car(red , random.randint(225 , 625) , -100 , 50 , 100 , 20)
car2 = Car(gray , random.randint(225 , 625) , -350 , 50 , 100 , 20)
car3 = Car(yellow , random.randint(225 , 625) , -550 , 50 , 100 , 20)

opposite_cars = [car1 , car2 , car3]

class Fuel:
    def __init__(self , x , y ):
        self.x = x
        self.y = y
        
    def draw(self):
        pygame.draw.rect(gameWindow , orange , [self.x , self.y , 50 , 50] )

    def move(self):
        if (self.y > 600):
            self.y = -300
            self.x = random.randint(225 , 625)

        else:
            self.y += 10
            
fuel = Fuel(random.randint(225 , 625) , -300)

      
def reset():
    
    global score 
    score = 0
    
    car.x = 425
    car.y = 500
    
    car1.x = random.randint(225 , 625)
    car1.y = -100
    
    car2.x = random.randint(225 , 625)
    car2.y = -350
    
    car3.x = random.randint(225 , 625)
    car3.y = -550

class GreenLine:
    def __init__(self , x , y):
        self.x = x
        self.y = y
        
    def draw(self):
         pygame.draw.rect(gameWindow , darkGreen , [self.x , self.y , screen_width , 2])

    def move(self):
        if self.y > 600 :
            self.y = -20
            
        self.y += 10
        
greenLine1 = GreenLine(0 , 0)
greenLine2 = GreenLine(0 , 200)
greenLine3 = GreenLine(0 , 400)

greenLines = [greenLine1 , greenLine2 , greenLine3 ]

def drawBasicBackground():
     
    gameWindow.fill(green)
    
    for greenLine in greenLines:
        greenLine.draw()
        greenLine.move()
    
    pygame.draw.rect(gameWindow , black , [ 225 , 0 , 450 , 600 ])
    pygame.draw.rect(gameWindow , darkGreen , [215 , 0 , 10 , 600])
    pygame.draw.rect(gameWindow , darkGreen , [675 , 0 , 10 , 600])
    textScreen("Score : " + str(score * 10 ) , red , 5 , 5)
    devScreen("Developed by - Vishesh Pandey" , red , 695 , 575)
           
def draw():
    
    drawBasicBackground()
    
    for i in zebra:
        i.moveZebra()
        i.plotZebra()
        
    fuel.draw()
    fuel.move()  
    
    car.draw()
    
    for opposite_car in opposite_cars :
        opposite_car.move()
        opposite_car.draw()
        
    pygame.display.update()
        
def handle_car_movement(keys):
    if keys[pygame.K_d]:
        if car.x < 625 :
            car.x += 5
            
    if keys[pygame.K_a] :
        if car.x > 225 :
            car.x -= 5
            
    if keys[pygame.K_w] :
        if car.y > 0 :
            car.y -= 5
            
    if keys[pygame.K_s] :
        if car.y < 500 :
            car.y += 5 
     
# Creating a game loop
def gameloop():
    
    global score 
    
    reset()

    exit_game = False
    game_over = False
          
    fps = 25

    while not exit_game : # condition to not exit the game

        if game_over :
            # gameWindow.fill(white)
            textScreen(" Game Over ! Press Enter to Restart ", red , 100, 250 )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
      
        else:
            
            # handling the event in the pygame
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True   
                    
            keys = pygame.key.get_pressed()
            handle_car_movement(keys)
                
            draw()

            #Condition to Increase the score------
            if abs(car.x - fuel.x)<50 and abs(car.y - fuel.y)<50 :
                score +=1
                fuel.y = -300
                fuel.x = random.randint(225 , 625)

            # Conditions for gameOver--------------------------
            for i in opposite_cars :
                if abs(car.x - i.x) < 50 and abs(car.y - i.y)<50 :
                    game_over = True
                    break

        clock.tick(fps)
            
    pygame.quit()
    quit()

gameloop()