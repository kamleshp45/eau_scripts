# eau_scripts
This repository contains the scripts for Edison Automated Upgrade. Currently, it offers the functionality to check whether the EDNAU PR with given site, environment and version contains a single file change (the changed file will be .edison_automated_upgrade) or not.

Please follow below steps to setup the script.

- Install python, if not installed already.
- Clone this repository and change the directory to repository folder.
- Run 'python -m venv env' to create a virtual environment. It will create 'env' folder inside your repository.
- Run 'source env/Scripts/activate' to activate the virtual environment.
- Run 'pip install -r requirements.txt' to install all the dependencies in your virtual environment.
- Create a new file 'github_token.txt' and add your github token there. Make sure there is no extra line at the end of file.

Now your system is ready to execute the script. Follow below commands to run the script.

- Add subscriptions in 'subscription.csv' file for which you want to run the script. The formate should be 'site,env,version'. The sample file is already present in case you want to see.
- There is an output file 'output.csv' which will store the output of the script.
- Run 'python main.py' to execute the script.
