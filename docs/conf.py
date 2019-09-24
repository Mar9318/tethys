# -*- coding: utf-8 -*-
#
# Tethys Platform documentation build configuration file, created by
# sphinx-quickstart on Sat Oct 18 17:30:09 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
from unittest import mock

import pbr.version
import pbr.git

from django.conf import settings
import django

# Mock Dependencies
# NOTE: No obvious way to automatically anticipate all the sub modules without
# installing the package, which is what we are trying to avoid.
MOCK_MODULES = [
    'bokeh', 'bokeh.embed', 'bokeh.resources',
    'channels',
    'conda', 'conda.cli', 'conda.cli.python_api',
    'condorpy',
    'django_gravatar',
    'dask', 'dask.delayed', 'dask.distributed',
    'distributed', 'distributed.protocol', 'distributed.protocol.serialize',
    'distro',
    'docker', 'docker.types', 'docker.errors',
    'guardian', 'guardian.admin',
    'model_utils', 'model_utils.managers',
    'plotly', 'plotly.offline',
    'social_core', 'social_core.exceptions',
    'social_django',
    'sqlalchemy', 'sqlalchemy.orm',
    'tethys_apps.harvester',  # Mocked to prevent issues with loading apps during docs build.
    'tethys_compute.utilities',  # Mocked to prevent issues with DictionaryField and List Field during docs build.
    'yaml'
]


# Mock dependency modules so we don't have to install them
# See: https://docs.readthedocs.io/en/latest/faq.html#i-get-import-errors-on-libraries-that-depend-on-c-modules
class MockModule(mock.MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return mock.MagicMock()


print('NOTE: The following modules are mocked to prevent timeouts during the docs build process on RTD:')
print('{}'.format(', '.join(MOCK_MODULES)))
sys.modules.update((mod_name, MockModule()) for mod_name in MOCK_MODULES)

# Fixes django settings module problem
sys.path.insert(0, os.path.abspath('..'))

installed_apps = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tethys_config',
    'tethys_quotas',
    'tethys_apps',
    'tethys_gizmos',
    'tethys_services',
    'tethys_compute',
]

settings.configure(INSTALLED_APPS=installed_apps)
django.setup()

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinxcontrib.napoleon',
    'sphinx.ext.extlinks',
    'sphinx.ext.todo',
    'sphinxarg.ext'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Tethys Platform'
copyright = u'2019, Tethys Platform'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = pbr.version.VersionInfo('tethys_platform').version_string()
# The full version, including alpha/beta/rc tags.
release = pbr.version.VersionInfo('tethys_platform').version_string_with_vcs()

# A string of reStructuredText that will be included at the end of every source
# file that is read. This is the right place to add substitutions that should be
# available in every file.
branch = pbr.git._run_git_command(['rev-parse', '--abbrev-ref', 'HEAD'], pbr.git._get_git_directory())
on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    # Hack to try to get the branch name if possible, otherwise assume 'release'
    branch = pbr.git._run_git_command(['branch'], pbr.git._get_git_directory()).split('*')[-1].split('\n')[0].\
        strip(')').split('/')
    branch = branch[-1] if len(branch) == 2 else 'release'
    print(branch)

rst_epilog = """
.. |branch| replace:: {branch}
""".format(branch=branch)

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'images/default_favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/tethys.css',
]

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
smartquotes = False

# Output file base name for HTML help builder.
htmlhelp_basename = 'TethysPlatformdoc'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'TethysPlatform.tex', u'Tethys Platform Documentation',
   u'Nathan Swain', 'manual'),
]

# markup to shorten external links (see: http://www.sphinx-doc.org/en/stable/ext/extlinks.html)
install_tethys_link = 'https://raw.githubusercontent.com/tethysplatform/tethys/{}/scripts/install_tethys.%s'.\
    format(branch)

extlinks = {'install_tethys': (install_tethys_link, None)}

# -- Options for manual page output ---------------------------------------
# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'tethysplatform', u'Tethys Platform Documentation', [u'Nathan Swain'], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'TethysPlatform', u'Tethys Platform Documentation',
   u'Nathan Swain', 'TethysPlatform', 'One line description of project.',
   'Miscellaneous'),
]

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# If this is True, todo and todolist produce output, else they produce nothing. The default is False.
todo_include_todos = True

# If this is True, todo emits a warning for each TODO entries. The default is False.
todo_emit_warnings = True

html_theme = 'sphinx_materialdesign_theme'

html_theme_options = {
    # Specify a list of menu in Header.
    # Tuples forms:
    #  ('Name', 'external url or path of pages in the document', boolean, 'icon name')
    #
    # Third argument:
    # True indicates an external link.
    # False indicates path of pages in the document.
    #
    # Fourth argument:
    # Specify the icon name.
    # For details see link.
    # https://material.io/icons/
    'header_links': [
        ('Home', 'index', False, 'home'),
        ('Tutorials', 'tutorials', False, 'assignment'),
        ('SDK', 'tethys_sdk', False, 'build'),
        ('CLI', 'tethys_cli', False, 'keyboard_arrow_right'),
        ('Tethys Portal', 'tethys_portal', False, 'web'),
        ('Software Suite', 'software_suite', False, 'developer_board'),
        ("Issues", "https://github.com/tethysplatform/tethys/issues", True, 'bug_report'),
        ("GitHub", "https://github.com/tethysplatform/tethys", True, 'launch')
    ],

    # Customize css colors.
    # For details see link.
    # https://getmdl.io/customize/index.html
    #
    # Values: amber, blue, brown, cyan deep_orange, deep_purple, green, grey, indigo, light_blue,
    #         light_green, lime, orange, pink, purple, red, teal, yellow(Default: indigo)
    'primary_color': 'blue',
    # Values: Same as primary_color. (Default: pink)
    'accent_color': 'light_blue',

    # Customize layout.
    # For details see link.
    # https://getmdl.io/components/index.html#layout-section
    'fixed_drawer': False,
    'fixed_header': True,
    'header_waterfall': True,
    'header_scroll': False,

    # Render title in header.
    # Values: True, False (Default: False)
    'show_header_title': True,
    # Render title in drawer.
    # Values: True, False (Default: True)
    'show_drawer_title': False,
    # Render footer.
    # Values: True, False (Default: True)
    'show_footer': True
}
