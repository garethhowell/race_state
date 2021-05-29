from setuptools import setup, find_packages

setup(name="race_state", packages=find_packages())

extras_require={
    "test": ["coverage", "mypy", "pycodestyle", "pytest", "pytest-cov",
    "pytest-mock", "pytest-asyncio"]
}