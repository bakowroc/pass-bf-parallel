import dispy
import os

dockerfile_path = os.path.join(os.path.dirname(dispy.__file__), 'data')

if len(dockerfile_path) > 0:
    command = f'''
    mkdir /tmp/dispy-docker
    cd /tmp/dispy-docker
    cp {dockerfile_path}/Dockerfile .
    docker build -t dispy .
    '''
    try:
        os.system(command)
    except OSError as err:
        print(err)
