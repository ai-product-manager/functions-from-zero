#!/usr/bin/env python

from mylib.logistics import distance_between_two_points, time_between_two_points
import click


@click.group()
def cli():
    """Logistics CLI tool."""


@cli.command("distance")
@click.argument("city1")
@click.argument("city2")
def distance_command(city1, city2):
    """Calculate the distance between two cities.

    Example: ./logisticsCLI.py distance Lima Arequipa
    """
    dist = distance_between_two_points(city1, city2)
    click.echo(f"The distance between {city1} and {city2} is {dist:.2f} km.")


@cli.command("time")
@click.argument("city1")
@click.argument("city2")
@click.option("--speed", default=80, help="The speed in km/h.")
def time_command(city1, city2, speed):
    """Calculate the time it takes to travel between two cities.

    Example: ./logisticsCLI.py time Lima Arequipa --speed 100
    """
    time = time_between_two_points(city1, city2, speed)
    click.echo(
        f"The time it takes to travel between {city1} and {city2} is {time:.2f} hours."
    )


if __name__ == "__main__":
    cli()
