from setuptools import setup

long_description = open('README.rst').read()

setup(
    name='tswift',
    version='0.3.0',
    description='MetroLyrics API',
    long_description=long_description,
    install_requires=['lxml', 'requests', 'google'],
    url='https://github.com/brenns10/tswift',
    author='Stephen Brennan',
    author_email='stephen@brennan.io',
    license='Revised BSD',
    py_modules=['tswift'],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Development Status :: 4 - Beta',
        'Topic :: Multimedia :: Sound/Audio',
        'Natural Language :: English',
    ],
    keywords='lyrics metrolyrics scrape',
    entry_points={
        'console_scripts': [
            'tswift=tswift:main',
        ],
    },
)
