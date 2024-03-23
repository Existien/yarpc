from pathlib import Path
from yarpc.templating_engine import TemplatingEngine
from difflib import unified_diff
from yarpc.utils import to_snake_case
from shutil import rmtree
import pkg_resources


class Generator:
    """Code generator using a templating engine.

    Args:
        output_base_dir (str): The directory the paths provided in the spec are relative to
    """

    def __init__(self, output_base_dir: str):
        self._output_base_dir = output_base_dir
        self._engine = TemplatingEngine(f"{Path(__file__).parent}/templates")

    def generate(self, outputs: list, check_only: bool) -> bool:
        """Generates code based on the provided specification

        Args:
            outputs (list): A list of outputs to be generated
            check_only (bool): If True, does not persist the generate,
                but only uses it to check for differences.
        Returns:
            bool: Whether there are no differences between the existing code
                and the generated one. Always True if check_only is False.
        """
        is_up_to_date = True
        for output in outputs:
            output_location = self._get_location(output)
            if not check_only and Path(output_location).exists():
                print(f"Cleaning {output_location}")
                rmtree(output_location)
            for object in output['objects']:
                is_up_to_date = (
                    is_up_to_date and
                    self._generate_object(object, output, check_only)
                )
        return is_up_to_date

    def _get_location(self, output: dict) -> str:
        """Returns the output location relative to the
        configured output base dir.

        Args:
            output (dict): The output specification
        Returns:
            str: The output path
        """
        if output['location'][0] == '/':
            return output['location']
        else:
            return f"{self._output_base_dir}/{output['location']}"

    def _is_up_to_date(self, filename: str, content: str) -> bool:
        """Returns whether a file is consistent with the generated content.

        Args:
            filename (str): the file to compare
            content (str): the content to compare it with
        Returns:
            bool: Whether the file contains the expected content
        """
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

    def _generate_object(self, object: dict, output: dict, check_only: bool) -> bool:
        """Generates an object for a specific output

        Args:
            object (dict): The object to generate
            output (dict): The output to generate it for
            check_only (bool): If True, the object will not be persisted,
                but just used to compare the existing file with the generate.
        Returns:
            bool: Whether the existing file is in sync with the generate.
                Always True if check_only is False.
        """
        context = {
            "object": object,
            "output": output,
            "version": pkg_resources.get_distribution('yarpc').version
        }
        language = output['language']
        is_up_to_date = True
        for target in object.get('targets', []):
            target_context = {**context, 'target': target}
            filename = Path(f"{self._get_location(output)}/{self._generate_filename(target['className'], target['template'], language)}")
            is_up_to_date = (
                is_up_to_date and
                self._generate_file(filename, language, target['template'], target_context, check_only)
            )
        if object.get('kind') == 'struct':
            filename = Path(f"{self._get_location(output)}/{self._generate_filename(object['name'], 'struct', language)}")
            is_up_to_date = (
                is_up_to_date and
                self._generate_file(filename, language, 'struct', context, check_only)
            )
        elif object.get('kind') == 'enum':
            filename = Path(f"{self._get_location(output)}/{self._generate_filename(object['name'], 'enum', language)}")
            is_up_to_date = (
                is_up_to_date and
                self._generate_file(filename, language, 'enum', context, check_only)
            )
        return is_up_to_date

    def _generate_filename(self, name: str, template: str, language: str) -> str:
        """Generates a filename based on the object name, template and language.

        Args:
            name (str): The name of the object
            template (str): The kind of object
            language (str): The language the file should be in

        Returns:
            str: The filename
        """
        match language:
            case 'py':
                return f"{to_snake_case(name)}.py"
        raise Exception(f"Filename for language {language} and template {template} could not be generated")

    def _generate_file(self, filename: Path, language: str, template: Path, context: dict, check_only: bool) -> bool:
        """ Generates a source file from specs and a template

        Args:
            filename (Path): the file to generate
            language (str): the language to generate for
            template (Path): the template file to use
            context (dict): data used by the template, such as the spec
            check_only (bool): whether to check for differences instead of generating code
        Returns:
            bool: whether the generated file is up to date
        """
        print(f"Generate {filename}")
        rendered = self._engine.render(language, template, context)

        if check_only:
            return self._is_up_to_date(filename, rendered)
        else:
            filename.parent.mkdir(parents=True, exist_ok=True)
            with open(filename, "w") as f:
                f.write(rendered)
            return True