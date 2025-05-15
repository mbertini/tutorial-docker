### Install NVIDIA Container Toolkit

Follow the instructions at https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

Run these commands on the Linux host to install the NVIDIA Container Toolkit, which allows Docker to utilize the GPU.

```bash

sudo apt-get install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

check the /etc/docker/daemon.json file to ensure that the default runtime is set to nvidia:

```json
{
  ...
  "runtimes": {
    "nvidia": {
      "path": "nvidia-container-runtime",
      "runtimeArgs": []
    }
  }
}
```

You may need to add the runtimes section to your ~/.docker/daemon.json file if it doesn't exist. If you do, make sure to restart the Docker daemon after making changes.

Test that Docker can use NVIDIA GPU:
```bash

docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

it should print the list of available GPUs and their status.


### Building the image

```bash 

docker build -t 7_cuda .
```

### Running the container

```bash

docker run --gpus all -p 8899:5000 7_cuda
```

As soon as the app starts it will download the ResNet model. Once finished it will work.