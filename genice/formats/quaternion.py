import logging

import numpy as np

from genice import rigid

def run(lattice, water_type="TIP3P", guests=[]):
    """
    Rigid water molecule 
    """
    logger = logging.getLogger()
    lattice.stage1()   #replicate the unit cell
    lattice.stage2()   #prepare random graph
    lattice.stage3()   #Make an ice graph
    lattice.stage4()   #Depolarize
    lattice.stage5()   #Orientation
    logger.info("Output water molecules as rigid rotors (Quaternion).")
    s = ""
    if lattice.cell[1,0] == 0 and lattice.cell[2,0] == 0 and lattice.cell[2,1] == 0:
        s += "@BOX3\n"
        s += "{0} {1} {2}\n".format(lattice.cell[0,0]*10,lattice.cell[1,1]*10,lattice.cell[2,2]*10)
    else:
        s += "@BOX9\n"
        for d in range(3):
            s += "{0} {1} {2}\n".format(lattice.cell[0,d]*10,lattice.cell[1,d]*10,lattice.cell[2,d]*10)
    s += "@NX4A\n"
    s += "{0}\n".format(len(lattice.reppositions))
    for i in range(len(lattice.reppositions)):
        position = np.dot(lattice.reppositions[i],lattice.cell)*10   #in Angstrom
        quat     = rigid.rotmat2quat(lattice.rotmatrices[i].transpose())
        s += "{0:9.4f} {1:9.4f} {2:9.4f}  {3:9.4f} {4:9.4f} {5:9.4f} {6:9.4f}\n".format(position[0],
                                                                            position[1],
                                                                            position[2],
                                                                            quat[0],
                                                                            quat[1],
                                                                            quat[2],
                                                                            quat[3])
    s = "\n".join(lattice.doc) + "\n" + s
    print(s,end="")