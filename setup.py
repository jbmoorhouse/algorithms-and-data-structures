from setuptools import setup, find_packages

def setup_package():
    setup(
        name="pyads",
        version="0.1",
        packages=find_packages(),
    )

if __name__ == "__main__":
    setup_package()