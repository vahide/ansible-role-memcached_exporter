
# Description

memcached Exporter deployment made easy with Ansible.
For installing memcached use [prometheus memcached_exporter](https://github.com/prometheus/memcached_exporter)

## Role Variables
All variables which can be overridden are stored in defaults/main.yml file.


## Example
# Playbook
```
---
- name: memcached Exporter Install
  hosts: memcached
  user: root
  roles:
    - ansible-role-memcached-exporter
  tags:
    - prometheus_memcached_exporter
```

## License

Apache License 2.0, see [LICENSE](https://github.com/vahide/ansible-role-memcached_exporter/blob/main/LICENSE).
