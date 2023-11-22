import pygame
pygame.init()
class Button:
    def __init__(self, x, y, width, height, text, font=None, font_size=20, normal_color=(200, 200, 200), hover_color=(255, 255, 255), text_color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.font_size = font_size
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.is_hovered = False

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

        # Create font and render text surface
        if self.font:
            font = pygame.font.Font(self.font, self.font_size)
        else:
            font = pygame.font.Font(None, self.font_size)  # Default font if not specified

        text_surface = font.render(self.text, True, self.text_color)

        # Center the text on the button
        text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))

        # Draw text on the button
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        # Check if the button is clicked
        return self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height

# Example usage:
