"""Console script for pydpu."""
import click
import grpc

from .evpn import evpn_configure
from .inventory import get_inventory
from .ipsec import create_new_tunnel, get_stats
from .storage import NvmeController, NvmeNamespace, NvmeSubsystem


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
def evpn(ctx):
    pass  # pragma: no cover


@evpn.command()
@click.pass_context
def iface(ctx):
    evpn_configure(ctx.obj["ADDRESS"])
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
def list(ctx, **kwargs):
    click.echo("work in progress")
    try:
        s = NvmeSubsystem(
            nqn="nqn.2022-09.io.spdk:opi1", model="OPI Model", serial="OPI SN"
        )
        click.echo(s)
        res = s.list(ctx.obj["ADDRESS"])
        click.echo(res)
    except grpc.RpcError as e:
        print(e)
        # raise


@storage.command()
@click.pass_context
def subsystem(ctx, **kwargs):
    click.echo("work in progress")
    try:
        s = NvmeSubsystem(
            nqn="nqn.2022-09.io.spdk:opi1", model="OPI Model", serial="OPI SN"
        )
        click.echo(s)
        res = s.create(ctx.obj["ADDRESS"])
        click.echo(res)
        # res = s.update(ctx.obj["ADDRESS"])
        # click.echo(res)
        res = s.list(ctx.obj["ADDRESS"])
        click.echo(res)
        res = s.get(ctx.obj["ADDRESS"])
        click.echo(res)
        res = s.stats(ctx.obj["ADDRESS"])
        click.echo(res)
        res = s.delete(ctx.obj["ADDRESS"])
        click.echo(res)
    except grpc.RpcError as e:
        print(e)
        # raise


@storage.command()
@click.pass_context
def controller(ctx, **kwargs):
    click.echo("work in progress")
    try:
        s = NvmeSubsystem(
            nqn="nqn.2022-09.io.spdk:opi1", model="OPI Model", serial="OPI SN"
        )
        click.echo(s)
        c = NvmeController(subsystem=s, queue=1024)
        click.echo(c)
        res = c.create(ctx.obj["ADDRESS"])
        click.echo(res)
    except grpc.RpcError as e:
        click.echo(e)
        # raise


@storage.command()
@click.pass_context
def namespace(ctx, **kwargs):
    click.echo("work in progress")
    try:
        s = NvmeSubsystem(
            nqn="nqn.2022-09.io.spdk:opi1", model="OPI Model", serial="OPI SN"
        )
        click.echo(s)
        n = NvmeNamespace(subsystem=s, volume="Malloc1")
        click.echo(n)
        res = n.create(ctx.obj["ADDRESS"])
        click.echo(res)
    except grpc.RpcError as e:
        click.echo(e)
        # raise


if __name__ == "__main__":
    main()  # pragma: no cover
