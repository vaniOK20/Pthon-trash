import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

black=(0, 0, 0)
white=(255, 255, 255)
move=[False, '']

nodes={'math': [0, 0, [0, 0], [0], '+'], 'num': [200, 0, [], [100]]}

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	if move[0] and pygame.mouse.get_pressed()[0]:
		nodes[move[1]][0]=pygame.mouse.get_pos()[0]-posx
		nodes[move[1]][1]=pygame.mouse.get_pos()[1]-posy
	else:
		move[0]=False

	if pygame.mouse.get_pressed()[2]:
		nodes[f'math{len(nodes)}']=[pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], [0, 0], [0], '+']

	screen.fill(white)
	for node in nodes:
		node_=nodes[node]
		x, y=pygame.mouse.get_pos()
		if x>node_[0] and x<node_[0]+150 and y>node_[1] and y<node_[1]+100 and pygame.mouse.get_pressed()[0]:
			posx=pygame.mouse.get_pos()[0]-nodes[node][0]
			posy=pygame.mouse.get_pos()[1]-nodes[node][1]
			move=[True, node]
		pygame.draw.rect(screen, black, (node_[0], node_[1], 150, 100), 10)

		num_ins=len(node_[2])
		for i, in_ in enumerate(node_[2]):
			in_y=node_[1]+(i+1)*(100//(num_ins+1))
			pygame.draw.circle(screen, (0, 255, 0), (node_[0]-10, in_y), 5)

		num_outs=len(node_[3])
		for i, out in enumerate(node_[3]):
			out_y=node_[1]+(i+1)*(100//(num_outs+1))
			pygame.draw.circle(screen, (255, 0, 0), (node_[0]+160, out_y), 5)


	pygame.display.flip()
	clock.tick(60)