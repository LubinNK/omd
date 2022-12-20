"""Initialization of terminal commands"""
from string import Template
from random import randint
import pizzas
import click


def log(pattern: Template):
    """Decorator with pattern on time"""
    def decorator(func: callable):
        def wrapper(pizza: pizzas.Pizza):
            name, time = func(pizza)
            click.echo(name + ' ' + pattern.substitute(t=time))
            return name + ' ' + pattern.substitute(t=time)
        return wrapper
    return decorator


@log(Template('🚴 Deliver for $t min!'))
def deliver(pizza: pizzas.Pizza):
    """Deliver the pizza for randint min"""
    return type(pizza).__name__, randint(3, 15)


@log(Template('🚴 Pick up for $t min!'))
def pickup(pizza: pizzas.Pizza):
    """Pick up in your own"""
    return type(pizza).__name__, randint(5, 30)


@log(Template('🥘 Prepare for $t min!'))
def preparing(pizza: pizzas.Pizza):
    """Preparing pizza"""
    return type(pizza).__name__, pizza.time + randint(-4, 4)


@click.group()
def cli():
    """Initializing click group"""


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option('--size', default='L')
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool, size: str):
    """ Prepare and deliver (optional) the pizza"""
    item = pizzas.MENU_DICT[pizza.lower()](size)
    preparing(item)
    if delivery:
        deliver(item)
    else:
        pickup(item)


@cli.command()
def menu():
    """Print Menu"""
    menu_str = []
    for _, item in pizzas.MENU_DICT.items():
        menu_str.append(f'- {item.dict()["name"]}: '
                        f'{", ".join(item.dict()["recipe"])}\n')
    click.echo(''.join(menu_str))
