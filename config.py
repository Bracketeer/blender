import os

class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = 'yeah'

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False
