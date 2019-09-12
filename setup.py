from setuptools import setup

setup(name='example',
      entry_points={'intake.drivers':
          ['exmaple-data-source = example:ExampleDataSource']},
      py_modules=['example'])
