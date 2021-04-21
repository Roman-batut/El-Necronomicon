#Imports
import pygame
from PIL import Image, ImageFilter

#Effet de Blur
def blur(fenetre) :
    pygame.image.save(fenetre, "Assets/paused.jpeg")
    pausedImage = Image.open("Assets/paused.jpeg")
    blurredimage = pausedImage.filter(ImageFilter.GaussianBlur(3))
    blurredimage.save('Assets/paused.jpeg')
    pausedImageF = pygame.image.load("Assets/paused.jpeg")
    fenetre.blit(pausedImageF, (0, 0))

#Tests de collision
def isColliding(contenu) :
  contenuCopy = contenu.copy()
  collisions = []
  for entity in contenuCopy :
    if entity.hasRect :
      try :
        rect1 = entity.collideRect
      except AttributeError:
        rect1 = entity.Rect
      for entity2 in contenuCopy:
        if entity2.hasRect:
          try :
            rect2 = entity2.collideRect
          except AttributeError:
            rect2 = entity2.Rect
          if rect1.colliderect(rect2):
            collisions.append([entity, entity2])
  return collisions

#Effet de changement de couleur
def colorShift(image, color) :
        image = image.convert_alpha()
        colorImage = pygame.Surface(image.get_rect().size).convert_alpha()
        colorImage.fill(color)
        image.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
        return image