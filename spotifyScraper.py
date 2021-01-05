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
    
    def getAlbum(self, ID):      
        url = f'https://api.spotify.com/v1/albums/{ID}'
        self.defaultSearch(url)   
        
    def getAlbumTracks(self, ID):
        url = f'https://api.spotify.com/v1/albums/{ID}/tracks'
        self.defaultSearch(url)

    def searchFilter(self, **kwargs):
        url_appender = '?'
        
        for i in kwargs:
            if url_appender == '?':
                url_appender += f'{i}={kwargs[i]}'
            else:
                url_appender += f'&{i}={kwargs[i]}'
                
        print(url_appender)
        

        self.search(url_appender)


    def search(self, url_appender):
        self.checkValidToken()

        url = 'https://api.spotify.com/v1/search'+url_appender
        
        self.response = requests.get(url, headers=self.headers)
    
    def getArtist(self, ID):
        url = f'https://api.spotify.com/v1/artists/{ID}'
        self.defaultSearch(url)
        
    def getArtistAlbums(self, ID):
        url = f'https://api.spotify.com/v1/artists/{ID}/albums'
        self.defaultSearch(url)
        
    def getArtistTops(self, ID, country):
        url = f'https://api.spotify.com/v1/artists/{ID}/top-tracks?country={country}'
        self.defaultSearch(url)
        
    def getCategoryPlaylists(self, ID):
        url = f'https://api.spotify.com/v1/browse/categories/{ID}/playlists'
        self.defaultSearch(url)
        
    def getUserPlaylists(self, ID):
        url = f'https://api.spotify.com/v1/users/{ID}/playlists'
        self.defaultSearch(url)
    
    def getPlaylistTracks(self, ID):
        url = f'https://api.spotify.com/v1/playlists/{ID}/tracks'
        self.defaultSearch(url)
    
    def getUserProfile(self, ID):
        url = f'https://api.spotify.com/v1/users/{ID}'
        self.defaultSearch(url)
    
    def run(self):
        
        #self.getToken()
        #self.getAlbum('6nVACH6a27eOWiumAJhDWS')
        #self.getAlbumTracks('6nVACH6a27eOWiumAJhDWS')
        self.searchFilter(q='crystal+dolphin', type='track', limit='2')
        #self.getArtist('0OdUWJ0sBjDrqHygGUXeCF')
        #self.getArtistAlbums('1vCWHaC5f2uS3yhpwWbIA6')
        #self.getArtistTops('43ZHCT0cAZBISjO8DG9PnE', 'SE')
        #self.getCategoryPlaylists('party')
        #self.getUserPlaylists('12182963393')
        #self.getPlaylistTracks('3hn9aLwfBzkwA4CukUzxwS')
        #self.getUserProfile('bruh')
        
        
        print(self.response.text)
        pass

if __name__ == '__main__':
    spotifyScrape = spotifyScrape()
    spotifyScrape.run()
