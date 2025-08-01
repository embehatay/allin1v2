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
		self.__api = "https://api.subsource.net/v1"
		self.__search = self.__api + "/movie/search"
		self.__getSub = self.__api + "/subtitle/"
		self.__download = self.__getSub + "download/"
		self.headers = {
			'content-type': 'application/json'
		}

	def search(self, query, tmdb_id, language, year, results, season=None, episode=None):
		if season: type = 'tvseries'
		else: type = 'movie'
		if language == "vie": language = "vi"
		for item in modules.meta_lists.meta_languages:
			if language == item["iso"]: language = item["name"].lower()
		payload = json.dumps({"query": query + " " + str(year), "includeSeasons": True if season else False})
		logger("Tham so de so sanh: " + type, year)
		try: 
			response = requests.request("POST", self.__search, headers=self.headers, data=payload, timeout=5000)
			logger("Ket qua search sub source: ", str(response))
			response = json.loads(response.text)
			search_result = None
			for result in response['results']:
				if result['type'] == type and str(result['releaseYear']) == str(year) and re.search(query, result['title'], re.IGNORECASE):
					search_result = result
					break
			return self.searchSubtitles(search_result, language)
		except Exception as exc: 
			logger("Exception: " + str(exc), "search@subsource")
			traceback.print_exc()
			return

	def searchSubtitles(self, result, language):
		try:
			logger("Language cua sub phim: " + str(language), "searchSubtitles@subsource")
			response = requests.get(self.__api + str(result['link']), params={"language": language}, timeout=5000)
			logger("Danh sach sub source: ", response.text)
			return json.loads(response.text)["subtitles"]
		except Exception as exc: 
			logger("Exception: " + str(exc), "searchSubtitles@subsource")
			traceback.print_exc()
			return
	
	def download(self, chosen_sub, filepath, temp_zip, temp_path, final_path):
		try: 
			response = requests.get(self.__getSub + chosen_sub["link"], timeout=5000)
			download_token = json.loads(response.text)["subtitle"]["download_token"]
			logger(f"Download token '{download_token}'", "hihi")
			response = requests.get(self.__download + download_token, stream=True, timeout=5000)
			response.raise_for_status()
			with open(temp_zip, 'wb') as file:
				# Iterate over the response content in chunks to handle large files efficiently
				for chunk in response.iter_content(chunk_size=8192):
					file.write(chunk)
			logger(f"ZIP file '{temp_zip}' downloaded successfully", "hihi")
			if exists(final_path): delete_file(final_path)
			zipSubName = None
			with ZipFile(temp_zip, 'r') as zip_ref:
				zipSubName = zip_ref.namelist()[0]
				zip_ref.extractall(filepath)
			logger(f"Successfully extracted '{temp_zip}' to '{filepath}'.", str(zipSubName))
			if exists(temp_zip): delete_file(temp_zip)
			rename_file(os.path.join(filepath, zipSubName), final_path)
			return final_path
		except Exception as exc: 
			logger("Exception: " + str(exc), "download@subsource")
			traceback.print_exc()
			return