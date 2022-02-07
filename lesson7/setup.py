from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='07.02.2022',
    description='Very useful code',
    url='https://github.com/GRO1982',
    author='Grzhyvach Alexii',
    author_email='IT.orank@gmail.com',
    license='GRO_LIC',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:sort_files']}
)
