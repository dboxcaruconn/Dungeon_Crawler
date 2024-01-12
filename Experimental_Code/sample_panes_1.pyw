import pygame

# Constants for screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Pane class to manage each GUI pane
class Pane:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Dynamic GUI Panes Game")
    clock = pygame.time.Clock()

    # Colors for different panes
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

    # Initialize panes (dividing the screen into four equal parts for now)
    panes = [
        Pane(0, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, colors[0]),
        Pane(SCREEN_WIDTH // 2, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, colors[1]),
        Pane(0, SCREEN_HEIGHT // 2, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, colors[2]),
        Pane(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, colors[3])
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle resizing events here

        screen.fill((0, 0, 0))  # Clear screen

        # Draw panes
        for pane in panes:
            pane.draw(screen)

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Maintain 60 frames per second

    pygame.quit()

if __name__ == "__main__":
    main()
