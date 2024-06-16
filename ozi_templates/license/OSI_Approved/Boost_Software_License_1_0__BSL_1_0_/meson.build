# SPDX-License-Identifier: Unlicense
files = [
    'bsl-1.0.txt'
]
foreach file: files
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(
            file, 
            subdir: 'ozitemplates'/'license'/'OSI_Approved'/fs.name(meson.current_source_dir()))
    endif
endforeach
