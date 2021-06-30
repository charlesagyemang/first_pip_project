import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='finneynie',
     version='0.1',
     scripts=['finneynie'] ,
     author="Charles Opoku-Agyemang",
     author_email="micnkru@gmail.com",
     description="A Docker and AWS utility package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/KehillahGhanaLimited/gold-api",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
