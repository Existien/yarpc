import jinja2
from yarpc.utils import (
    to_snake_case,
    to_camel_case,
    to_pascal_case,
    find_type,
    extract_inner_names,
    extract_dependencies,
)
from .languages import languages

class TemplatingEngine:
    """A jinja2 templating engine with custom filters

    Args:
        template_dir (str): The directory to look for jinja files in
    """
    def __init__(self, template_dir: str):
        self._template_dir = template_dir
        self._env = {}
        for language in languages().keys():
            self._env[language] = jinja2.Environment(
                loader=jinja2.FileSystemLoader(self._template_dir),
                trim_blocks=True,
                lstrip_blocks=True,
            )
            self._register_filters(language)
            self._register_globals(language)

    def _register_filters(self, language: str):
        """Registers custom filters for a specific language

        Args:
            language (str): The language to register filters for
        """
        filters = {
            'snake_case': to_snake_case,
            'camel_case': to_camel_case,
            'pascal_case': to_pascal_case,
            'find_type': find_type,
            'extract_inner': extract_inner_names,
            'extract_dependencies': extract_dependencies,
        }
        filters.update(languages().get(language).get_jinja_filters())
        for key, value in filters.items():
            self._env[language].filters[key] = value

    def _register_globals(self, language: str):
        """Registers custom globals for a specific language

        Args:
            language (str): The language to register globals for
        """
        jinja_globals = languages().get(language).get_jinja_globals()
        for key, value in jinja_globals.items():
            self._env[language].globals[key] = value


    def render(self, language: str, template: str, context: dict) -> str:
        """Renders a template using data form the provided context.

        Args:
            language (str): The target language
            template (str): The name of the template
            contest (dict): The context containing the information needed
                for the generation

        Returns:
            str: The generated content
        """
        template_file = f"{language}/{template}.j2"
        return self._env[language].get_template(template_file).render(**context)