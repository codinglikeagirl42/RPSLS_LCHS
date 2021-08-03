Created by Kimberly Horan @2021
Art work is from: https://www.pngaaa.com and is for personal, non commercial use only.


Flask Setup

After forking/cloning this repo, users will need to create a virtual environment, activate it, and then install Flask. Use a command line interface to navigate into the project folder, then enter the following commands.

Mac

python3 -m venv flask-env
. flask-env/bin/activate
pip3 install Flask



Windows (GitBash)

py -3 -m venv flask-env
. flask-env/Scripts/activate
pip install Flask


To be able to push to a remote git repository you will need to create a new repository, and type in the following code in your local terminal:

$ git remote set-url origin https://git-repo/new-repository.git


To verify that the changes were made: $ git remote -v