#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Jalal Belsifar with help from JT and Piero"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    file = os.listdir(dirname)

    dunder_pattern = re.compile(r'__(\w+)__')

    special_path = []
    for f in file:
        if dunder_pattern.search(f):
            full_path = os.path.abspath(os.path.join(dirname, f))
            special_path.append(full_path)
    return special_path


def copy_to(path_list, dest_dir):
    """given a list of paths, copies those files into the given directory"""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for path in path_list:
        shutil.copy2(path, dest_dir)
    return f'Copied to: {dest_dir}'


def zip_to(path_list, dest_zip):
    """given a list of paths, zip those files up into the given zipfile"""
    print(f"Command I'm going to do: \nzip -j {dest_zip}")
    command_list = ['zip', '-j', dest_zip]
    command_list.extend(path_list)
    subprocess.call(
        command_list,
    )


def main(args):
    """Main driver code for copyspecial."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument(
        'from_dir', help="Shows absolute path of special files")
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)
    directory_list = ns.from_dir
    tozip = ns.tozip
    todir = ns.todir

    paths_list = get_special_paths(directory_list)
    if tozip:
        zip_to(paths_list, tozip)
    elif todir:
        copy_to(paths_list, todir)
    for path in paths_list:
        print(path)


if __name__ == "__main__":
    main(sys.argv[1:])
