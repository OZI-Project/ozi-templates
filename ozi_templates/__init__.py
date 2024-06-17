"""ozi-templates module"""

# Part of OZI-Templates.
# See LICENSE.txt in the project root for details.
from __future__ import annotations

from functools import _lru_cache_wrapper
from types import FunctionType
from typing import Any

from jinja2 import Environment
from jinja2 import PackageLoader
from jinja2 import select_autoescape

from ozi_templates.filter import current_date
from ozi_templates.filter import next_minor
from ozi_templates.filter import sha256sum
from ozi_templates.filter import underscorify
from ozi_templates.filter import wheel_repr

__all__ = ('load_environment',)
FILTERS = (
    next_minor,
    underscorify,
    zip,
    sha256sum,
    wheel_repr,
    current_date,
)


def _init_environment(_globals: dict[str, Any]) -> Environment:  # pragma: no cover
    """Initialize the rendering environment, set filters, and set global metadata."""
    env = Environment(
        loader=PackageLoader('ozi_templates', '.'),
        autoescape=select_autoescape(),
        enable_async=True,
        auto_reload=False,
    )
    for f in FILTERS:
        match f:
            case type():
                env.filters.setdefault(f.__name__, f)
            case FunctionType():
                env.filters.setdefault(f.__name__, f)
            case _lru_cache_wrapper():  # pragma: defer to pyright,mypy
                env.filters.setdefault(f.__wrapped__.__name__, f)
    env.globals = env.globals | _globals
    return env


def load_environment(  # pragma: no cover
    project: dict[str, str],
    _globals: dict[str, Any],
) -> Environment:
    """Load the rendering environment for templates.

    :return: jinja2 rendering environment for OZI
    :rtype: Environment
    """
    env = _init_environment(_globals)
    env.globals = env.globals | {'project': project}
    return env
