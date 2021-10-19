# Import 'random' module
import pygame,math

pygame.init()
screen = pygame.display.set_mode((400,600))

pygame.display.set_caption("Shooting Spaceship")
background_image = pygame.image.load("bg2.jpg").convert()
player_image = pygame.image.load("s4.png").convert_alpha()

# Load the "e3.png" and name it as 'enemy_image'


player=pygame.Rect(200,200,30,30)

# The following lines are commented as it is not required anymore
#WHITE=(255,255,255)
#enemy=pygame.Rect(100,100,30,30)

angle=0
change=0
distance=5
forward=False

# Create empty lists 'xvel','yvel','enemies'



# Create a variable 'enemycount' to store the count of enemies



# "for" loop to repeat the task

  # Create 10 'enemy' rectangles at random x,y coordinates
  
  # Assign 10 random values to 'xvel' in the range of -3 to 3
  
  

def newxy(x,y,distance,angle):
  angle=math.radians(angle+90)
  xnew=x+(distance*math.cos(angle))
  ynew=y-(distance*math.sin(angle))
  return xnew,ynew

while True:
  screen.blit(background_image,[0,0])
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      
    if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_LEFT:
          change = 6
       if event.key ==pygame.K_RIGHT:
        change = -6 
       if event.key == pygame.K_UP:
        forward = True
        
    if event.type == pygame.KEYUP:
      if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
          change = 0
      if event.key == pygame.K_UP:
        forward = False
        
  # Initialise 'i' to 0. 'i' is used as 'index' variable to access every element of 'xvel' and 'yvel'
   
   
  # For every 'enemy' in the 'enemies' list do the following
  for enemy in enemies:
      # Increment x-coordinate with 'xvel[i]'
      enemy.x=enemy.x + xvel[i]
      # Check if x-coordinate is less than -250 or greater than 650 and change direction
      if enemy.x < -250 or enemy.x > 650 :
        xvel[i] = -1*xvel[i]
      # Increment 'i' by '1'
      i+=1    
      # Display 'enemy_image' on 'enemy' rectangle on the screen
      screen.blit(enemy_image,enemy)  
     
  if forward:
      player.x,player.y=newxy(player.x, player.y, distance, angle)  
  if player.x<0:
      player.x=400
  if player.x>400:
      player.x=0
  if player.y<0:
      player.y=600
  if player.y>600:
      player.y=0
  angle = angle + change
  newimage=pygame.transform.rotate(player_image,angle) 
  screen.blit(newimage ,player)
  
  # The following line is commented as it is not required anymore
  #pygame.draw.rect(screen,WHITE,enemy)

  pygame.display.update()
  pygame.time.Clock().tick(30)
  
  
