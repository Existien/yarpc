from .base_language import BaseLanguage, ObjectKind, Target, DBusTypes
from typing import Dict


def __get_lang_modules():
    import importlib
    from pathlib import Path
    init_files = Path(__file__).parent.glob('*/__init__.py')
    module_names = list(map(lambda x: x.parent.parts[-1], init_files))
    return list(map(lambda x: (x, importlib.import_module(f"yarpc.languages.{x}")), module_names))


def languages() -> Dict[str, BaseLanguage]:
    """Returns a dictionary with the supported languages

    Args:
        name (str): The name of the language to get

    Returns:
        Dict[str, BaseLanguage]: Dictionary with the names of the language and the respective language classes
    """
    if not hasattr(languages, 'modules'):
        languages.modules = __get_lang_modules()
    return {
        mod[0]: mod[1].Language() for mod in languages.modules
    }
