import requests
import sys


def get_location(ip):
    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,district,zip,lat,lon,org,proxy,query?"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            return {
                #'IP': data['query'],
                'Country': data['country'],
                'Region': data['regionName'],
                'City': data['city'],
                'District': data['district'],
                'ZIP': data.get('zip', 'N/A'),
                'Lat': data['lat'],
                'Lon': data['lon'],
                'Org': data.get('org', 'N/A'),
                #'Proxy': data.get('proxy')
            }
        else:
            return f"Error: {data['message']}"
    else:
        return f"Error: Unable to reach the API (status code: {response.status_code})"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <IP_ADDRESS>")
        sys.exit(1)

    ip_address = sys.argv[1]
    location = get_location(ip_address)

    if isinstance(location, dict):
        print(f"Location information for IP {ip_address}:")
        for key, value in location.items():
            print(f"{key}: {value}")
    else:
        print(location)
