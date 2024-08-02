from setuptools import setup, find_packages
import os

version = '1.1.0'

setup(name='RobotVisualComparison',
      version=version,
      description="Visual regression library and report generator for robot framework",
      long_description="""\
Visual regression library and report generator for robot framework. Capture elements, fullscreens and compare them against beta and prod. Visit https://vie.git.bwinparty.com/Charan.Ravula/RobotVisualcomparison for documentation.""",
      classifiers=[
        'Framework :: Robot Framework',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
      ],
      keywords='visual-regression image-comparison robotframework ',
      author='Charan Kumar Ravula',
      author_email='ravulacharankumar@outlook.com',
      url='https://vie.git.bwinparty.com/Charan.Ravula/RobotVisualcomparison',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      package_data={'': ['*.exe']},
      install_requires=[
          'pillow',
          'robotframework',
          'flask'
      ],
      entry_points={
          'console_scripts': [
              'reportgen = RobotVisualComparison.reportgen:report_gen',
              'rcsetup = RobotVisualComparison.rcsetup:rcsetup'
          ]
      },
)
