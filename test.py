import pickle

# Replace 'your_file.pkl' with the actual path to your PKL file
file_path = 'C:/Users/Admin/Downloads/Programs/last_played/plugin.video.last_played/repo/a4kSubtitles-master/a4kSubtitles/lib/third_party/iso639/data/iso-639_langs.pkl'
try:
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    print(data) # This will print the loaded Python object
except Exception as e:
    print(f"Error loading pickle file: {e}")