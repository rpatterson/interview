from setuptools import setup, find_packages

version = '0.1'

setup(name='verkada-assignment-camera',
      version=version,
      description="The camera simulation in the Verkada coding assignment.",
      long_description="""\
""",
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords='python verkada',
      author='Ross Patterson',
      author_email='me@rpatterson.net',
      url='https://github.com/rpatterson/interview',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      extras_require={'test': [
          # Testing tools
          'coverage', 'nose',

          # Useful tool for static analysis
          'flake8',

          # Debug tools
          'ipdb',
      ], },
      entry_points=dict(
          console_scripts=['verkada-camera = camera:main'],
      ),
      )
