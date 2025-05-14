# Install NVIDIA Container Toolkit

Run these commands on the Linux host to install the NVIDIA Container Toolkit, which allows Docker to utilize the GPU.

```bash


sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```