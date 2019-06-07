#!/usr/bin/env python
# coding: utf-8

#     !ipython -m _routine -- add 9bc79ddb7200e77394f546bc69e11c6f
#     !ipython -m _routine -- update
#     !ipython -m _routine -- update --id 9bc79ddb7200e77394f546bc69e11c6f

import click
from IPython import get_ipython


@click.group()
def main():
    pass


@main.add_command
@click.command(help="A valid gist sha. Run this where the repository is")
@click.argument("id")
def add(id):
    package, conda = __package__, __import__("os").environ["CONDA_PREFIX"]
    get_ipython().system(
        "source activate $conda && git submodule add https://gist.github.com/$id src/$package/$id"
    )


@main.add_command
@click.command(help="A valid gist sha. Run this where the repository is")
@click.option("--id", default=None)
def update(id):
    package, conda = __package__, __import__("os").environ["CONDA_PREFIX"]
    if id:
        get_ipython().system(
            "source activate $conda && git submodule update src/$package/$id"
        )
    else:
        get_ipython().system(
            "source activate $conda && git submodule update --recursive"
        )


if __name__ == "__main__":
    if __import__("sys").argv[0] == __import__("ipykernel_launcher").__file__:
        get_ipython().system(
            "jupyter nbconvert --to python --TemplateExporter.exclude_input_prompt=True __main__.ipynb && black __main__.py && isort __main__.py        "
        )
    else:
        main()
