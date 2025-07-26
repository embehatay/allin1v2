import re
from urllib.parse import unquote

print(str(" https://sgp1-4.download.real-debrid.com/d/BCZSMWWJEN3MK45/The.Last.of.Us.S02E03.The.Path.2160p.MAX.WEB-DL.DDP5.1.Atmos.DV.HDR.H.265-G66.mkv".rsplit("/", 1)[1].rsplit(".", 1)))

"The.Last.of.Us.S02E03.The.Path.2160p.MAX.WEB-DL.DDP5.1.Atmos.DV.HDR.H.265-G66.vie.srt"
"The.Last.of.Us.S02E03.The.Path.2160p.MAX.WEB-DL.DDP5.1.Atmos.DV.HDR.H.265-G66.vi.srt"
print(unquote("The.Last.Of.Us.S02E04.2160p.MAX.WEB-DL.DV.HDR%5BBen%20The%20Men%5D.srt"))
# Replace 'your_file.pkl' with the actual path to your PKL file
# file_path = 'C:/Users/Admin/Downloads/Programs/last_played/plugin.video.last_played/repo/a4kSubtitles-master/a4kSubtitles/lib/third_party/iso639/data/iso-639_langs.pkl'
# try:
#     with open(file_path, 'rb') as file:
#         data = pickle.load(file)
#     print(data) # This will print the loaded Python object
# except Exception as e:
#     print(f"Error loading pickle file: {e}")
results = [{'service_name': 'opensubtitles', 'service': 'OpenSubtitles', 'lang': 'Vietnamese', 'name': 'E03', 'rating': 0, 'lang_code': 'vi', 'sync': 'false', 'impaired': 'true', 'color': 'springgreen', 'action_args': {'url': 9634308, 'lang': 'Vietnamese', 'filename': 'E03', 'gzip': True}}, {'service_name': 'opensubtitles', 'service': 'OpenSubtitles', 'lang': 'Vietnamese', 'name': 'E03', 'rating': 0, 'lang_code': 'vi', 'sync': 'false', 'impaired': 'false', 'color': 'springgreen', 'action_args': {'url': 9634301, 'lang': 'Vietnamese', 'filename': 'E03', 'gzip': True}}, {'service_name': 'opensubtitles', 'service': 'OpenSubtitles', 'lang': 'Vietnamese', 'name': 'The.Big.Bang.Theory.S01E03.Fuzzyboots.Corollary.mHD BluRay DD 5.1 x264-Anonymous', 'rating': 0, 'lang_code': 'vi', 'sync': 'false', 'impaired': 'false', 'color': 'springgreen', 'action_args': {'url': 9634294, 'lang': 'Vietnamese', 'filename': 'The.Big.Bang.Theory.S01E03.Fuzzyboots.Corollary.mHD BluRay DD 5.1 x264-Anonymous', 'gzip': True}}, {'service_name': 'opensubtitles', 'service': 'OpenSubtitles', 'lang': 'Vietnamese', 'name': 'The.Big.Bang.Theory.1x03.The.Fuzzy.Boots.Corollary.720p.HDTV.x264.AC3-CTU', 'rating': 0, 'lang_code': 'vi', 'sync': 'false', 'impaired': 'true', 'color': 'springgreen', 'action_args': {'url': 9634284, 'lang': 'Vietnamese', 'filename': 'The.Big.Bang.Theory.1x03.The.Fuzzy.Boots.Corollary.720p.HDTV.x264.AC3-CTU', 'gzip': True}}, {'service_name': 'opensubtitles', 'service': 'OpenSubtitles', 'lang': 'Vietnamese', 'name': 'E03', 'rating': 0, 'lang_code': 'vi', 'sync': 'false', 'impaired': 'true', 'color': 'springgreen', 'action_args': {'url': 8805070, 'lang': 'Vietnamese', 'filename': 'E03', 'gzip': True}}, {'service_name': 'opensubtitles', 'service': 'OpenSubtitles', 'lang': 'Vietnamese', 'name': 'E03', 'rating': 0, 'lang_code': 'vi', 'sync': 'false', 'impaired': 'true', 'color': 'springgreen', 'action_args': {'url': 9634309, 'lang': 'Vietnamese', 'filename': 'E03', 'gzip': True}}, {'service_name': 'opensubtitles', 'service': 'OpenSubtitles', 'lang': 'Vietnamese', 'name': 'E03', 'rating': 0, 'lang_code': 'vi', 'sync': 'false', 'impaired': 'true', 'color': 'springgreen', 'action_args': {'url': 9634307, 'lang': 'Vietnamese', 'filename': 'E03', 'gzip': True}}, {'service_name': 'opensubtitles', 'service': 'OpenSubtitles', 'lang': 'Vietnamese', 'name': 'E03', 'rating': 0, 'lang_code': 'vi', 'sync': 'false', 'impaired': 'true', 'color': 'springgreen', 'action_args': {'url': 9634306, 'lang': 'Vietnamese', 'filename': 'E03', 'gzip': True}}, {'service_name': 'opensubtitles', 'service': 'OpenSubtitles', 'lang': 'Vietnamese', 'name': 'E03', 'rating': 0, 'lang_code': 'vi', 'sync': 'false', 'impaired': 'false', 'color': 'springgreen', 'action_args': {'url': 9634312, 'lang': 'Vietnamese', 'filename': 'E03', 'gzip': True}}, {'service_name': 'opensubtitles', 'service': 'OpenSubtitles', 'lang': 'Vietnamese', 'name': 'E03', 'rating': 0, 'lang_code': 'vi', 'sync': 'false', 'impaired': 'false', 'color': 'springgreen', 'action_args': {'url': 9634280, 'lang': 'Vietnamese', 'filename': 'E03', 'gzip': True}}, {'service_name': 'opensubtitles', 'service': 'OpenSubtitles', 'lang': 'Vietnamese', 'name': 'E03', 'rating': 0, 'lang_code': 'vi', 'sync': 'false', 'impaired': 'false', 'color': 'springgreen', 'action_args': {'url': 9634311, 'lang': 'Vietnamese', 'filename': 'E03', 'gzip': True}}, {'service_name': 'opensubtitles', 'service': 'OpenSubtitles', 'lang': 'Vietnamese', 'name': 'E03', 'rating': 0, 'lang_code': 'vi', 'sync': 'false', 'impaired': 'false', 'color': 'springgreen', 'action_args': {'url': 9634303, 'lang': 'Vietnamese', 'filename': 'E03', 'gzip': True}}]
score = 0
best_match_sub = results[0]
for result in results:
    current_score = 0
    if re.search('720p', result["name"], re.IGNORECASE): current_score += 1
    if re.search('1080p', result["name"], re.IGNORECASE): current_score += 2
    if re.search('2160p', result["name"], re.IGNORECASE): current_score += 3
    if re.search('bluray', result["name"], re.IGNORECASE): current_score += 4
    print(result['name'] + " score: " + str(current_score))
    if current_score > score: 
        score = current_score
        best_match_sub = result

print("Best match: " + str(best_match_sub))