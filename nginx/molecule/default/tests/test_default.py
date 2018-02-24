import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nginx_is_installed(host):
    # Given
    nginx = host.package('nginx')
    # Then
    assert nginx.is_installed


def test_nginx_is_running(host):
    # Given
    nginx = host.service('nginx')
    # Then
    assert nginx.is_running
