from setuptools import setup, find_packages

setup(
    name="folder_organizer",
    version="2020.0.0.2",
    keywords="folder, organize, file, extension, download",
    description="A small, simple program to be used to sort files in a specified folder by file type.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    license="Unlicense",
    author="gustavs-vagalis",
    author_email="gustavs.vagalis@gmail.com",
    url="https://github.com/gustavs-vagalis/folder-organizer",
    project_urls={
        "Source": "https://github.com/gustavs-vagalis/folder-organizer",
        "Tracker": "https://github.com/gustavs-vagalis/folder-organizer/issues"
    },
    packages=find_packages(),
    entry_points={
        "console_scripts": (
            "organize = folder_organizer.__main__:main",
        )
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: Freeware",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: System :: Filesystems"
    ],
    data_files=[("", ["LICENSE"])]
)
