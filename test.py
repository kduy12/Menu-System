import pygame

class EightBitButton:
    def __init__(self, x, y, text, font=None, font_size=20, normal_color=(200, 200, 200), hover_color=(255, 255, 255), text_color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.font_size = font_size
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.is_hovered = False

        # Create font and render text surface
        if self.font:
            self.font = pygame.font.Font(self.font, self.font_size)
        else:
            self.font = pygame.font.Font(None, self.font_size)  # Default font if not specified

        self.update_size()

    def update_size(self):
        text_surface = self.font.render(self.text, True, self.text_color)
        self.width = text_surface.get_width() + 20  # Add padding
        self.height = text_surface.get_height() + 10  # Add padding

    def draw(self, screen):
        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Check if mouse is over the button
        if self.x < mouse_x < self.x + self.width and self.y < mouse_y < self.y + self.height:
            self.is_hovered = True
        else:
            self.is_hovered = False

        # Button color based on hover state
        button_color = self.hover_color if self.is_hovered else self.normal_color

        # Draw button rectangle
        pygame.draw.rect(screen, button_color, (self.x, self.y, self.width, self.height))

        # Draw text on the button
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        # Check if the button is clicked
        return self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height

# Example usage:
pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

button_font_path = "8-BIT WONDER.TTF"  # Replace with your font file path
button = EightBitButton(100, 100, "Click Me!", font=button_font_path, font_size=24)

running = True
while running:
    screen.fill((50, 50, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button.is_clicked(mouse_pos):
                print("Button clicked!")

    # Draw the button
    button.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
