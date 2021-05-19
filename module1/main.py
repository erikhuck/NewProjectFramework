"""Pareses the arguments of the selected handler and executes that handler"""

from argparse import Namespace
from sys import argv
from dotenv import load_dotenv

from python_scripts.utils.parse_args import parse_args


def main():
    """Main function of this repository"""

    # Load the environment variables in the .env file, accessible via os.getenv('NAME_OF_ENVIRONMENT_VARIABLE')
    load_dotenv('.env')

    args: Namespace = parse_args(argv[1:])

    if args.handler_type == 'handler-type1':
        pass
    elif args.handler_type == 'handler-type2':
        pass


if __name__ == '__main__':
    main()
