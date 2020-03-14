import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MIXPOTATOS", # Replace with your own username
    version="0.0.1",
    author="YANAN",
    author_email="yananw@uchicago.edu",
    description="MSCA CLASS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EllanWYN/ass3-python",
    packages=setuptools.find_packages(exclude=["*test*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)