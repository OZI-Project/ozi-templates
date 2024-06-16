# ozi/templates/license/OSI_Approved/Open_Software_License_3_0__OSL_3_0_/meson.build
# SPDX-License-Identifier: Unlicense
files = [
    'osl-3.0.txt'
]
foreach file: files
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(
            file, 
            subdir: 'ozi_templates'/'license'/'OSI_Approved'/fs.name(meson.current_source_dir()))
    endif
endforeach
