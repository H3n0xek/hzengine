# -*- coding: utf-8 -*-
from fabric.operations import local
import os

GIT = 1 
MERCURIAL = 2

PROJECT_DIR = os.path.split(os.path.realpath(__file__))[0]

class Repository:
    """Базовый класс для обслуживания одного репозитория"""
    app_list = list() # Список имен приложений
    vcs = None # VCS
    vcs_url = None # URL репозитория
    repodir = None # директория репозитория    

    def fetch(self):
        if self.vcs == GIT:
            local('git clone %s %s' % (self.vcs_url, self.repodir))
        elif self.vcs == MERCURIAL:
            local('hg clone %s %s' %  (self.vcs_url, self.repodir))
        else:
            raise ValueError, \
                  'Invalid vcs: %d (%s)' % (self.vcs, self.vcs_url)

    def install(self):
        for app in self.app_list:
            # make a symlink in a project dir
            local('cd %s && ln -s %s %s' % (
                       self.repodir,
                       os.path.join(self.repodir, app),
                       os.path.join(PROJECT_DIR, app)))
    
    def update(self):
        if self.vcs == GIT:
            local('cd %s && git pull' % self.repodir)
        elif self.vcs == MERCURIAL:
            local('cd %s && hg pull' % self.repodir)
        else:
            raise ValueError, \
                  'Invalid vcs: %d (%s)' % (self.vcs, self.vcs_url)


