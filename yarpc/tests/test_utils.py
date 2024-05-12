import pytest
from yarpc.utils import to_snake_case, to_camel_case, to_pascal_case

@pytest.mark.parametrize("input, expected", [
    ("lower", "lower"),
    ("snake_case", "snake_case"),
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


@pytest.mark.parametrize("input, expected", [
    ("lower", "lower"),
    ("snake_case", "snakeCase"),
    ("snak3_w1th_3_numbers", "snak3W1th3Numbers"),
    ("camelCase", "camelCase"),
    ("PascalCase", "pascalCase"),
    ("H2G2Content", "h2g2Content"),
    ("TLAClass", "tlaClass"),
    ("TLA2Class", "tla2Class"),
    ("NewTLAAdapter", "newTlaAdapter"),
    ("NewTLA", "newTla"),
])
def test_to_camel_case(input, expected):
    assert to_camel_case(input) == expected


@pytest.mark.parametrize("input, expected", [
    ("lower", "Lower"),
    ("snake_case", "SnakeCase"),
    ("snak3_w1th_3_numbers", "Snak3W1th3Numbers"),
    ("camelCase", "CamelCase"),
    ("PascalCase", "PascalCase"),
    ("H2G2Content", "H2g2Content"),
    ("TLAClass", "TlaClass"),
    ("TLA2Class", "Tla2Class"),
    ("NewTLAAdapter", "NewTlaAdapter"),
    ("NewTLA", "NewTla"),
])
def test_to_pascal_case(input, expected):
    assert to_pascal_case(input) == expected