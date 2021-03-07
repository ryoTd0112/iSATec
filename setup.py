#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = [requirement.strip() for requirement in requirements_file.readlines()]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Ryo Tandai",
    author_email='ryo.s1042@gmail.com',
    # python_requires='>=3.5',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.5',
        # 'Programming Language :: Python :: 3.6',
        # 'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="iSATex is an ideal software package for all uses of Raman microscope and/or FT-IR. Open-source-software development from the researcher’s perspectives would be complementary with the development of the modern analytical geosciences.",
    entry_points={
        'console_scripts': [
            'isatec=isatec.cli:main',
        ],
    },
    install_requires=requirements,
    license="LGPL license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='isatec',
    name='isatec',
    packages=find_packages(include=['isatec', 'isatec.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ryoTd0112/isatec',
    version='0.0.15',
    zip_safe=False,
)
