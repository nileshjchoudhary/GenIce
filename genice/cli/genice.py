import sys
import argparse as ap
import logging
from genice.plugin import safe_import
from genice import __version__
from genice.cli import SmartFormatter, help_format, logger_setup
from genice.genice import GenIce
from genice.plugin import descriptions


# 遅延評価。descriptions()関数は重いので、必要なければ呼びたくない。
def help_type():
    return 'R|Crystal type (1c, 1h, etc. See https://github.com/vitroid/GenIce for available ice structures.)\n\nIf you want to analyze your own structures, please try analice tool.\n\n' + descriptions("lattice", width=55)

def getoptions():
    parser = ap.ArgumentParser(description='GenIce is a swiss army knife to generate hydrogen-disordered ice structures. (version {0})'.format(__version__), prog='genice', formatter_class=SmartFormatter)
    parser.add_argument('--version',
                        '-V',
                        action='version',
                        version='%(prog)s {0}'.format(__version__))
    parser.add_argument('--rep',
                        '-r',
                        nargs=3,
                        type=int,
                        dest='rep',
                        default=[1, 1, 1],
                        help='Repeat the unit cell along a, b, and c axes. [1,1,1]')
    parser.add_argument('--shift',
                        '-S',
                        nargs=3,
                        type=float,
                        dest='shift',
                        default=[0., 0., 0.],
                        help='Shift the unit cell along a, b, and c axes. (0.5==half cell) [0,0,0]')
    parser.add_argument('--dens',
                        '-d',
                        type=float,
                        dest='dens',
                        default=-1,
                        help='Specify the ice density in g/cm3 (Guests are not included.)')
    parser.add_argument('--add_noise',
                        type=float,
                        dest='noise',
                        default=0.,
                        metavar='percent',
                        help='Add a Gauss noise with given width (SD) to the molecular positions of water. The value 1 corresponds to 1 percent of the molecular diameter of water.')
    parser.add_argument('--seed',
                        '-s',
                        type=int,
                        dest='seed',
                        default=1000,
                        help='Random seed [1000]')
    parser.add_argument('--format',
                        '-f',
                        dest='format',
                        default="gromacs",
                        metavar="name",
                        help=help_format)
    parser.add_argument('--water',
                        '-w',
                        dest='water',
                        default="tip3p",
                        metavar="model",
                        help='Specify water model. (tip3p, tip4p, etc.) [tip3p]')
    parser.add_argument('--guest',
                        '-g',
                        nargs=1,
                        dest='guests',
                        metavar="D=empty",
                        action="append",
                        help='Specify guest(s) in the cage type. (D=empty, T=co2*0.5+me*0.3, etc.)')
    parser.add_argument('--Guest',
                        '-G',
                        nargs=1,
                        dest='spot_guests',
                        metavar="13=me",
                        action="append",
                        help='Specify guest in the specific cage. (13=me, 32=co2, etc.)')
    parser.add_argument('--Group',
                        '-H',
                        nargs=1,
                        dest='groups',
                        metavar="13=bu-:0",
                        action="append",
                        help='Specify the group. (-H 13=bu-:0, etc.)')
    parser.add_argument('--anion',
                        '-a',
                        nargs=1,
                        dest='anions',
                        metavar="3=Cl",
                        action="append",
                        help='Specify a monatomic anion that replaces a water molecule. (3=Cl, 39=F, etc.)')
    parser.add_argument('--cation',
                        '-c',
                        nargs=1,
                        dest='cations',
                        metavar="3=Na",
                        action="append",
                        help='Specify a monatomic cation that replaces a water molecule. (3=Na, 39=NH4, etc.)')
    parser.add_argument('--visual',
                        dest='visual',
                        default="",
                        metavar="visual",
                        help='Specify the yaplot file to store the depolarization paths. [""]')
    parser.add_argument('--depol',
                        dest='depol',
                        default="strict",
                        help='Depolarization. (strict, optimal, or none) ["strict"]')
    parser.add_argument('--asis',
                        action='store_true',
                        dest='asis',
                        default=False,
                        help='Assumes all given HB pairs to be fixed. No shuffle and no depolarization.')
    parser.add_argument('--debug',
                        '-D',
                        action='store_true',
                        dest='debug',
                        help='Output debugging info.')
    parser.add_argument('--quiet',
                        '-q',
                        action='store_true',
                        dest='quiet',
                        help='Do not output progress messages.')
    parser.add_argument('Type',
                        help=help_type)
    return parser.parse_args()










def main():
    # Module-loading paths
    # 1. Look for the modules in the current working directory
    sys.path.append(".")

    # Parse options
    options = getoptions()

    # Set verbosity level
    logger = logger_setup(options.debug, options.quiet)
    logger.debug("Debug mode.")

    logger.debug(options.Type)

    lattice_type = options.Type
    seed = options.seed
    rep = options.rep
    sh  = options.shift
    density = options.dens
    asis = options.asis
    anions = dict()
    if options.anions is not None:
        logger.info(options.anions)
        for v in options.anions:
            key, value = v[0].split("=")
            anions[int(key)] = value
    cations = dict()
    if options.cations is not None:
        for v in options.cations:
            key, value = v[0].split("=")
            cations[int(key)] = value
    spot_guests = dict()
    if options.spot_guests is not None:
        for v in options.spot_guests:
            key, value = v[0].split("=")
            spot_guests[int(key)] = value
    groups = dict()
    if options.groups is not None:
        for v in options.groups:
            key, value = v[0].split("=")
            groups[int(key)] = value

    logger.debug("Lattice: {0}".format(lattice_type))
    assert lattice_type is not None

    signature = "Command line: {0}".format(" ".join(sys.argv))

    # Initialize the Lattice class with arguments which are required for plugins.
    lat = GenIce(safe_import("lattice", lattice_type),
                signature=signature,
                density=density,
                rep=rep,
                cations=cations,
                anions=anions,
                spot_guests=spot_guests,
                spot_groups=groups,
                asis=asis,
                shift=sh,
                seed=seed,
    )

    water_type = options.water
    guests = options.guests
    noise = options.noise
    depol = options.depol
    file_format = options.format

    # Main part of the program is contained in th Formatter object. (See formats/)
    logger.debug("Output file format: {0}".format(file_format))
    formatter = safe_import("format", file_format)

    if options.visual != "":
        record_depolarization_path = open(options.visual, "w")
    else:
        record_depolarization_path = None

    del options  # Dispose for safety.

    lat.generate_ice(water_type=water_type,
                     guests=guests,
                     formatter=formatter,
                     record_depolarization_path=record_depolarization_path,
                     noise=noise,
                     depol=depol,
                     )


if __name__ == "__main__":
    main()