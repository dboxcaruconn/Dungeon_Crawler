# Simple pygame program

# Import and initialize the pygame library
import pygame
import pygame_gui
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

# Set window dimensions to the screen's dimensions
initial_width = screen_info.current_w
initial_height = screen_info.current_h
#initial_width = 800
#initial_height = 600

# Set up the drawing window with the screen's dimensions
screen = pygame.display.set_mode((initial_width, initial_height),pygame.FULLSCREEN)

# Create a UIManager instance
manager = pygame_gui.UIManager((initial_width, initial_height))

# Define the button attributes
button_color = (0, 200, 0)  # Green color
button_hover_color = (0, 255, 0)  # Brighter green
text_color = (255, 255, 255)  # White color
button_rect = pygame.Rect(initial_width // 2 - 50, initial_height // 2 - 25, 100, 50)
button_font = pygame.font.Font(None, 36)

# Dropdown menu data
dropdown_options = ['0.5', '0.75', '1.0', '1.25', '1.5', '1.75', '2.0']
dropdown_rect = pygame.Rect(50, 50, 100, 30)

# Create the Dropdown
dropdown_menu = pygame_gui.elements.UIDropDownMenu(options_list=dropdown_options, 
                                                   starting_option='1.0',
                                                   relative_rect=dropdown_rect,
                                                   manager=manager)

# Run until the user asks to quit
clock = pygame.time.Clock()
running = True
while running:

    time_delta = clock.tick(60)/1000.0

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Fill the background with black
    screen.fill((0, 0, 0))

# EVENTS
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
        # Process UI events
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == dropdown_menu:
                    scale_option = float(event.text)
                    screen_width = int(initial_width * scale_option)
                    screen_height = int(initial_height * scale_option)
                    screen = pygame.display.set_mode((screen_width, screen_height))

        manager.process_events(event)

    # Update the UI
    manager.update(time_delta)

    manager.draw_ui(screen)

    # Draw the button
    button_current_color = button_color if not button_rect.collidepoint(mouse_pos) else button_hover_color
    pygame.draw.rect(screen, button_current_color, button_rect)

    # Draw the text on the button
    text_surface = button_font.render('Close', True, text_color)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    # Flip the display
    pygame.display.flip()

# Clean up before quitting (remove lock file and close)
single_instance.clean_up()
pygame.quit()
