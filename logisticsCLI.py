#!/usr/bin/env python

from mylib.logistics import distance_between_two_points
import click


@click.group()
def cli():
    """Logistics CLI tool."""


@cli.command("distance")
@click.argument("city1")
@click.argument("city2")
def distance_command(city1, city2):
    """Calculate the distance between two cities."""
    dist = distance_between_two_points(city1, city2)
    click.echo(f"The distance between {city1} and {city2} is {dist:.2f} km.")


if __name__ == "__main__":
    cli()
