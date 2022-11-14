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
#     default="SELECT * FROM events LIMIT 20",
#     help="SQL query to execute",
# )

@click.option(
    "--referee", '-e',
    # default="""SELECT SUBSTRING_INDEX(_c17, "'", 15) FROM matches_55_43_csv""",
    default="""
            SELECT referee FROM matches_55_43
            """,
    help="referee of the match",
)

def cli_query(referee):
    """Execute a SQL query"""
    querydb(referee)


# run the CLI
if __name__ == "__main__":
    cli()
    