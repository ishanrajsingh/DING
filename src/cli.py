import argparse

def init(args):
    print("To be implemented")

def parse_args():
    parser= argparse.ArgumentParser(prog="ding")

    commands= parser.add_subparsers(dest="command", required=True)

    init_parser = commands.add_parser("init")
    init_parser.set_defaults(func=init)

    return parser.parse_args()


def main():
    args = parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
