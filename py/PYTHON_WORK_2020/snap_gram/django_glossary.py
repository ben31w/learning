# venv commands:

# Create a virtual environment.
venv_create_command = 'python3 -m venv /path/to/new/virtual/environment'

# Activate a virtual environment.
venv_activate_command = 'source environmentname/bin/activate'

# Deactivate a virtual environment.
venv_deactivate_command = 'deactivate'

# django commands:

# Migrate (modify) a database. When issued for the first time, it creates a 
#  database for the project to store info.
migrate = 'python manage.py migrate'

# Starts the Django development server.
runserver = 'python manage.py runserver'

# Creates the infrastructure for a new app. Specifially, it creates a folder 
#  called appname with the files models.py, admin.py, views.py, and more.
startapp = 'python manage.py startapp appname'

# Prepare a database for migration(s) after code has been modified.
makemigrations = 'python manage.py makemigrations appname'

# Create a superuser for your site.
createsuperuser = 'python manage.py createsuperuser'

terms = {
    'web framework': "a set of tools designed to help build interactice "
        "websites and web applications.",
    'website': "a group of globally accessible, interlinked webpages that have "
        "a single domain name and run on a web server. Websites consist mostly "
        "of static content, like visuals and text that end users can read but "
        "not manipulate.",
    'web application (short def.)': "an application software that is accessible "
        "via a web browser and runs on a web server.",
    'web application (long def.)': "an application software that is accessible "
        "via a web browser and runs on a web server, unlike computer-based "
        "software programs that are stored locally on the Operating System of "
        "the device. Web apps are programmed using a client-server structure. "
        "The client-side script (written in HTML, Javascript, etc.) deals with "
        "presentation of the information, while the server-side script (written "
        "in ASP, PHP, etc.) deals with storing and retrieving the info. Web "
        "apps are designed for interaction with the end user, who not just "
        "reads but manipulates the web app's data. Examples: webmail, online "
        "retail, online banking",
    'server': "a piece of computer hardware or software that provides "
        "functionality for other programs or devices, called clients. Servers "
        "can provide various functionalities, often called 'services', such as "
        "sharing data or resources among multiple clients, or performing "
        "computation for a client.",
    'spec': "short for specification, a piece of writing that describes a "
        "project. A full spec details the project goals, describes the "
        "project's functionality, and discusses its appearance and user "
        "interface.",
    'venv': "a standard Python module that provides support for creating "
        "virtual environments. To create a virtual environment inside a "
        f"directory, enter this command: '{venv_create_command}'. To activate "
        "the virtual environment, navigate to its parent directory and enter "
        f"this command: '{venv_activate_command}'. To deactivate it, enter "
        f"'{venv_deactivate_command}.' Packages installed in the virtual "
        "environment are only available while the environment is active.",
    'virtual environment': "a place on your system where you can install "
        "packages and isolate them from all other Python packages.",
    'django': "a Python-based, free, open-source web framework. In Django, "
        "every web app you want to create is called a project, and a project "
        "is a sum of applications. An application is a set of code files "
        "relying on the MVT pattern. When building a website using Django, the "
        "website is the project, and the forum, news, and contact engine are "
        "applications.",
    'localhost': "a server that only processes requests on your system.",
    'model': "the single, definitive source of information on your data that "
        "you want to store. It contains the essential fields and behaviors of "
        "the data you’re storing. Each model is a Python class that subclasses "
        "django.db.models.Model. Each attribute of the model represents a "
        "database field. Django uses all the info to automatically generate a "
        "database-access API.",
}

# Print the terms in alphabetical order.
for term, definition in sorted(terms.items()):
    print(f"{term}: {definition}\n")