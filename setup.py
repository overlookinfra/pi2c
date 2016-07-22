from setuptools import setup, find_packages


setup(
    name='pi2c',
    version='0.1.5',
    packages=find_packages(),
    install_requires=['python-icinga2api'],
    entry_points={
        'console_scripts': [
            'pi2c = pi2c.__main__:main'
        ]
    },
    author='Matt Kirby',
    author_email='kirby@puppet.com',
    description='A CLI tool for icinga2 api interactions',
    license='Apache License 2.0',
    url='github.com:mattkirby/pi2c'
)
