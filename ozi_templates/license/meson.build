# OZI 0.1 meson.build:source_files,source_children
# Part of OZI-Licenses.
# See LICENSE.txt in the project root for details.
# DO NOT EDIT BY HAND - This file was generated for use with OZI tools.
# ozi-fix -> meson rewrite is the standard editing pipeline.
source_files = [
    'agpl-3.0.txt',
    'apache-2.0.txt',
    'artistic-2.0.txt',
    'bsd-3-clause.txt',
    'cc0-1.0.txt',
    'epl-1.0.txt',
    'gfdl-1.3.txt',
    'gpl-2.0.txt',
    'gpl-3.0.txt',
    'isc.txt',
    'lgpl-2.0.txt',
    'lgpl-2.1.txt',
    'lgpl-3.0.txt',
    'mit.txt',
    'ofl-1.1.txt',
    'zlib.txt',
]
foreach file : source_files
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(
            file,
            subdir: 'ozi_templates' / 'license',
        )
    endif
endforeach
source_children = [
    'CC0_1_0_Universal__CC0_1_0__Public_Domain_Dedication',
    'DFSG_approved',
    'Free_To_Use_But_Restricted',
    'OSI_Approved',
    'Public_Domain',
]
foreach child : source_children
    subdir(child.underscorify())
endforeach
if false
    executable('templates_license_children', children)
endif
