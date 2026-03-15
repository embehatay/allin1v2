# -*- coding: utf-8 -*-
from cmath import log
import os
import shutil
from zipfile import ZipFile
from datetime import timedelta
from caches.main_cache import main_cache
from modules.kodi_utils import requests, json, notification, sleep, delete_file, rename_file, quote, logger, exists
import modules.meta_lists
from modules.kodi_utils import logger
import traceback
import re

user_agent = 'Fen v1.0'

class SubsourceAPI:
	def __init__(self):
		self.__api = "https://api.subsource.net/api/v1"
		self.__search = self.__api + "/movies/search"
		self.__getSub = self.__api + "/subtitles/"
		self.headers = {
			'X-API-Key': 'sk_66822bc74602f40016a03263b24bf6c9b3a67eb35439cb3ca30ff1773d164631'
		}
		self.movieId = None
		self.episode = None

	def search(self, imdb_id, season=None, episode=None):
		self.episode = int(episode)
		payload = {"searchType": "imdb", "season": season, "imdb": imdb_id}
		try: 
			response = requests.request("GET", self.__search, headers=self.headers, params=payload, timeout=5000)
			logger("Ket qua search sub source: ", str(response))
			self.movieId = response.json()["data"][0]["movieId"]
			return self.searchSubtitles()
		except Exception as exc: 
			logger("Exception: " + str(exc), "search@subsource")
			traceback.print_exc()
			return

	def searchSubtitles(self):
		try:
			payload2 = {'movieId': self.movieId, 'language': 'vietnamese'}
			response = requests.request("GET", self.__getSub, headers=self.headers, params=payload2)
			logger("Danh sach sub source: ", response.text)
			choosenSub = response.json()["data"][0]
			score = int(choosenSub["rating"]["good"]) - int(choosenSub["rating"]["bad"]) + int(choosenSub["downloads"])
			for subtitle in response.json()["data"]:
				currentScore = int(subtitle["rating"]["good"]) - int(subtitle["rating"]["bad"]) + int(subtitle["downloads"])
				if currentScore > score:
					score = currentScore
					choosenSub = subtitle
			return [choosenSub]
		except Exception as exc:
			logger("Exception: " + str(exc), "searchSubtitles@subsource")
			traceback.print_exc()
			return
	
	def download(self, chosen_sub, filepath, temp_zip, temp_path, final_path):
		try: 
			response = requests.get(self.__getSub + str(chosen_sub['subtitleId']) + '/download', headers=self.headers, timeout=5000)
			response.raise_for_status()
			with open(temp_zip, 'wb') as file:
				# Iterate over the response content in chunks to handle large files efficiently
				for chunk in response.iter_content(chunk_size=8192):
					file.write(chunk)
			logger(f"ZIP file '{temp_zip}' downloaded successfully", "hihi")
			if exists(final_path): delete_file(final_path)
			zipSubName = None
			with ZipFile(temp_zip, 'r') as zip_ref:
				zipSubName = zip_ref.namelist()[self.episode - 1]
				zip_ref.extract(zipSubName, filepath)
			logger(f"Successfully extracted '{temp_zip}' to '{filepath}'.", str(zipSubName))
			if exists(temp_zip): delete_file(temp_zip)
			rename_file(os.path.join(filepath, zipSubName), final_path)
			return final_path
		except Exception as exc: 
			logger("Exception: " + str(exc), "download@subsource")
			traceback.print_exc()
			return