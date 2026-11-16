def run(args):
    print(f"Deploying {args.app} to {args.env}")
    if args.version:
        print(f"Version: {args.version}")


def add_parser(subparsers):
    p = subparsers.add_parser("deploy", help="Deploy an application")
    p.add_argument("--app", required=True, help="Application name")
    p.add_argument("--env", required=True, help="Environment (dev, prod)")
    p.add_argument("--version", help="Version to deploy")
    p.set_defaults(func=run)
