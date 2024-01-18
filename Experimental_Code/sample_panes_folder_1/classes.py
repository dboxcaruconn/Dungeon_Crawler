import pygame
import time


# pane class to manage each GUI pane
class Pane:
    def __init__(self, scale, x, y, width, height, color, title):
        self.scale = scale
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
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.scale*8))  # Adjusted y-position
        screen.blit(text, text_rect)


# Button class to manage each button
class Button:
    def __init__(self, scale, x, y, width, height, button_color, hover_color, 
                 text_color=(0, 0, 0), text=None, font=None, 
                 hover_text=None, image=None):
        self.scale = scale
        self.rect = pygame.Rect(x, y, width, height)
        self.button_color = button_color
        self.hover_color = hover_color
        self.text = text
        self.font = font
        self.text_color = text_color
        self.hover_text = hover_text
        self.image = pygame.transform.scale(image, (width, height)) if image else None
        self.hover_start_time = None

    def is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)
    
    def draw(self, screen, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.button_color, self.rect)

        if self.image:
            screen.blit(self.image, (self.rect.x, self.rect.y))

        if self.text:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)
        
        if self.is_hovered():
            if self.hover_start_time is None:
                self.hover_start_time = time.time()
            elif time.time() - self.hover_start_time > 0.1:  # 100 milliseconds
                if self.hover_text and self.font:
                    hover_text_surface = self.font.render(self.hover_text, True, self.text_color)
                    screen.blit(hover_text_surface, (self.rect.x + self.rect.width + self.scale*2, self.rect.y - self.scale*0))
        else:
            self.hover_start_time = None

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

