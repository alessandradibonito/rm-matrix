import pygame
import random

WIDTH = 1200
HEIGHT = 800
FPS = 60

FONT_SIZE = 16

GREEN = (0, 255, 120)
BLACK = (0, 0, 0)

RAIN_TEXT = "NAMJOONNAMJOONNAMJOONRMRMRM"

START_MORPH = 4.0
FULL_MORPH = 8.0

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RM Matrix")

clock = pygame.time.Clock()

font = pygame.font.SysFont(
    "Consolas",
    FONT_SIZE,
    bold=True
)

RM_PATTERN = [
"RRRRRRRRRR      MM         MM",
"RR      RR      MMM       MMM",
"RR      RR      MMMM     MMMM",
"RRRRRRRRRR      MM MM   MM MM",
"RRRRRRR         MM  MM MM  MM",
"RR   RRR        MM   MMM   MM",
"RR    RRR       MM    M    MM",
"RR     RRR      MM         MM",
"RR      RRR     MM         MM",
]

targets = []

cell = 22

shape_width = len(RM_PATTERN[0]) * cell
shape_height = len(RM_PATTERN) * cell

offset_x = (WIDTH - shape_width) // 2
offset_y = (HEIGHT - shape_height) // 2

for row, line in enumerate(RM_PATTERN):

    for col, char in enumerate(line):

        if char != " ":

            for _ in range(8):

                targets.append(
                    {
                        "target_x":
                            offset_x
                            + col * cell
                            + random.randint(-6, 6),

                        "target_y":
                            offset_y
                            + row * cell
                            + random.randint(-6, 6),

                        "x":
                            random.randint(0, WIDTH),

                        "y":
                            random.randint(-HEIGHT, 0)
                    }
                )

print("Targets:", len(targets))

start_ticks = pygame.time.get_ticks()

running = True

while running:

    clock.tick(FPS)

    elapsed = (
        pygame.time.get_ticks()
        - start_ticks
    ) / 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    for x in range(0, WIDTH, FONT_SIZE):

        for y in range(0, HEIGHT, FONT_SIZE * 2):

            if random.random() < 0.03:

                char = random.choice(RAIN_TEXT)

                txt = font.render(
                    char,
                    True,
                    GREEN
                )

                screen.blit(txt, (x, y))

    if elapsed > START_MORPH:

        progress = min(
            (elapsed - START_MORPH)
            /
            (FULL_MORPH - START_MORPH),
            1.0
        )

        for p in targets:

            current_x = (
                p["x"] +
                (
                    p["target_x"]
                    - p["x"]
                )
                * progress
            )

            current_y = (
                p["y"] +
                (
                    p["target_y"]
                    - p["y"]
                )
                * progress
            )

            char = random.choice(
                [
                    "N",
                    "A",
                    "M",
                    "J",
                    "O",
                    "O",
                    "N"
                ]
            )

            particle = font.render(
                char,
                True,
                GREEN
            )

            screen.blit(
                particle,
                (
                    current_x,
                    current_y
                )
            )

    pygame.display.flip()

pygame.quit()