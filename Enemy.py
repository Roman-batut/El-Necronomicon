#Imports 
import pygame, math, random
import Engine
import Bullet
import Player
import Fonctions
import Matrix
import random

#Classe Ennemi
class Enemy(Engine.Entity) :
  def __init__(self, name, cible, moteur) :
    super().__init__(name, moteur, bounded = True)

    self.InitSprite("Assets/Enemies/" + str(name) + ".png")
    self.pos = [random.randint(16, moteur.Rlongueur - 16), random.randint(16, moteur.Rlargeur - 16)]
    self.InitRect(self.pos, [17, 24])
    self.cible = cible
    self.bullets = []
    self.fireFrame = 0
    self.colorShiftDuration = 0
    self.hp = 3

    #self.deltaPos = [0,0]

  def Update(self) : 
    self.Sprite = self.SpriteCopy.copy()
    #Angle
    try:
      distEnemyPlayer = math.sqrt(
          (self.Rect.centerx - self.cible.Rect.centerx)**2 +
          (self.Rect.centery - self.cible.Rect.centery)**2)

      distEnemyPlayerX = self.Rect.centerx - self.cible.Rect.centerx
      distEnemyPlayerY = self.cible.Rect.centery - self.Rect.centery

      cos = distEnemyPlayerX / distEnemyPlayer
      
      #Power Invisible
      if self.cible.Power == "Invisible" and self.cible.isPower == True :
        angle = (math.acos(cos) * 180 / math.pi) + random.randint(-40,40)
      else : angle = math.acos(cos) * 180 / math.pi

      if distEnemyPlayerY > 0:
          angle = 360 - angle

    except ZeroDivisionError : angle = 0

    #On attribue des balles
    if self.fireFrame < self.engine.frame :
      self.bullets.append(Bullet.Bullet(self.name + "Bullet", [self.Rect.centerx, self.Rect.centery], angle, self, self.engine))
      self.fireFrame = self.engine.frame + 30

    #Collisions 
    for collision in self.engine.collisions :
      if self in collision :
        collider = collision[((collision.index(self) + 1) % 2)]
        if "Bullet" == collider.__class__.__name__:
          if collider.source.__class__.__name__ == "Gun" :
            collider.Destroy()
            self.colorShiftDuration = 10
            self.hp -= 1
           
    if self.colorShiftDuration > 0:
      self.Sprite = Fonctions.colorShift(self.Sprite,(133, 33, 18))
      self.colorShiftDuration -= 1

    if self.hp <= 0:
      if self in self.engine.scene.contenu:
        self.engine.scene.contenu.remove(self)
        self.engine.manager.Ennemies.remove(self)
      
    #Mouvement de l'Enemy
    self.deltaPos = [0,0]
    enemyDeplacement = 1 #vitesse

    #Paterne Suit le Joueur
    if self.Rect.centerx != self.cible.Rect.centerx :
      self.deltaPos[0] += math.copysign(enemyDeplacement, self.cible.Rect.centerx - self.Rect.centerx) / 5
    if self.Rect.centery != self.cible.Rect.centery :
      self.deltaPos[1] += math.copysign(enemyDeplacement, self.cible.Rect.centery - self.Rect.centery) / 5
    
    #Paterne Fuit le Joueur
    '''
    if self.Rect.centerx != self.cible.Rect.centerx :
      self.deltaPos[0] -= math.copysign(enemyDeplacement, self.cible.Rect.centerx - self.Rect.centerx)
    if self.Rect.centery != self.cible.Rect.centery :
      self.deltaPos[1] -= math.copysign(enemyDeplacement, self.cible.Rect.centery - self.Rect.centery)
    '''
    #Paterne Recopie Mouvement
    """
    if self.deltaPos[0] != self.cible.deltaPos[0] :
      self.deltaPos[0] -= math.copysign(enemyDeplacement, self.cible.deltaPos[0])
    if self.deltaPos[1] != self.cible.deltaPos[1] :
      self.deltaPos[1] -= math.copysign(enemyDeplacement, self.cible.deltaPos[1])
    """
    #Paterne Rotation
    '''
    joueur = [self.cible.Rect.centerx, self.cible.Rect.centery]
    ennemi = [self.Rect.centerx, self.Rect.centery]
    try : 
      R = math.sqrt((joueur[0] - ennemi[0])**2 + (joueur[1] - ennemi[1])**2)
      angle_rotation = 2*math.asin(enemyDeplacement/(2*R))
      angle_rotation = angle_rotation / math.pi * 180
    except ZeroDivisionError:
      angle_rotation = 0  
    ennemi[0] -= joueur[0]
    ennemi[1] -= joueur[1]
    nouvelEnnemi = Matrix.rotMat(ennemi, angle_rotation)
    self.deltaPos[0] = nouvelEnnemi[0] - ennemi[0]
    self.deltaPos[1] = nouvelEnnemi[1] - ennemi[1]
    '''
    #Application du mouvement
    self.pos[0] += self.deltaPos[0]
    self.pos[1] += self.deltaPos[1]

    #print(self.pos)

    self.Rect = self.Sprite.get_rect(center = (self.pos[0], self.pos[1]))
    #self.Rect = pygame.Rect.move(self.Rect, (self.deltaPos[0], self.deltaPos[1]))

    #Update
    super().Update()




    