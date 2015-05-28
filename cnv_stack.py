import arg_parser
import data_factory


def main():
    args = arg_parser.parse()
    print args
    factory = data_factory.DataFactory(args.get("bedfile"))


if __name__ == '__main__':
    main()

