# SPDX-License-Identifier: Unlicense
files = [
    'apsl-1.0.txt',
    'apsl-1.1.txt',
    'apsl-1.2.txt',
    'apsl-2.0.txt',
]
foreach file: files
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(
            file, 
            subdir: 'ozi_templates'/'license'/'OSI_Approved'/fs.name(meson.current_source_dir()))
    endif
endforeach
