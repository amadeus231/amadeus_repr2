import pygame, sys
from pygame.locals import *


pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))

pygame.display.set_caption("Hello! it's new record")


while True:
	for event in pygame.event.get():
		if event == "QUIT":
			pygame.quit()
			sys.exit()
	pygame.display.update()

