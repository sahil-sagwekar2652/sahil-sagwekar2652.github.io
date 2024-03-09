Title: How to solve "failed to mount: no such device" error with the docker daemon
Date: 2023-12-28 20:24
Author: Sahil Sagwekar
Category: devops
Slug: how-to-solve-failed-to-mount-no-such-device-error-with-the-docker-daemon

Solution {#heading-solution}
========

**The solution to this problem could be as simple as rebooting your system.**

The problem is caused mostly when the kernel updates itself during a system update. In my case, I was on Arch Linux when I ran the command `sudo pacman -Syu` to start a system update.

Upon completing the update, an error came up on my screen when I tried to run `docker` .

I used the following command to check the docker daemon logs - (Only works for systemd-based distros)
```bash
sudo journalctl -xeu docker.service
```
This was the **output** -

![alt](https://cdn.hashnode.com/res/hashnode/image/upload/v1703598770959/abade4a3-c9dc-419d-b89b-b2289e59949c.png){.image--center .mx-auto}

The first error message says - `msg="failed to mount overlay: no such device" storage-driver=overlay2`

Let us try to understand what `overlay` is and what are Layers in the context of Docker containers.

Docker Layers {#heading-docker-layers}
=============

Containers were meant to be a better and more efficient alternative to VMs, the preferred solution for running applications in isolation. Individual VMs do not share any resources between them. Each VM has its own full-fledged operating system which creates its own file system. Even two VMs of the same operating system share nothing with each other. While this kind of setup also has its use cases, it's a waste of resources in our context. Containers solve this problem by sharing resources.

What is an image? It's a collection of filesystem layers and metadata. These layers are together run by Docker as a container. Containers are a running instance of an image. We can run multiple containers of the same image.

Docker implements a **copy-on-write** mechanism. Multiple containers share the same base system of the base image. The base directory of the image is read-only and all the changes are recorded in a different directory which is then layered on top of the base directory. The Overlay driver is used by Docker to implement it's layered file system. Layers can be shared across multiple running containers.

![alt](https://cdn.hashnode.com/res/hashnode/image/upload/v1703792704561/f1a4cdf8-1f5d-4fba-a2e0-26403830724f.png){.image--center .mx-auto}

#### References : {#heading-references}

Learn more about docker layers

-   <https://jvns.ca/blog/2019/11/18/how-containers-work--overlayfs/>

-   <https://www.petermcconnell.com/posts/docker-overlayfs/>

-   <https://youtu.be/FCk5ylLjnxw>
