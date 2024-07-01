# ozi/templates/project.name/meson.build
# SPDX-License-Identifier: Unlicense
source_templates = [
    '__init__.py.j2',
    '__init__.pyi.j2',
    'meson.build.j2',
    'new_ext.pyx.j2',
    'new_module.py.j2',
    'py.typed.j2',
]
foreach file: source_templates
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(file, subdir: 'ozi_templates'/'project.name')
    endif
endforeach
