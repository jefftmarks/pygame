import pygame
import random

# Initialize pygame
pygame.init()

# Create display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Collision Detection")

# Define clocok
FPS = 60
clock = pygame.time.Clock()

# Set game values
VELOCITY = 5

# Load in images
dragon_img = pygame.image.load('assets/dragon_right.png')
dragon_rect = dragon_img.get_rect()
dragon_rect.topleft = (25, 25)

coin_img = pygame.image.load('assets/coin.png')
coin_rect = coin_img.get_rect()
coin_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

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
    if keys[pygame.K_LEFT]:
        dragon_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT]:
         dragon_rect.x += VELOCITY
    if keys[pygame.K_UP]:
         dragon_rect.y -= VELOCITY
    if keys[pygame.K_DOWN]:
         dragon_rect.y += VELOCITY

    # Check for collision between two rects
    if dragon_rect.colliderect(coin_rect):
        coin_rect.x = random.randint(0, WINDOW_WIDTH - 32)
        coin_rect.y = random.randint(0, WINDOW_HEIGHT - 32)

    # Fill the display surface to cover old images
    display_surface.fill((0, 0, 0))

    # Draw rectangles
    pygame.draw.rect(display_surface, (255, 0, 0), dragon_rect, 1)
    pygame.draw.rect(display_surface, (255, 255, 0), coin_rect, 1)

    # Blit assets
    display_surface.blit(dragon_img, dragon_rect)
    display_surface.blit(coin_img, coin_rect)

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)
				
# End the game
pygame.quit()