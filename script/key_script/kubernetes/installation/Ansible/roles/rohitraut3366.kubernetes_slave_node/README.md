Role Name
=========

A brief description of the role goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

## compalsory Master Node inventory Group Name 
```
tag_Name_K8S_Master
```
For custome group name: You can change In tasks 
```
- name: Create token to join
  command: "kubeadm token create  --print-join-command"
  delegate_to: "{{ groups['tag_Name_K8S_Master'][0]  }}"
  register: join_token

```


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: rohitraut3366.Kubernetes-Worker-Node-Configuration }

License
-------

BSD

Author Information
------------------
Rohit Raut
[LinkedIn](https://www.linkedin.com/in/rohit-raut-71b8a119a/)
# Kubernetes-Worker-Node-Configuration