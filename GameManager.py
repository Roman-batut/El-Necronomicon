import pygame
from pygame.locals import *
import Engine
import Player
import Enemy
import Walls
import Trigger

def WallWrapper(engine):
  for wall in engine.scene.wallPrimitives:
    wallObj = Walls.Wall("wall", engine, wall)
    engine.scene.walls.append(wallObj)

class Manager():
  def __init__(self, engine):

    self.engine = engine

    self.engine.Init(self)

    self.transition = False

  def Setup(self):
    #On crée un joueur
    joueur = Player.Player("Player", self.engine)

    self.Ennemies = []

    for i in range(2):
      self.Ennemies.append(Enemy.Enemy("Zoubida", joueur, self.engine))

    self.engine.scene.contenu.append(Trigger.Porte("Porte", self.engine, [0,0], [16,16]))

    #enemy = Enemy.Enemy("Zoubida", joueur, self.engine)
    #enemy2 = Enemy.Enemy("zoubida2leretour", joueur, self.engine)

    WallWrapper(self.engine)

  
  #C'est ici que se trouve la boucle principale
  def Run(self):
    continuer = True
    while continuer :
      self.engine.Update()

      #if len(self.Ennemies) == 0:
      #  print("salle cleared")

      if self.transition:
        pass



      #On remplit self.keystrokes une seule fois par frame
      for event in pygame.event.get() :
            if event.type == QUIT :
              pygame.quit()
              continuer = False
            if event.type == KEYDOWN : 
              if event.key == pygame.K_p :
                self.engine.pause = not self.engine.pause
                
              else : 
                self.engine.keystrokes.append(event.key)
            if event.type == KEYUP :
              if event.key in self.engine.keystrokes:
                self.engine.keystrokes.remove(event.key)
