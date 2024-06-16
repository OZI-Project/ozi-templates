# SPDX-License-Identifier: Unlicense
files = [
    '0bsd.txt',
    'bsd-2-clause.txt',
    'bsd-3-clause-clear.txt',
    'bsd-3-clause.txt',
    'bsd-4-clause.txt',
]
foreach file: files
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(
            file, 
            subdir: 'ozi_templates'/'license'/'OSI_Approved'/fs.name(meson.current_source_dir()))
    endif
endforeach
