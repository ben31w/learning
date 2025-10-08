"""
A glossary for terms and commands relating to Git, a popular, distributed 
version control software.

THE BASICS:
Git helps people manage their work on a project. When you implement a new 
feature in a project, Git tracks the changes you make to each file. When your 
new code works, you commit the changes you've made, and Git records the new 
state of your project. If you make a mistake and want to revert your changes, 
you can easily return to any previously working state. Projects are stored in
repositories, which contain everything associated with the project: its code, 
information on its collaborators, any issues or bug reports, etc.
"""
terms = {
    'version control': "software that allows you to create 'snapshots' or "
        "'save states' of a project whenever it's in a working state. If you "
        "make changes to a project, version control allows you revert back to "
        "a previous working state if the current state isn't functioning well. "
        "Git is the most popular version control software.",
    'repository': "a set of files in a program that Git is actively tracking. ",
    'branch': "a version of the project you're working on.",
    'commit': "a snapshot of the project at a particular point in time.",
    'project log': "a history of a project's commits.",
    'tracked': "a file that has been previously staged or committed.",
    'untracked': "a file that has NOT been staged or committed.",
    'ignored': "a file that Git has been explicitly told to ignore. Usually "
        "consists of build artifacts and machine generated files, such as "
        "compiled code (.o, .class, .pyc) and files generated at runtime "
        "(.log, .lock, .tmp). They are tracked in a special file called "
        "'.gitignore'.",
}

git_commands = {
    'git config --global user.name': "returns the username Git uses to track "
        "who's working on the project. To change the current username, enter "
        "the command followed by a space, followed by the new username.",
    'git config --global user.email': "returns the email address Git uses to "
        "track who's working on the project. To change the current email "
        "address, enter the command followed by a space, followed by the new "
        "email address. Although Git requires a username and email address, "
        "the email address does not need to be real.",
    'git init': "initializes an empty repository in the current directory. "
        "This will create a hidden .git directory, which Git uses to manage "
        "the repository's files (you don't need to do anything with this "
        "directory).",
    'git status': "returns the status of the project being worked on. It "
        "displays the project's branch, a message stating whether any project "
        "files were modified since the last commit, and any untracked files "
        "(i.e., files inside the directory but not the repository).",
    'git add .': "adds all untracked files within a project/directory to the "
        "repository. This does NOT commit them.",
    'git commit': "on its own, it creates a commit if there aren't any "
        "already. Otherwise, it returns the project's status.",
    'git commit -m "message"': "same as git commit, but the -m flag allows you "
        "to record a message in the project's log.",
    'git commit -a': "adds all modified files to the current commit.",
    'git commit -am "message"': "adds all modified files to the current commit "
        "and records a message in the project's log.",
    'git commit --amend -m "new message"': "edits the message of the most "
        "recent commit.",
    'git log': "returns the project's log, which tracks all the commits made "
        "along with the author, date, message, and unique 40-character "
        "reference ID of each commit.",
    'git log --pretty=oneline': "returns a more streamlined version of the log "
        "that only provides the two most important parts of each commit: the "
        "reference ID and the message.",
    'git checkout .': "abandons any changes made since the last commit and "
        "restores the project to the last committed state.",
    'git checkout ': "allows you to check out any previous commit if you enter "
        "the first six characters of the commit's reference ID following the "
        "command. When you check out a previous commit, you leave the master "
        "branch and enter the detached HEAD state (detached means you are not "
        "currently in a named branch). To return to the master branch, enter "
        "the command followed by the word master.",
    'git reset --hard ': "allows you to revert to a previous commit "
        "permanently if you enter the first six characters of the commit's "
        "reference ID following the command. To do this, you need to be "
        "working from the master branch, so verify using git status.",
    'rmdir /s.git': "deletes the .git directory, resetting the project's "
        "repository. In MacOS and Linux, use the command 'rm -rf .git'. You "
        "can also just delete the .git directory from File Explorer.",
}

# Print the terms in alphabetical order.
print("-------------------terms-------------------\n")
for term, definition in sorted(terms.items()):
    print(f"{term}: {definition}\n")

# Print the git commands in alphabetical order.
print("-------------------git commands-------------------\n")
for command, description in sorted(git_commands.items()):
    print(f"{command}: {description}\n")