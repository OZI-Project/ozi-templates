# OZI 0.1 meson.build:source_files,source_children
# Part of OZI-Licenses.
# See LICENSE.txt in the project root for details.
# DO NOT EDIT BY HAND - This file was generated for use with OZI tools.
# ozi-fix -> meson rewrite is the standard editing pipeline.
source_files = [
    '0bsd.txt', 
    'afl-3.0.txt',
    'agpl-3.0.txt',
    'apache-2.0.txt',
    'apsl-1.0.txt',
    'apsl-1.1.txt',
    'apsl-1.2.txt',
    'apsl-2.0.txt',
    'artistic-2.0.txt',
    'blueoak-1.0.0.txt',
    'bsd-2-clause.txt',
    'bsd-3-clause-clear.txt',
    'bsd-3-clause.txt',
    'bsd-4-clause.txt',
    'bsl-1.0.txt',
    'cc-by-4.0.txt',
    'cc-by-sa-4.0.txt',
    'cc0-1.0.txt',
    'cecill-2.1.txt',
    'cecill-b.txt',
    'cecill-c.txt',
    'ecl-2.0.txt',
    'efl-2.0.txt',
    'epl-1.0.txt',
    'epl-2.0.txt',
    'eupl-1.1.txt',
    'eupl-1.2.txt',
    'gfdl-1.3.txt',
    'gpl-2.0.txt',
    'gpl-3.0.txt',
    'isc.txt',
    'lgpl-2.0.txt',
    'lgpl-2.1.txt',
    'lgpl-3.0.txt',
    'miros.txt',
    'mit-0.txt',
    'mit.txt',
    'mpl-2.0.txt',
    'mulanpsl-2.0.txt',
    'ncsa.txt',
    'ofl-1.1.txt',
    'ogtsl.txt',
    'osl-3.0.txt',
    'postgresql.txt',
    'unlicense.txt',
    'upl-1.0.txt',
    'wtfpl.txt',
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
    'CeCILL_B_Free_Software_License_Agreement__CECILL_B_',
    'CeCILL_C_Free_Software_License_Agreement__CECILL_C_',
    'Eiffel_Forum_License__EFL_',
    'DFSG_approved',
    'exceptions',
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
