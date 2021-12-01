#!/usr/bin/env python

"""
Simulates a fair-cake cutting procedure given n agents with valuations on a
one-dimensional cake divided into m pieces. The simulation generates agents and
their valuations given valuation generation functions, runs the specified
procedure, and reports results for each agent given their allocated piece.
"""

import sys
import logging
from optparse import OptionParser
from util import *

# import cake-cutting procedures
from dummy import DUMMY
from stromquist import STROMQUIST

# TODO add more procedures

procedures = ['dummy', 'stromquist']

class Sim:
    def __init__(self, config):
        self.config = config

    def run_sim(self):
        """Generate agents, run procedure, and print results"""
        conf = self.config
        logging.debug("Starting simulation with config: %s" % str(conf))

        # Determine the procedure to run
        if (conf.procedure.lower() == 'dummy'):
            procedure = DUMMY(conf)
        elif conf.procedure.lower() == 'stromquist':
            procedure = STROMQUIST(conf)
        # TODO add more procedures
        else:
            raise ValueError("invalid procedure %s" % conf.procedure.lower())

        # Create procedure-specific agents
        ids = range(len(conf.agents_to_run))
        agents = [procedure.agent(conf, i) for i in ids]

        # Initialize agent valuations
        for agent, (val_generator, args) in zip(agents, conf.agents_to_run):
            if val_generator == 'Uniform':
                agent.gen_uniform_valuation(*args)
            elif val_generator == 'Random':
                agent.gen_random_int_valuation(*args)
            # TODO add more valuation generators
            else:
                raise ValueError("invalid valuation generator %s"
                                 % val_generator)
        logging.debug("Agents: %s" % agents)

        # Run procedure to get a list of the pieces allocated to each agent
        allocations = procedure.run(agents)
        logging.info("Allocations: %s" % allocations)

        # TODO print summary statistics and analysis


def configure_logging(loglevel):
    """Configure logging messages"""
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    root_logger = logging.getLogger('')
    strm_out = logging.StreamHandler(sys.__stdout__)
#    strm_out.setFormatter(logging.Formatter('%(levelno)s: %(message)s'))
    strm_out.setFormatter(logging.Formatter('%(message)s'))
    root_logger.setLevel(numeric_level)
    root_logger.addHandler(strm_out)


def parse_valuations(args):
    """
    Each element is a valuation generator name like "Uniform", with an agent
    count appended after a comma, and an optional comma-separated list of
    integer arguments appended after another comma, e.g. "Uniform,1" or
    "Random,3,1,5".
    Returns an array with a list of tuples of valuation generator names and
    their arguments, each repeated the specified number of times.
    """
    ans = []
    for c in args:
        s = c.split(',')
        if len(s) == 2:
            name, count = s
            ans.extend([(name, [])]*int(count))
        elif len(s) > 2:
            name, count, val_args = s[0], s[1], s[2:]
            ans.extend([(name, list(map(int, val_args)))]*int(count))
        else:
            raise ValueError("Bad argument: %s\n" % c)
    return ans


def main(args):
    """Parse arguments, create simulation object, and run it"""
    usage_msg = ("Usage:  %prog procedure [options] "
                 "ValuationGenerator1,count[,arg1,...] "
                 "ValuationGenerator2,count[,arg1,...] ...")
    parser = OptionParser(usage=usage_msg)

    def usage(msg):
        print(("Error: %s\n" % msg))
        parser.print_help()
        sys.exit()

    parser.add_option("--loglevel",
                      dest="loglevel", default="info",
                      help="Set the logging level: 'debug' or 'info'")

    parser.add_option("--num-pieces",
                      dest="num_pieces", default=10, type="int",
                      help="Set number of pieces the cake is divided into")

    (options, args) = parser.parse_args()

    # Get procedure name
    if len(args) == 0:
        usage("expected procedure argument in %s" % procedures)
    procedure, args = args[0], args[1:]
    if procedure not in procedures:
        usage("invalid procedure %s" % procedure)

    # Leftover args are valuation generator names, with counts and optional
    # arguments, e.g. "Uniform,3" or "Random,3,1,5"
    if len(args) == 0:
        # Default to three uniform agents
        agents_to_run = [('Uniform', []), ('Uniform', []), ('Uniform', [])]
    else:
        try:
            agents_to_run = parse_valuations(args)
        except ValueError as e:
            usage(e)

    configure_logging(options.loglevel)

    config = Params()
    config.add("procedure", procedure)
    config.add("num_pieces", options.num_pieces)
    config.add("agents_to_run", agents_to_run)

    sim = Sim(config)
    sim.run_sim()

if __name__ == "__main__":
    # The next two lines are for profiling
    import cProfile
    cProfile.run('main(sys.argv)', 'out.prof')
#    main(sys.argv)
