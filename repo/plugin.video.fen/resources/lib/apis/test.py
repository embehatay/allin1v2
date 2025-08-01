import requests
import json
import urllib3.util.connection
import os
import zipfile

urllib3.util.connection.HAS_IPV6 = False

user_agent = 'Fen v1.0'

class SubsourceAPI:
	def __init__(self):
		self.__api = "https://api.subsource.net/v1"
		self.__search = self.__api + "/movie/search"
		self.__getSub = self.__api + "/subtitle/"
		self.__download = self.__getSub + "download/"

	def search(self, query, tmdb_id, language, year, season=None, episode=None):
		# cache_name = 'opensubtitles_%s_%s' % (tmdb_id, language)
		# if season: cache_name += '_%s_%s' % (season, episode)
		# cache = main_cache.get(cache_name)
		# logger("Main cache name: ", cache)
		# if cache: return cache
		if language == "vie": language = "vi"
		tmdb = 'tmdb_id'
		if season: type = 'tvseries'
		else: type = 'movie'
		headers = {
			'content-type': 'application/json',
		}
		payload = json.dumps({"query": query + " " + str(year), "includeSeasons": False})
		try: 
			response = requests.request("POST", self.__search, headers=headers, data=payload)
			# response = requests.request("POST", self.__search, data=payload)
			response = json.loads(response.text)
			search_result = None
			for result in response['results']:
				if result['type'] == type and result['releaseYear'] == year:
					search_result = result
			self.searchSubtitles(search_result, language)
		except Exception: 
			print("Exception: " + str(Exception))
			return
		# main_cache.set(cache_name, response, expiration=timedelta(hours=24))
		print("Ket qua search: ", str(response))
		# return response['data']

	def searchSubtitles(self, result, language):
		response = requests.get(self.__api + str(result['link']), params={"language": language})
		print(response.text)

	def download_zip_from_url(self, url, filename):
		"""
		Downloads a ZIP file from a given URL and saves it to a specified filename.

		Args:
			url (str): The URL of the ZIP file to download.
			filename (str): The local path and filename to save the downloaded ZIP file.
		"""
		try:
			# Send a GET request to the URL, enabling streaming for potentially large files
			response = requests.get(url, stream=True)
			response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

			# Open the local file in binary write mode
			with open(filename, 'wb') as file:
				# Iterate over the response content in chunks to handle large files efficiently
				for chunk in response.iter_content(chunk_size=8192):
					file.write(chunk)
			print(f"ZIP file '{filename}' downloaded successfully from '{url}'")

		except requests.exceptions.RequestException as e:
			print(f"Error downloading the file: {e}")
		except IOError as e:
			print(f"Error writing the file to disk: {e}")

zip_url = "https://api.subsource.net/v1/subtitle/download/e38f2628610f0d02628386b6ab6375bc919be92f0a483727f7e8b49c16ae0f19"  # Replace with your actual ZIP file URL
output_filename = "downloaded_archive.zip"
extraction_path = '.'
try:
	# Open the zip file in read mode ('r')
	zipSubName = None
	with zipfile.ZipFile(output_filename, 'r') as zip_ref:
		zipSubName = zip_ref.namelist()[0]

	# zip_ref.extract('test.srt', extraction_path)
	print(f"Successfully extracted '{output_filename}' to '{extraction_path}'.")
except FileNotFoundError:
	print(f"Error: The file '{output_filename}' was not found.")
except zipfile.BadZipFile:
	print(f"Error: '{output_filename}' is not a valid ZIP file or is corrupted.")
except Exception as e:
	print(f"An unexpected error occurred: {e}")
# subsource = SubsourceAPI()
# subsource.search("superman", 12345, "vietnamese", 2025)
# subsource.download_zip_from_url(zip_url, output_filename)
# subsource.searchSubtitles({"link": "/subtitles/superman-2025"}, 'vietnamese')
