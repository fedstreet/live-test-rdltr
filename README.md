# Setting up the rdltr application

**WARNING:** The installation steps have been tested with Python 3.9.7. Some dependencies may fail to install for 3.10.

1. Clone the fork of the *rdltr* repository:

       git clone https://github.com/olleont52/rdltr

2. Create a new Python virtual environment where the application will be installed. Activate it. For example:

       python -m venv venv-rdltr
       In Linux: source venv-rdltr/bin/activate
       In Windows: venv-rdltr\Scripts\activate.bat

3. While still inside the virtual environment, change to the folder with the *rdltr* repository
   and install the application from source:

       cd rdltr
       pip install -e .

4. Set necessary environment variables:

     - In Linux:
     
           export RDLTR_DB_URL=sqlite:///(full-path-to-a-DB-file)
           # For example: export RDLTR_DB_URL=sqlite:////home/user/projects/rdltr/rdltr.db
           export RDLTR_SECRET_KEY=MyArbitrarySecretKey

     - In Windows:
     
           set RDLTR_DB_URL=sqlite:///(full-path-to-a-DB-file)
           :: For example: set RDLTR_DB_URL=sqlite:///C:\home\projects\rdltr\rdltr.db
           set RDLTR_SECRET_KEY=MyArbitrarySecretKey

5. Initialize the database:

       rdltr_db

6. Start the application:

       rdltr

7. Verify that it works:

     - Open <http://localhost:5000> in browser.
       (5000 is the default port, and it may be changed by defining the environment variable RDLTR_PORT.)
     - Try registering a new user to be sure that it works. For some combinations of package versions
       it happened that the application started OK, but a new user could not be registered.

8. If you have problems installing particular Python package dependencies, it may be because the package version
   is not currently available on [PyPI](https://pypi.org/) for the installed version of Python. You may try to install
   a package manually via *pip*, or use a supported version of Python, or modify package versions in the **setup.cfg**
   of the *rdltr* repository (chances that they will work correctly).

9. For resolving problems with starting up the application, you may visit the original documentation site:
   <https://samr1.github.io/rdltr/index.html>.

# Setting up the learning project

There are two options. One is creating a project step-by-step based on video lessons.
The other is loading an example project from GitHub. Below are the steps for the second option.

1. Clone the fork of the **live-test-rdltr** repository. (It is this repository. If you already cloned it,
   you don't need to do it twice.)

     > git clone https://github.com/olleont52/live-test-rdltr

2. Create a virtual environment for the testing project. For instance, if you open it in PyCharm,
   the IDE will offer you to create a new environment.

3. In the virtual environment, you need to install dependencies from the requirements.txt
   (if it's not automatically done by the IDE):

       pip install -r requirements.txt

4. There are many options to actually run the tests. You may use *pytest* from command line,
   use the tools in IDE or just follow the video lessons.
