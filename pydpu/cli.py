"""Console script for pydpu."""
import click
import grpc

from .dpuredfish import accounts, certificates, managers, systems, update
from .evpn import bridge_create, port_create, svi_create, vrf_create
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
def bridge(ctx):
    bridge_create(ctx.obj["ADDRESS"])
    click.echo("work in progress")


@evpn.command()
@click.pass_context
def port(ctx):
    port_create(ctx.obj["ADDRESS"])
    click.echo("work in progress")


@evpn.command()
@click.pass_context
def vrf(ctx):
    vrf_create(ctx.obj["ADDRESS"])
    click.echo("work in progress")


@evpn.command()
@click.pass_context
def svi(ctx):
    svi_create(ctx.obj["ADDRESS"])
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
def show(ctx, **kwargs):
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
        c = NvmeController(
            subsystem=s, queue=1024, pf=0, vf=0, port=0, max_nsq=8, max_ncq=8
        )
        click.echo(c)
        res = c.create(ctx.obj["ADDRESS"])
        click.echo(res)
        # res = c.update(ctx.obj["ADDRESS"])
        # click.echo(res)
        res = c.list(ctx.obj["ADDRESS"])
        click.echo(res)
        res = c.get(ctx.obj["ADDRESS"])
        click.echo(res)
        res = c.stats(ctx.obj["ADDRESS"])
        click.echo(res)
        res = c.delete(ctx.obj["ADDRESS"])
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
        # res = n.update(ctx.obj["ADDRESS"])
        # click.echo(res)
        res = n.list(ctx.obj["ADDRESS"])
        click.echo(res)
        res = n.get(ctx.obj["ADDRESS"])
        click.echo(res)
        res = n.stats(ctx.obj["ADDRESS"])
        click.echo(res)
        res = n.delete(ctx.obj["ADDRESS"])
        click.echo(res)
    except grpc.RpcError as e:
        click.echo(e)
        # raise


@main.group()
@click.option("-u", "--username", default="root", help="DPU BMC redfish username")
@click.option("-p", "--password", default="0penBmc", help="DPU BMC redfish password")
@click.pass_context
def redfish(ctx, username, password):
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)
    ctx.obj["USERNAME"] = username
    ctx.obj["PASSWORD"] = password


@redfish.command()
@click.pass_context
def test(ctx, **kwargs):
    s = systems.Systems(ctx.obj["ADDRESS"], ctx.obj["USERNAME"], ctx.obj["PASSWORD"])
    click.echo(list(s.get_processors()))
    m = managers.Managers(ctx.obj["ADDRESS"], ctx.obj["USERNAME"], ctx.obj["PASSWORD"])
    click.echo(m.get_bmc_datetime())
    a = accounts.AccountService(
        ctx.obj["ADDRESS"], ctx.obj["USERNAME"], ctx.obj["PASSWORD"]
    )
    click.echo(list(a.get_accounts()))
    c = certificates.CertificateService(
        ctx.obj["ADDRESS"], ctx.obj["USERNAME"], ctx.obj["PASSWORD"]
    )
    click.echo(list(c.get_certificates()))
    u = update.UpdateService(
        ctx.obj["ADDRESS"], ctx.obj["USERNAME"], ctx.obj["PASSWORD"]
    )
    click.echo(list(u.get_versions()))


if __name__ == "__main__":
    main()  # pragma: no cover
