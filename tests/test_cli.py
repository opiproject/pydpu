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


def test_cli_ipsec_create_tunnel(runner):
    """Test `dpu ipsec create-tunnel"""
    result = runner.invoke(
        cli.main, ("--address", "localhost:50002", "ipsec", "create-tunnel")
    )
    assert result.exit_code == 0


def test_cli_storage_subsystems(runner):
    """Test `dpu storage subsystems"""
    result = runner.invoke(
        cli.main, ("--address", "localhost:50003", "storage", "subsystems")
    )
    assert result.exit_code == 0
