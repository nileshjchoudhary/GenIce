#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Plugin handler.
"""

from logging import getLogger, basicConfig, INFO, DEBUG
import re
import pkg_resources as pr
import glob
import os
import importlib
import sys
from collections import defaultdict
from textwrap import fill
from genice2.decorators import timeit, banner

def scan(category):
    logger = getLogger()

    modules = {}
    desc = dict()
    modules["desc"] = desc

    logger.info("\nPredefined {0}s".format(category))
    module = importlib.import_module("genice2.{0}s".format(category))
    mods = []
    for path in module.__path__:
        for mod in sorted(glob.glob(path+"/*.py")):
            mod = os.path.basename(mod)[:-3]
            if mod[:2] != "__":
                mods.append(mod)
    logger.info(mods)
    modules["system"] = mods

    for mod in modules["system"]:
        try:
            module = importlib.import_module("genice2.{0}s.{1}".format(category, mod))
            if "desc" in module.__dict__:
                desc[mod] = module.desc["brief"]
        except:
            pass

    logger.info("Extra {0}s".format(category))
    groupname = 'genice_{0}'.format(category)
    mods = []
    for ep in pr.iter_entry_points(group=groupname):
        label, m = str(ep).split("=")
        mods.append(label)
        try:
            module = ep.load()
            if "desc" in module.__dict__:
                desc[label] = module.desc["brief"]
        except:
            pass
    logger.info(mods)
    modules["extra"] = mods

    logger.info("Local {0}s".format(category))
    mods = [os.path.basename(mod)[:-3] for mod in sorted(glob.glob("./{0}s/*.py".format(category)))]
    for mod in mods:
        module = importlib.import_module("{0}s.{1}".format(category, mod))
        if "desc" in module.__dict__:
            desc[mod] = module.desc["brief"]
    logger.info(mods)
    modules["local"] = mods

    return modules



def descriptions(category, width=72):
    titles={ "lattice": {"system": "1. Lattice structures served with GenIce",
                         "extra":  "2. Lattice structures served by external plugins",
                         "local":  "3. Lattice structures served locally",
                         "title":  "[Available lattice structures]"},
             "format": {"system": "1. Formatters served with GenIce",
                        "extra":  "2. Formatters served by external plugins",
                        "local":  "3. Formatters served locally",
                        "title":  "[Available formatters]"},
             "loader": {"system": "1. File types served with GenIce",
                        "extra":  "2. File types served by external eplugins",
                        "local":  "3. File types served locally",
                        "title":  "[Available input file types]"},
             "molecule": {"system": "1. Molecules served with GenIce",
                        "extra":  "2. Molecules served by external plugins",
                        "local":  "3. Molecules served locally",
                        "title":  "[Available molecules]"},
             }
    mods = scan(category)
    catalog = " \n \n{0}\n \n".format(titles[category]["title"])
    desc = mods["desc"]
    for group in ("system", "extra", "local"):
        desced = defaultdict(list)
        undesc = []
        for L in mods[group]:
            if L in desc:
                desced[desc[L]].append(L)
            else:
                undesc.append(L)
        for dd in desced:
            desced[dd] = ", ".join(desced[dd])
        catalog += "{0}\n \n".format(titles[category][group])
        table = ""
        for dd in sorted(desced, key=lambda x: desced[x]):
            table += "{0}\t{1}\n".format(desced[dd], dd)
        if table == "":
            table = "(None)\n"
        table = [fill(line, width=width, drop_whitespace=False, expand_tabs=True, tabsize=16, subsequent_indent=" "*16) for line in table.splitlines()]
        table = "\n".join(table)+"\n"
        undesc = " ".join(undesc)
        if undesc != "":
            undesc = "(Undocumented) " + undesc
        catalog += table + "----\n" + undesc + "\n \n \n"
    return catalog


def audit_name(name):
    """
    Audit the mol name to avoid the access to external files
    """
    return re.match('^[A-Za-z0-9-_]+$', name) is not None


def import_extra(category, name):
    logger = getLogger()
    logger.info("Extra {0} plugin: {1}".format(category,name))
    groupname = 'genice_{0}'.format(category)
    module = None
    for ep in pr.iter_entry_points(group=groupname):
        logger.debug("    Entry point: {0}".format(ep))
        if ep.name == name:
            logger.debug("      Loading {0}...".format(name))
            module = ep.load()
    if module is None:
        logger.error("Nonexistent module: {0}".format(name))
        sys.exit(1)
    return module


def safe_import(category, name):
    """
    Load a plugin.

    The plugins can exist either in the system, as a extra plugin, or in the
    local folder.

    category: The type of the plugin; "lattice", "format", "molecule", or "loader".
    name:     The name of the plugin.
    """
    logger = getLogger()
    assert category in ("lattice", "format", "molecule", "loader")

    # single \? as a plugin name ==> show descriptions
    if name == "?":
        print(descriptions(category))
        sys.exit(0)

    usage = False
    if name[-1:] == "?":
        usage = True
        name = name[:-1]

    assert audit_name(name), "Dubious {0} name: {1}".format(category, name)

    module = None
    try:
        module = importlib.import_module(category + "s." + name)  # at ~/.genice
    except ImportError as e:
        pass
    if module is None:
        fullname = "genice2." + category + "s." + name
        logger.debug("Load module: {0}".format(fullname))
        try:
            module = importlib.import_module(fullname)
        except:
            pass
    if module is None:
        module = import_extra(category, name)

    if usage:
        if "desc" in module.__dict__:
            logger.info("Usage for '{0}' plugin".format(name))
            print(module.desc["usage"])
            sys.exit(0)

    return module


if __name__ == "__main__":
    basicConfig(level=INFO)
    if len(sys.argv) == 1:
        cats = ("lattice", "format", "molecule", "loader")
    else:
        cats = argv[1:]
    modules = {cat: scan(cat) for cat in cats}
    print(modules)