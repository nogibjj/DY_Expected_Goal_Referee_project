#!/usr/bin/env python

import click
from dblib.querydb import querydb

# build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL database"""


# build a click command
@cli.command()
# @click.option(
#     "--query", '-q',
#     default="SELECT * FROM matches_55_43_csv LIMIT 20",
#     help="SQL query to execute",
# )

@click.option(
    "--referee", '-e',
    default="SELECT _c17 FROM matches_55_43_csv",
    help="referee of the match",
)

def cli_query(referee):
    """Execute a SQL query"""
    querydb(referee)


# run the CLI
if __name__ == "__main__":
    cli_query()