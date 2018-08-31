# Saving content into content store

The `config` function provides a means to save configuration content onto a
target store.  The `config` function consumes existing `git_datastore`.
The device's configuration to be stored in GIT repository and merged in upstream
master branch, allowing the comparison (diff) of any content in the store.

The `ansible_network_provider` is used to gather configuration content from devices.

## How to save and merge content in the content store

Saving a configuration from a target device is fairly simple and straightforward.
The `config` function will gather the active configuration running on the target
device and store the content as file in the defined datastore.

Below is an example of how to call the `config` function.

```
- hosts: network_devices
  tasks:
    - name: ansible-network.content_store
      include_role:
        name: ansible-network.content_store
        tasks_from: config
      vars:
        config_store_scm_url: "git@github.com:myuser/network_content_store.git"
        config_store_scm_private_key_file: "~/.ssh/id_rsa"

```

The example playbook above will :

1- Add SSH credentials for `config_store_scm_url` (requires read-write permissions).

2- Clone `config_store_scm_url`, checkout `config_store_remote_branch` and creates branch `config_store_version` based on existing content of `config_store_remote_branch`.

3- Gather device's configuration (requires `ansible_network_provider`) and store at `<hostname>/config/running.cfg` of `config_store_version`.

4- Merge pushed content of `config_store_version` branch into `config_store_remote_branch`.

## Function Parameters (Specs)

For additional details about variables supported by this role and theirs respective default values [config_spec](https://github.com/ansible-network.config_store/blob/devel/meta/config_spec.yaml)

## Notes
None
