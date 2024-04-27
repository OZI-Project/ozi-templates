# ozi/templates/tests/meson.build
# SPDX-License-Identifier: CC0-1.0
tests_templates = [
    'meson.build.j2',
    'new_test.py.j2',
]
foreach file: tests_templates
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(file, subdir: 'ozi'/'templates'/'tests')
    endif
endforeach