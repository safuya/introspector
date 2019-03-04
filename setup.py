import pathlib
from setuptools import setup

NAME = 'introspector'
HERE = pathlib.Path(__file__).parent
REQUIRES_PYTHON = '>=3.6.0'
INSTALL_REQUIRES = []
README = (HERE / 'README.md').read_text()

setup(
        name=NAME,
        version='1.0.1',
        description='Introspect stuff in Python',
        long_description=README,
        python_requires=REQUIRES_PYTHON,
        long_description_content_type='text/markdown',
        url='https://code.tvac.bt.co.uk/pipelinesquad/introspector',
        author='Robert Hughes',
        author_email='robert.hughes@bt.com',
        license='MIT',
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: Implementation :: CPython'
        ],
        packages=['introspector'],
        include_package_data=True,
        install_requires=INSTALL_REQUIRES,
        entry_points={}
)
