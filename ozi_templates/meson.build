# OZI 0.1 meson.build:source_files,source_children
# Part of OZI-Templates.
# See LICENSE.txt in the project root for details.
# DO NOT EDIT BY HAND - This file was generated for use with OZI tools.
# ozi-fix -> meson rewrite is the standard editing pipeline.
source_files = [
    '__init__.py',
    'filter.py',
    'py.typed',
    '.gitignore.j2',
    'LICENSE.txt.j2',
    'PKG-INFO.j2',
    'README.rst.j2',
    'bandit.meson.options',
    'bandit.pyproject.toml',
    'black.meson.options',
    'black.pyproject.toml',
    'CHANGELOG.md.j2',
    'coverage.pyproject.toml',
    'doc8.meson.options',
    'doc8.pyproject.toml',
    'flake8.meson.options',
    'flake8.pyproject.toml',
    'isort.meson.options',
    'isort.pyproject.toml',
    'meson.build.j2',
    'meson.options.j2',
    'mypy.meson.options',
    'mypy.pyproject.toml',
    'new_child.j2',
    'ozi.wrap.j2',
    'project.ozi.wrap.j2',
    'project.PKG-INFO',
    'project.array.meson.options',
    'project.feature.meson.options',
    'project.integer.meson.options',
    'project.meson.build',
    'pydocstyle.meson.options',
    'pylint.pyproject.toml',
    'pyproject.toml.j2',
    'pyright.meson.options',
    'pyright.pyproject.toml',
    'pytest.pyproject.toml',
    'pytest.meson.options',
    'restructuredtext-lint.meson.options',
    'requirements.in.j2',
    'root.pyproject.toml',
    'ruff.pyproject.toml',
    'semantic_release.pyproject.toml',
    'setuptools_scm.pyproject.toml',
    'tox.pyproject.toml',
]
foreach file: source_files
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(file, subdir: 'ozi_templates')
    endif
endforeach
source_children = []
foreach child: source_children
    subdir(child)
endforeach
