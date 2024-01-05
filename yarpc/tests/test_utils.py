import pytest
from yarpc.utils import to_snake_case

@pytest.mark.parametrize("input, expected", [
    ("lower", "lower"),
    ("snak3_w1th_3_numbers", "snak3_w1th_3_numbers"),
    ("camelCase", "camel_case"),
    ("PascalCase", "pascal_case"),
    ("H2G2Content", "h2g2_content"),
    ("TLAClass", "tla_class"),
    ("TLA2Class", "tla2_class"),
    ("NewTLAAdapter", "new_tla_adapter"),
    ("NewTLA", "new_tla"),
])
def test_to_snake_case(input, expected):
    assert to_snake_case(input) == expected