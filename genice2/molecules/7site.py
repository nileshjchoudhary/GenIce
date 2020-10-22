# coding: utf-8
desc={"ref": {"TIP7P": "Zhao, C.-L. et al. Seven-Site Effective Pair Potential for Simulating Liquid Water. J. Phys. Chem. B 123, 4594–4603 (2019)."},
      "brief": "A seven-site water model.",
      "usage": "No options available."
      }

import math
import numpy as np


from logging import getLogger
import genice2.molecules

class Molecule(genice2.molecules.Molecule):

    def __init__(self):
        oh = 0.04786*2 #nm
        ol = 0.041    #nm
        hangle = math.radians(104.52) / 2
        mangle = math.radians(109.47) / 2
        mass=18
        ohz = oh * math.cos(hangle)
        ohy = oh * math.sin(hangle)
        olz =-ol * math.cos(mangle)
        olx = ol * math.sin(mangle)
        oz  = -ohz*2/mass


        self.sites = np.array([[0, 0,oz],
                          [0, ohy,ohz+oz],
                          [0,-ohy,ohz+oz],
                          [0, ohy/2,ohz/2+oz],
                          [0,-ohy/2,ohz/2+oz],
                          [ olx,0,olz+oz],
                          [-olx,0,olz+oz],
                          ]) # nm, OHHMMLL

        self.atoms = ["O", "H", "H", ".", ".", ".", "."]
        self.labels = ["OW","HW1","HW2","MW1","MW2","LW1","LW2"]
        self.name = "SOL"