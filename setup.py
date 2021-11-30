import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-lionel_s",
    version="0.0.1",
    author="Lionel Smith",
    author_email="lionelsmith_1997@hotmail.com",
    description="A test function that adds 6 to a number",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lionel-Smith/pip_package.git",
    project_urls={
        "Bug Tracker": "https://github.com/Lionel-Smith/pip_package.git/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)