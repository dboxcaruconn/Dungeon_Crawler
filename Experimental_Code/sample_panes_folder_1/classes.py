import pygame
import pygame_gui
import os

# pane class to manage each GUI pane
class Pane:
    def __init__(self, x, y, width, height, color, title):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.title = title

    # draw method to draw the pane
    def draw(self, screen, font):  # Make sure 'font' parameter is included here
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        text = font.render(self.title, True, (0, 0, 0))  # Use the passed 'font' to render the title
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + 20))  # Adjusted y-position
        screen.blit(text, text_rect)


# Button class to manage each button
class Button:
    def __init__(self, x, y, width, height, text, font, button_color, hover_color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.button_color = button_color
        self.hover_color = hover_color
        self.text_color = text_color

    def draw(self, screen, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.button_color, self.rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

