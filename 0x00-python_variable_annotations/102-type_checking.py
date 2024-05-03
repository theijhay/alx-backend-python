#!/usr/bin/env python3
"""Use mypy to validate the following piece of code and
apply any necessary changes."""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''Zooms an array
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
