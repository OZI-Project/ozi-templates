# ozi/templates/license/OSI_Approved/SIL_Open_Font_License_1_1__OFL_1_1_/meson.build
# SPDX-License-Identifier: Unlicense
files = [
    'ofl-1.1.txt'
]
foreach file: files
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(
            file, 
            subdir: 'ozi_templates'/'license'/'OSI_Approved'/fs.name(meson.current_source_dir()))
    endif
endforeach
