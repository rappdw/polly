
import versioneer
from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='polly',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='polly',
    long_description=long_description,
    url='https://github.com/rappdw/polly.git',

    author='Dan Rapp',
    author_email='rappdw@gmail.com',

    license='MIT',
    keywords='library',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        # Set this topic to what works for you
        'Topic :: Python :: Library',
        # Pick your license as you wish (should match "license" above)
        'License :: MIT',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    setup_requires=[
        # Setuptools 18.0 properly handles Cython extensions.
        'setuptools>=18.0'
    ],
    install_requires=[
    ],

    extras_require={
        'dev': [
            'wheel>=0.30.0'
        ],
        'test': [
            'pytest',
            'pytest-cov',
            'pylint'
        ],
    },

    package_data={
        # 'sample': ['package_data.dat'],
    },
    #scripts=[],
)
        