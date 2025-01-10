from mylib.calc import add, sub, mul, div, power, sqrt
from calcCLI import cli
from click.testing import CliRunner
import pytest


@pytest.fixture
def runner():
    return CliRunner()


# write a test for each command in calcCLI.py
def test_add_command(runner):
    result = runner.invoke(cli, ["add", "3", "4"])
    assert result.exit_code == 0
    assert "The sum of 3.0 and 4.0 is 7.0" in result.output


def test_sub_command(runner):
    result = runner.invoke(cli, ["sub", "3", "4"])
    assert result.exit_code == 0
    assert "The difference of 3.0 and 4.0 is -1.0" in result.output


def test_mul_command(runner):
    result = runner.invoke(cli, ["mul", "3", "4"])
    assert result.exit_code == 0
    assert "The product of 3.0 and 4.0 is 12.0" in result.output


def test_div_command(runner):
    result = runner.invoke(cli, ["div", "3", "4"])
    assert result.exit_code == 0
    assert "The quotient of 3.0 and 4.0 is 0.75" in result.output


def test_power_command(runner):
    result = runner.invoke(cli, ["power", "3", "4"])
    assert result.exit_code == 0
    assert "3.0 raised to the power of 4.0 is 81.0" in result.output


def test_sqrt_command(runner):
    result = runner.invoke(cli, ["sqrt", "9"])
    assert result.exit_code == 0
    assert "The square root of 9.0 is 3.0" in result.output


def test_add():
    assert add(3, 4) == 7
    assert add(3, -4) == -1
    assert add(3, 0) == 3
    assert add(0, 0) == 0


def test_sub():
    assert sub(3, 4) == -1
    assert sub(3, -4) == 7
    assert sub(3, 0) == 3
    assert sub(0, 0) == 0


def test_mul():
    assert mul(3, 4) == 12
    assert mul(3, -4) == -12
    assert mul(3, 0) == 0
    assert mul(0, 0) == 0


def test_div():
    assert div(3, 4) == 0.75
    assert div(3, -4) == -0.75
    assert div(3, 1) == 3
    assert div(0, 1) == 0


def test_power():
    assert power(3, 4) == 81
    assert power(3, 0) == 1
    assert power(0, 0) == 1
    assert power(0, 1) == 0


def test_sqrt():
    assert sqrt(9) == 3
    assert sqrt(16) == 4
    assert sqrt(0) == 0
    assert sqrt(1) == 1
