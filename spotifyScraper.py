import requests
import spotifyToken
import json
import pycountry

accessAuth = spotifyToken.spotifyPy()

class spotifyScrape:
    def __init__(self):
        self.accessToken = 'bruh'
    
    def getToken(self):
        accessAuth.requestAccess()
        self.accessToken = accessAuth.accessTokenData['access_token']
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.accessToken}'
        }
        
    def checkValidToken(self):
        url = 'https://api.spotify.com/v1/albums/6400dnyeDyD2mIFHfkwHXN'
        
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.accessToken}'
        }
        
        request = requests.get(url, headers=headers)
        if request.status_code in range(400,402):
            self.getToken()            
        
    
    def getAlbum(self, ID):
        self.checkValidToken()
        
        url = f'https://api.spotify.com/v1/albums/{ID}'

        self.response = requests.get(url, headers=self.headers)    
        
        
    def getAlbumTracks(self, ID):
        self.checkValidToken()
        url = f'https://api.spotify.com/v1/albums/{ID}/tracks'
        
        self.response = requests.get(url, headers=self.headers)


    def searchFilter(self, query, option, limit, offset):
        search_header = {}
        
        tempStr = ''
        for i in query:
            if i == ' ':
                tempStr += '+'
            else:
                tempStr += i
        search_header['q'] = f'{tempStr}'
        search_header['type'] = f'{option}'
        
        if limit != '':
            search_header['limit'] = f'{limit}'
        if offset != '':
            search_header['offset'] = f'{offset}'
        

        self.search(search_header)


    def search(self, header):
        self.checkValidToken()

        url = 'https://api.spotify.com/v1/search'
        for i in header:
            if i == 'q':
                url += f'?q=f{header[i]}'
            else:
                url += f'&{i}={header[i]}'
        
        self.response = requests.get(url, headers=self.headers)
        

    def run(self):
        
        #self.getToken()
        #self.getAlbum('6nVACH6a27eOWiumAJhDWS')
        #self.getAlbumTracks('6nVACH6a27eOWiumAJhDWS')
        #self.searchFilter('crystal dolphin', 'track', '1', '')
        pass

if __name__ == '__main__':
    spotifyScrape = spotifyScrape()
    spotifyScrape.run()
