# ozi_templates/subprojects/meson.build
# SPDX-License-Identifier: Unlicense
subprojects_templates = [
    'ozi.wrap.j2',
]
foreach file: subprojects_templates
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(file, subdir: 'ozi_templates'/'subprojects')
    endif
endforeach