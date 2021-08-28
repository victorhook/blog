#!/usr/bin/env python

import argparse
from datetime import datetime
from pathlib import Path
import os
import sys

post = format(
"""\
---
layout:      post
title:       {}
date:        {}
categories:  {}
tags:        {}
image:       {}
---

""")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--no-interactive', help='No interaction.' +
                        ' This will just create a default post.',
                        action='store_true')
    return parser.parse_args()


def get(name: str) -> str:
    return input(f'> {name}: ')


def save(date: str, data: str):
    base = Path(__file__).parent
    filename = date.split(' ')[0] + '-' + title.replace(' ', '-')
    filepath = str(base.joinpath('_posts').joinpath(filename)) + '.md'
    if os.path.exists(filepath):
        print(f'WARNING: Post "{filepath}" already exists, use a different title.')
        return

    with open(filepath, 'w') as f:
        f.write(data)
    print(f'Created new post at {filepath}')

if __name__ == '__main__':
    args = parse_args()

    print('Create a new post:')

    if args.no_interactive:
        title = 'Title'
        categories = ''
        tags = ''
        date = ''
        image = ''
    else:
        title = get('Title')
        categories = get('Categories (space separated list)')
        tags = get('Tags (space separated list)')
        date = get('Date (leave blank to use today)')
        image = get('Front image name: ')

    if not date:
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    post = post.format(title, date, categories, tags, image)
    save(date, post)