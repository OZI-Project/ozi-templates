# ozi/templates/license/OSI_Approved/Mulan_Permissive_Software_License_v2__MulanPSL_2_0_/meson.build
# SPDX-License-Identifier: Unlicense
files = [
    'mulanpsl-2.0.txt'
]
foreach file: files
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(
            file, 
            subdir: 'ozi_templates'/'license'/'OSI_Approved'/fs.name(meson.current_source_dir()))
    endif
endforeach
