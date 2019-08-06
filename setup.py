# Copyright 2019 Yuhui
#
# Licensed under the GNU General Public License, Version 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.gnu.org/licenses/gpl-3.0.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

from datetime import datetime
now = datetime.now()
timestamp = now.strftime('%Y%m%d%H%M%S')

from datagovsg import name, version, author, author_email

release_status = 'Development Status :: 5 - Production/Stable'
packages = [
    'datagovsg',
]
with open('requirements.txt', 'r') as requirements_file:
    requirements = requirements_file.read().split('\n')
minimum_python_version = 3

test_folders = [
    'tests',
]
exclude_packages = [] + test_folders

description = 'Python package for interacting with APIs available at Data.gov.sg'
with open('README.rst', 'r') as readme_file:
    long_description = readme_file.read()
    long_description_content_type = 'text/x-rst'

license = 'GNU General Public License v3'
url = 'https://github.com/yuhui/datagovsg'
project_urls = {
    'Source': 'https://github.com/yuhui/datagovsg',
    'Bug Tracker': 'https://github.com/yuhui/datagovsg/issues',
}
keywords = [
    'data.gov.sg',
    'python',
    'singapore',
    'wrapper',
]

platforms = [
    'MacOS X',
    'POSIX',
    'Windows',
]
classifiers = [
    release_status,
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Topic :: Internet',
]

setup(
    name=name,
    #version='{}.{}'.format(version, timestamp), # TestPyPi
    version=version, # PyPi

    packages=find_packages(exclude=exclude_packages),
    install_requires=requirements,
    platforms=platforms,
    python_requires='>={}'.format(minimum_python_version),

    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    license=license,
    url=url,
    project_urls=project_urls,
    keywords=keywords,
    classifiers=classifiers,

    zip_safe=False,
)
