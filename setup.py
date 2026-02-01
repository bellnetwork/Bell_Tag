from setuptools import setup, find_packages

setup(
    name="bell_tag",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
    ],
    python_requires=">=3.9",
    include_package_data=True,
    description="Bell Tag Analytics Python package for automatic server-side tracking.",
    author="Bell Network",
    author_email="support@bellnetwork.eu",
    url="https://belltagmanager.com",
    license="MIT",
)
