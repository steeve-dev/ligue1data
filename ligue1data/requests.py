import http.client
import json

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


def getLigue1Teams(id):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "08b693ac18msh71caadac3647d76p1d887fjsn29e7dc24331f",
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }
    conn.request("GET", f"/v3/teams/statistics?league=61&season=2023&team={id}", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    response = json.loads(data)
    team = response.get("response", {}).get("team", [])
    goals = response.get("response", {}).get("total", [])
    return team




