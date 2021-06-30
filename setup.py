import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("version.txt", "r") as file:
    version = file.read().strip()

with open("app_name.txt", "r") as name:
    app_name = name.read().strip()


setuptools.setup(
     name='witty_flow_sms',
     version=version,
     author="Charles Opoku-Agyemang",
     author_email="micnkru@gmail.com",
     description="A Docker and AWS utility package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/charlesagyemang/first_pip_project",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
