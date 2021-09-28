import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="instagram-magic",
    version="0.0.12",
    author="olsoncarsen",
    author_email="gashilovdmitry@yandex.ru",
    description="If you want to learn some tricks, you are welcome",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/olsoncarsen/instagram-magic",
    project_urls={
        "Bug Tracker": "https://github.com/olsoncarsen/instagram-magic/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
		extras_require={
				'testing': [
						"pytest",
				],
    },
    packages=['instagram_magic'],
    python_requires=">=3.8",
)
