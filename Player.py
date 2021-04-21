#Imports
import pygame
import Engine
import Gun
import Fonctions
from pygame.locals import *
from time import perf_counter

#Class Joueur
class Player(Engine.Entity) :
  def __init__(self, name, moteur) :
    #Permet d'appeler la fonction __init__() d'Objet
    super().__init__(name, moteur)

    self.engine.player = self

    self.InitSprite("Assets/Soldier(Holding).png")
    self.InitRect([moteur.Rlongueur//2, moteur.Rlargeur//2], [16, 16])
    self.collideRect = pygame.Rect((self.Rect.left, self.Rect.bottom - 2), (16, 2))

    #On attribue une arme
    self.Gun = Gun.Gun(self, self.engine)

    #Mise en place du système de dash 
    self.isDashing = False
    self.ableToDash = True
    self.dashRechargeTime = 5
    self.lastDashTime = 0
    self.dashFrames = 0
    self.t = 1

    #Mise en place du système de power
    self.PowerList = ["Bullet-Time", "Speed", "Invincible", "Confusion", "Fire-Rate"]
    self.Power = "Bullet-Time"
    self.PowerChoose = 0
    self.isPower = False
    self.ableToPower = True
    self.powerFrames = 600

    #Autres
    self.SpriteDos = pygame.image.load("Assets/Soldier(Dos).png")
    self.canFlip = True
    self.colorShiftDuration = 0
    self.mouseDuration = 30

    #self.deltaPos = [0,0]

  def Update(self) :

    self.canFlip = True
    self.Sprite = self.SpriteCopy.copy()

    #Mouvements Joueur
    self.deltaPos = [0,0]
    self.deplacement = 1
    
    #Mouvement de Dash (roulade)
    if not self.ableToDash:
      if perf_counter() - self.lastDashTime > self.dashRechargeTime:
        self.ableToDash = True
        self.engine.able_to_dash = True

    if K_LSHIFT in self.engine.keystrokes and self.ableToDash == True :
      self.isDashing = True
      self.ableToDash = False
      self.engine.able_to_dash = False

      self.lastDashTime = perf_counter()
      self.dashFrames = 3
      
    if self.dashFrames > 0 :
      self.deplacement = 15
      self.dashFrames -= 1
    else :
       self.isDashing = False

    #Power Change
    if pygame.mouse.get_pressed(num_buttons = 3)[1] and self.mouseDuration < self.engine.frame :
      self.Power = self.PowerList[int(self.PowerChoose)%len(self.PowerList)]
      self.PowerChoose += 1
      self.mouseDuration = self.engine.frame + 10
      print(self.Power)

    #Power Fire-Rate
    if self.Power == "Fire-Rate" :
      if K_SPACE in self.engine.keystrokes :
        if self.powerFrames > 0 :
          self.powerFrames -= 1
          self.Gun.fireRate = 5
        else : self.Gun.fireRate = 10
      else : self.isPower = False ; self.Gun.fireRate = 10

    #Power Confusion
    if self.Power == "Confusion" :
      if K_SPACE in self.engine.keystrokes : 
        if self.powerFrames > 0 :
          self.powerFrames -= 1
          self.isPower = True
          self.Sprite = Fonctions.colorShift(self.Sprite, (248,248,255))
        else : self.isPower = False
      else : self.isPower = False

    #Power Invincible
    if self.Power == "Invincible" :
      if K_SPACE in self.engine.keystrokes : 
        if self.powerFrames > 0 :
          self.powerFrames -= 1
          self.engine.change_hp = 0
        else : self.engine.change_hp = 10
      else : self.isPower = False
      
    #Power Speed
    if self.Power == "Speed" :
      if K_SPACE in self.engine.keystrokes : 
        if self.powerFrames > 0 :
          self.powerFrames -= 1
          self.deplacement = 4
        else : self.deplacement = 2
      else : self.isPower = False
      
    #Power Bullet-Time
    if self.Power == "Bullet-Time" :
      if K_SPACE in self.engine.keystrokes : 
        if self.powerFrames > 0 :
          self.isPower = True
          self.powerFrames -= 1
          self.Gun.fireRate = 20
        else : self.isPower = False ; self.Gun.fireRate = 10
      else : self.isPower = False ; self.Gun.fireRate = 10

    #Mouvements Latéraux et horizontaux 
    if K_q in self.engine.keystrokes :
        self.deltaPos[0] -= self.deplacement
    if K_d in self.engine.keystrokes :
        self.deltaPos[0] += self.deplacement
    if K_z in self.engine.keystrokes :
        self.deltaPos[1] -= self.deplacement
    if K_s in self.engine.keystrokes :
        self.deltaPos[1] += self.deplacement

    if self.Gun.angle < 180 :
      self.Sprite = self.SpriteDos

    if self.Rect.topleft[0] + 2 <= pygame.mouse.get_pos()[0] // self.engine.rapport <= self.Rect.topright[0] - 2 :
      self.canFlip = False

    if (self.Gun.angle + 90) % 360 < 180 and self.canFlip:
      self.Sprite = pygame.transform.flip(self.Sprite, True, False)

    #Application du mouvement
    self.Rect = pygame.Rect.move(self.Rect, (self.deltaPos[0], self.deltaPos[1]))
    self.collideRect = pygame.Rect.move(self.collideRect, (self.deltaPos[0], self.deltaPos[1]))
    #print(self.collideRect.bottom)

    #Collisions 
    for collision in self.engine.collisions :
      if self in collision and not self.Gun in collision :
        #print(collision.index(self))
        collider = collision[(collision.index(self) + 1) % 2]
        if "Bullet" == collider.__class__.__name__ :
          if "Enemy" == collider.source.__class__.__name__ :
            collider.Destroy()
            self.colorShiftDuration = 10
            self.engine.Touche = True  
            self.nombredefoisoutouche = 0
        elif "Enemy" == collider.__class__.__name__ :
          self.colorShiftDuration = 10
           
    if self.colorShiftDuration > 0:
      self.Sprite = Fonctions.colorShift(self.Sprite,(133, 33, 18))
      self.colorShiftDuration -= 1
        
    #Update
    super().Update()