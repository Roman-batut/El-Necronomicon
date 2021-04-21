#Imports
import pygame
import Engine
import math
import Bullet
import Matrix
import Fonctions

#Classe Gun
class Gun(Engine.Entity):
    def __init__(self, user, moteur):
        super().__init__(self, moteur, bounded=False)

        self.user = user
        self.InitSprite("Assets/Gunne(Hold).png")
        self.InitRect([user.Rect.centerx, user.Rect.centery], [33, 17])

        self.angle = 0
        self.bullets = []
        #Ce point virtuel permet de garder une trace d'où la bouche du canon se trouve (pour le spawn des balles)
        self.virtPoint = [15,-3]
        self.virtPointCopy = self.virtPoint.copy()

        self.fireFrame = 0
        self.fireRate = 10

        #self.deltaPos = [0,0]

        self.renderPriorities = [self.user, -1]

    def Update(self) :

      flipped = False
      canFlip = True

      #En utilisant un peu de géométrie, on calcule l'angle formé par le curseur et le joueur
      try:
        distCursorPlayer = math.sqrt(
            (self.Rect.centerx -
             pygame.mouse.get_pos()[0] // self.engine.rapport)**2 +
            (self.Rect.centery -
             pygame.mouse.get_pos()[1] // self.engine.rapport)**2)

        distPlayerXCursor = self.Rect.centerx - pygame.mouse.get_pos(
        )[0] // self.engine.rapport

        distCursorPlayerY = pygame.mouse.get_pos(
        )[1] // self.engine.rapport - self.Rect.centery

        cos = distPlayerXCursor / distCursorPlayer
        self.angle = math.acos(cos) * 180 / math.pi

        if distCursorPlayerY > 0:
            self.angle = 360 - self.angle

      except ZeroDivisionError : self.angle = 0

      #Quelques corrections pour que le Sprite soit toujour orienté vers le haut
      if not self.user.canFlip :
        canFlip = False

      if (self.angle + 90) % 360 < 180 and canFlip:
        flipped = True
        self.Sprite = pygame.transform.flip(self.SpriteCopy, False, True)
        #self.virtPoint[1] =  - self.virtPoint[1]
        self.virtPoint = Matrix.rotMat(self.virtPointCopy, self.angle)
      else :
        self.Sprite = self.SpriteCopy
        self.virtPoint = Matrix.rotMat(self.virtPointCopy, self.angle - 20)

      self.Sprite = pygame.transform.rotate(self.Sprite, -self.angle + 180)

      #On replace le point virteul dans le repère du rendu
      self.virtPoint[0] = -self.virtPoint[0]
      self.virtPoint[0] += self.Rect.centerx
      self.virtPoint[1] += self.Rect.centery


      #Tirer 
      if pygame.mouse.get_pressed(num_buttons = 3)[0] and self.fireFrame < self.engine.frame:
        self.bullets.append(Bullet.Bullet("PlayerBullet", self.virtPoint, self.angle, self, self.engine))

        self.fireFrame = self.engine.frame + self.fireRate
      
      if flipped:
        self.Rect = self.Sprite.get_rect(center = (self.user.Rect.bottomright[0] - 12 - 2,self.user.Rect.bottomright[1] - 4))
      else:
        self.Rect = self.Sprite.get_rect(center = (self.user.Rect.bottomright[0] - 2,self.user.Rect.bottomright[1] - 4))

      if self.user.colorShiftDuration > 0:
        self.Sprite = Fonctions.colorShift(self.Sprite, (133, 33, 18))
      
      if self.user.Power == "Invisible" and self.user.isPower == True :
        self.Sprite = Fonctions.colorShift(self.Sprite, (248,248,255))

      super().Update()

    def Draw(self, rendu):
      resultat = super().Draw(rendu)

      #Pour débug l'orientation de l'arme
      #pygame.draw.line(rendu, (255,0,0), (self.virtPoint[0], self.virtPoint[1]), self.Rect.center)
      return resultat