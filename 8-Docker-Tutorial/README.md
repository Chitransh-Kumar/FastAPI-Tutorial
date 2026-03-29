# Docker:

- It is a platform designed to help developers build, share and run container applications.

---

## Why do we need Docker?

1. Consistency across environments - Applications behave differently in development, testing and production environments due to variation in configuration.

2. Isolation - Running multiple websites on the same host can create conflicts. Docker provides isolated environments for each application. Virtual machines can also be used for this work, but it can become very heavy.

3. Scalability - Scaling applications to handle increased load can be challenging.

---

## Docker Engine:

- It is the core component of the Docker platform, responsible for creating, running and managing Docker containers.

- Components of Docker Engine:

1. Docker Daemon: It is the background service running on the host machine. It manages docker objects such as containers, images, networks and volumes.

2. Docker CLI: It is the tool that users interact with to communicate with the Docker daemon.

3. REST API: It allows communication between Docker CLI and Docker daemon.

---

## Docker Image:

- It is a lightweight, stand-alone and executable software package that includes everything you need to run a software program, such as the code, the environment variables, runtime, libraries and configuration files.

- Components of Docker Image: Base Image, Application code, Dependencies, Metadata.

- Docker Image Lifecycle: Creation, Storage, Distribution, Execution.

---

## Dockerfile:

- It is a text file that contains a series of instructions used to build a Docker image. Each instruction in the Dockerfile creates a layer in the image, allowing for efficient image creation and reuse of layers.

---

## Docker Container:

- It is a lighweight, portable and isolated environment that encapsulates an application and its dependencies, allowing it to run consistently across different environments.

---

## Registry:

- It is a service that stores and distributes docker images. It acts as a repository where users can push, pull and manages Docker images.

- Components of Docker Registry: Repositories, Tags.

- Types of Docker Registry: Docker Hub, Private Registries, Third-party registries.

- Benefits: Centralized Image Registry, Version Control, Collaboration, Security.

