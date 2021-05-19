from argparse import ArgumentParser, Namespace


def parse_args(argv) -> Namespace:
    """Gets the arguments for this repo"""

    parser: ArgumentParser = ArgumentParser()

    subparsers = parser.add_subparsers(dest='handler_type', title='handler_type')
    subparsers.required = True

    handler_type1_parser: ArgumentParser = subparsers.add_parser('handler-type1')
    pass
    handler_type2_parser: ArgumentParser = subparsers.add_parser('handler-type2')
    pass

    args: Namespace = parser.parse_args(argv)
    return args
