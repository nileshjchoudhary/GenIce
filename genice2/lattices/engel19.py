desc={
    "ref": {
        "91_2_8335121": "Engel, E.A., Anelli, A., Ceriotti, M. et al. Mapping uncharted territory in ice from zeolite networks to ice structures. Nat Commun 9, 2173 (2018). https://doi.org/10.1038/s41467-018-04618-6",
        "engel19": "Engel, E.A., Anelli, A., Ceriotti, M. et al. Mapping uncharted territory in ice from zeolite networks to ice structures. Nat Commun 9, 2173 (2018). https://doi.org/10.1038/s41467-018-04618-6"
    },
    "usage": "No options available.",
    "brief": "Hypothetical zeolitic ice"
}
import numpy as np
import genice2.lattices
from genice2.cell import cellvectors

class Lattice(genice2.lattices.Lattice):
    def __init__(self):
        self.cell = np.array([
            [6.331905, 0.67821, 0.172529],
            [0.341629, 2.362688, 0.104548],
            [-0.194688, -0.045858, 19.24393],
        ])
        self.waters = np.array([
            [0.539971, -0.115768, 0.452746],
            [-0.650595, -0.018121, -0.049594],
            [-0.468972, -0.385463, -0.184161],
            [-0.626046, -0.063437, -0.424731],
            [0.401823, 0.207404, 0.305102],
            [0.570927, -0.111427, 0.073114],
            [-0.382022, 0.16204, -0.308987],
            [0.279838, 0.736876, 0.178377],
            [0.104891, -0.433818, -0.173447],
            [-0.181639, 0.404043, 0.322565],
            [0.117547, -0.152965, 0.413358],
            [-0.175868, 0.153089, 0.177791],
            [-0.191194, 0.009668, -0.073435],
            [0.049651, -0.23942, -0.323133],
            [0.049165, 0.53938, 0.040609],
            [-0.094826, -0.616247, -0.466185],
        ])
        self.coord = 'relative'
