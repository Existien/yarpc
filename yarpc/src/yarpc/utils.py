def find_type(type_name: str, objects: list) -> dict:
    hits = list(filter(lambda x: x.get('name') == type_name, objects))
    if len(hits) == 1:
        return hits[0]
    return {}

def to_snake_case(name: str) -> str:
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
