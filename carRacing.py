# Developed By Vishesh Pandey
import pygame
import random

x = pygame.init()

white = (255 , 255 , 255 ) # Road
black = ( 0 , 0 , 0 ) # Road
red = (255 , 0 , 0 ) # opposite car
green = (0 , 255 , 0) # grass
silver = (192 , 192 , 192) # boundry
darkGray = ( 169 , 169 , 169)
gray = (137 , 137 , 137)
darkGreen = ( 20 , 128 , 8 )
yellow = (247 , 247 , 11)
blue = ( 0 , 0 , 255 ) # this is users car
orange = (255,165,0) # this is fuel to increase the score

# orange - fuel

screen_width = 900
screen_height = 600

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

def plot_car(gameWindow , color , car_x , car_y , car_size_y , car_size_x):
    pygame.draw.rect(gameWindow , color , [ car_x , car_y , car_size_y , car_size_x ])

def plot_fuel(gameWindow , color , fuel_x , fuel_y):
    pygame.draw.rect(gameWindow , color , [ fuel_x , fuel_y , 50,50 ])

def plot_object(gameWindow , color , object_position_x , object_position_y , object_size_x , object_size_y):
    pygame.draw.rect(gameWindow , color , [object_position_x , object_position_y , object_size_x , object_size_y])

def plot_opposite_car(gameWindow , color , opposite_car_x , opposite_car_y):
    pygame.draw.rect(gameWindow , color , [ opposite_car_x , opposite_car_y , 50 , 100])

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

class Car:
    def __init__(self , color , x , y , height , width ):
        self.color = color 
        self.x = x 
        self.y = y
        self.height = height
        self.width = width
    
    def draw(self):
        pygame.draw.rect(gameWindow , self.color , [ self.x , self.y , self.height , self.width ])

    def move(self):
        self.y += 20
        
        if self.y > 700 :
            self.y = -150 
            self.x = random.randint(225 , 625)
            self.y += 20
            
car1 = Car(red , random.randint(225 , 625) , -100 , 50 , 100)
car2 = Car(gray , random.randint(225 , 625) , -350 , 50 , 100)
car3 = Car(yellow , random.randint(225 , 625) , -550 , 50 , 100)

opposite_cars = [car1 , car2 , car3]

def drawCar():
    
    car1.move()
    car1.draw()
    
    car2.move()
    car2.draw()
    
    car3.move()
    car3.draw()

def zebraPlot():
                
    zebra1.moveZebra()
    zebra1.plotZebra()
    
    zebra2.moveZebra()
    zebra2.plotZebra()
    
    zebra3.moveZebra()
    zebra3.plotZebra()
    
    zebra4.moveZebra()
    zebra4.plotZebra()
       
def reset():
    car1.x = random.randint(225 , 625)
    car1.y = -100
    
    car2.x = random.randint(225 , 625)
    car2.y = -350
    
    car3.x = random.randint(225 , 625)
    car3.y = -550

# Creating a game loop
def gameloop():
    
    reset()

    exit_game = False
    game_over = False

    # Properties of the users car
    car_position_x = 425 
    car_position_y = 500
    car_size_x = 50
    car_size_y = 100

    # Properties of the objects comming from the front
    object_position_x = 0
    object_position_y = 0

    object1_position_x = 0
    object1_position_y = 200

    object2_position_x = 0
    object2_position_y = 400

    object3_position_x = 0
    object3_position_y = 0

    object4_position_x = 0
    object4_position_y = 200

    object5_position_x = 0
    object5_position_y = 400
    

    # Properties of fuel
    fuel_position_x = random.randint(225 , 625)
    fuel_position_y = -300
        
    fps = 25

    object_position_x = random.randint(20 , screen_width/2)
    object_position_y = -50

    score = 0

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

                # this code will detect weather you have clicked any key or not
                if event.type == pygame.KEYDOWN:

                    # this will actually detect which key you have clicked
                    # + this will start moving the car

                    if event.key == pygame.K_d:
                        if car_position_x < 625 :
                            car_position_x += 20

                    if event.key == pygame.K_a:
                        if car_position_x > 225 :
                            car_position_x -= 20

                    if event.key == pygame.K_w:
                        if car_position_y > 0 :
                            car_position_y -= 20

                    if event.key == pygame.K_s:
                        if car_position_y < 500 :
                            car_position_y += 20
                

            gameWindow.fill(green)
            pygame.draw.rect(gameWindow , black , [ 225 , 0 , 450 , 600 ])
            pygame.draw.rect(gameWindow , darkGreen , [215 , 0 , 10 , 600])
            pygame.draw.rect(gameWindow , darkGreen , [675 , 0 , 10 , 600])

            textScreen("Score : " + str(score * 10 ) , red , 5 , 5)
            devScreen("Developed by - Vishesh Pandey" , red , 695 , 575)

            # Plotting the zebra to show car is moving ------------
      
            zebraPlot()

       
            

            #Moving Objects------------------

            if ( object_position_y > 620 ):
                object_position_y = -20
                plot_object(gameWindow, darkGreen , 635 , object_position_y , 250 , 2)
                object_position_y += 10

            plot_object(gameWindow, darkGreen , 685 , object_position_y , 250 , 2)
            object_position_y += 10

            if ( object1_position_y > 620 ):
                object1_position_y = -20
                plot_object(gameWindow, darkGreen , 635 , object1_position_y , 250 , 2)
                object1_position_y += 10

            plot_object(gameWindow, darkGreen , 685 , object1_position_y , 250 , 2)
            object1_position_y += 10

            if ( object2_position_y > 620 ):
                object2_position_y = -20
                plot_object(gameWindow, darkGreen , 635 , object2_position_y , 250 , 2)
                object2_position_y += 10

            plot_object(gameWindow, darkGreen , 685 , object2_position_y , 250 , 2)
            object2_position_y += 10

            if ( object3_position_y > 620 ):
                object3_position_y = -20
                plot_object(gameWindow, darkGreen , 0 , object3_position_y , 215 , 2)
                object3_position_y += 10

            plot_object(gameWindow, darkGreen , 0 , object3_position_y , 215 , 2)
            object3_position_y += 10

            if ( object4_position_y > 620 ):
                object4_position_y = -20
                plot_object(gameWindow, darkGreen , 0 , object4_position_y , 215 , 2)
                object4_position_y += 10

            plot_object(gameWindow, darkGreen , 0 , object4_position_y , 215 , 2)
            object4_position_y += 10

            if ( object5_position_y > 620 ):
                object5_position_y = -20
                plot_object(gameWindow, darkGreen , 0 , object5_position_y , 215 , 2)
                object5_position_y += 10

            plot_object(gameWindow, darkGreen , 0 , object5_position_y , 215 , 2)
            object5_position_y += 10
            

            # Plotting the opposite car-----------
            drawCar()
            
  


            # Plotting the fuel -------------------

            plot_fuel(gameWindow , red , fuel_position_x , fuel_position_y )
            fuel_position_y += 20

            if ( fuel_position_y > 600 ):
                fuel_position_y = -300 
                fuel_position_x = random.randint(225 , 625)
                plot_fuel(gameWindow , orange , fuel_position_x , fuel_position_y )
                fuel_position_y += -10

            plot_fuel(gameWindow , orange , fuel_position_x , fuel_position_y )
            fuel_position_y += -10    

            #Condition to Increase the score------
            
            if abs(car_position_x - fuel_position_x)<50 and abs(car_position_y - fuel_position_y)<50 :
                score +=1
                fuel_position_y = -300
                fuel_position_x = random.randint(225 , 625)


            # Conditions for gameOver--------------------------
            
            for i in opposite_cars :
                if abs(car_position_x - i.x) < 50 and abs(car_position_y - i.y)<50 :
                    game_over = True
                    break
            

            if abs(car_position_x - object_position_x )<10 and abs(car_position_y - object_position_y)<10 :
                game_over = True

                
            #--------------------------------------------------------------------------------------------------------------

            plot_car(gameWindow , blue , car_position_x , car_position_y , car_size_x , car_size_y )

        pygame.display.update()
        clock.tick(fps)
            
    pygame.quit()
    quit()

gameloop()