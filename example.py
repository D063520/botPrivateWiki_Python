# coding=utf-8
import os
import csv
import pywikibot
from SPARQLWrapper import SPARQLWrapper, JSON
from pywikibot import config2
from datetime import datetime
import requests

from IdSparql import IdSparql

family = 'my'
mylang = 'my'
familyfile=os.path.relpath("./config/my_family.py")
if not os.path.isfile(familyfile):
  print ("family file %s is missing" % (familyfile))
config2.register_family_file(family, familyfile)
config2.password_file = "user-password.py"
config2.usernames['my']['my'] = 'myUser'

#connect to the wikibase
wikibase = pywikibot.Site("my", "my")
wikibase_repo = wikibase.data_repository()

wikibase_item = pywikibot.ItemPage(wikibase_repo)
data = {}
data['labels'] = {"en": "Hello World"}
data['descriptions'] = {"en": "This is an example"}
wikibase_item.editEntity(data, comment="This is my change")

