import spotifyScraper
scraper = spotifyScraper.spotifyScrape()

#running command
scraper.getAlbumTracks(ID='6400dnyeDyD2mIFHfkwHXN')

#esier access
response = scraper.response

#example: getting all the tracks
response_json = response.json()

       
print(f'Getting Tracks\n')
        
for i in response_json['items']:
    print(i['name']+ '       ' + i['uri'])
