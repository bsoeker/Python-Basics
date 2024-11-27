import argparse


def greet(name: str) -> None:
    print(f"Hello, {name}!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Greet someone")
    parser.add_argument("--name", "-n",  type=str, default="World",
                        help="name of the person to greet", )
    args = parser.parse_args()

    greet(args.name)
