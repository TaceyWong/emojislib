import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

from emojislib.__version__ import version
setuptools.setup(
    name="emojislib",
    version=version,
    author="Tacey Wong",
    author_email="xinyong.wang@qq.com",
    description="Emojis for Python 😄 🐍 😋",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TaceyWong/emojislib",
    packages=setuptools.find_packages(),
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Emoji',
        'Topic :: Funny chars',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)