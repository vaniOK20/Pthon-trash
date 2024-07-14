import pygame
import numpy as np

pygame.init()

width, height=800, 600
screen=pygame.display.set_mode((width, height))

def fade(t):
	return t*t*t*(t*(t*6-15)+10)

def lerp(t, a, b):
	return a + t * (b - a)

def grad(hash, x, y):
	h=hash&3
	u=x if h&1==0 else -x
	v=y if h&2==0 else -y
	return u+v

def perlin(x, y, perm):
	xi=int(x)&255
	yi=int(y)&255
	xf=x-int(x)
	yf=y-int(y)
	u=fade(xf)
	v=fade(yf)
	
	n00=grad(perm[perm[xi]+yi], xf, yf)
	n01=grad(perm[perm[xi]+yi+1], xf, yf-1)
	n10=grad(perm[perm[xi+1]+yi], xf-1, yf)
	n11=grad(perm[perm[xi+1]+yi+1], xf-1, yf-1)
	
	x1=lerp(u, n00, n10)
	x2=lerp(u, n01, n11)
	return lerp(v, x1, x2)

scale=10.0
seed=0
np.random.seed(seed)
perm=np.arange(256)
np.random.shuffle(perm)
perm=np.stack([perm, perm]).flatten()

pixels=np.zeros((width, height, 3), dtype=np.uint8)

for y in range(height):
	for x in range(width):
		noise_val=perlin(x/scale, y/scale, perm)
		color=int((noise_val+1)/2*255)
		pixels[x, y]=(50, color, 50)

surface=pygame.surfarray.make_surface(pixels)
surface=pygame.transform.scale(surface, (surface.get_width()+500, surface.get_height()+500))

running=True
while running:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False

	screen.blit(surface, (0, 0))
	pygame.display.flip()

pygame.quit()
