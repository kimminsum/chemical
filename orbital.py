import pygame,random,time
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))
    a = random.randrange(1, 500)
    # Draw a solid blue circle in the center
    for i in range(2):

        pygame.draw.circle(screen, (0, 0, 255), (a, 250), 10)
        time.sleep(1)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()