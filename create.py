import sys
import os
import re
from github import Github

foldername = str(sys.argv[1])
path = "Directory where projects will be created and sorted by language"
token = "GitHub Personal acces Token"

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
        os.mkdir(path + "/Java/" + foldername)
        os.chdir(path + "/Java/" + foldername)

    elif sys.argv[2] == "js":
        os.mkdir(path + "/JavaScript/" + foldername)
        os.chdir(path + "/JavaScript/" + foldername)

    elif sys.argv[2] == "py":
        os.mkdir(path + "/Python/" + foldername)
        os.chdir(path + "/Python/" + foldername)

    elif sys.argv[2] == "rn":
        os.mkdir(path + "/ReactNative/" + foldername)
        os.chdir(path + "/ReactNative/" + foldername)

    elif sys.argv[2] == "fl":
        os.mkdir(path + "/Flutter/" + foldername)
        os.chdir(path + "/Flutter/" + foldername)
        pjname = re.sub("[^0-9a-zA-Z]+", "", foldername.lower())
        os.system(f'flutter create --project-name {pjname} .')

    else:
        print(f'Please specify Project language! ("create <ProjectName> <ProjectLanguage (j, js, py, rn, fl)>")')

    for c in commands:
            os.system(c)

    print(f'Project {foldername} created locally')
    os.chdir(path)
    os.system('code .')

else:
    print(f'Please specify Project language! ("create <ProjectName> <ProjectLanguage (j, js, py)>")')