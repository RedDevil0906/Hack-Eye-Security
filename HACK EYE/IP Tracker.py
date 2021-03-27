def iptracker(ip):
    import urllib.request
    import json
    values = json.loads(urllib.request.urlopen("http://ip-api.com/json/"+ip).read())
    return(values['country'],values['regionName'],values['city'],values['zip'],values['lat'],values['lon'],values['timezone'])
Country,Region,City,Zip,Lat,Long,Tz = iptracker(input("Enter IP address: "))
print('Country:',Country)
print('Region:',Region)
print('City:',City)
print('Zip:',Zip)
print('Latitude:',Lat)
print('Longitude:',Long)a
print('Timezone:',Tz)
