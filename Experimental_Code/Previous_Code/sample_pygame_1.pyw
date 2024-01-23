# Simple pygame program

# Import and initialize the pygame library
import pygame
import os
import sys
import logging
import tempfile
import signal

# Ensure single instance
import single_instance

lock_file_path = single_instance.ensure_single_instance()
if not lock_file_path:
    sys.exit("Another instance of the game is already running.")
    
# Set the signal handler for termination signals
signal.signal(signal.SIGINT, single_instance.signal_handler)
signal.signal(signal.SIGTERM, single_instance.signal_handler)

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Clean up before quitting
single_instance.clean_up(lock_file_path)

pygame.quit()
