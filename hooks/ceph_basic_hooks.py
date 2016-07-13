import ceph

from charmhelpers.core.hookenv import (
    log,
    DEBUG,
    config,
    relation_ids,
    related_units,
    relation_get,
    relation_set,
    leader_set, leader_get,
    is_leader,
    remote_unit,
    Hooks, UnregisteredHookError,
    service_name,
    relations_of_type,
    status_set,
    local_unit, ERROR)

hooks = Hooks()


@hooks.hook('install.real')
@harden()
def install():
    execd_preinstall()
    add_source(config('source'), config('key'))
    apt_update(fatal=True)
    apt_install(packages=ceph.PACKAGES, fatal=True)


if __name__ == '__main__':
    try:
        hooks.execute(sys.argv)
    except UnregisteredHookError as e:
        log('Unknown hook {} - skipping.'.format(e))