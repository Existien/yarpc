from argparse import ArgumentParser
import os
import sys
from yarpc.spec_loader import SpecLoader
from yarpc.spec_resolver import SpecResolver
from yarpc.generator import Generator

def __parse_args():
    """Parses the command line arguments

    Returns:
        Namespace: Object containing the parsed command line arguments
    """
    parser = ArgumentParser(
        description="Codegenerator for creating D-Bus "
        "clients and services from yaml specifications"
    )
    parser.add_argument(
        "--check", action="store_true",
        help="Don't generate files, but return a non-zero exit code when the "
            "existing files are not consistent with the yaml specifications.",
        default=False
    )
    parser.add_argument(
        "spec_dir", metavar="YAML_SPEC_DIRECTORY",
        help="The directory containing he yaml specifications."
    )
    parser.add_argument(
        "--output-base", metavar="OUTPUT_BASE_DIRECTORY",
        help="The directory the relative paths in the YAML spec are relative to.",
        default=os.getcwd()
    )
    return parser.parse_args(sys.argv[1:])

def main():
    args = __parse_args()
    specs = SpecLoader().load(args.spec_dir)
    outputs = SpecResolver().get_outputs(specs)
    is_up_to_date = Generator(args.output_base).generate(outputs, args.check)
    if not is_up_to_date:
        sys.exit(1)


if __name__ == "__main__":
    main()
