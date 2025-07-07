"""ozi-templates module"""

# Part of OZI-Templates.
# See LICENSE.txt in the project root for details.
from __future__ import annotations

import sys
from functools import _lru_cache_wrapper
from itertools import zip_longest
from pathlib import Path
from types import FunctionType
from typing import TYPE_CHECKING, TypeAlias, TypeVar

from jinja2 import (
    BaseLoader,
    ChoiceLoader,
    Environment,
    FileSystemBytecodeCache,
    FileSystemLoader,
    PackageLoader,
    select_autoescape,
)
from platformdirs import user_cache_dir

from ozi_templates.filter import current_date, next_minor, underscorify, wheel_repr

if TYPE_CHECKING:
    from collections.abc import Mapping

    VT = TypeVar(
        'VT',
        str,
        int,
        float,
        bytes,
        None,
    )
    _Val: TypeAlias = list['_Key[VT]'] | Mapping['_Key[VT]', VT] | VT
    _Key: TypeAlias = VT | _Val[VT]

__all__ = ('load_environment',)
FILTERS = (
    next_minor,
    underscorify,
    zip,
    zip_longest,
    wheel_repr,
    current_date,
)


def _get_template_loader(target: Path | None = None) -> BaseLoader:
    """Get the appropriate loader."""
    if getattr(sys, 'frozen', False):  # pragma: defer to pyinstaller
        bundle_dir = sys._MEIPASS  # type: ignore
        loader = FileSystemLoader(Path(bundle_dir) / 'ozi_templates')
    else:
        loader = PackageLoader('ozi_templates', '.')
    return ChoiceLoader([loader, FileSystemLoader('.' if target is None else target)])


def _init_environment(
    _globals: dict[str, _Val[str]], target: Path | None = None
) -> Environment:
    """Initialize the rendering environment, set filters, and set global metadata."""
    env = Environment(
        loader=_get_template_loader(target=target),
        autoescape=select_autoescape(),
        bytecode_cache=FileSystemBytecodeCache(
            user_cache_dir(appname='OZI', appauthor='OZI-Project', ensure_exists=True)
        ),
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


def load_environment(
    project: dict[str, str | list[str]],
    _globals: dict[str, _Val[str]],
    target: Path | None = None,
) -> Environment:
    """Load the rendering environment for templates.

    :param project: initial project namespace for rendering
    :param _globals: other globals for jinja2
    :param target: optional target folder for project template overrides
    :return: jinja2 rendering environment for OZI
    :rtype: Environment
    """
    env = _init_environment(_globals, target=target)
    env.globals = env.globals | {'project': project}
    return env
