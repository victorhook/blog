#!/usr/bin/env python3

import os
from PIL import Image
from pathlib import Path

IMAGE_SIZE_THRESH_HOLD = 3e6


if __name__ == '__main__':
    base = Path(__file__).parent.parent
    images = base.joinpath('assets').joinpath('images')
    total_trimmed = 0
    for img in os.listdir(str(images)):
        if img.lower().endswith('jpg'):
            img_path = images.joinpath(img)
            size = img_path.stat().st_size
            if size > IMAGE_SIZE_THRESH_HOLD:
                print(f'Image {img} to big: {round(size/1e6, 2)}Mb, reducing size to: ', end='')
                img = Image.open(str(img_path))
                img.save(str(img_path), quality=60)
                total_trimmed += 1
                size = img_path.stat().st_size
                print(f' {round(size/1e6, 2)}Mb')
            else:
                print(img, 'OK')


    print(f'\n-- Trimmed {total_trimmed} images -- ')