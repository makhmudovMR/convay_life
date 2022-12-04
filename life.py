import pygame
import random


class Life():
  def __init__(self):
    pygame.init()
    self.size_x = 800
    self.size_y = 600
    self.cell_size = 10
    self.fps = 15
    self.screen = pygame.display.set_mode([self.size_x, self.size_y])
    self.clock = pygame.time.Clock()

    self.loopFlag = True
    self.currMatrix = None

  def generate_matrix(self, currMatrix):
    if currMatrix == None:
      # generate clear matrix and return
      return [[random.randint(0, 1) for x in range(0, round(self.size_y / self.cell_size))] for y in range (0, round(self.size_x / self.cell_size))]
    else:
      new_matrix = [[0 for x in range(0, round(self.size_y / self.cell_size))] for y in range (0, round(self.size_x / self.cell_size))]
      for x in range(1,len(currMatrix) - 1):
        for y in range(1, len(currMatrix[x]) - 1):
          summ = 0
          summ += currMatrix[x-1][y-1] + currMatrix[x-1][y] + currMatrix[x-1][y+1]
          summ += currMatrix[x][y-1] + currMatrix[x][y+1]
          summ += currMatrix[x+1][y-1] + currMatrix[x+1][y] + currMatrix[x+1][y+1]
          if (currMatrix[x][y] == 1):
            if (summ == 2 or summ == 3):
              new_matrix[x][y] = 1
            if (summ < 2 or summ > 3):
              new_matrix[x][y] = 0
          else:
            if (summ == 3):
              new_matrix[x][y] = 1
      return new_matrix

  def draw_grid(self, matrix):
    self.screen.fill(pygame.Color('black'))
    for x in range(len(matrix)):
      for y in range(len(matrix[x])):
        if (matrix[x][y] == 1):
          pygame.draw.rect(self.screen, pygame.Color('green'), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
        else:
          pygame.draw.rect(self.screen, pygame.Color('black'), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))




  def loop(self):
    while self.loopFlag:

      new_matrix = self.generate_matrix(self.currMatrix)
      self.draw_grid(new_matrix)
      self.currMatrix = new_matrix


      pygame.display.flip()
      self.clock.tick(self.fps)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.loopFlag = False


life = Life()
life.loop()
