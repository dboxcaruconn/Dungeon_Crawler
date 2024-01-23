import pygame
import time

# Button class to manage each button
class Button:
    def __init__(self, scale, x, y, width, height, button_color, hover_color, 
                 text_color=(0, 0, 0, 255), hover_text_color=(255, 255, 255 ,255), text=None, font=None, 
                 hover_text=None, image=None):
        self.scale = scale
        self.rect = pygame.Rect(x, y, width, height)
        self.button_color = button_color
        self.hover_color = hover_color
        self.text = text
        self.font = font
        self.text_color = text_color
        self.hover_text_color = hover_text_color
        self.hover_text = hover_text
        self.image = pygame.transform.scale(image, (width, height)) if image else None
        self.hover_start_time = None

    def is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)
    
    def draw(self, screen, mouse_pos):
        # Create a new Surface with alpha channel for button background
        button_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        button_surface.fill(self.button_color if not self.rect.collidepoint(mouse_pos) else self.hover_color)

        # Draw the button surface onto the screen with blending
        screen.blit(button_surface, (self.rect.x, self.rect.y), special_flags=pygame.BLEND_RGBA_MULT)

        # Draw the image if it exists
        if self.image:
            screen.blit(self.image, (self.rect.x, self.rect.y))

        # Render and draw the text
        if self.text:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)
        
        # Render and draw the hover text with background
        if self.is_hovered():
            if self.hover_start_time is None:
                self.hover_start_time = time.time()
            elif time.time() - self.hover_start_time > 0.1:  # 100 milliseconds
                if self.hover_text and self.font:
                    hover_text_surface = self.font.render(self.hover_text, True, self.hover_text_color)
                    hover_text_rect = hover_text_surface.get_rect(x=self.rect.x + self.rect.width + self.scale*4, y=self.rect.y)
                    # Draw background rectangle for hover text
                    pygame.draw.rect(screen, self.hover_color, hover_text_rect.inflate(self.scale, self.scale))
                    # Draw hover text
                    screen.blit(hover_text_surface, hover_text_rect)

        else:
            self.hover_start_time = None

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)