from pathlib import Path
import jinja2
from difflib import unified_diff
from yarpc.filters import JinjaFilters
import pkg_resources


class Generator:

    def __init__(self, specs, template_dir):
        self._specs = specs
        self._template_dir = template_dir
        self._filters = JinjaFilters(self._specs)
        self._initialize_jinja_environment()

    def generate(self, check_only):
        is_up_to_date = True
        # for spec in self._specs:
            # if 'outputs' in spec:

    def _initialize_jinja_environment(self):
        self._env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(self._template_dir),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self._filters.register_filters(self._env)
    
    def _is_up_to_date(self, filename, content):
        try:
            with open(filename, "r") as f:
                old_content = f.read().splitlines()
        except FileNotFoundError:
            old_content = []
        new_content = content.splitlines()
        diff = '\n'.join(
            unified_diff(
                old_content, new_content,
                fromfile=f"{filename}.old", tofile=f"{filename}.new",
                lineterm=''
            )
        )
        if diff:
            print(diff)
            return False
        return True
    
    def _generate_file(self, filename: Path, spec: dict, template: Path, check_only: bool) -> bool:
        """ Generates a source file from specs and a template

        Args:
            filename (Path): the file to generate
            spec (dict): the spec to use
            template (Path): the template file to use
            check_only (bool): whether to check for differences instead of generating code
        Returns:
            bool: whether the generated file is up to date
        """
        kwargs = {
            "spec": spec,
            "version": pkg_resources.get_distribution('yarpc').version
        }
        rendered = self._env.get_template(template).render(**kwargs)

        if check_only:
            return self._is_up_to_date(filename, rendered)
        else:
            filename.parent.mkdir(parents=True, exist_ok=True)
            with open(filename, "w") as f:
                f.write(rendered)
            return True