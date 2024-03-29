[![Build Status](https://travis-ci.com/KasidisGit/riddle-me-this.svg?branch=master)](https://travis-ci.com/KasidisGit/riddle-me-this)
[![codecov](https://codecov.io/gh/KasidisGit/riddle-me-this/branch/master/graph/badge.svg)](https://codecov.io/gh/KasidisGit/riddle-me-this)
# Riddle Me This

It is an online educational game that tests knowledge and creativity of a player. The questions will come in the form of pictures. The player has to turn those pictures into only a single word. Each word is illustrated by pictures. This game application is designed as a mixture of guess the word games and pictures trivia quiz to improve the player creativity but still fun and rewarding. The more level is increased, the more complicated pictures will be. To solve tricky quizzes, You need to think outside the box. We will collect score of each player and put it in scoreboard showing top 10 players with their highest score.

## Team members

| Name | Github ID |
|-----|------------|
| Tiranan Emson | [TirananE](https://github.com/TirananE) |
| Booyanuch Kaewrakrob | [noeybynk](https://github.com/noeybynk) |
| Sukrita Kittipitayakorn | [SukritaEarn](https://github.com/SukritaEarn) |
| Kasidis Luangwutiwong | [KasidisGit](https://github.com/KasidisGit) |

## Project Documents

* [Project Proposal](https://docs.google.com/document/d/17h1Ol01eRqQ6tj3vDWJW9umjiuNYy6Nby9mrc0ZfD0Y/edit#)
* [Iteration Plan](https://docs.google.com/document/d/1HG85SXgtpRnwHKSpw-7xCFtjdfBGe11zce4vNnasJK4/edit#)
* [Iteration Script](https://docs.google.com/document/d/1eBriBu04WbI6myoH9GuHBDf7wkmMbYwD7kY3xDfpSIA/edit)
* [Task Board](https://trello.com/b/y8vxcJPa/riddle-me-this)
* [Code Review](https://docs.google.com/document/d/1QnH53fsqkTB0lhTCFExOkOOEtXv0lpKw0SpMnZ8ifWo/edit)

## Requirements

The application requires python add-on modules as in [requirements.txt](requirements.txt)

## Installation Steps

Step 1: Clone the repository

        git clone https://github.com/KasidisGit/riddle-me-this

Step 2: Change directory to riddle-me-this

        cd /some/directory/riddle-me-this

Step 3: Install virtualenv

        python -m pip install virtualenv

Step 4: Create a virtualenv directory named env inside the project directory

        virtualenv env

Step 5: Activate the virtualenv using the activate script. Use the “.” command or “source” command.

        .env/bin/activate

or:

        source env/bin/activate

When virtualenv is activated it prepends `(env)` to your shell prompt so you know it is active.

Step 6: Install requirements from requirements.txt

        (env)cmd> pip install -r requirements.txt

Step 7: Create database tables

        (env)cmd> python manage.py migrate

Step 8: Load data from `.json` files

        (env)cmd> python manage.py loaddata */fixtures/*.json

Step 9: Runserver

        (env)cmd> python3 manage.py runserver --insecure

Step 10: Exit the virtualenv using deactivate. You can also exit by closing the shell window.

        (env)cmd> deactivate

