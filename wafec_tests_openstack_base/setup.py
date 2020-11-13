from setuptools import setup, find_packages

setup(
    name="wafec-tests-openstack-base",
    version="0.1.1",
    author="Wallace",
    author_email="wallacefcardoso@gmail.com",
    packages=find_packages("src"),
    namespace_packages=['wafec_tests_openstack_base'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    entry_points={
        'console_scripts': [

        ]
    }
)
