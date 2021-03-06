# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    LONG_DESC = fh.read()
    setup(
        name="hydra-ax-sweeper",
        version="0.1.0",
        author="Omry Yadan, Shagun Sodhani",
        author_email="omry@fb.com, sshagunsodhani@gmail.com",
        description="Hydra Ax Sweeper plugin",
        long_description=LONG_DESC,
        long_description_content_type="text/markdown",
        url="https://github.com/facebookresearch/hydra/",
        packages=find_packages(exclude=["tests", "example"]),
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Operating System :: POSIX :: Linux",
        ],
        install_requires=["hydra-core>=1.0.0-rc1", "ax-platform[mysql]==0.1.9"],
        include_package_data=True,
    )
