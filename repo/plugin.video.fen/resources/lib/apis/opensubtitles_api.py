# -*- coding: utf-8 -*-
from cmath import log
import shutil
from zipfile import ZipFile
from datetime import timedelta
from caches.main_cache import main_cache
from modules.kodi_utils import requests, json, notification, sleep, delete_file, rename_file, quote, logger, exists
# from modules.kodi_utils import logger

user_agent = 'Fen v1.0'

class OpenSubtitlesAPI:
	def __init__(self):
		self.headers = {'User-Agent': user_agent, 'Api-Key': "ZOqH073CohDfqGY0aPCCMLKMK702Db6D"}

	def search(self, query, tmdb_id, language, season=None, episode=None):
		# cache_name = 'opensubtitles_%s_%s' % (tmdb_id, language)
		# if season: cache_name += '_%s_%s' % (season, episode)
		# cache = main_cache.get(cache_name)
		# logger("Main cache name: ", cache)
		# if cache: return cache
		if language == "vie": language = "vi"
		tmdb = 'tmdb_id'
		if season: tmdb = 'parent_tmdb_id'
		url = 'https://api.opensubtitles.com/api/v1/subtitles?' + tmdb + '=%s&query=%s%s&languages=%s' \
				% (tmdb_id, quote(query), '&season_number=%d&episode_number=%d' % (season, episode) if season else '', language)
		response = self._get(url, retry=True)
		try: response = json.loads(response.text)
		except: return
		# main_cache.set(cache_name, response, expiration=timedelta(hours=24))
		logger("Ket qua search: ", str(response))
		return response['data']

	def download(self, chosen_sub, filepath, temp_zip, temp_path, final_path):
		try: 
			result = json.loads(self._post(chosen_sub, retry=True).text)
			download_url = result["link"]
		except: return
		result = self._get(download_url, stream=True, retry=True)
		with open(temp_zip, 'wb') as f: f.write(result.content)
		if exists(final_path): delete_file(final_path)
		rename_file(temp_zip, final_path)
		return final_path

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