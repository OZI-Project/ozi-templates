# ozi/filter.py
# SPDX-License-Identifier: Unlicense
"""Filters for use in the OZI project templates."""
from __future__ import annotations

import string
from datetime import datetime
from datetime import timezone
from functools import lru_cache

ALPHANUMS = string.ascii_uppercase + string.ascii_lowercase + '0123456789'


def current_date(_format: str) -> str:
    """Get the local date in a given format.

    :param _format: The date formatting template.
    :type _format: str
    :return: Formatted date
    :rtype: str
    """
    return datetime.now(tz=timezone.utc).date().strftime(_format)


@lru_cache
def underscorify(s: str) -> str:
    """Replace non-alphanumerics with underscores for normalization (cached).

    :param s: The text to be normalized
    :type s: str
    :return: The normalized text
    :rtype: str
    """
    return ''.join([c if c in ALPHANUMS else '_' for c in s])


@lru_cache
def wheel_repr(version: str) -> str:
    """Transform versions of the form "X.Y" into "pyXY".

    :param version: The version.
    :type version: str
    :return: The wheel tag version.
    :rtype: str
    """
    major, _, minor_end = version.partition('.')
    minor, *_ = minor_end.partition('.')
    return f'py{major}{minor}'


def next_minor(version: str) -> str:
    """Given a Python version, determine the next minor version.

    :param version: Python version string
    :type version: str
    :return: The next minor version
    :rtype: str
    """
    major, minor, *_ = map(int, version.split('.'))
    return f'{major}.{minor + 1}'
