from setuptools import setup, find_packages
from blockchain_parser import __version__


setup(
    name='blockchain-parser-1.0',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/chainlaboratory/blockchain-parser-1.0',
    author='Antoine Le Calvez',
    author_email='antoine@p2sh.info',
    description='Bitcoin blockchain parser',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    test_suite='blockchain_parser.tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=[
        'python-bitcoinlib==0.11.0',
        'plyvel==1.5.1',
        'ripemd-hash==1.0.1'
    ]
)
