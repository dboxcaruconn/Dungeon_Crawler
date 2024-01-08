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
single_instance.start()

# RUN THE GAME
pygame.init()

# Initialize a temporary window to get the screen information
temp_surface = pygame.display.set_mode((0, 0), pygame.HIDDEN)
screen_info = pygame.display.Info()
pygame.display.quit()

# Set window dimensions to half of the screen's dimensions
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Set up the drawing window with half the screen's dimensions
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Define the button attributes
button_color = (0, 200, 0)  # Green color
button_hover_color = (0, 255, 0)  # Brighter green
text_color = (255, 255, 255)  # White color
button_rect = pygame.Rect(screen_width // 2 - 50, screen_height // 2 - 25, 100, 50)
button_font = pygame.font.Font(None, 36)

# Red perimeter for debugging
pygame.draw.rect(screen, (0, 0, 255), button_rect)

# Run until the user asks to quit
running = True
while running:

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

# Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Allow exiting fullscreen with ESC key
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is within the button
            if button_rect.collidepoint(event.pos):
                running = False

    # Fill the background with black
    screen.fill((0, 0, 0))

    # Draw the button
    button_current_color = button_color if not button_rect.collidepoint(mouse_pos) else button_hover_color
    pygame.draw.rect(screen, button_current_color, button_rect)

    # Draw the text on the button
    text_surface = button_font.render('Close', True, text_color)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)
    
    # Flip the display
    pygame.display.flip()

# Clean up before quitting
single_instance.clean_up()
pygame.quit()
