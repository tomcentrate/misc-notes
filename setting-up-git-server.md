# Setting up your own Git Server (explained)

Sometimes you'll need to setup your own git server for privately hosted material. Following along the official documentation [https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server]

## Setup a User
A git remote, such as [git@github.com:tomcentrate/misc-notes.git] can kinda be read like:
    
    scp -r ./ git@github.com:tomcentrate/misc-notes.git/

so, we need to create a user.
    
    adduser git
    passwd git
    

    

