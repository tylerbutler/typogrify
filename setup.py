from setuptools import setup, find_packages


def get_readme():
    with open('README.rst') as file:
        return file.read()

setup(
    name='typogrify-engineer',
    version='2.0.0',
    packages=find_packages(),
    author='Christian Metts',
    author_email='xian@mintchaos.com',
    license='BSD',
    description='Typography related template filters for Django & Jinja2 applications',
    long_description=get_readme(),
    url='https://github.com/mintchaos/typogrify',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Utilities'
    ],

    install_requires=['smartypants>=1.8.2']
)
