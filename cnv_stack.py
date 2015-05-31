import arg_parser
from data_factory import DataFactory
from draw import Artist


def main():
    args = arg_parser.parse()
    print args
    factory = DataFactory(args.get("bedfile"))
    artist = Artist(factory)
    artist.draw()

if __name__ == '__main__':
    main()

