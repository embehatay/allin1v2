import requests

def save_srt_from_url(url, output_filename):
    """
    Downloads an SRT file from a given URL and saves it locally.

    Args:
        url (str): The URL of the SRT file.
        output_filename (str): The name of the file to save the SRT content to.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        with open(output_filename, 'wb') as f:
            f.write(response.content)
        print(f"SRT file successfully downloaded and saved as '{output_filename}'")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading the SRT file: {e}")
    except IOError as e:
        print(f"Error saving the SRT file: {e}")

# Example usage:
srt_url = "https://www.opensubtitles.com/download/30B5D6CC826419BEF88CA0903C06166A34758F9F947AB7DC02076CDD314D5F80683386DB0A5D070785F7FF07CDEC0C0C2F4A0481343BEC8299D32C615EA0855D6625CDC2AD8D40AFEA74EFBEAFD899F9F59353EE549C5AC9987DAFC29B148753CB594C342D85858E8C88C00E14D5B601CFEFACECB59EDB4BBA1FF9C36C99C21C781E9A1F35F8A02F0FAAD8BCACBBB1AD7625295E58C2D4A715BC5120FF4D33A06E949E80A94F32E454A069F7CC0ED2CE9ECC6E9CF0903B34324B52058AD6B2A84980540F51758F685ED8B977E0FE01D719897A71E0A5FA182D3B1E95FAEDFC5644B549123B70631CDBADA6CE24107B74C4A940D27E9E3DD983262B6A42451D21728A46AE33667EEC02C4355A2CD9D1820FA4B064D1B3FFA81ACE906A3D6B116AD51CA8FAF3BAA279B9B11C150DA5BF6897A7AB1A265DD49E6E8A174C59AD4DD6C02F0394B6E38BFF90DE3B3BBDD036890FD0DF36A58EEE91/subfile/The.Big.Bang.Theory.S01E03.Fuzzyboots.Corollary.mHD%20BluRay%20DD%205.1%20x264-Anonymous.srt"  # Replace with the actual URL
output_file = "downloaded_subtitle.srt"
save_srt_from_url(srt_url, output_file)