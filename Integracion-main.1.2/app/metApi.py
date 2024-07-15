import requests
import json

apisHosts = {
    'post_venta' : 'http://44.220.241.211/todos_los_datos',
}

def post_ventaApi():
    #url = 'http://'+apisHosts['post_venta']+'/post_venta/'
    url = apisHosts['post_venta']
    r = requests.get(url)
    print("owo")
    if r.status_code == 200:
        json_data = r.json().get("despachos", [])
    else:
        json_data = [1]
        print(f'Error en la petición GET: {r.status_code}')
    return json_data

