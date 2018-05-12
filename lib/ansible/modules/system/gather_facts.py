#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'core'}


DOCUMENTATION = '''
---
module: gather_facts
version_added: 2.6
short_description: Gathers facts about remote hosts
description:
     - This module takes care of executing the configured facts modules, the default is to use the M(setup) module.
     - This module is automatically called by playbooks to gather useful variables about remote hosts that can be used in playbooks.
     - It can also be executed directly by C(/usr/bin/ansible) to check what variables are available to a host.
     - Ansible provides many I(facts) about the system, automatically.
notes:
    - This module is mostly a wrapper around other fact gathering modules.
    - Options passed to this module must be supported by all the underlying fact modules configured.
author:
    - "Ansible Core Team"
'''

RETURN = """
# depends on the fact module called
"""

EXAMPLES = """
# Display facts from all hosts and store them indexed by I(hostname) at C(/tmp/facts).
# ansible all -m gather_facts --tree /tmp/facts
"""
