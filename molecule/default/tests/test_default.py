import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_executables(host):
    for version in ("3.5", "3.6"):  # "3.7" N/A for centos7
        assert (
            host.file("/usr/bin/python%s" % version).exists
            or host.file("/usr/local/bin/python%s" % version).exists
        )
        assert (
            host.file("/usr/bin/pip%s" % version).exists
            or host.file("/usr/local/bin/pip%s" % version).exists
        )
