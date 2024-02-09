import os
import platform

import pkg_resources
from setuptools import find_packages, setup

setup(
    name="reazonspeechx",
    py_modules=["reazonspeechx"],
    version="3.1.1",
    description="Time-Accurate Automatic Speech Recognition using ReazonSpeech.",
    readme="README.md",
    python_requires=">=3.8",
    author="Max Bain, Tasuku SUENAGA a.k.a. gunyarakun",
    url="https://github.com/gunyarakun/reazonspeechx",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ]
    + [f"pyannote.audio==3.1.1"],
    entry_points={
        "console_scripts": ["reazonspeechx=reazonspeechx.transcribe:cli"],
    },
    include_package_data=True,
    extras_require={"dev": ["pytest"]},
)
