# SPDX-License-Identifier: MIT-0
files = [
    'cecill-b.txt',
]
foreach file: files
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(
            file, 
            subdir: 'ozi_templates'/'license'/fs.name(meson.current_source_dir()))
    endif
endforeach
