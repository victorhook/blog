#!/usr/bin/python3

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
categories:  {}
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
    base = Path(__file__).parent.parent
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
        date = ''
        image = ''
    else:
        title = get('Title')
        categories = get('Categories (space separated list)')
        image = get('Front image name: ')

    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    post = post.format(title, categories, image)
    save(date, post)