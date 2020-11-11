from pathlib import Path
from setuptools import setup, find_packages

DESCRIPTION = ("Flask-RESTx API for accessing Tor relay/process")
APP_ROOT = Path(__file__).parent
README = (APP_ROOT / "README.md").read_text()
AUTHOR = "Nvor"
PROJECT_URLS = {
    "Source Code": "https://github.com/Nvor/Tor-Relay-API"
}
INSTALL_REQUIRES = [
    "Flask",
    #"Flask-Bcrypt",
    #"Flask-Cors",
    #"Flask-Migrate",
    "flask-restx",
    "Flask-SQLAlchemy",
    "PyJWT",
    #"python-dateutil",
    "python-dotenv",
    "requests",
    "urllib3",
    "werkzeug==0.16.1",
]

setup(
    name="Tor-Relay-API",
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    version="0.1",
    author=AUTHOR,
    maintainer=AUTHOR,
    license="GPL",
    url="https://github.com/Nvor/Tor-Relay-API",
    project_urls=PROJECT_URLS,
    packages=find_packages(where="app"),
    package_dir={"": "app"},
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
)