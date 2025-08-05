# -*- coding: utf-8 -*-
from cmath import log
import shutil
import os
import traceback
from zipfile import ZipFile
from datetime import timedelta
from caches.main_cache import main_cache
from modules.kodi_utils import requests, json, notification, sleep, delete_file, rename_file, quote, logger, exists
# from modules.kodi_utils import logger

user_agent = 'Fen v1.0'

class SubDLAPI:
	def __init__(self):
		self.headers = {'User-Agent': user_agent, 'Api-Key': "kevL-JTv9idrG79Nk9YSyvAh7daNrymP"}

	def search(self, query, tmdb_id, language, results, season=None, episode=None):
		# cache_name = 'opensubtitles_%s_%s' % (tmdb_id, language)
		# if season: cache_name += '_%s_%s' % (season, episode)
		# cache = main_cache.get(cache_name)
		# logger("Main cache name: ", cache)
		# if cache: return cache
		if language == "vie": language = "vi"
		url = 'https://api.subdl.com/api/v1/subtitles?tmdb_id='+str(tmdb_id)+'&languages='+language+'&api_key=kevL-JTv9idrG79Nk9YSyvAh7daNrymP'
		if season:
			url += '&type=tv&season_number='+str(season)+'&episode_number='+str(episode)
		else:
			url += '&type=movie'
		response = self._get(url, retry=True)
		try: response = json.loads(response.text)
		except: return
		# main_cache.set(cache_name, response, expiration=timedelta(hours=24))
		logger("Ket qua search: ", str(response))
		return response['subtitles']

	def download(self, chosen_sub, filepath, temp_zip, temp_path, final_path):
		try: 
			response = requests.get('https://dl.subdl.com' + chosen_sub["url"], timeout=5000)
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
			logger("Exception: " + str(exc), "download@subdl")
			traceback.print_exc()
			return

	def _get(self, url, stream=False, retry=False):
		response = requests.get(url, headers=self.headers, stream=stream)
		logger("Ket qua lay tu " + str(url), str(response))
		if '200' in str(response): return response
		elif '429' in str(response) and retry:
			notification(32740, 3500)
			sleep(10000)
			return self._get(url, stream)
		else: return
	
	def _post(self, chosen_sub, retry=False):
		headers = {
			'Accept': 'application/json',
			'Api-Key': 'ZOqH073CohDfqGY0aPCCMLKMK702Db6D',
			'Content-Type': 'application/json',
			'User-Agent': user_agent
		}
		
		payload = json.dumps({'file_id': chosen_sub['attributes']['files'][0]['file_id']})
		response = requests.request("POST", "https://api.opensubtitles.com/api/v1/download", headers=headers, data=payload)
		logger("Ket qua tim link download: ", str(response.text))
		if '200' in str(response): return response
		elif '429' in str(response) and retry:
			notification(32740, 3500)
			sleep(10000)
			return self._post("https://api.opensubtitles.com/api/v1/download")
		else: return