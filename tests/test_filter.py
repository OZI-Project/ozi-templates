# noqa: INP001
# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

from hypothesis import assume
from hypothesis import given
from hypothesis import strategies as st

import ozi_templates.filter


@given(_format=st.text())
def test_fuzz_current_date(_format: str) -> None:  # noqa: PT019
    ozi_templates.filter.current_date(_format=_format)


@given(version=st.from_regex(r'^([0-9]+)\.([0-9]+)\.([0-9]+)$'))
def test_fuzz_next_minor(version: str) -> None:
    assume('.' in version)
    ozi_templates.filter.next_minor(version=version)


@given(s=st.text())
def test_fuzz_underscorify(s: str) -> None:
    ozi_templates.filter.underscorify(s=s)


@given(
    version=st.from_regex(
        r'^([0-9]+)\.([0-9]+)\.([0-9]+)(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+[0-9A-Za-z-]+)?$'
    )
)
def test_fuzz_wheel_repr(version: str) -> None:
    assume('.' in version)
    ozi_templates.filter.wheel_repr(version=version)
