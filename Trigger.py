import pygame
import Engine

class Porte(Engine.Entity):
  def __init__(self, name, engine, pos, size):
    super().__init__(name, engine, bounded=False)

    self.pos = pos
    self.size = size

    self.open = False
    
    self.surfaceRed = pygame.Surface(tuple(self.size))
    self.surfaceRed.fill((255,0,0))

    self.surfaceGreen = pygame.Surface(tuple(self.size))
    self.surfaceGreen.fill((0,255,0))

    self.InitSprite("Assets/Tiles/FloorTileDark.png")
    self.Sprite = self.surfaceRed
    self.InitRect(self.pos, self.size)


  def Update(self):
    if len(self.engine.manager.Ennemies) == 0:
      self.open = True
      self.Sprite = self.surfaceGreen

      for collision in self.engine.collisions :
        if self in collision :
          collider = collision[(collision.index(self) + 1) % 2]
          if "Player" == collider.__class__.__name__ :
            self.engine.manager.transition = True
