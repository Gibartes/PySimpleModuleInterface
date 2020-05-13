from setuptools import setup, find_packages

setup(
    name 		= 'moduleInterface',
    version 	= '2.0.0',
    description	= 'Python Module Interface With Normalized Dynamic Actuator',
    author		= 'gibartes',
    install_requires = [],
    packages    = find_packages(exclude = ['docs','*.c','*.h','makefile']),
    keyword		= 'interface',
    python_requires = '>=3',
    zip_safe    = False,
    classifiers = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',        
    ]
)
