# ozi/templates/license/OSI_Approved/Zero_Clause_BSD__0BSD_/meson.build
# SPDX-License-Identifier: Unlicense
files = [
    '0bsd.txt'
]
foreach file: files
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(
            file, 
            subdir: 'ozi_templates'/'license'/'OSI_Approved'/fs.name(meson.current_source_dir()))
    endif
endforeach
