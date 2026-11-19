import pytest

from audio import envelope as mod

CASES = [
    ('adsr', [0.05, 0.1, 0.1, 0.5, 0.8, 1.0], 0.5, True),
    ('adsr', [0.5, 0.1, 0.1, 0.5, 0.8, 1.0], 0.5, True),
    ('adsr', [1.0, 0.1, 0.1, 0.5, 0.8, 1.0], 0.0, True),
    ('gate', [[1, 0.1, -1], 0.5], [0, 2], False),
    ('velocity_curve', [0.5, 2], 0.25, True),
    ('portamento', [0, 10, 3], 3, False),
    ('release_samples', [[1, 0.1, 0.1], 0.5], 2, False),
    ('adsr', [0, 0, 0, 1, 1, 1], 1, False),
    ('adsr', [0.2, 0.1, 0.1, 0.5, 0.8, 1.0], 0.5, True),
    ('adsr', [0.9, 0.1, 0.1, 0.5, 0.8, 1.0], 0.25, True),
    ('gate', [[], 0.5], [], False),
    ('velocity_curve', [1.0, 3], 1.0, True),
    ('portamento', [10, 0, 3], 7, False),
    ('release_samples', [[], 0.5], 0, False),
    ('release_samples', [[1, 1], 0.5], 0, False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_envelope_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
