import pygame

# Initialize pygame
pygame.init()

# Create display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Images")

# Load images... returns surface objects with the image drawn on it
# We can then get the rect of the surface and use the rect to position the image
dragon_left_img = pygame.image.load("assets/dragon_left.png")
dragon_left_rect = dragon_left_img.get_rect()
dragon_left_rect.topleft = (0,0)

dragon_right_img = pygame.image.load("assets/dragon_right.png")
dragon_right_rect = dragon_right_img.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)


# Main game loop
running = True
while running:
    # Loop through list of event objects
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# Blit surface object
		display_surface.blit(dragon_left_img, dragon_left_rect)
		display_surface.blit(dragon_right_img, dragon_right_rect)

		pygame.draw.line(display_surface, (255,255,255), (0, 75), (WINDOW_WIDTH, 75), 4)

		# Update the display
		pygame.display.update()
				
#End the game
pygame.quit()