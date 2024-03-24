import jinja2
from yarpc.utils import (
    to_snake_case,
    find_type,
    extract_inner_names,
    extract_dependencies,
)

class TemplatingEngine:
    """A jinja2 templating engine with custom filters

    Args:
        template_dir (str): The directory to look for jinja files in
    """
    def __init__(self, template_dir: str):
        self._template_dir = template_dir
        self._env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(self._template_dir),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self._register_filters()

    def _register_filters(self):
        """Registers custom filters
        """
        self._env.filters['snake_case'] = to_snake_case
        self._env.filters['find_type'] = find_type
        self._env.filters['extract_inner'] = extract_inner_names
        self._env.filters['extract_dependencies'] = extract_dependencies

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
        return self._env.get_template(template_file).render(**context)