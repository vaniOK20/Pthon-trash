import pygame
import math

# Ініціалізація Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Polygon Line Connector")

# Колір
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Полігон, масив точок (x, y)
polygon_points = [(100, 100), (200, 150), (300, 100), (400, 200), (300, 300), (100, 200)]
lines = [(polygon_points[i], polygon_points[(i+1)%len(polygon_points)]) for i in range(len(polygon_points))]

def distance_point_to_line(px, py, x1, y1, x2, y2):
    line_mag = math.hypot(x2-x1, y2-y1)
    if line_mag<0.000001:
        return math.hypot(px-x1, py-y1)
    u = ((px-x1)*(x2-x1) + (py-y1)*(y2-y1)) / (line_mag*line_mag)
    if u<0:
        return math.hypot(px-x1, py-y1)
    elif u>1:
        return math.hypot(px-x2, py-y2)
    else:
        ix = x1 + u*(x2-x1)
        iy = y1 + u*(y2-y1)
        return math.hypot(px-ix, py-iy)

def find_closest_line(mx, my, lines):
    min_dist = float('inf')
    closest_line = None
    for line in lines:
        dist = distance_point_to_line(mx, my, *line[0], *line[1])
        if dist<min_dist:
            min_dist = dist
            closest_line = line
    return closest_line

def find_closest_point(mx, my, polygon_points):
    min_dist = float('inf')
    closest_point = None
    for point in polygon_points:
        dist = math.hypot(mx-point[0], my-point[1])
        if dist<min_dist:
            min_dist = dist
            closest_point = point
    return closest_point

def add_point_to_polygon(mx, my, polygon_points, lines):
    closest_point = find_closest_point(mx, my, polygon_points)
    closest_line = find_closest_line(mx, my, lines)
    idx=None
    if closest_line:
        try:
            idx = polygon_points.index(closest_line[1])
            polygon_points.insert(idx, (mx, my))
        except Exception as e:
            pass
    if not idx is None and closest_point:
        polygon_points.remove(closest_point)
        recalculate_lines(polygon_points, lines)

def recalculate_lines(polygon_points, lines):
    lines.clear()
    for i in range(len(polygon_points)):
        lines.append((polygon_points[i], polygon_points[(i+1)%len(polygon_points)]))

def is_point_in_polygon(px, py, polygon_points):
    n = len(polygon_points)
    inside = False
    xints = 0
    p1x, p1y = polygon_points[0]
    for i in range(n+1):
        p2x, p2y = polygon_points[i%n]
        if py>min(p1y, p2y):
            if py<=max(p1y, p2y):
                if px<=max(p1x, p2x):
                    if p1y!=p2y:
                        xints = (py-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x==p2x or px<=xints:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

running = True
while running:
    screen.fill(WHITE)
    
    for line in lines:
        pygame.draw.line(screen, BLACK, line[0], line[1], 2)
    
    for point in polygon_points:
        pygame.draw.circle(screen, RED, point, 5)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if is_point_in_polygon(mx, my, polygon_points):
                add_point_to_polygon(mx, my, polygon_points, lines)
    
    pygame.display.flip()

pygame.quit()
