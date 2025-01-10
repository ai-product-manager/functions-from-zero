#!/usr/bin/env python3

from mylib.calc import add, sub, mul, div, power, sqrt
import click


@click.group()
def cli():
    """A calculator program"""


@cli.command("add")
@click.argument("a", type=float)
@click.argument("b", type=float)
def add_command(a, b):
    """Add two numbers

    Example:
    ./calcCLI.py add 3 4
    """
    # use colored output to print the result
    click.echo(click.style(f"The sum of {a} and {b} is {add(a, b)}", fg="green"))


@cli.command("sub")
@click.argument("a", type=float)
@click.argument("b", type=float)
def sub_command(a, b):
    """Subtract two numbers

    Example:
    ./calcCLI.py sub 3 4
    """
    # use colored output to print the result
    click.echo(click.style(f"The difference of {a} and {b} is {sub(a, b)}", fg="green"))


@cli.command("mul")
@click.argument("a", type=float)
@click.argument("b", type=float)
def mul_command(a, b):
    """Multiply two numbers

    Example:
    ./calcCLI.py mul 3 4
    """
    # use colored output to print the result
    click.echo(click.style(f"The product of {a} and {b} is {mul(a, b)}", fg="green"))


@cli.command("div")
@click.argument("a", type=float)
@click.argument("b", type=float)
def div_command(a, b):
    """Divide two numbers

    Example:
    ./calcCLI.py div 3 4
    """
    # use colored output to print the result
    click.echo(click.style(f"The quotient of {a} and {b} is {div(a, b)}", fg="green"))


@cli.command("power")
@click.argument("a", type=float)
@click.argument("b", type=float)
def power_command(a, b):
    """Raise a number to the power of another number

    Example:
    ./calcCLI.py power 3 4
    """
    # use colored output to print the result
    click.echo(
        click.style(f"{a} raised to the power of {b} is {power(a, b)}", fg="green")
    )


@cli.command("sqrt")
@click.argument("a", type=float)
def sqrt_command(a):
    """Get the square root of a number

    Example:
    ./calcCLI.py sqrt 4
    """
    # use colored output to print the result
    click.echo(click.style(f"The square root of {a} is {sqrt(a)}", fg="green"))


if __name__ == "__main__":
    cli()
