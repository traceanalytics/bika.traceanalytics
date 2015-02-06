from setuptools import setup, find_packages

version = '0.1'

setup(name='bika.traceanalytics',
      version=version,
      description='Bika LIMS Trace Analytics',
      long_description=open('README.md').read(),
      classifiers=[
          'Framework :: Plone',
          'Programming Language :: Python',
      ],
      keywords='Bika Open Source LIMS',
      author='Naralabs',
      author_email='info@naralabs.com',
      url='www.naralabs.com',
      license='',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['bika'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'bika.lims',
          'archetypes.schemaextender',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              'robotsuite',
              'robotframework-selenium2library',
              'plone.app.robotframework'
          ]
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
