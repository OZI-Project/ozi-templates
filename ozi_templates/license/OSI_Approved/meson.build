# SPDX-License-Identifier: MIT-0
files = [
    '0bsd.txt',
    'afl-3.0.txt',
    'agpl-3.0-only.txt',
    'agpl-3.0-or-later.txt',
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
    'cecill-2.1.txt',
    'efl-2.0.txt',
    'epl-1.0.txt',
    'epl-2.0.txt',
    'eupl-1.1.txt',
    'eupl-1.2.txt',
    'gfdl-1.3-only.txt',
    'gfdl-1.3-or-later.txt',
    'gpl-2.0-only.txt',
    'gpl-2.0-or-later.txt',
    'gpl-3.0-only.txt',
    'gpl-3.0-or-later.txt',
    'isc.txt',
    'lgpl-2.0-only.txt',
    'lgpl-2.0-or-later.txt',
    'lgpl-2.1-only.txt',
    'lgpl-2.1-or-later.txt',
    'lgpl-3.0-only.txt',
    'lgpl-3.0-or-later.txt',
    'miros.txt',
    'mit-0.txt',
    'mit-cmu.txt',
    'mit.txt',
    'mpl-2.0.txt',
    'mulanpsl-2.0.txt',
    'ofl-1.1.txt',
    'ogtsl.txt',
    'osl-3.0.txt',
    'postgresql.txt',
    'unlicense.txt',
    'upl-1.0.txt',
    'zlib.txt',
]
foreach file: files
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(
            file, 
            subdir: 'ozi_templates'/'license'/fs.name(meson.current_source_dir()))
    endif
endforeach

children = [
    'Academic_Free_License__AFL_',
    'Apache_Software_License',
    'Apple_Public_Source_License',
    'Artistic_License',
    'Blue_Oak_Model_License__BlueOak_1_0_0_',
    'BSD_License',
    'Boost_Software_License_1_0__BSL_1_0_',
    'CEA_CNRS_Inria_Logiciel_Libre_License__version_2_1__CeCILL_2_1_',
    'CMU_License__MIT_CMU_',
    'Eclipse_Public_License_1_0__EPL_1_0_',
    'Eclipse_Public_License_2_0__EPL_2_0_',
    'Eiffel_Forum_License__EFL_',
    'European_Union_Public_Licence_1_1__EUPL_1_1_',
    'European_Union_Public_Licence_1_2__EUPL_1_2_',
    'GNU_Affero_General_Public_License_v3',
    'GNU_Affero_General_Public_License_v3_or_later__AGPLv3__',
    'GNU_Free_Documentation_License__FDL_',
    'GNU_General_Public_License__GPL_',
    'GNU_General_Public_License_v2__GPLv2_',
    'GNU_General_Public_License_v2_or_later__GPLv2__',
    'GNU_General_Public_License_v3__GPLv3_',
    'GNU_General_Public_License_v3_or_later__GPLv3__',
    'GNU_Lesser_General_Public_License_v2__LGPLv2_',
    'GNU_Lesser_General_Public_License_v2_or_later__LGPLv2__',
    'GNU_Lesser_General_Public_License_v3__LGPLv3_',
    'GNU_Lesser_General_Public_License_v3_or_later__LGPLv3__',
    'GNU_Library_or_Lesser_General_Public_License__LGPL_',
    'ISC_License__ISCL_',
    'MirOS_License__MirOS_',
    'MIT_License',
    'MIT_No_Attribution_License__MIT_0_',
    'Mozilla_Public_License_2_0__MPL_2_0_',
    'Mulan_Permissive_Software_License_v2__MulanPSL_2_0_',
    'Open_Group_Test_Suite_License',
    'Open_Software_License_3_0__OSL_3_0_',
    'PostgreSQL_License',
    'SIL_Open_Font_License_1_1__OFL_1_1_',
    'The_Unlicense__Unlicense_',
    'Universal_Permissive_License__UPL_',
    'University_of_Illinois_NCSA_Open_Source_License',
    'Zero_Clause_BSD__0BSD_',
    'zlib_libpng_License',
]
foreach child: children
    subdir(child)
endforeach
if false
    executable('templates_license_osi_children', children)
endif
