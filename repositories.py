from utils import Repository, MERCURIAL, GIT
import os

PROJECT_DIR = os.path.split(os.path.realpath(__file__))[0]
REPO_DIR = os.path.join(PROJECT_DIR, '.repos')

class django_diario(Repository):
    app_list = [ 'diario' ]
    vcs = MERCURIAL
    vcs_url = 'http://bitbucket.org/semente/django-diario'
    repodir = os.path.join(REPO_DIR, 'django-diario')


class diario_extras(Repository):
    app_list = [ 'diario_extviews', 'diario_moderation' ]
    vcs = GIT
    vcs_url = 'http://github.com/H3n0xek/diario-extras'
    repodir = os.path.join(REPO_DIR, 'diario-extras')


class django_registration(Repository):
    app_list = [ 'registration' ]
    vcs = MERCURIAL
    vcs_url = 'http://bitbucket.org/ubernostrum/django-registration'
    repodir = os.path.join(REPO_DIR, 'django-registration')


class django_vlfa(Repository):
    app_list = [ 'vlfa_base', 'vlfa_edit', 'vlfa_moderation' ]
    vcs = GIT
    vcs_url = 'http://github.com/H3n0xek/django-vlfa'
    repodir = os.path.join(REPO_DIR, 'django-vlfa')


repos = [ django_diario, diario_extras, django_registration, django_vlfa ]

all = [ repo() for repo in repos ]

