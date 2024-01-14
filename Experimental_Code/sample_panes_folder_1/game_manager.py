import pygame
import pygame_gui
import os
from classes import Pane
from classes import Button

class GameManager:
    def __init__(self):
        pygame.init()

        # Screen Information
        temp_surface = pygame.display.set_mode((0, 0), pygame.HIDDEN)
        screen_info = pygame.display.Info()
        pygame.display.quit()

        self.SCREEN_WIDTH = screen_info.current_w
        self.SCREEN_HEIGHT = screen_info.current_h

        # Setup the main screen
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.DOUBLEBUF)
        pygame.display.set_caption("DUNGEON CRAWLER")

        # UIManager
        self.manager = pygame_gui.UIManager((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # Clock
        self.clock = pygame.time.Clock()

        # Custom Font (Ensure the font file is available in the same directory or adjust the path accordingly)
        font_name = 'GENOGRUNGE.OTF'
        font_path = os.path.join(os.path.dirname(__file__), font_name)
        self.custom_font = pygame.font.Font(font_path, 36)

        # Panes and other UI elements
        self._initialize_panes()
        
        # Locate the Panes
        hero_pane = next(pane for pane in self.panes if pane.title == "Heroes")
        journal_pane = next(pane for pane in self.panes if pane.title == "Journal")
        inventory_pane = next(pane for pane in self.panes if pane.title == "Inventory")
        exploration_pane = next(pane for pane in self.panes if pane.title == "Exploration")
        
        # Initialize the Close button
        self.close_button = Button(
            x=journal_pane.x + 20, y=journal_pane.y + 20, width=100, height=50, 
            text="Close Game", 
            font=self.custom_font, 
            button_color=(0, 200, 0), 
            hover_color=(0, 255, 0), 
            text_color=(255, 255, 255)
        )

    def _initialize_panes(self):
        colors = [(145, 145, 120), (0, 255, 0)]
        titles = ["Heroes", "Exploration", "Journal", "Inventory"]
        self.panes = [
            Pane(0, 0, self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2, colors[0], titles[0]),
            Pane(self.SCREEN_WIDTH // 2, 0, self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2, colors[1], titles[1]),
            Pane(0, self.SCREEN_HEIGHT // 2, self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2, colors[1], titles[2]),
            Pane(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2, self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2, colors[0], titles[3])
        ]

    def run(self):
        running = True
        while running:
            time_delta = self.clock.tick(60)/1000.0

            # Event handling
            running = self._handle_events()

            # Update the UI
            self.manager.update(time_delta)
            
            # Draw everything
            self._draw()

            # Update the display
            pygame.display.flip()

        pygame.quit()

    def _handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.close_button.is_clicked(mouse_pos):
                    return False
            self.manager.process_events(event)
        return True

    def _draw(self):
        self.screen.fill((0, 0, 0))  # Clear screen
        for pane in self.panes:
            pane.draw(self.screen, self.custom_font)
        
        # Draw the button
        self.close_button.draw(self.screen, pygame.mouse.get_pos())

        pygame.display.update()
