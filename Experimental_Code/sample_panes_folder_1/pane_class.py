import pygame

class Pane:
    def __init__(self, scale, x, y, width, height, color, title, alpha=255):
        self.scale = scale
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.title = title
        self.alpha = alpha  # Add an alpha attribute for transparency

    def darker_color(self, amount=30):
        return tuple(max(0, c - amount) if c - amount >= 0 else 0 for c in self.color[:3])  # Ensure color stays within bounds

    def draw(self, screen, font):
        # Create a new Surface with per-pixel alpha capabilities
        pane_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pane_surface.fill((*self.color[:3], self.alpha))  # Fill the surface with the pane's color and alpha

        # Draw the darker title bar on the pane surface
        darker_color = self.darker_color()
        pygame.draw.rect(pane_surface, (*darker_color, self.alpha), (0, 0, self.width, 30*self.scale))

        # Render the title text
        text = font.render(self.title, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, 14*self.scale))
        pane_surface.blit(text, text_rect)  # Blit the text onto the pane surface

        # Finally, blit the pane surface onto the screen at the pane's position
        screen.blit(pane_surface, (self.x, self.y))
