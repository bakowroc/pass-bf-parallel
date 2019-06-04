### Installation
#### Install pipenv

`pip3 install pipenv` or `pip install pipenv` (depends on system settings)


#### Install packages
`pipenv install`

#### Setup docker environment
##### Install docker 
###### (Linux only supported here unfortunately)
[https://docs.docker.com/install/linux/docker-ce/ubuntu/](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

##### Create image
`pipenv run python ./src/setup.py`

##### Run node
`docker run --net=host -it dispy`

##### Run the program
`pipenv run python ./src/main.py <password_to_guess>`

Be careful though, the number of possibilities is like ~```40^len(password_to_guess)```
