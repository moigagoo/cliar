from setuptools import setup, find_packages

from sys import version_info


short_description = 'Cliar lets you create powerful commandline interfaces from regular Python classes. Using type hints, you can add validation and on-the-fly parsing.'

try:
    long_description = open('README.rst').read()
except:
    long_description = short_description


setup(
    name='cliar',
    version='1.1.8',
    author='Konstantin Molchanov',
    description=short_description,
    long_description=long_description,
    author_email='moigagoo@live.com',
    url='https://bitbucket.org/moigagoo/cliar',
    py_modules=['cliar'],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix']
)
