# coding: utf-8

desc={"ref": {"TIP3P": "Jorgensen, Chandrasekhar, Madura, Impey, Klein, J Chem Phys, 79, 926 (1983)."},
      "brief": "Physical model of water; Oxygen atom is on the lattice point.",
      "usage": "No options available."
      }

import math
import numpy as np


oh = 0.09572
hangle = 104.52 * math.pi / 180 / 2
mass=18
ohz = oh * math.cos(hangle)
ohy = oh * math.sin(hangle)
oz  = 0 # -ohz*2/mass


sites = np.array([[0, 0,oz],
                  [0, ohy,ohz+oz],
                  [0,-ohy,ohz+oz]]) # nm, OHHM

labels = ["O","H","H"]
name = "SOL"