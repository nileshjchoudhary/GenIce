"""

Reshaping the unit cell.
  i:[ 1  1 -2]
  j:[ 1 -1  0]
  k:[1 1 1]
"""
import genice2.lattices
class Lattice(genice2.lattices.Lattice):
    def __init__(self):
        self.bondlen=0.29903306849378936
        self.coord='relative'

        import numpy as np
        self.cell=np.array([        [2.10215724, 0.00000000, 0.00000000],         [0.03387842, 1.07311259, 0.00000000],         [-0.22855330, 0.07358108, -1.38262585],         ])
        self.density=0.92
        self.waters="""
    0.9446    0.9625    0.2621
    0.1733    0.0289    0.4689
    0.1390    0.0504    0.6491
    0.0075    0.0277    0.6359
    0.8680    0.1077    0.3586
    0.9738    0.7980    0.5681
    0.1098    0.2149    0.3431
    0.9440    0.2137    0.5101
    0.8424    0.7753    0.5548
    0.0081    0.7765    0.3879
    0.1396    0.7992    0.4011
    0.0338    0.1090    0.1915
    0.0332    0.3601    0.4396
    0.8674    0.3589    0.6066
    0.9732    0.0492    0.8161
    0.7789    0.9613    0.4291
    0.6113    0.9625    0.5954
    0.8399    0.0289    0.8022
    0.8056    0.0504    0.9824
    0.6742    0.0277    0.9692
    0.5347    0.1077    0.6919
    0.6405    0.7980    0.9014
    0.7765    0.2149    0.6765
    0.6107    0.2137    0.8435
    0.5090    0.7753    0.8882
    0.6748    0.7765    0.7212
    0.8063    0.7992    0.7344
    0.7004    0.1090    0.5248
    0.6998    0.3601    0.7730
    0.5341    0.3589    0.9399
    0.6399    0.0492    0.1495
    0.4456    0.9613    0.7624
    0.2780    0.9625    0.9288
    0.5066    0.0289    0.1356
    0.4723    0.0504    0.3158
    0.3408    0.0277    0.3026
    0.2013    0.1077    0.0252
    0.3071    0.7980    0.2347
    0.4431    0.2149    0.0098
    0.2773    0.2137    0.1768
    0.1757    0.7753    0.2215
    0.3415    0.7765    0.0545
    0.4729    0.7992    0.0677
    0.3671    0.1090    0.8582
    0.3665    0.3601    0.1063
    0.2008    0.3589    0.2733
    0.3066    0.0492    0.4828
    0.1122    0.9613    0.0957
    0.1113    0.4625    0.5954
    0.3399    0.5289    0.8022
    0.3056    0.5504    0.9824
    0.1742    0.5277    0.9692
    0.0347    0.6077    0.6919
    0.1405    0.2980    0.9014
    0.2765    0.7149    0.6765
    0.1107    0.7137    0.8435
    0.0090    0.2753    0.8882
    0.1748    0.2765    0.7212
    0.3063    0.2992    0.7344
    0.2004    0.6090    0.5248
    0.1998    0.8601    0.7730
    0.0341    0.8589    0.9399
    0.1399    0.5492    0.1495
    0.9456    0.4613    0.7624
    0.7780    0.4625    0.9288
    0.0066    0.5289    0.1356
    0.9723    0.5504    0.3158
    0.8408    0.5277    0.3026
    0.7013    0.6077    0.0252
    0.8071    0.2980    0.2347
    0.9431    0.7149    0.0098
    0.7773    0.7137    0.1768
    0.6757    0.2753    0.2215
    0.8415    0.2765    0.0545
    0.9729    0.2992    0.0677
    0.8671    0.6090    0.8582
    0.8665    0.8601    0.1063
    0.7008    0.8589    0.2733
    0.8066    0.5492    0.4828
    0.6122    0.4613    0.0957
    0.4446    0.4625    0.2621
    0.6733    0.5289    0.4689
    0.6390    0.5504    0.6491
    0.5075    0.5277    0.6359
    0.3680    0.6077    0.3586
    0.4738    0.2980    0.5681
    0.6098    0.7149    0.3431
    0.4440    0.7137    0.5101
    0.3424    0.2753    0.5548
    0.5081    0.2765    0.3879
    0.6396    0.2992    0.4011
    0.5338    0.6090    0.1915
    0.5332    0.8601    0.4396
    0.3674    0.8589    0.6066
    0.4732    0.5492    0.8161
    0.2789    0.4613    0.4291
"""

