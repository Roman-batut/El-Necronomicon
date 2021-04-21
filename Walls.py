import pygame
import Engine

class Wall(Engine.Entity):
  def __init__(self, name, moteur, wall):
    super().__init__(name, moteur, bounded = False)

    self.InitSprite(wall[0])
    self.InitRect([wall[1][0], wall[1][1]], [wall[2], wall[3]])
    #print(self.Rect)

    #if wall[1][0] == 80:
    #  if wall[1][1] == 48:
    #    print("trouvé")

    #print(wall[1][0], wall[1][1], wall[2], wall[3])

    if wall[3] == 32:
      self.collideRect = pygame.Rect([wall[1][0], wall[1][1] + 16], [16,16])#[wall[2], wall[3] - 16])
      #print("a")
      #print(wall[1][0], wall[1][1] + 16 )
    else :
      self.collideRect = pygame.Rect([wall[1][0], wall[1][1]], [16,16])#[wall[2], wall[3]])
      #print(wall[1][0], wall[1][1])
      #print("b")