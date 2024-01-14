import pygame
import os

# Pane class to manage each GUI pane
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

# main function
def main():
    pygame.init()
    # Initialize a temporary window to get the screen information
    temp_surface = pygame.display.set_mode((0, 0), pygame.HIDDEN)
    screen_info = pygame.display.Info()
    pygame.display.quit()

    # Set window dimensions to the screen's dimensions
    SCREEN_WIDTH = screen_info.current_w
    SCREEN_HEIGHT = screen_info.current_h

    # Set up the drawing window with the screen's dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.FULLSCREEN)

    pygame.display.set_caption("DUNGEON CRAWLER")
    clock = pygame.time.Clock()

    # Setting the font path relative to the current script
    font_name = 'GENOGRUNGE.OTF'
    font_path = os.path.join(os.path.dirname(__file__), font_name)
    custom_font = pygame.font.Font(font_path, 36)

    # Colors for different panes
    colors = [(145, 145, 120),  # 0: Dark gray
              (0, 255, 0)]      # 1: Bright green
    
    # Titles for different panes
    titles = ["Heroes", "Exploration", "Journal", "Inventory"]

    # Initialize panes
    panes = [    Pane(0, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, colors[0], titles[0]),
        Pane(SCREEN_WIDTH // 2, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, colors[1], titles[1]),
        Pane(0, SCREEN_HEIGHT // 2, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, colors[1], titles[2]),
        Pane(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, colors[0], titles[3])
    ]

    # main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle resizing events here

        screen.fill((0, 0, 0))  # Clear screen

        # Draw panes
        for pane in panes:
            pane.draw(screen, custom_font)

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Maintain 60 frames per second

    pygame.quit()
   
# call main function
if __name__ == "__main__":
    main()