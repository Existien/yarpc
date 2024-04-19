#!/bin/bash

# copy files to apropriate location
mv -i docs/* /workspace/docs/source/chapters/outputs/
mv -i tests/behave_tests/* /workspace/tests/behave-tests/
mv -i tests/definitions/* /workspace/tests/definitions/
mv -i tests/service/* /workspace/tests/
mv -i yarpc/* /workspace/yarpc/src/yarpc/languages/

# cleanup
cd ..
rm -r {{ cookiecutter._project_slug }}

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