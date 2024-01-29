import pygame
import pygame_gui

import path_defs
import button_config
from pane_class import Pane
from button_class import Button

class GameManager:

    def __init__(self):
        pygame.init()

        # Screen Information
        screen_info = pygame.display.Info()
        pygame.display.quit()

        self.SCREEN_WIDTH = screen_info.current_w
        self.SCREEN_HEIGHT = screen_info.current_h
        self.scale = self.SCREEN_HEIGHT // 720

        # Setup the main screen
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.SRCALPHA)
        pygame.display.set_caption("DUNGEON CRAWLER")

        # UIManager
        self.manager = pygame_gui.UIManager((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # Clock
        self.clock = pygame.time.Clock()

        # Custom Fonts
        self.custom_font = path_defs.font_path('JUSTMB__.TTF', 16*self.scale)
        self.custom_title_font = path_defs.font_path('Draconis.otf', 28*self.scale)

        # Panes and other UI elements
        self._initialize_panes()

        # Locate the Panes
        heroes_pane = next(pane for pane in self.panes if pane.title == "Heroes")
        journal_pane = next(pane for pane in self.panes if pane.title == "Journal")
        inventory_pane = next(pane for pane in self.panes if pane.title == "Inventory")
        exploration_pane = next(pane for pane in self.panes if pane.title == "Exploration")
        
        pane_dict = {'heroes_pane_x': heroes_pane.x, 'heroes_pane_y': heroes_pane.y,
                     'journal_pane_x': journal_pane.x, 'journal_pane_y': journal_pane.y,
                     'inventory_pane_x': inventory_pane.x, 'inventory_pane_y': inventory_pane.y,
                     'exploration_pane_x': exploration_pane.x, 'exploration_pane_y': exploration_pane.y
                     }
        
        # Close Game Button
        close_button_config = button_config.close_game_button_config(
            self.scale, self.custom_font, pane_dict)
        self.close_game_button = Button(**close_button_config)
        
        # Max Heroes Pane Button
        max_heroes_pane_button_config = button_config.max_heroes_pane_button_config(
            self.scale, self.custom_font, pane_dict)
        self.max_heroes_pane_button = Button(**max_heroes_pane_button_config)


    def _initialize_panes(self):
        colors = [(155, 155, 130),  # Lighter Grey
                  (145, 145, 120)]  # Grey

        pane_ratios = [
            (1, 2), # width ratio   (Heroes, Exploration)
            (2,     # height        (Heroes,
             1),    # ratio          Journal)
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
            Pane(self.scale, pane_positions[0][0], pane_positions[0][1], 
                 pane_sizes[0][0], pane_sizes[0][1], colors[0], "Heroes"),
            #Exploration Pane:
            Pane(self.scale, pane_positions[1][0], pane_positions[1][1], 
                 pane_sizes[1][0], pane_sizes[1][1], colors[1], "Exploration"),
            #Journal Pane:
            Pane(self.scale, pane_positions[2][0], pane_positions[2][1], 
                 pane_sizes[2][0], pane_sizes[2][1], colors[1], "Journal"),
            #Inventory Pane:
            Pane(self.scale, pane_positions[3][0], pane_positions[3][1], 
                 pane_sizes[3][0], pane_sizes[3][1], colors[0], "Inventory")
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
            #pygame.display.flip()

        pygame.quit()

    def _handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            #Close Game Button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.close_game_button.is_clicked(mouse_pos):
                    return False
            self.manager.process_events(event)
        return True

    def _draw(self):
        self.screen.fill((0, 0, 0))  # Clear screen
        for pane in self.panes:
            pane.draw(self.screen, self.custom_title_font)
        
        # Draw the button
        self.close_game_button.draw(self.screen, pygame.mouse.get_pos())
        self.max_heroes_pane_button.draw(self.screen, pygame.mouse.get_pos())

        pygame.display.update()