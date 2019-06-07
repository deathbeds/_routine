#!/usr/bin/env python
# coding: utf-8

__file__ = __import__("pathlib").Path(globals().get("__file__", "__init__.ipynb"))


__all__ = tuple()
for notebook in __file__.parent.glob("*/[!_]*.ipynb"):
    name = notebook.stem.split(".", 1)[0]
    with __import__("pidgin").PidginLoader(lazy=True), __import__("importnb").Notebook(
        lazy=True
    ):
        globals()[name] = __import__("importlib").import_module(
            ".".join(notebook.parent.parts[-2:] + (name,))
        )

    __all__ += (name,)
__all__


if __name__ == "__main__":
    get_ipython().system(
        "jupyter nbconvert --to python --TemplateExporter.exclude_input_prompt=True __init__.ipynb"
    )
    get_ipython().system("black __init__.py")
    get_ipython().system("isort __init__.py")
