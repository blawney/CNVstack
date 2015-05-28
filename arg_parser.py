import argparse
import os

class MakeAbsolutePathAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, os.path.realpath(os.path.abspath(values)))

def parse():
    '''
    Parses the command line args
    :return: Dictionary of commandline options
    '''
    parser = setup_parser()
    return vars(parser.parse_args())


def setup_parser():
    '''
    Adds arguments to the parser
    :return: a configured ArgumentParser object
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-b",
                        "--bedfile",
                        required = True,
                        action = MakeAbsolutePathAction,
                        dest = "bedfile")
    return parser