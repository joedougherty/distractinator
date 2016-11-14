try:
    from setuptools import setup
except ImportError:
    from distuils.core import setup

setup(
        name="distractinator",
        version='0.1',
        description="For use with the Distractinator USB receiver.",
        author="Joe Dougherty",
        author_email="joseph.dougherty@gmail.com",
        packages=['distractinator'],
        install_requires=['pyserial>=3.1.1'],
        entry_points={
            'console_scripts': ['notify = distractinator:main'],
            }
        )

