import pygame

# Initialize pygame
pygame.init()

# Create display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Adding Sound")

# Load sound effects
sound_1 = pygame.mixer.Sound('assets/sound_1.wav')
sound_2 = pygame.mixer.Sound('assets/sound_2.wav')

# Play the sound effects
sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)

# Change volume
sound_2.set_volume(.1)
sound_2.play()

# Load background music
pygame.mixer.music.load('assets/music.wav')

# Play and stop the music
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(1000)
sound_2.play()
pygame.time.delay(5000)
pygame.mixer.music.stop()

# Main game loop
running = True
while running:
    # Loop through list of event objects
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# Update the display
		pygame.display.update()
				
# End the game
pygame.quit()