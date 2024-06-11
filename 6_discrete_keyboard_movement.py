import pygame

# Initialize pygame
pygame.init()

# Create display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Discrete Movement")

# Set game values
VELOCITY = 30

# Load in images
dragon_img = pygame.image.load('assets/dragon_right.png')
dragon_rect = dragon_img.get_rect()
dragon_rect.centerx = WINDOW_WIDTH // 2
dragon_rect.bottom = WINDOW_HEIGHT

# Main game loop
running = True
while running:
    # Loop through list of event objects
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				
				# Check for discrete movement
				if event.type == pygame.KEYDOWN:
						match event.key:
							case pygame.K_LEFT:
								dragon_rect.x -= VELOCITY
							case pygame.K_RIGHT:
								dragon_rect.x += VELOCITY
							case pygame.K_UP:
								dragon_rect.y -= VELOCITY
							case pygame.K_DOWN:
								dragon_rect.y += VELOCITY

		# Fill the display surface to cover old images
		display_surface.fill((0, 0, 0))

		# Blit assets
		display_surface.blit(dragon_img, dragon_rect)

		# Update the display
		pygame.display.update()
				
# End the game
pygame.quit()