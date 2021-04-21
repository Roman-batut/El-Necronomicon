import pygame, math
import Engine

class Bullet(Engine.Entity):
  def __init__(self, name, pos, angle, source, moteur):
    super().__init__(self, moteur, bounded=False)

    self.pos = pos
    self.angleRaw = angle
    #On va avoi besoin d'angles en radians
    self.angle = angle * math.pi / 180 + math.pi
    self.source = source

    self.InitSprite("Assets/Bullets/" + name + ".png")
    self.InitRect([self.pos[0] - 4,
                   self.pos[1] - 4], [9,9])

  def Update(self):

    #Auto-Destruction des balles quand elles sortent de l'écran, histoire de pas updater un million d'entités
    SurfRect = pygame.Rect((0,0), (self.engine.Rlongueur, self.engine.Rlargeur))
    if not SurfRect.collidepoint(tuple(self.pos)):
      self.Destroy()

    deplacement = 4.0
    #On passe d'un angle à des coordonées en x,y
    self.deltaPos = [deplacement * math.cos(self.angle), deplacement * math.sin(self.angle)]

    #Rotation du Sprite
    self.Sprite = pygame.transform.rotate(self.SpriteCopy, 360 - self.angleRaw)

    #Mise à jour de self.deltaPos
    self.pos[0] += self.deltaPos[0]
    self.pos[1] += self.deltaPos[1]

    #Destruction du projectile au contact d'un mur
    for collision in self.engine.collisions :
      if self in collision :
        collider = collision[(collision.index(self) + 1) % 2]
        if "Wall" == collider.__class__.__name__ :
          self.Destroy()

    #Mise à jour du Rect
    self.Rect = self.Sprite.get_rect(center = (self.pos[0], self.pos[1]))

    super().Update()

  def Destroy(self):
    if self in self.source.bullets:
        self.source.bullets.remove(self)
    if self in self.engine.scene.contenu:
      self.engine.scene.contenu.remove(self)