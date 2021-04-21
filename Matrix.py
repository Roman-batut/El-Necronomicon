#DES MATRIIIICES
import math
import numpy as np

def rotMat(vec2d, thetaD):
  thetaR = thetaD * math.pi / 180

  npVec = np.array(vec2d)

  #Permet de calculer directement les coordonées d'un point après une rotation autour d'un point
  mat = np.array([[math.cos(thetaR), -math.sin(thetaR)],
                  [math.sin(thetaR), math.cos(thetaR)]])

  result = npVec.dot(mat)
  return result.tolist()