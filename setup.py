from setuptools import setup

with open("README.md",encoding="utf-8") as fh:
  long_description = fh.read()

AUTHOR_NAME = 'Raghava'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
  name=SRC_REPO,
  version='0.0.1',
  author=AUTHOR_NAME,
  author_email='raghavadasari@gmail.com',
  description='A simple python package for movies recommendation.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://raghava44u.github.io/raghava-portfolio/',
  package=[SRC_REPO],
  python_requires=LIST_OF_REQUIREMENTS,
)