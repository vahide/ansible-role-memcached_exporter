import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_directories(host):
    dirs = [
        "/var/lib/memcached_exporter"
    ]
    for dir in dirs:
        d = host.file(dir)
        assert d.is_directory
        assert d.exists


def test_files(host):
    files = [
        "/etc/systemd/system/memcached_exporter.service",
        "/usr/local/bin/memcached_exporter"
    ]
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_permissions_didnt_change(host):
    dirs = [
        "/etc",
        "/root",
        "/usr",
        "/var"
    ]
    for file in dirs:
        f = host.file(file)
        assert f.exists
        assert f.is_directory
        assert f.user == "root"
        assert f.group == "root"


def test_user(host):
    assert host.group("memcached_exporter").exists
    assert "memcached_exporter" in host.user("memcached_exporter").groups
    assert host.user("memcached_exporter").shell == "/usr/sbin/nologin"
    assert host.user("memcached_exporter").home == "/"


def test_service(host):
    s = host.service("memcached_exporter")
#    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    sockets = [
        "tcp://127.0.0.1:9150"
    ]
    for socket in sockets:
        s = host.socket(socket)
        assert s.is_listening

