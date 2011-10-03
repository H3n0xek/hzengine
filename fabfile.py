# -*- coding: utf-8 -*-
from fabric.operations import local
from fabric.colors import red, green, white
from hzdeploy.utils import Repository
from hzdeploy.repositories import all as all_repos
import os

PROJECT_DIR = os.path.split(os.path.realpath(__file__))[0]

def updatedb():
	"""Обновление базы: синхронизация и выполнение миграций"""
	# TODO: реализовать бэкап базы
	local('cd %s && python manage.py syncdb' % PROJECT_DIR) 
	local('cd %s && python manage.py migrate' % PROJECT_DIR)


def install():
	"""Первоначальная установка движка

	Загрузка всех репозиториев приложений и создание симлинков,
	затем инициализируется БД и запускаются миграции"""

	def fetch_all_repos(repo_list):
		for repo in repo_list:
			repo.fetch()
	
	def install_all_repos(repo_list):
		for repo in repo_list:
			repo.install()
	
	fetch_all_repos(all_repos)
	install_all_repos(all_repos)
	updatedb()


def update(self):
	"""Обновление уже установленного движка

	Обновление каждого репозитория и миграция БД"""
	
	def update_all_repos(repo_list)	:
		for repo in repo_list:
			repo.update()

	update_all_repos(all_repos)
	updatedb()
		
