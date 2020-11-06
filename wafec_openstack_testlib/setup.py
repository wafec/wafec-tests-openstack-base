from setuptools import setup, find_packages

setup(
    name="wafec.openstack.testlib",
    version="0.0.7",
    author="Wallace",
    author_email="wallacefcardoso@gmail.com",
    packages=find_packages("src"),
    namespace_packages=['wafec.openstack.testlib'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[

    ],
    entry_points={
        'console_scripts': [

        ]
    }
)
