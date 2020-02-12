# User Color Webpage
This is a web based CRUD application that allows users to be added with their favorite color. When looking up a user in the database, the background will change correlating with their favorite color.

## Getting Started

There are multiple ways to run this application. They will be listed below in the following order: Ansible, Docker-Compose, Docker.

### Prerequisites
* [docker](https://docs.docker.com/)
* [docker-compose](https://docs.docker.com/compose/install/)
* [ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html?extIdCarryOver=true&sc_cid=701f2000001OH7YAAW)

### Ansible

Ansible is the quickest and easiest way to get this application running. Ansible must be installed in order for this to work.

From the playbooks directory
If Docker is installed run
```bash
ansible-playbook playbook_local_usercolor.yml
```

If Docker is not installed run
```bash
ansible-playbook playbook_local_docker_usercolor.yml
```
These commands will run the application locally. If you wish to run on different hosts other than local, please update you inventory.

[Ansible Inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html)

Run this command once your host inventory has been updated. (note: make sure to change hosts within playbook to match the inventory ip addresses you want)
```bash
ansible-playbook playbook_node_usercolor.yml
```

### Docker-Compose

If Docker and Docker-Compose are installed, then just clone the repo and run
```bash
docker-compose up
```
### Docker

If Docker is installed, begin by building the image
```bash
docker build -t app_image .
```
This will build an image called 'app_image' in from your Dockerfile in your current directory.
To run the image that was built use
```bash
docker run -p 5000:5000 app_image
```
