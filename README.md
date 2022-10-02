# machine_learning_project

#### Build Docker image
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker should be lowercase

To list docker images
``` 
docker images
REPOSITORY                   TAG       IMAGE ID       CREATED              SIZE
ml_project                   latest    b6a0bc27b865   About a minute ago   925MB
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 b6a0bc27b865
```

To check and stop docker container
```
docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS                    NAMES
2b5b36542b35   b6a0bc27b865   "/bin/sh -c 'gunicor…"   About a minute ago   Up About a minute   0.0.0.0:5000->5000/tcp focused_chebyshev
docker stop <container_id>
```