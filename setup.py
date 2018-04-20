from setuptools import setup, find_packages

version = '0.1'

setup(name='interview',
      version=version,
      description="Common scaffolding for Python interview excercises",
      long_description="""\
""",
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords='python interviews code-tests',
      author='Ross Patterson',
      author_email='me@rpatterson.net',
      url='https://github.com/rpatterson/interview',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # Web framework
          'Flask',
      ],
      extras_require={'test': [
          # Testing tools
          'coverage', 'nose',

          # Useful tool for static analysis
          'flake8',

          # Debug tools
          'ipdb',
      ], },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
