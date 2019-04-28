#!/usr/bin/python

import os
import ansible_runner

private_dir = '/tmp/demo'
if not os.path.exists(private_dir):
    os.makedirs(private_dir)

result = ansible_runner.run(
            private_data_dir=private_dir,
            inventory=['localhost'],
            playbook='/home/vagrant/work/test/playbooks/test.yml')
print result.status
