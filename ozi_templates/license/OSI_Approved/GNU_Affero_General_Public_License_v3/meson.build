# SPDX-License-Identifier: Unlicense
files = [
    'agpl-3.0-only.txt',
    'agpl-3.0-or-later.txt',
]
foreach file: files
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(
            file, 
            subdir: 'ozi_templates'/'license'/'OSI_Approved'/fs.name(meson.current_source_dir()))
    endif
endforeach
