import jinja2

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
        pass

    def render(self, language, template, context):
        template_file = f"{language}/{template}.j2"
        return self._env.get_template(template_file).render(**context)