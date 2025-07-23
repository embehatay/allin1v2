import xbmc
import json

def checkReponse(response):
    result = False
    if ( ('result' in response) and ('error' not in response) ):
        result = True
    return result

def JSexecute(request):
    request_string = json.dumps(request)
    response = xbmc.executeJSONRPC(request_string)
    if ( response ):
        response = json.loads(response)
    return response

# Performs single JSON query and returns result boolean, data dictionary and error string
def JSquery(request):
    result = False
    data = {}
    error = ''
    if ( request ):
        response = JSexecute(request)
        if ( response ):
            result = checkReponse(response)
            if ( result ):
                data = response['result']
            else: error = response['error']
    return (result, data, error)
path = 'https://sgp1-4.download.real-debrid.com/d/W5UJDCJMRZBL290/The.X-Files.S02E06.Ascension.1080p.BluRay.REMUX.AVC.DTS-HD.MA.5.1-NOGRP.mkv'
print(path.rsplit('/', 1)[-1].rsplit('.', 1)[0])
# print(('Last played subtile folder: ' + str(JSquery({"jsonrpc": "2.0", "method": "Settings.GetSettingValue", "params": { "setting": ["subtitles.custompath"], "playerid": 0 }, "id": 0}))))