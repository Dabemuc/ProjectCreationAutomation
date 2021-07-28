import sys
import os
from github import Github

foldername = str(sys.argv[1])
path = "Directory where projects will be created and sorted by language"
token = "GitHub Personal acces Token"
_dirj = path + "/Java/"
_dirjs = path + "/JavaScript/"
_dirpy = path + "/Python/"

g = Github(token)
user = g.get_user()
login = user.login
repo = user.create_repo(foldername)

commands = [f'echo "# {repo.name}" >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{foldername}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

if len(sys.argv) == 3:
    if sys.argv[2] == "j":
        os.mkdir(_dirj + foldername)
        os.chdir(_dirj + foldername)

        for c in commands:
            os.system(c)

        print(f'Java project {foldername} created locally')
        os.chdir(path)
        os.system('code .')

    elif sys.argv[2] == "js":
        os.mkdir(_dirjs + foldername)
        os.chdir(_dirjs + foldername)

        for c in commands:
            os.system(c)

        print(f'JavaScript project {foldername} created locally')
        os.chdir(path)
        os.system('code .')

    elif sys.argv[2] == "py":
        os.mkdir(_dirpy + foldername)
        os.chdir(_dirpy + foldername)

        for c in commands:
            os.system(c)

        print(f'Python project {foldername} created locally')
        os.chdir(path)
        os.system('code .')

    else:
        print(f'Please specify Project language! ("create <ProjectName> <ProjectLanguage (j, js, py)>")')

else:
    print(f'Please specify Project language! ("create <ProjectName> <ProjectLanguage (j, js, py)>")')