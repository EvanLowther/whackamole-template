import pygame
import sys
import random

def main():
    try:

        pygame.init()

        screen_width = 640
        screen_height = 512
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Whack-a-Mole")

        # Define colors
        GREEN = (144, 238, 144)
        BLACK = (0, 0, 0)

        mole_image = pygame.image.load("mole.png")
        mole_rect = mole_image.get_rect()

        def draw_grid():
            screen.fill(GREEN)
            cell_size = 32
            for x in range(0, screen_width, cell_size):
                pygame.draw.line(screen, BLACK, (x, 0), (x, screen_height))
            for y in range(0, screen_height, cell_size):
                pygame.draw.line(screen, BLACK, (0, y), (screen_width, y))

        def move_mole():
            mole_rect.x = random.randrange(0, screen_width, 32)
            mole_rect.y = random.randrange(0, screen_height, 32)

        move_mole()

        running = True
        while running:
            draw_grid()
            screen.blit(mole_image, mole_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_rect.collidepoint(event.pos):
                        move_mole()
        pygame.quit()


    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
