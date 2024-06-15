# SPDX-License-Identifier: Unlicense
files = [
    'gfdl-1.3-only.txt',
    'gfdl-1.3-or-later.txt',
]
foreach file: files
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(
            file, 
            subdir: 'ozi_templates'/'license'/'OSI_Approved'/fs.name(meson.current_source_dir()))
    endif
endforeach
