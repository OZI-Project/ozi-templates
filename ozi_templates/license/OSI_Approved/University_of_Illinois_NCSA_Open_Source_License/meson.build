# ozi/templates/license/OSI_Approved/zlib_libpng_License/meson.build
# SPDX-License-Identifier: Unlicense
files = [
    'ncsa.txt'
]
foreach file: files
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(
            file, 
            subdir: 'ozi_templates'/'license'/'OSI_Approved'/fs.name(meson.current_source_dir()))
    endif
endforeach
