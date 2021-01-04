import requests
import base64

class spotifyPy:    
    def requestAccess(self):
        credentials = 'client-id:client-token'
        byteCreds = credentials.encode('ascii')
        base64Creds = base64.b64encode(byteCreds)
        
        tokenData = {'grant_type':'client_credentials'}
        tokenHeader = {'Authorization':f'Basic {base64Creds.decode()}'}
         
        self.request = requests.post('https://accounts.spotify.com/api/token', data=tokenData, headers=tokenHeader)
        self.accessTokenData = self.request.json()
        
    def run(self):
        self.requestAccess()
        self.checkToken()
        

if __name__ == '__main__':
    spotifyPy = spotifyPy()
    spotifyPy.run()