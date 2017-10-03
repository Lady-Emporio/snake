import pygame
import sys
from OOPdisplay import My_display

screen=My_display()
MY_FPS=1
timer = pygame.time.Clock() #ограничим кол-во кадров


segment_width = 15
segment_height = 15
segment_margin = 3
WHITE = (255, 255, 255)
allspriteslist = pygame.sprite.Group()
class Segment(pygame.sprite.Sprite):
	def __init__(self, x, y):
	 super().__init__()
 

	 self.image = pygame.Surface([segment_width, segment_height])
	 self.image.fill(WHITE)
 

	 self.rect = self.image.get_rect()
	 self.rect.x = x
	 self.rect.y = y
snake_segments = []
for i in range(5):
	x = 250 - (segment_width + segment_margin) * i
	y = 30
	segment = Segment(x, y)
	snake_segments.append(segment)
	allspriteslist.add(segment)



x_change = segment_width + segment_margin
y_change = 0

while True: # Основной цикл программы
	for event in pygame.event.get(): # Обрабатываем события
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change = (segment_width + segment_margin) * -1
				y_change = 0
			if event.key == pygame.K_RIGHT:
				x_change = (segment_width + segment_margin)
				y_change = 0
			if event.key == pygame.K_UP:
				x_change = 0
				y_change = (segment_height + segment_margin) * -1
			if event.key == pygame.K_DOWN:
				x_change = 0
				y_change = (segment_height + segment_margin)


	old_segment = snake_segments.pop()
	allspriteslist.remove(old_segment)
	
	x = snake_segments[0].rect.x + x_change
	y = snake_segments[0].rect.y + y_change
	segment = Segment(x, y)

	snake_segments.insert(0, segment)
	allspriteslist.add(segment)



	screen.Mblit(screen.bg,(0,0))      # Каждую итерацию необходимо всё перерисовывать        
	allspriteslist.draw(screen)


	pygame.display.update()     # обновление и вывод всех изменений на экран
	timer.tick(MY_FPS)
	