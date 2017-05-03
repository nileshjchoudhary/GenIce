import logging
from genice import rigid


def run(lattice, water_type="TIP3P", guests=[]):
    """
    Gro file format
    defined in http://manual.gromacs.org/current/online/gro.html
    """
    logger = logging.getLogger()
    lattice.stage1()   #replicate the unit cell
    res = lattice.stage2()   #prepare random graph
    if not res:
        self.rotmatrices = [rigid.rand_rotation_matrix() for pos in self.reppositions]
    else:
        lattice.stage3()   #Make an ice graph
        lattice.stage4()   #Depolarize
        lattice.stage5()   #Orientation
    lattice.stage6(water_type)  #Water atoms
    lattice.stage7(guests)      #Guest atoms
    logger.info("Total number of atoms: {0}".format(len(lattice.atoms)))
    logger.info("Output in Gromacs format.")
    if len(lattice.atoms) > 99999:
        logger.info("Gromacs fixed format cannot deal with atoms more than 99999. Residue number and atom number are faked.")
    s = ""
    s += "#Generated by GenIce https://github.com/vitroid/GenIce \n"
    s += "{0}\n".format(len(lattice.atoms))
    molorder = 0
    for i in range(len(lattice.atoms)):
        resno, resname, atomname, position = lattice.atoms[i]
        if resno == 0:
            molorder += 1
        if len(lattice.atoms) > 99999:
            s += "{0:5d}{1:5s}{2:>5s}{3:5d}{4:8.3f}{5:8.3f}{6:8.3f}\n".format(9999,resname, atomname, 9999,position[0],position[1],position[2])
        else:
            s += "{0:5d}{1:5s}{2:>5s}{3:5d}{4:8.3f}{5:8.3f}{6:8.3f}\n".format(molorder,resname, atomname, i+1,position[0],position[1],position[2])
    if lattice.cell[1,0] == 0 and lattice.cell[2,0] == 0 and lattice.cell[2,1] == 0:
        s += "    {0} {1} {2}\n".format(lattice.cell[0,0],lattice.cell[1,1],lattice.cell[2,2])
    else:
        assert lattice.cell[0,1] == 0 and lattice.cell[0,2] == 0 and lattice.cell[1,2] == 0
        s += "    {0} {1} {2} {3} {4} {5} {6} {7} {8}\n".format(lattice.cell[0,0],
                                                                    lattice.cell[1,1],
                                                                    lattice.cell[2,2],
                                                                    lattice.cell[0,1],
                                                                    lattice.cell[0,2],
                                                                    lattice.cell[1,0],
                                                                    lattice.cell[1,2],
                                                                    lattice.cell[2,0],
                                                                    lattice.cell[2,1],
                                                                    )
    s += '#' + "\n#".join(lattice.doc) + "\n"
    print(s,end="")