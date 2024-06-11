import pygame

# Initialize pygame
pygame.init()

# Create display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hello World")

# Main game loop
running = True
while running:
    # Loop through list of event objects
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				running = False
				
#End the game
pygame.quit()
