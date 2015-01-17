from setuptools import setup

setup(
    name='spotipy',
    version='2.3.0',
    description='simple client for the Spotify Web API',
    author="@plamere",
    author_email="paul@echonest.com",
    url='http://spotipy.readthedocs.org/',
    install_requires=['requests>=1.0', 'future>=0.14.3'],
    license='LICENSE.txt',
    packages=['spotipy'])
