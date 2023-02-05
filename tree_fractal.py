import pygame
import random
import math

pygame.display.set_caption('fractals')
(width, height) = (600, 600)
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)

branch_lenght_scale = random.uniform(.7, .8)
branch_spacing_angle = random.randint(6, 13)

class Line:
    def __init__(self, x1, y1, r, angle ):
        self.x1 = x1
        self.y1= y1

        self.r = r
        self.angle = angle
        self.growth = False

        self.x2 = self.x1 + self.r * math.cos(-self.angle)
        self.y2 = self.y1 + self.r * math.sin(-self.angle)

    def draw(self):
        pygame.draw.line(screen, white ,(self.x1, self.y1), (self.x2, self.y2))


lines = []
to_add_to_lines = []
stem_drawn = False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                to_add_to_lines = []
                for i, line in enumerate(lines):
                    if line.growth == False:
                        line1 = Line(line.x2, line.y2, line.r * branch_lenght_scale, line.angle + math.pi / branch_spacing_angle)
                        line1.draw() 
                        to_add_to_lines.append(line1)
                        line2 = Line(line.x2, line.y2, line.r * branch_lenght_scale, line.angle - math.pi / branch_spacing_angle)
                        line2.draw()
                        to_add_to_lines.append(line2)
                    line.growth = True
                for i, line in enumerate(to_add_to_lines):
                    lines.append(line)

    area = screen.get_rect()
    w = area[2]
    h = area[3]

    if stem_drawn == False:
        stem = Line(w/2, h, 100, math.pi / 2)
        lines.append(stem)
        stem.draw()
        stem_drawn = True

    screen.fill(black)

    for i, line in enumerate(lines):
        line.draw()


    pygame.display.flip()

