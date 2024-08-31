import setuptools


__version__ = "0.0.0"

REPO_NAME = "MLOps_Foundation"
AUTHOR_USER_NAME = "Asutosh"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "ashutoshsidhya69@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Mlpos foundation project",
    long_description_content="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)