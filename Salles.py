import pygame, random, os, json

def ChargerSalle(fichier, moteur):
  with open(fichier, "r") as fichierNiveau:
    niveau = json.load(fichierNiveau)

  #print(len(niveau), len(niveau[0]))
  return niveau

def RenderSalle(niveau, moteur) :

  tileReferences = []
  tiles = {}
  assetFile = "Assets/Tiles"
  with os.scandir("./" + assetFile + "/") as referenceList :
    for item in referenceList :
      if item.name.endswith(".png") :
        tileReferences.append(item.name)
        tiles[tileReferences[-1]] = pygame.image.load("./" + assetFile + "/" + tileReferences[-1])

  surface = pygame.Surface((moteur.Rlongueur, moteur.Rlargeur))

  surface.fill((39,39,68))

  #print(niveau)
  
  xmax = 16
  ymax = 12

  walls =[]
  
  for x in range(xmax) :
    for y in range(ymax) :
      #for image in niveau[x][y]:
      if niveau[y][x] != 0 :
        image = tiles[niveau[y][x]]
        if "Floor" in niveau[y][x]:
          surface.blit(image, (x * 16, (y + 1) * 16 - image.get_rect().height))
        else:
          walls.append([assetFile + "/" + niveau[y][x], (x * 16, (y + 1) * 16 - image.get_rect().height), image.get_rect().width, image.get_rect().height])
          #walls.append([assetFile + "/" + niveau[y][x], (x * 16, y * 16), image.get_rect().width, image.get_rect().height])
  
  """
  for x in range(xmax):
    for y in range(ymax):
      for image in niveau[xmax - x - 1][ymax - y - 1]:
        for i in range(len(niveau[xmax - x - 1][ymax - y - 1]) - 1):
          surface.blit(niveau[xmax - x - 1][ymax - y - 1][i + 1], (x * 16, y * 16))
  """
  for wall in walls:
    #print(wall[1])
    pass
  return surface, walls

def GenererSalle(moteur) :
  #On collectionne tous les fichiers image
  tileReferences = []
  assetFile = "Assets/Tiles"
  with os.scandir("./" + assetFile + "/") as referenceList :
    for item in referenceList :
      if item.name.endswith(".png") :
        tileReferences.append(item.name)

  #On charge toutes les images
  tiles = []
  for tileRef in tileReferences :
    tiles.append(pygame.image.load("./" + assetFile + "/" + tileRef))

  floorTileReferences = []
  assetFile = "Assets/Tiles/Floor"
  with os.scandir("./" + assetFile + "/") as referenceList :
    for item in referenceList :
      if item.name.endswith(".png") :
        floorTileReferences.append(item.name)

  #On charge toutes les images
  floorTiles = []
  for tileRef in floorTileReferences :
    floorTiles.append(pygame.image.load("./" + assetFile + "/" + tileRef))

  niveau = [[0] * moteur.Rlargeur for i in range(moteur.Rlongueur)]

  #walls = []

  for x in range(moteur.Rlongueur//16) :
    for y in range(moteur.Rlargeur//16) :
      niveau[x][y] = [floorTiles[random.randint(0, len(floorTiles) - 1)]]
      if random.randint(0,2) == 2:
        niveau[x][y].append(tiles[0])
        
  return niveau
  #cetteteam est debile je veux mourir
