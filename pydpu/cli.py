"""Console script for pydpu."""
import click

from .inventory import get_inventory
from .ipsec import create_new_tunnel, get_stats
from .storage import nvme_subsystems


@click.group()
@click.version_option(None, "-V", "--version")
@click.option("--address", help="IP address of the DPU gRPC management.", required=True)
@click.pass_context
def main(ctx, address):
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)
    ctx.obj["ADDRESS"] = address


@main.group()
@click.pass_context
def inventory(ctx):
    pass  # pragma: no cover


@inventory.command()
@click.pass_context
def get(ctx):
    get_inventory(ctx.obj["ADDRESS"])
    click.echo("work in progress")


@main.group()
@click.pass_context
def ipsec(ctx):
    pass  # pragma: no cover


@ipsec.command()
@click.pass_context
def create_tunnel(ctx, **kwargs):
    create_new_tunnel(ctx.obj["ADDRESS"])
    click.echo("work in progress")


@ipsec.command()
@click.pass_context
def stats(ctx, **kwargs):
    get_stats(ctx.obj["ADDRESS"])
    click.echo("work in progress")


@main.group()
@click.pass_context
def storage(ctx):
    pass  # pragma: no cover


@storage.command()
@click.pass_context
def subsystems(ctx, **kwargs):
    nvme_subsystems(ctx.obj["ADDRESS"])
    click.echo("work in progress")


if __name__ == "__main__":
    main()  # pragma: no cover
