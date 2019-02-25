from cleo import Command
import os


class PackageCommand(Command):
    """
    Creates a new package, Run this command out of your masonite project

    package
        {name : Name of your Masonite project}
        {--c|commands: make package with command}
        {--h|helpers: make package with command}
        {--p|providers: make package with command}
    """
    
    def handle(self):
        """
        MANIFEST.in
        setup.py
        requirements.txt
        .gitignore
        {name}/
            __init__.py
            commands/ #  optional
                __init__.py
            helpers/ #  optional
                __init__.py
            providers/ #  optional
                __init__.py
            integration.py
            
        tests/
            __init__.py
            test_{name}.py
        
        
        """
        name = self.argument("name")
        
        if not os.path.exists(name):
            os.makedirs(os.path.join(name, name))
        
        # create ./setup.py
        setup = open(os.path.join(os.getcwd(), name, "setup.py"), "w+")
        setup.write("from setuptools import setup\n\n")
        setup.write("setup(\n    ")
        setup.write('name="{0}",\n    '.format(name))
        setup.write("version='0.0.1',\n    ")
        setup.write("packages=['{0}'],\n    ".format(name))
        setup.write("install_requires=[\n        ")
        setup.write("'masonite',\n    ")
        setup.write("],\n    ")
        setup.write("include_package_data=True,\n")
        setup.write(")\n")
        setup.close()
        # create tests/__init__.py

        # create ./setup.py
        manifest = open(os.path.join(os.getcwd(), name, "MANIFEST.in"), "w+")
        manifest.close()
        # create ./setup.py
        requirements = open(os.path.join(os.getcwd(), name, "requirements.txt"), "w+")
        requirements.close()
        # create ./setup.py

        gitignore = open(os.path.join(os.getcwd(), name, ".gitignore"), "w+")
        gitignore.close()
        # create ./setup.py
        init_file = open(
            os.path.join(os.getcwd(), name, "{0}/{1}".format(name, "__init__.py")), "w+"
            )
        init_file.close()
        # create ./setup.py
        integration_file = open(
            os.path.join(os.getcwd(), name, "{0}/{1}".format(name, "integration.py")),
            "w+",
            )
        integration_file.write("import os\n\n")
        integration_file.write(
            "package_directory = os.path.dirname(os.path.realpath(__file__))\n\n"
            )
        integration_file.close()
        self.info("Package Created Successfully!")
