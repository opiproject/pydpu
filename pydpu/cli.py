"""Console script for pydpu."""
import click

from .inventory import get_inventory
from .ipsec import create_new_tunnel, get_stats
from .storage import nvme_subsystems


@click.group()
@click.version_option(None, "-V", "--version")
def main():
    pass  # pragma: no cover


@main.group()
def inventory():
    pass  # pragma: no cover


@inventory.command()
def get():
    get_inventory()
    click.echo("work in progress")


@main.group()
def ipsec():
    pass  # pragma: no cover


@ipsec.command()
def create_tunnel(**kwargs):
    create_new_tunnel()
    click.echo("work in progress")


@ipsec.command()
def stats(**kwargs):
    get_stats()
    click.echo("work in progress")


@main.group()
def storage():
    pass  # pragma: no cover


@storage.command()
def subsystems(**kwargs):
    nvme_subsystems()
    click.echo("work in progress")


if __name__ == "__main__":
    main()  # pragma: no cover
