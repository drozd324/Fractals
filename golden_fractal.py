import pygame
import random
import math

pygame.display.set_caption('fractals')
(width, height) = (600, 600)
screen = pygame.display.set_mode((width, height))

white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)

branch_lenght_scale = .7
branch_spacing_angle = 5

class Line:
    def __init__(self, x, y, r, angle, r3, r3_angle):
        self.x = x
        self.y= y
        self.r = r
        self.angle = angle

        self.x1 = self.x + self.r * math.cos(-self.angle + math.pi)
        self.y1 = self.y + self.r * math.sin(-self.angle + math.pi)
        self.x2 = self.x + self.r * math.cos(-self.angle)
        self.y2 = self.y + self.r * math.sin(-self.angle)

        self.r3 = r3
        self.r3_angle = r3_angle
        self.x3 = self.x + self.r * math.cos(-self.angle - self.r3_angle)
        self.y3 = self.y + self.r * math.sin(-self.angle - self.r3_angle)
        self.distance = math.hypot(self.x1 - self.x2, self.y1 - self.y2)

    def draw(self):
        pygame.draw.line(screen, white ,(self.x1, self.y1), (self.x2, self.y2))


lines = []
to_add_to_lines = []

length = random.randint(200, 400)
angle = random.uniform(0, 2 * math.pi)
r3 = random.randint(100,600)
r3_angle = random.uniform(math.pi / 3, math.pi * 2/3)

stem = Line(width/2, height/2, length/2, angle, r3, r3_angle)
lines.append(stem)
stem.draw()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                to_add_to_lines = []
                for i, line in enumerate(lines):
                    line1_mid_x, line1_mid_y = (line.x1 + line.x3) / 2, (line.y1 + line.y3) / 2
                    line1 = Line(line1_mid_x, line1_mid_y, math.hypot(line1_mid_x - line.x1, line1_mid_y - line.y1) , - math.atan2(line.y3 - line.y1, line.x3 - line.x1 ), r3, r3_angle)
                    line1.draw() 
                    to_add_to_lines.append(line1)
                    
                    line2_mid_x, line2_mid_y = (line.x2 + line.x3) / 2, (line.y2 + line.y3) / 2
                    line2 = Line(line2_mid_x, line2_mid_y, math.hypot(line2_mid_x - line.x2, line2_mid_y - line.y2) , - math.atan2(line.y3 - line.y2, line.x3 - line.x2 ), r3, r3_angle)
                    line2.draw() 
                    to_add_to_lines.append(line2)
                        
                lines = []
                for i, line in enumerate(to_add_to_lines):
                    lines.append(line)

                screen.fill(black)

                for i, line in enumerate(lines):
                    line.draw()
                print(str(len(lines)) + " lines drawn on the screen")

            if event.key == pygame.K_r:
                screen.fill(black)

                lines = []
                length = random.randint(200, 400)
                angle = random.uniform(0, 2 * math.pi)
                r3 = random.randint(100,600)
                r3_angle = random.uniform(math.pi / 3, math.pi * 2/3)

                stem = Line(width/2, height/2, length/2, angle, r3, r3_angle)
                lines.append(stem)
                stem.draw()

    pygame.display.flip()

