# noqa: INP001
from collections.abc import Mapping  # noqa: TC003
from typing import TypeAlias
from typing import TypeVar

import hypothesis.strategies as st
from hypothesis import given

from ozi_templates import load_environment

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


@given(
    project=st.dictionaries(st.from_regex('[a-zA-Z_]*'), st.text()),
    _globals=st.dictionaries(st.from_regex('[a-zA-Z_]*'), st.text()),
)
def test_load_environment(  # noqa: PT019
    project: dict[str, str], _globals: dict[str, _Val[str]]
) -> None:
    load_environment(project, _globals=_globals)
