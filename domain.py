import numpy as np
import torch

# Total domain : [-1,1]
def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

# convert (rho, phi) -> (x,y)
def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

def soft_weight(bdry, eps):
    return (1-bdry/eps)*(np.abs(bdry)<eps)


# is_star <0 means inside star, >0 outside star
def is_star(x,y) :
    n = 5
    m = 3
    r, theta = cart2pol(x,y)
    nom = np.cos((2*np.arcsin(1)+np.pi*m)/(2*n))
    denom = np.cos((2*np.arcsin(np.cos(n*theta))+np.pi*m)/(2*n))
    return r - nom/denom


def circle(x,y) :
    return x**2 + y**2 -1


#small insdie radius : r
def donut(x,y,r) :
    return np.min(x**2+y**2-r**2, 1-x**2-y**2)


def ellipse(x,y, a, b) :
    return x**2/a+y**2/b-1


