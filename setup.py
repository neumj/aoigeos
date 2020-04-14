from setuptools import setup, find_packages

reqs = [
    "bokeh",
    "numpy",
    "pandas",
    "scikit-learn"
]

conda_reqs = [
    "bokeh",
    "numpy",
    "pandas",
    "scikit-learn"
]

test_pkgs = []

setup(
    name="aoigeos",
    python_requires='>3.4',
    description="Python package for generating aois",
    url="https://github.com/neumj/aoigeos",
    install_requires=reqs,
    conda_install_requires=conda_reqs,
    test_requires=test_pkgs,
    packages=find_packages(),
    include_package_data=True
)

