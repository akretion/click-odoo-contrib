# Copyright 2018 ACSONE SA/NV (<http://acsone.eu>)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='click-odoo-contrib',
    description='click-odoo scripts collection',
    long_description='\n'.join((
        open(os.path.join(here, 'README.rst')).read(),
        open(os.path.join(here, 'CHANGES.rst')).read(),
    )),
    use_scm_version=True,
    packages=find_packages(),
    setup_requires=[
        'setuptools-scm',
    ],
    install_requires=[
        'click-odoo',
    ],
    license='LGPLv3+',
    author='ACSONE SA/NV',
    author_email='info@acsone.eu',
    url='http://github.com/acsone/setuptools-odoo',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: '
        'GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Odoo',
    ],
    entry_points='''
        [console_scripts]
        click-odoo-uninstall=click_odoo_contrib.uninstall:main
    ''',
)