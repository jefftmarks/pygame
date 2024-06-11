import pygame

# Initialize pygame
pygame.init()

# Create display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Text")

COLORS = {
	"BLACK": (0, 0, 0),
	"GREEN": (0, 255, 0),
	"DARK_GREEN": (10, 50, 10)
}

# See all available system fonts
fonts = pygame.font.get_fonts()
for font in sorted(fonts):
	print(font)

# Define fonts
system_font = pygame.font.SysFont('calibri', 64)
custom_font = pygame.font.Font('assets/AttackGraffiti.ttf', 32)

# Define text
system_txt = system_font.render('Dragons Rule', True, COLORS["GREEN"], COLORS["DARK_GREEN"])
system_txt_rect = system_txt.get_rect()
system_txt_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

custom_txt = custom_font.render('Move the dragon soon!', True, COLORS["GREEN"])
custom_txt_rect = custom_txt.get_rect()
custom_txt_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100)

# Main game loop
running = True
while running:
    # Loop through list of event objects
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# Blit text surface
		display_surface.blit(system_txt, system_txt_rect)
		display_surface.blit(custom_txt, custom_txt_rect)

		# Update the display
		pygame.display.update()
				
# End the game
pygame.quit()