import requests
import spotifyToken

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
        print(self.accessToken)
        
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
            
    def defaultSearch(self, url):
        self.checkValidToken()
        self.response = requests.get(url, headers=self.headers) 
        
    def searchFilter(self, **kwargs):
        self.url_appender = '?'
        print(kwargs)
        
        for i in kwargs:
            if self.url_appender == '?':
                self.url_appender += f'{i}={kwargs[i]}'
            else:
                self.url_appender += f'&{i}={kwargs[i]}'
    
    def getAlbum(self, ID, **kwargs):   
        self.searchFilter(**kwargs)
        url = f'https://api.spotify.com/v1/albums/{ID}'+self.url_appender
        self.defaultSearch(url)   
        
    def getAlbumTracks(self, ID, **kwargs):
        self.searchFilter(**kwargs)
        url = f'https://api.spotify.com/v1/albums/{ID}/tracks'+self.url_appender
        self.defaultSearch(url)
                
    def search(self, **kwargs):
        self.searchFilter(**kwargs)
        self.checkValidToken()

        url = 'https://api.spotify.com/v1/search'+self.url_appender
        
        self.response = requests.get(url, headers=self.headers)
    
    def getArtist(self, ID):
        url = f'https://api.spotify.com/v1/artists/{ID}'
        self.defaultSearch(url)
        
    def getArtistAlbums(self, ID, **kwargs):
        self.searchFilter(**kwargs)
        url = f'https://api.spotify.com/v1/artists/{ID}/albums'+self.url_appender
        self.defaultSearch(url)
        
    def getArtistTops(self, ID, country):
        url = f'https://api.spotify.com/v1/artists/{ID}/top-tracks?country={country}'
        self.defaultSearch(url)
        
    def getCategoryPlaylists(self, ID, **kwargs):
        self.searchFilter(**kwargs)
        url = f'https://api.spotify.com/v1/browse/categories/{ID}/playlists'+self.url_appender
        self.defaultSearch(url)
        
    def getUserPlaylists(self, ID, **kwargs):
        self.searchFilter(**kwargs)
        url = f'https://api.spotify.com/v1/users/{ID}/playlists'+self.url_appender
        self.defaultSearch(url)
    
    def getPlaylistTracks(self, ID, **kwargs):
        self.searchFilter(**kwargs)
        url = f'https://api.spotify.com/v1/playlists/{ID}/tracks'+self.url_appender
        self.defaultSearch(url)
    
    def getUserProfile(self, ID):
        url = f'https://api.spotify.com/v1/users/{ID}'
        self.defaultSearch(url)
    
    def run(self):
        pass

if __name__ == '__main__':
    spotifyScrape = spotifyScrape()
    spotifyScrape.run()
