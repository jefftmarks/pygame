import pygame

# Initialize pygame
pygame.init()

# Create display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Restricted Movement")

# Define clocok
FPS = 60
clock = pygame.time.Clock()

# Set game values
VELOCITY = 5

# Load in images
dragon_img = pygame.image.load('assets/dragon_right.png')
dragon_rect = dragon_img.get_rect()
dragon_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Main game loop
running = True
while running:
    # Loop through list of event objects
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Get keys currently pressed down 
    keys = pygame.key.get_pressed()
    
    # Move dragon continuously
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.left > 0:
        dragon_rect.x -= VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.right < WINDOW_WIDTH:
         dragon_rect.x += VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_rect.top > 0:
         dragon_rect.y -= VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_rect.bottom < WINDOW_HEIGHT:
         dragon_rect.y += VELOCITY

    # Fill the display surface to cover old images
    display_surface.fill((0, 0, 0))

    # Blit assets
    display_surface.blit(dragon_img, dragon_rect)

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)
				
# End the game
pygame.quit()