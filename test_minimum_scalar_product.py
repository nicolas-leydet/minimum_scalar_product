import pytest

from solve import minimum_scalar_product


multitest = pytest.mark.parametrize


@multitest('v1, v2, result', [
    ([1, 3, -5],
     [-2, 4, 1],
     -25),
    ([1, 2, 3, 4, 5],
     [1, 0, 1, 0, 1],
     6),
])
def test_minimum_scalar_product(v1, v2, result):
    assert result == minimum_scalar_product(v1, v2)
