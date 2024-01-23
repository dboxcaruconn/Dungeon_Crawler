import pygame

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
        
    def darker_color(self, amount=30):
        return tuple(max(0, c + amount) for c in self.color)

    # draw method to draw the pane
    def draw(self, screen, font):  # Make sure 'font' parameter is included here
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        # Where you draw the rectangle
        darker_color = self.darker_color()
        pygame.draw.rect(screen, darker_color, (self.x, self.y, self.width, self.scale * 30))
        text = font.render(self.title, True, (0, 0, 0))  # Use the passed 'font' to render the title
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.scale*14))  # Adjusted y-position
        screen.blit(text, text_rect)

