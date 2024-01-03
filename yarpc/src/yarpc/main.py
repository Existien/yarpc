from argparse import ArgumentParser
import os
import sys
import json
from yarpc.specification_loader import load_specifications
from yarpc.spec_resolver import SpecResolver

def __parse_args():
    parser = ArgumentParser(
        description="Codegenerator for creating D-Bus "
        "clients and services from yaml specifications"
    )
    parser.add_argument(
        "--check", action="store_true",
        help="Don't generate files, but return a non-zero exit code when the "
            "existing files are not consistent with the yaml specifications."
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

    if args.check:
        print("--check is not implemented yet")
        exit(1)

    specs = load_specifications(args.spec_dir)
    resolver = SpecResolver(specs)
    outputs = resolver.get_outputs()
    print(json.dumps(outputs,indent=2))

if __name__ == "__main__":
    main()
