# config_store

This Ansible Network role is designed to store contents of network devices in GIT.
This role is network platform agnostic.

## Requirements

* Ansible 2.5 or later
* Ansible Network Engine Role 2.6.2 or later

## Functions

This section provides a list of the available functions that are including in this role.
Any of the provided functions can be implemented in Ansible playbooks to perform content oriented activities on network devices.

* `config` to store content of running/active configuration ( Details: [source](https://github.com/ansible-network/config_store/blob/devel/tasks/config.yaml), [docs](https://github.com/ansible-network/config_store/blob/devel/docs/tasks/config.md)).
* `yang` to store content of yang specs (Details:  [source](https://github.com/ansible-network/config_store/blob/devel/tasks/yang_spec.yaml), [docs](https://github.com/ansible-network/config_store/blob/devel/docs/tasks/yang.md))
* `facts` store device facts (aka parsed content). (future)
* `command` store command output (aka raw content). (future)

## Variables

The following are the list of variables for each of the role functions.

* `config`: [spec](https://github.com/ansible-network/yang/blob/devel/meta/config_spec.yaml)
* `yang`: [spec](https://github.com/ansible-network/yang/blob/devel/meta/yang_spec.yaml)

## Example

Use timestamps as branches and merge content into master:

```
- name: "Network Configuration Snapshot"
  hosts: network
  gather_facts: yes
  connection: network_cli

  tasks:
    - name: "ansible-network.config_store"
      include_role:
        name: ansible-network.config_store
        tasks_from: config
      vars:
        config_store_version: "{{ hostvars[ansible_play_hosts[0]].ansible_date_time.iso8601_basic }}"


- name: "Network Yang Specs Snapshot"
  hosts: network:&yang
  gather_facts: yes
  connection: netconf

  tasks:
    - name: "ansible-network.config_store"
      include_role:
        name: ansible-network.config_store
        tasks_from: yang
        vars:
          config_store_version: "{{ hostvars[ansible_play_hosts[0]].ansible_date_time.iso8601_basic }}"

```

## License

GPLv3

## Author Information

Ansible Network Community (ansible-network)
