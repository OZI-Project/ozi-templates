# ozi_templates/tests/meson.build
# SPDX-License-Identifier: Unlicense
tests_templates = [
    'meson.build.j2',
    'new_test.py.j2',
]
foreach file: tests_templates
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(file, subdir: 'ozi_templates'/'tests')
    endif
endforeach