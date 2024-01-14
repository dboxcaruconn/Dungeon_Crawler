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

        # Custom Font
        font_name = 'SOURCESANSPRO-REGULAR.OTF'
        font_path = os.path.join(os.path.dirname(__file__), font_name)
        self.custom_font = pygame.font.Font(font_path, 20)
        
        # Custom Title Font
        title_font_name = 'GENOGRUNGE.OTF'
        title_font_path = os.path.join(os.path.dirname(__file__), title_font_name)
        self.custom_title_font = pygame.font.Font(title_font_path, 36)

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

        pane_ratios = [
            (1, 2),  # width ratio (Heroes,Exploration)
            (2, 1),  # height ratio (Heroes,Journal)
        ]

        total_width_ratio = sum(pane_ratios[0])
        total_height_ratio = sum(pane_ratios[1])
        
        left_pane_width = self.SCREEN_WIDTH * pane_ratios[0][0] // total_width_ratio
        right_pane_width = self.SCREEN_WIDTH * pane_ratios[0][1] // total_width_ratio
        top_pane_height = self.SCREEN_HEIGHT * pane_ratios[1][0] // total_height_ratio
        bottom_pane_height = self.SCREEN_HEIGHT * pane_ratios[1][1] // total_height_ratio

        pane_sizes = [
            (left_pane_width, top_pane_height),  # "Heroes"
            (right_pane_width, top_pane_height),  # "Exploration"
            (left_pane_width, bottom_pane_height),  # "Journal"
            (right_pane_width, bottom_pane_height)   # "Inventory"
        ]

        pane_positions = [
            (0, 0),  # x, y for "Heroes"
            (left_pane_width, 0),  # x, y for "Exploration"
            (0, top_pane_height),  # x, y for "Journal"
            (left_pane_width, top_pane_height)  # x, y for "Inventory"
        ]

        self.panes = [
            #Hero Pane:
            Pane(pane_positions[0][0], pane_positions[0][1], pane_sizes[0][0], pane_sizes[0][1], colors[0], "Heroes"),
            #Exploration Pane:
            Pane(pane_positions[1][0], pane_positions[1][1], pane_sizes[1][0], pane_sizes[1][1], colors[1], "Exploration"),
            #Journal Pane:
            Pane(pane_positions[2][0], pane_positions[2][1], pane_sizes[2][0], pane_sizes[2][1], colors[1], "Journal"),
            #Inventory Pane:
            Pane(pane_positions[3][0], pane_positions[3][1], pane_sizes[3][0], pane_sizes[3][1], colors[0], "Inventory")
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
            pane.draw(self.screen, self.custom_title_font)
        
        # Draw the button
        self.close_button.draw(self.screen, pygame.mouse.get_pos())

        pygame.display.update()
