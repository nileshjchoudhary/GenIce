"""

Command line: /Volumes/workarea/venvs/genice2/bin/genice zeolite[NON] -f python
Reshaping the unit cell.
  i:[1 0 0]
  j:[0 1 0]
  k:[0 0 1]
"""

desc={
    "ref": {
        "engel34": "Engel, E.A., Anelli, A., Ceriotti, M. et al. Mapping uncharted territory in ice from zeolite networks to ice structures. Nat Commun 9, 2173 (2018). https://doi.org/10.1038/s41467-018-04618-6",
        "NON": "Database of Zeolite Structures, https://asia.iza-structure.org/IZA-SC/framework.php?STC=NON"
    },
    "usage": "No options available.",
    "brief": "Hypothetical zeolitic ice"
}

import genice2.lattices
class Lattice(genice2.lattices.Lattice):
    def __init__(self):
        self.bondlen=0.30360000000000015
        self.coord='relative'
        from genice2.cell import cellvectors
        self.cell = cellvectors(a=2.05810969, b=1.40940273, c=1.25447286)
        self.density=0.7228522408550825
        self.waters="""
    0.2222    0.5000    0.0000
    0.2222    0.0000    0.5000
    0.7222    0.0000    0.0000
    0.7222    0.5000    0.5000
    0.7778    0.5000    0.0000
    0.7778    0.0000    0.5000
    0.2778    0.0000    0.0000
    0.2778    0.5000    0.5000
    0.8162    0.5000    0.2108
    0.8162    0.0000    0.7108
    0.3162    0.0000    0.2108
    0.3162    0.5000    0.7108
    0.1838    0.5000    0.2108
    0.1838    0.0000    0.7108
    0.6838    0.0000    0.2108
    0.6838    0.5000    0.7108
    0.1838    0.5000    0.7892
    0.1838    0.0000    0.2892
    0.6838    0.0000    0.7892
    0.6838    0.5000    0.2892
    0.8162    0.5000    0.7892
    0.8162    0.0000    0.2892
    0.3162    0.0000    0.7892
    0.3162    0.5000    0.2892
    0.0000    0.1018    0.8873
    0.0000    0.6018    0.3873
    0.5000    0.6018    0.8873
    0.5000    0.1018    0.3873
    0.0000    0.8982    0.8873
    0.0000    0.3982    0.3873
    0.5000    0.3982    0.8873
    0.5000    0.8982    0.3873
    0.0000    0.8982    0.1127
    0.0000    0.3982    0.6127
    0.5000    0.3982    0.1127
    0.5000    0.8982    0.6127
    0.0000    0.1018    0.1127
    0.0000    0.6018    0.6127
    0.5000    0.6018    0.1127
    0.5000    0.1018    0.6127
    0.2031    0.6736    0.5000
    0.2031    0.1736    0.0000
    0.7031    0.1736    0.5000
    0.7031    0.6736    0.0000
    0.7969    0.6736    0.5000
    0.7969    0.1736    0.0000
    0.2969    0.1736    0.5000
    0.2969    0.6736    0.0000
    0.2031    0.3264    0.5000
    0.2031    0.8264    0.0000
    0.7031    0.8264    0.5000
    0.7031    0.3264    0.0000
    0.7969    0.3264    0.5000
    0.7969    0.8264    0.0000
    0.2969    0.8264    0.5000
    0.2969    0.3264    0.0000
    0.8757    0.1625    0.1897
    0.8757    0.6625    0.6897
    0.3757    0.6625    0.1897
    0.3757    0.1625    0.6897
    0.1243    0.1625    0.1897
    0.1243    0.6625    0.6897
    0.6243    0.6625    0.1897
    0.6243    0.1625    0.6897
    0.8757    0.8375    0.1897
    0.8757    0.3375    0.6897
    0.3757    0.3375    0.1897
    0.3757    0.8375    0.6897
    0.1243    0.8375    0.1897
    0.1243    0.3375    0.6897
    0.6243    0.3375    0.1897
    0.6243    0.8375    0.6897
    0.1243    0.8375    0.8103
    0.1243    0.3375    0.3103
    0.6243    0.3375    0.8103
    0.6243    0.8375    0.3103
    0.8757    0.8375    0.8103
    0.8757    0.3375    0.3103
    0.3757    0.3375    0.8103
    0.3757    0.8375    0.3103
    0.1243    0.1625    0.8103
    0.1243    0.6625    0.3103
    0.6243    0.6625    0.8103
    0.6243    0.1625    0.3103
    0.8757    0.1625    0.8103
    0.8757    0.6625    0.3103
    0.3757    0.6625    0.8103
    0.3757    0.1625    0.3103
"""
