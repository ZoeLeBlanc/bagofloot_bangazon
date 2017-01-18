import sys
import click
from lootbag_db import *
from child_db import *

test = Lootbag()
test_child = Child()

@click.group()
def lootbag():
    """Lootbag is a program that helps you determine who you need to deliver toys too and manage a naught and nice list. Highly recommended by S.Nicholas."""
    pass


@click.group()
def create():
    """Create new instance"""
    pass
        
@create.command('bag')
@click.argument('name', required=1)
def create_bag(name):
    """Create a bag"""
    click.echo("name")
    test.create_bag(name)

@create.command('kid')
@click.argument('toy', required=1)
@click.argument('name', required=1)
@click.argument('bag', required=1)
def create_kid(toy, name, bag):
    """Create a child"""
    test_child.create_child(toy, name, bag)

@click.command('ls')
@click.argument('name', required=1)
@click.option('--item', type=click.Choice(['deliveries', 'kids', 'toys', 'toy']), help="Choose an item in the lootbag to list (deliveries, kids, toys, or for a kid all their toys")
def ls(name, item):
    """List everything in an item"""
    if item == 'deliveries':
        test.toys_delivered(name)
    if item == 'kids':
        test.get_all_kids(name)
    if item == 'toys':
        test.get_toy_list(name)
    if item == 'toy':
        test_child.get_all_toys(name)

@click.command('rm-kid')
@click.argument('name', required=1)
@click.option('--item', type=click.Choice(['toys', 'toy']), help="Choose an item to remove from child (toy or all toys)")
def remove_from_kid(name, item):
    """Remove item from kid"""
    if item == 'toys':
        test_child.remove_all_toys(name)
    if item == 'toy':
        test_child.remove_toy(name)

lootbag.add_command(rm-kid)
lootbag.add_command(ls)
lootbag.add_command(create)


if __name__ == '__main__':
    lootbag()
    