import http.client

def getLigue1():
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "08b693ac18msh71caadac3647d76p1d887fjsn29e7dc24331f",
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

    conn.request("GET", "/v3/leagues?id=61", headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def getLigue1Teams():
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "08b693ac18msh71caadac3647d76p1d887fjsn29e7dc24331f",
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }
    conn.request("GET", "/v3/standings?season=2023&league=61", headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
