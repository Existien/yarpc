#!/bin/bash

# check whether repo is clean
pushd /workspace
if [[ "$(git status --porcelain)" != "" ]]; then
  echo "Script must be run from a clean repository."
  exit 1
fi

# copy files to apropriate location
popd
mv -i docs/* /workspace/docs/source/chapters/outputs/
mv -i tests/behave_tests/* /workspace/tests/behave-tests/
mv -i tests/definitions/* /workspace/tests/definitions/
mv -i tests/service/* /workspace/tests/
mv -i yarpc/* /workspace/yarpc/src/yarpc/languages/

# cleanup
cd ..
rm -r {{ cookiecutter._project_slug }}

# create commit
cd /workspace
git add .
git commit -m "
Bootstrap {{ cookiecutter.language }} support

Parameters used:
{%- for k,v in cookiecutter.items() -%}
{%- if not k.startswith('_') %}
  {{ k }}: {{ v }}
{%- endif -%}
{% endfor %}
"

echo "
Next steps:

- Fill out skeleton files in /workspace/yarpc/src/yarpc/languages/{{ cookiecutter.language_idl_key }}
- Run /workspace/tests/generate.sh
- Implement service in /workspace/tests/{{ cookiecutter.language_folder}}_service
  that forwards methods, signals and properties from the backend client to its own
  interface
- Fill out script /workspace/tests/{{ cookiecutter.language_folder}}_service/run.sh
  so that it builds and runs your service
- Fill out skeleton output documentation /workspace/docs/source/chapters/outputs/{{ cookiecutter.language_folder }}
"