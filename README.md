[![Build Status](https://travis-ci.org/bihealth/ansible-role-python3.svg?branch=master)](https://travis-ci.org/bihealth/ansible-role-python3)

# Python 3

Cross-platform Python 3 setup.
Will use `deadsnakes` PPA for Ubuntu and IUS for CentOS.
Note that Python availability greatly depends on these repositories.
For Debian 9, Python 3 will be built from source.

## Requirements

none

## Role Variables

See `defaults/main.yml` for all role variables and their documentation.

## Dependencies

none

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: bihealth.python3
```

## License

MIT

## Author Information

- Manuel Holtgrewe

Created with love at [Core Unit Bioinformatics (CUBI), Berlin Institute of Health (BIH)](https://www.cubi.bihealth.org).
