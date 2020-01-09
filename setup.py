import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='FT_WeScrape',
    version='0.0.1',
    author='Brent Jeffson Florendo',
    author_email='brentjeffson@gmail.com',
    description='Web Scraping For Novel, Manga',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/brentjeffson/WeScrape',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programmning Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6',
)