import re


def find_type(type_name: str, objects: list) -> dict:
    """Fins a type by name from a list of objects

    Args:
        type_name (str): The type to look for
        objects (list): The objects to search for the type

    Returns:
        dict: The type
    """
    hits = list(filter(lambda x: re.match(x.get('regex', x.get('name')), type_name), objects))
    if len(hits) == 1:
        return hits[0]
    return {}


def extract_inner_names(type_name: str, type: dict) -> list:
    """Returns the parameters of arrays or dicts

    Args:
        type_name (str): The type name, e.g. array<int32>
        type (dict): The type object, e.g. Array

    Returns:
        list: A list of the contained types, e.g. ['int32']
    """
    match = re.match(type.get('regex'), type_name)
    if not match:
        return []
    else:
        return match.groups()


def find_types(type_name: str, objects: list) -> list:
    """Returns the type objects contained in type_name

    Args:
        type_name (str): The type name, e.g. array<int32>
        objects (list): List of objects to search for the types

    Returns:
        list: A list of the contained type objects
    """
    hit = find_type(type_name, objects)
    if not hit:
        raise TypeError(f"Failed to find type: {type_name}")
    found_types = [hit]
    regex = found_types[0].get('regex')
    if regex:
        inner_names = re.match(regex, type_name).groups()
        for inner_name in inner_names:
            found_types.extend(find_types(inner_name, objects))
    return found_types


def extract_dependencies(type_name: str, objects: list) -> list:
    """Returns the type objects contained in the type of type_name

    Args:
        type_name (str): The type name
        objects (list): List of objects to search for the types

    Returns:
        list: A list of the contained type objects
    """
    inner = []
    outer = find_type(type_name, objects)
    if outer.get('kind') == 'struct':
        inner.append(outer.get('name'))
        for member in outer.get('members'):
            inner.extend(extract_dependencies(member.get('type'), objects))
    elif outer.get('kind') == 'enum':
        inner.append(outer.get('name'))
    elif outer.get('name') == 'array' or outer.get('name') == 'dict':
        in_arr = find_types(type_name, objects)
        for i in in_arr:
            inner.extend(extract_dependencies(i.get('name'), objects))
    return set(inner)


def to_snake_case(name: str) -> str:
    """Returns the snake casified version of name

    Args:
        name (str): a name
    Return:
        str: The name in snake case
    """
    new_name = name[0].lower()
    was_lower = name[0].islower()
    for i in range(1,len(name)):
        letter = name[i]
        if letter.isalpha() and was_lower != letter.islower():
            if letter.islower() and i>1:
                new_name = new_name[:-1] + '_' + new_name[-1]
            elif i<len(name)-1 and name[i+1].isupper():
                new_name += '_'
            was_lower = letter.islower()
        new_name += (letter.lower())
    return new_name
