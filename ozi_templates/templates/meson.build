# ozi_templates/templates/meson.build
# SPDX-License-Identifier: Unlicense
_templates = [
    '.release_notes.md.j2',
    'CHANGELOG.md.j2',
    '.parsed_commit_heading.j2',
]
foreach file: _templates
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(file, subdir: 'ozi_templates'/'templates')
    endif
endforeach