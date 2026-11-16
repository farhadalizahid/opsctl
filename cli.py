import argparse
from opsctl.version import __version__
from opsctl.commands import deploy, config


def main():
    parser = argparse.ArgumentParser(prog="opsctl", description="Operations control tool")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    status = subparsers.add_parser("status", help="Show system status")
    status.set_defaults(func=lambda args: print("opsctl is working"))
    deploy.add_parser(subparsers)
    config.add_parser(subparsers)
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

