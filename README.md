This is End to End 7 days ML porject by Krish Naik.

URL : https://www.youtube.com/watch?v=Rv6UFGNmNZg&t=1375s

Local reference : E:\Learning\Krish_projects\mlproject_7days_projects


Python setup.py file::
https://www.geeksforgeeks.org/what-is-setup-py-in-python/


In Python, setup.py is a module used to build and distribute Python packages. It typically contains information about the package, such as its name, version, and dependencies, as well as instructions for building and installing the package. This information is used by the pip tool, which is a package manager for Python that allows users to install and manage Python packages from the command line. By running the setup.py file with the pip tool, you can build and distribute your Python package so that others can use it.

Example
Following is an example of a setup.py file for a simple Python package called my_package. 

First, create a folder named ‘my_package’ with a python file named ‘__init__.py’ inside it. This ‘__init__.py’ file will be the root of the my_package and will contain all the functions and classes in the my_package module. Now your directory structure should look something like this:
 
 folder : mypackage
 
			__init__.py
			
		  setup.py
			
from setuptools import setup
  
setup(
    name='my_package',
    version='0.1',
    description='A sample Python package',
    author='John Doe',
    author_email='jdoe@example.com',
    packages=['my_package'],
    install_requires=[
        'numpy',
        'pandas',
    ],
)

Here, the setup function is called with several arguments that provide information about the package. The name and version arguments specify the package name and version, while the description and author arguments provide a brief description of the package and the author’s name. The author_email argument specifies the author’s email address, and the packages argument indicates which packages should be included in the distribution. Finally, the install_requires argument specifies the package dependencies, which are other packages that must be installed in order for the my_package package to work properly.

To use the setup.py file in Python, you first need to have the setuptools module installed. You can do this by running the following command:

pip install setuptools	


### Video 2: Exception and logger
File: exception.py
https://docs.python.org/3/tutorial/errors.html
https://www.tutorialspoint.com/python/python_exceptions.htm#:~:text=What%20is%20Exception%3F,object%20that%20represents%20an%20error.

Example
This example tries to open a file where you do not have write permission, so it raises an exception −

# Code
#!/usr/bin/python

try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print "Error: can\'t find file or read data"
else:
   print "Written content in the file successfully"
This produces the following result −

# Error: can't find file or read data


		  