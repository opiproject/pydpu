"""Console script for pydpu."""
import click


@click.group()
@click.version_option(None, "-V", "--version")
def main():
    pass  # pragma: no cover


@main.group()
def inventory():
    pass  # pragma: no cover


@inventory.command()
def get():
    print("work in progress")


@main.group()
def ipsec():
    pass  # pragma: no cover


@ipsec.command()
def create_tunnel(**kwargs):
    print("work in progress")


if __name__ == "__main__":
    main()  # pragma: no cover
