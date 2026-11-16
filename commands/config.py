import json
from pathlib import Path

CONFIG_DIR = Path.home() / ".opsctl"
CONFIG_FILE = CONFIG_DIR / "config.json"


def load_config():
    if not CONFIG_FILE.exists():
        return {}
    with open(CONFIG_FILE) as f:
        return json.load(f)


def save_config(cfg):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(cfg, f, indent=2)


def execute(args):
    cfg = load_config()

    if args.action == "get":
        if args.key:
            if args.key not in cfg:
                print(f"{args.key} is not set")
                return 1
            print(cfg[args.key])
        else:
            print(json.dumps(cfg, indent=2))
        return 0

    if args.action == "set":
        cfg[args.key] = args.value
        save_config(cfg)
        print(f"Set {args.key} = {args.value}")
        return 0

    return 1


def add_parser(subparsers):
    p = subparsers.add_parser("config", help="Get or set config values")
    actions = p.add_subparsers(dest="action", required=True)

    g = actions.add_parser("get", help="Get a config value")
    g.add_argument("key", nargs="?", help="e.g. api_endpoint")

    s = actions.add_parser("set", help="Set a config value")
    s.add_argument("key", help="e.g. api_endpoint")
    s.add_argument("value", help="e.g. https://api.example.com")

    p.set_defaults(func=execute)
    return p

