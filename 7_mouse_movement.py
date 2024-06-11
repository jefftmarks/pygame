import pygame

# Initialize pygame
pygame.init()

# Create display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mouse Movement")

# Set game values
VELOCITY = 30

# Load in images
dragon_img = pygame.image.load('assets/dragon_right.png')
dragon_rect = dragon_img.get_rect()
dragon_rect.topleft = (25, 25)


def map_dragon_to_mouse():
    mouse_xy = event.pos
    dragon_rect.centerx, dragon_rect.centery = mouse_xy


# Main game loop
running = True
while running:
    # Loop through list of event objects
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False	
				elif (
					event.type == pygame.MOUSEBUTTONDOWN or
					(event.type == pygame.MOUSEMOTION and event.buttons[0] == 1)
                ):
					map_dragon_to_mouse()
					
        # Fill the display
		display_surface.fill((0, 0, 0))

		# Blit assets
		display_surface.blit(dragon_img, dragon_rect)

		# Update the display
		pygame.display.update()
				
# End the game
pygame.quit()