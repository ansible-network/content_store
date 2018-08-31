#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
import os

from ansible.module_utils.basic import AnsibleModule


def main():
    """ main entry point for module execution
    """
    argument_spec = dict(
        repo=dict(type='path', required=True),
        remote=dict(default='origin'),
        branch=dict(default='master'),
        state=dict(default='present')
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    repo = module.params['repo']
    remote = module.params['remote']
    branch = module.params['branch']
    state = module.params['state']

    result = {'changed': False}

    if not os.path.exists(repo):
        module.fail_json(msg='repo %s does not exist' % repo)
    os.chdir(repo)

    rc, out, err = module.run_command('git checkout %s' % (branch))

    if rc > 0 and state == 'present':
        if not module.check_mode:
            module.run_command('git checkout -b %s %s' % (branch, remote))
        result['changed'] = True

    if rc == 0 and state == 'absent':
        if not module.check_mode:
            module.run_command('git checkout -d %s' % (branch))
        result['changed'] = True

    module.exit_json(**result)

if __name__ == '__main__':
    main()
