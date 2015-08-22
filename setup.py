from setuptools import setup

import cliar


try:
    long_description = open('README.rst').read()

except:
    long_description = cliar.__long_description__


setup(
    name=cliar.__title__,
    version=cliar.__version__,
    author=cliar.__author__,
    description=cliar.__description__,
    long_description=long_description,
    author_email=cliar.__author_email__,
    url='https://bitbucket.org/moigagoo/cliar',
    py_modules = ['cliar'],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix']
)
