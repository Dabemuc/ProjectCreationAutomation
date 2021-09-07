### About this project:
```
This Project was heavily inspired by Kalle Hallden's project: 
https://github.com/KalleHallden/ProjectInitializationAutomation

My attempt on automating the creation of a new coding project includes the following steps:
    - Creating a new project file at the desired location, while sorting the projects by used language
      (Currently, the program is set up to sort the projects into five subfolders called Java, 
      JavaScript, Python, ReactNative, FLutter, Microcontroller)
    - Creating git repository, pushing first commit and adding a readme.md file
    - launching VS Code

Happy Coding!
```

### How to install: 
```bash
Step 1 - Type the following commands into cmd (You need to have git and python installed!):
    git clone "https://github.com/Dabemuc/ProjectCreationAutomation.git"
    cd projectCreationAutomation
    pip install -r requirements.txt

Step 2 - Adjust parameters
    Change the following variables inside create.py:
        path = "Directory where projects will be created and sorted by language"
        token = "GitHub Personal access Token"
        
    You may have to manually type or copy in your GitHub Personal Access Token during the first 
    creation of a project!

    If you want to add languages, you have to add the directories and another block like this one fitting your needs:
        if sys.argv[2] == "j":
        os.mkdir(path + "/Java/" + foldername)
        os.chdir(path + "/Java/" + foldername)


Step 3 - Add "projectCreationAutomation" - folder to PATH so the Program can be executed inside the cmd
```


### How to use:
```bash
To run the program, open cmd and type:
    'create [project_name] [project_language (j, js, py, fl, rn, mc)]'

Example:
    'create MyProject py'
```