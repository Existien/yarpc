from .base_language import BaseLanguage, ObjectKind, Target, DBusTypes
import yarpc.languages.python as python
from typing import Dict

def languages() -> Dict[str, BaseLanguage]:
    """Returns a dictionary with the supported languages

    Args:
        name (str): The name of the language to get

    Returns:
        Dict[str, BaseLanguage]: Dictionary with the names of the language and the respective language classes
    """
    return {
        'py': python.Python(),
    }