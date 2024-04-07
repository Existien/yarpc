from argparse import ArgumentParser
import os
import sys
from yarpc.definitions_loader import DefinitionsLoader
from yarpc.definitions_resolver import DefinitionsResolver
from yarpc.generator import Generator

def __parse_args():
    """Parses the command line arguments

    Returns:
        Namespace: Object containing the parsed command line arguments
    """
    parser = ArgumentParser(
        description="Codegenerator for creating D-Bus "
        "clients and services from yaml interface definitions"
    )
    parser.add_argument(
        "--check", action="store_true",
        help="Don't generate files, but return a non-zero exit code when the "
            "existing files are not consistent with the yaml interface definitions.",
        default=False
    )
    parser.add_argument(
        "definitions_dir", metavar="YAML_DEFINITIONS_DIRECTORY",
        help="The directory containing he yaml interface definitions."
    )
    parser.add_argument(
        "--output-base", metavar="OUTPUT_BASE_DIRECTORY",
        help="The directory the relative paths in the YAML interface definitions are relative to.",
        default=os.getcwd()
    )
    return parser.parse_args(sys.argv[1:])

def main():
    args = __parse_args()
    definitions = DefinitionsLoader().load(args.definitions_dir)
    outputs = DefinitionsResolver().get_outputs(definitions)
    is_up_to_date = Generator(args.output_base).generate(outputs, args.check)
    if not is_up_to_date:
        sys.exit(1)


if __name__ == "__main__":
    main()
