from setuptools import setup, find_packages
import os

# Read the README file
readme_path = os.path.join("README", "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as fh:
        long_description = fh.read()
else:
    long_description = "A Python project boilerplate generator"
setup(
    name="newproj",
    version="1.0.0",
    author="Liam G",
    author_email="TemNet021@outlook.com",
    description="A fast, interactive Python project generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Golden021/newproj",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "newproj=newproj.cli:main",
        ],
    },
    install_requires=[],
    keywords="python project generator boilerplate template",
)  