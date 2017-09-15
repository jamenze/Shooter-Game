# We have access to pygame, because we did:
# $ pip install pygame
# It is NOT part of core. This is a 3rd party module.

import pygame

# Custom Classes:
from Player import Player
from Bad_guy import Bad_guy

# Have to init the pygame object so we can use it.
pygame.init()

# Set up screen size (as a tuple):
screen_size = (1000, 800)

# Because we are going to paint the background,
# we need a tuple for the color:
background_color = (82, 111, 53) # RGB

# Make a screen object / Create a screen for
# pygame to use to draw on:
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("An epic shooter made with python") # Screen title

the_player = Player('pikachu.png', 100, 100, screen)
bad_guy = Bad_guy(screen)

# the_player_image = pygame.image.load('pikachu.png')
# player = {
# 	"x": 100,
# 	"y": 100
# }

# the_bad_guy = pygame.image.load('')

game_on = True

# Set up the main game loop:
while game_on: 	# Will run forever (until break)
	
	# Loop through all the pygame events.
	# This is pyagme's escape hatch (Quit)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False
		elif event.type == pygame.KEYDOWN:
			print event.key
			# print "User pressed a key!!!"
			if event.key == 273:
				# user pressed up!
				# the_player.y -= the_player.speed
				the_player.should_move("up",True)
			elif event.key == 274:
				# the_player.y += the_player.speed
				the_player.should_move("down",True)
			if event.key == 275:
				# the_player.x += the_player.speed
				the_player.should_move("right",True)
			elif event.key == 276:
				# the_player.x -= the_player.speed
				the_player.should_move("left",True)
		elif event.type == pygame.KEYUP:
			if event.key == 273:
				the_player.should_move("up",False)
			elif event.key == 274:
				the_player.should_move("down",False)
			if event.key == 275:
				the_player.should_move("right",False)
			elif event.key == 276:
				the_player.should_move("left",False)


	# Paint the screen:
	screen.fill(background_color)

	# Update the bad guy based on where the player is:
	bad_guy.update_me(the_player) #pass it the player

	# Draw the bad guy
	bad_guy.draw_me() # don't have to pass it anything


	# # MUST be after fill, or we won't be able to see character
	# screen.blit(the_player.image, [player["x"], player["y"]])
	the_player.draw_me()

	# Flip the screen i.e. clear it so we can draw again and again
	pygame.display.flip()



