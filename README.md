# Libraries, modules and packages :taco:

This rpo wil explore libraries, modules and packages

### Libraries
AKA: Python standard libraries! These come out of the **box with python**
- these are maintained by python organisation
- you just need to import them, no need to install

### Modules
It's a piece of software that delivers useful functionality.
I have created some of these before, both functional and OOP.
Case in point:
- Project_Calculator (includes functions like the area of a triangle)
- OOP Calculator

### Packages and PIP
**pip** is a python packaging manager.
- This installs software and it's **dependencies**
- Some are better than the others

**Package Managers**

They exist for almost every modern language
e.g Ruby has Bundler which installs ruby gems (our version of external packages)

# Git branching and Workflows:

#### 1) Make sure your master is up to date
````
    $ git pull origin master
````

#### 2) Creating a new branch:

````buildoutcfg
    $ git checkout -b <name>
````
#### 3) Add and commit changes
````
    $ git add .
    $ git commit -m 'meaninful comment'
````

#### 4) Push your branch to the remote
````
    $ git push origin <branch>
````

#### 5) Merge branch on GitHub
Verify code, solve any conflicts and merge to master.

#### 6) Checkout to master and pull latewst version
````
    $ git checkout master
    $ git pull origin master
````

#### Moving betweem existing branches

````buildoutcfg
    $ git checkout <branch>
````

#### Temporarily store (stash) your code between gits
````
    $ git stash
````
#### Check current state of your version
````
    $ git status
````

### Important notes:

- Changes will travel with you if you don' commit them!
