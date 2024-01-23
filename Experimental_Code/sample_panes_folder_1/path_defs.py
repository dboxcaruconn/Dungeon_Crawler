import pygame
import os

def button_icon_path(file_name):
    button_icons_folder = 'Icons_Buttons'
    icon_path = os.path.join(os.path.dirname(__file__), button_icons_folder, file_name)
    loaded_icon = pygame.image.load(icon_path).convert_alpha()
    return loaded_icon

def font_path(font_name, font_size, fonts_folder='Fonts'):
    font_path = os.path.join(os.path.dirname(__file__), fonts_folder, font_name)
    return pygame.font.Font(font_path, font_size)
