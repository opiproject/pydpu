import pytest
from click.testing import CliRunner

from pydpu import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli(runner):
    """Basic test for CLI"""
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    help_result = runner.invoke(cli.main, ("--help",))
    assert help_result.exit_code == 0
    assert "Show this message and exit" in help_result.output


def test_cli_inventory_get(runner):
    """Test `dpu inventory get`"""
    result = runner.invoke(
        cli.main, ("--address", "localhost:50001", "inventory", "get")
    )
    assert result.exit_code == 0


def test_cli_evpn_bridge(runner):
    """Test `dpu evpn interface`"""
    result = runner.invoke(cli.main, ("--address", "localhost:50001", "evpn", "bridge"))
    assert result.exit_code == 0


def test_cli_evpn_port(runner):
    """Test `dpu evpn interface`"""
    result = runner.invoke(cli.main, ("--address", "localhost:50001", "evpn", "port"))
    assert result.exit_code == 0


def test_cli_evpn_vrf(runner):
    """Test `dpu evpn interface`"""
    result = runner.invoke(cli.main, ("--address", "localhost:50001", "evpn", "vrf"))
    assert result.exit_code == 0


def test_cli_evpn_svi(runner):
    """Test `dpu evpn interface`"""
    result = runner.invoke(cli.main, ("--address", "localhost:50001", "evpn", "svi"))
    assert result.exit_code == 0


def test_cli_ipsec_create_tunnel(runner):
    """Test `dpu ipsec create-tunnel"""
    result = runner.invoke(
        cli.main, ("--address", "localhost:50002", "ipsec", "create-tunnel")
    )
    assert result.exit_code == 0


def test_cli_storage_list(runner):
    """Test `dpu storage list"""
    result = runner.invoke(
        cli.main, ("--address", "localhost:50003", "storage", "list")
    )
    assert result.exit_code == 0


def test_cli_storage_subsystem(runner):
    """Test `dpu storage subsystem"""
    result = runner.invoke(
        cli.main, ("--address", "localhost:50004", "storage", "subsystem")
    )
    assert result.exit_code == 0


def test_cli_storage_controller(runner):
    """Test `dpu storage controller"""
    result = runner.invoke(
        cli.main, ("--address", "localhost:50005", "storage", "controller")
    )
    assert result.exit_code == 0


def test_cli_storage_namespace(runner):
    """Test `dpu storage namespace"""
    result = runner.invoke(
        cli.main, ("--address", "localhost:50006", "storage", "namespace")
    )
    assert result.exit_code == 0
