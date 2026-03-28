#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
from importlib import import_module

if __name__ == "__main__":
    save = import_module("5-save_to_json_file").save_to_json_file
    load = import_module("6-load_from_json_file").load_from_json_file

    try:
        items = load("add_item.json")
    except FileNotFoundError:
        items = []

    save(items + sys.argv[1:], "add_item.json")
