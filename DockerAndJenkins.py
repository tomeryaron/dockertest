
import docker
client = docker.from_env()
print(client.images.list())


# Create Build from DockerFile
path_to_dockerfile = '/Users/tomeryaron/Downloads/techworld-js-docker-demo-app-master/'
client.images.build(path=path_to_dockerfile, tag='imagefrompythonjenkins:1.0')
print(client.images.list())

import os
listimagescom = "docker images | grep my-app | awk '{print$1}'"
os.system(listimagescom)



