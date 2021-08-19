from setuptools import setup

install_requires = ["transformers>=4.9.2", "sentencepiece>=0.1.96", "torch>=1.9.0"]

extras = {}
extras["dev"] = ["black>=21.4b0", "isort>=5.5.4", "flake8>=3.8.3", "pytest>=6.2.4"]

setup(
    name="mariantranslate",
    version="0.1.8",
    author="Galuh Sahid",
    author_email="galuh.sahid@protonmail.com",
    description="Simple translator using Marian NMT.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords=["translation", "translator", "translate", "language", "marian", "nmt"],
    license="MIT",
    url="https://github.com/galuhsahid/mariantranslate",
    packages=['mariantranslate'],
    python_requires=">=3.6.0",
    install_requires=install_requires,
    extras_require=extras,
)
