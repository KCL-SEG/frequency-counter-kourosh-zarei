"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


from collections import Counter


def frequencies(items):
    items = [str(item) for item in items]
    _frequencies = Counter(items)
    return _frequencies
