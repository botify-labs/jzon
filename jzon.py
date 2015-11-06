# -*- coding: utf-8 -*-

import json
import click


@click.command()
@click.option('--indent', default=2, help='Indentation.')
@click.option('--sort-keys/--no-sort-keys', help='Sort keys.')
@click.argument('input', type=click.File('r'))
def jzon(indent, sort_keys, input):
    d = json.load(input)
    separators = (',', ': ') if indent else None
    click.echo(json.dumps(d, indent=indent, separators=separators, sort_keys=sort_keys))
