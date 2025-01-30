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
{% if not cookiecutter.use_separate_build_script %}
rm /workspace/tests/{{ cookiecutter.language_folder }}_service/build.sh
{% endif %}

# add language to run_tests.sh
echo "
# Run {{ cookiecutter.language }} tests
if [[ \${languages[*]} =~ \"{{ cookiecutter.language_folder }}\" ]];then
    {% if cookiecutter.use_separate_build_script -%}
    pushd {{ cookiecutter.language_folder }}_service
    ./build.sh
    popd
    {% endif -%}
    behave behave-tests/{{ cookiecutter.language_folder }}
fi
" >> /workspace/tests/run_tests.sh
sed -i 's/# EOL languages (used by cookiecutter)/{{ cookiecutter.language_folder }}\n        # EOL languages (used by cookiecutter)/g' /workspace/tests/run_tests.sh

# add language tests to ci
echo "
  Run-{{ cookiecutter.language|replace(' ','-') }}-Generator-Tests:
    runs-on: ubuntu-latest
    needs: Build-Docker-Image
    steps:
    - name: Checkout
      uses: actions/checkout@v4
    - name: Set up docker Buildx
      uses: docker/setup-buildx-action@v1
    - name: Download SDK
      uses: actions/download-artifact@v4
      with:
        name: yarpc-sdk
        path: /tmp
    - name: Load SDK
      run: docker load --input /tmp/yarpc-sdk.tar
    - name: Run behave tests
      run: bash {{ '\${{ github.workspace }}' }}/sdk/run.sh ./tests/run_tests.sh {{ cookiecutter.language_folder }}
" >> /workspace/.github/workflows/ci.yml

# create commit
cd /workspace
git add .
git commit -m "
feat: Bootstrap {{ cookiecutter.language }} support

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
{% if cookiecutter.use_separate_build_script -%}
- Fill out script /workspace/tests/{{ cookiecutter.language_folder}}_service/build.sh
  so that it builds your service
- Fill out script /workspace/tests/{{ cookiecutter.language_folder}}_service/run.sh
  so that it runs your service
{% else -%}
- Fill out script /workspace/tests/{{ cookiecutter.language_folder}}_service/run.sh
  so that it builds and runs your service
{% endif -%}
- Fill out skeleton output documentation /workspace/docs/source/chapters/outputs/{{ cookiecutter.language_folder }}
"
