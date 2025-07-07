# ozi/templates/.github/workflows/meson.build
# SPDX-License-Identifier: MIT-0
workflows = [
    'checkpoint.yml.j2',
    'cleanup.yml.j2',
    'draft.yml.j2',
    'generate_provenance.yml.j2',
    'harden_runner.yml.j2',
    'ozi.yml.j2',
    'provenance.yml.j2',
    'publish.yml.j2',
    'release.yml.j2',
]
foreach file: workflows
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(file, subdir: 'ozi_templates'/'.github'/'workflows')
    endif
endforeach
if false
    executable('source_files_child_templates_child_github_workflows', workflows)
endif