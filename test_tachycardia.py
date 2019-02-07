

import pytest


@pytest.mark.parametrize("a, expected", [('tachycardic', True),
    ('TachycarDic', True), ('....,.,.   tachycardic   ', True),
    ('TACHYCARDIC', True), ('kelsey', False), ('no heart issues', False)])


def test_is_tachycardic_param(a, expected):
    from tachycardia import is_tachycardic
    answer = is_tachycardic(a)
    assert answer == expected


def test_is_tachycardic():
    from tachycardia import is_tachycardic
    answer = is_tachycardic('tachycardic!!    ')
    assert answer is True
