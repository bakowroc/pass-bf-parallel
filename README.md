### Installation
#### Enter the project directory
`cd /path/to/project`

#### Install pipenv

`pip3 install pipenv` or `pip install pipenv` (depends on system settings)

#### Install packages
`pipenv install`

#### Setup docker environment
##### Install docker and docker-compose
###### (Linux only supported here unfortunately)
[https://docs.docker.com/install/linux/docker-ce/ubuntu/](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

##### Run slaves containers
`cd /path/to/project/docker`

`docker-compose up -d`

##### Run the client program
Go back to the root of the project:

`cd /path/to/project`

And run:

`pipenv run python ./src/main.py <password_to_guess> <number_of_hosts>`

- *password_to_guess* is a password you want to guess

- *number_of_hosts* is a number of parallel hosts


For instance:

`pipenv run python ./src/main.py admin 4`

will start process which would try to guess *admin* password in 4 parallel hosts.
