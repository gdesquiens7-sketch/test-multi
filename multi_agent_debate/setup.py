"""
Setup script for Multi-Agent Debate System
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="multi-agent-debate",
    version="1.0.0",
    author="Multi-Agent Debate System",
    description="Système collaboratif de débat multi-agent pour validation de cahiers des charges",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/votre-repo/multi-agent-debate",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "multi-agent-debate=debate_crew:main",
        ],
    },
    include_package_data=True,
)
