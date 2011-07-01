from fabric.api import run, env, cd, sudo


def production():
    env.hosts = ['yourhost.com']
    env.repo = ('/srv/yourproject/', 'origin', 'master')


def git_pull(hash=None):
    """Updates or resets the repository"""
    repo, parent, branch = env.repo
    if hash is None:
        hash = '%s/%s' % (parent, branch)
    with cd(repo):
        run('git fetch')
        run('git reset --hard %s' % hash)


def buildout():
    repo, parent, branch = env.repo
    with cd(repo):
        run('./bin/buildout')


def deploy(hash=None):
    repo, parent, branch = env.repo
    git_pull(hash)
    buildout()
    with cd(repo):
        run('./bin/django syncdb')
    restart_supervisor()


def reset(hash):
    deploy(hash)


def restart_nginx():
    sudo('/etc/init.d/nginx restart')


def restart_supervisor():
    sudo('supervisorctl restart all')
