import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

from __version__ import version
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
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)