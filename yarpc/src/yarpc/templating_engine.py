import jinja2
from yarpc.utils import to_snake_case, find_type, extract_inner_names, extract_dependencies

class TemplatingEngine:
    def __init__(self, template_dir):
        self._template_dir = template_dir
        self._env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(self._template_dir),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self._register_filters()

    def _register_filters(self):
        self._env.filters['snake_case'] = to_snake_case
        self._env.filters['find_type'] = find_type
        self._env.filters['extract_inner'] = extract_inner_names
        self._env.filters['extract_dependencies'] = extract_dependencies

    def render(self, language, template, context):
        template_file = f"{language}/{template}.j2"
        return self._env.get_template(template_file).render(**context)