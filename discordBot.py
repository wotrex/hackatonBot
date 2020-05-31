import discord
from discord.ext import commands
import requests 
import json

client = commands.Bot(command_prefix = '.')
# .matchstat

@client.event

async def getMatch(matchid):
    match = requests.get("https://api.opendota.com/api/matches/{}?api_key=19674c39-adc9-4622-8af5-7050103d6964".format(matchid))
    jsonresp = json.loads(match.text)
    return jsonresp
async def getProMatch():
    match = requests.get("https://api.opendota.com/api/proMatches?api_key=19674c39-adc9-4622-8af5-7050103d6964")
    jsonresp = json.loads(match.text)
    return jsonresp
async def getLastMatch():
    heroes = json.loads(requests.get("https://api.opendota.com/api/heroes?api_key=19674c39-adc9-4622-8af5-7050103d6964").text)
    leagues = ['RED STAR CUP','World E-sports Legendary League','Oceanic Esports Dota League','中国DOTA2职业联赛','ESL One Birmingham 2020 Online powered by Intel']
    last_match = await getProMatch()
    matchStats = await getMatch(last_match[0]['match_id'])
    league_name = matchStats['league']['name']
    if league_name in leagues:
        pass
    else:
        return
    radiant_team = "Noname"
    try:
        radiant_team = matchStats['radiant_team']['name']
    except:
        radiant_team = "Noname"
    radiant_score = matchStats['radiant_score']
    dire_team = "Noname"
    try:
        dire_team = matchStats['dire_team']['name']
    except:
        dire_team = "Noname"
    dire_score = matchStats['dire_score']
    duration = last_match[0]['duration']/60
    radiant_players = []
    dire_players = []
    for n in range(5):
        if (matchStats['players'][n]['name']) is None:
            radiant_players.append(matchStats['players'][n]['personaname'])
        else:
            radiant_players.append(matchStats['players'][n]['name'])
        for h in heroes:
            if h['id'] == matchStats['players'][n]['hero_id']:
                radiant_players.append(h['localized_name'])
        radiant_players.append(matchStats['players'][n]['kills'])
        radiant_players.append(matchStats['players'][n]['assists'])
        radiant_players.append(matchStats['players'][n]['deaths'])
        if (matchStats['players'][n+5]['name']) is None:
            dire_players.append(matchStats['players'][n+5]['personaname'])
        else:
            dire_players.append(matchStats['players'][n+5]['name'])
        for h in heroes:
            if h['id'] == matchStats['players'][n+5]['hero_id']:
                dire_players.append(h['localized_name'])
        dire_players.append(matchStats['players'][n+5]['kills'])
        dire_players.append(matchStats['players'][n+5]['assists'])
        dire_players.append(matchStats['players'][n+5]['deaths'])
    winner = 0
    if (matchStats['radiant_win']):
        winner = radiant_team
    else:
        winner = dire_team
    text = 'Лига: {}\n{} против {}\nСилы Света: {}. Счёт: {}.\nСилы Тьмы: {}. Счёт: {}.\nПобедили: {}\nПродолжительность: {} мин.\n\n{}:\nИгрок - Герой - Убийства - Помощь - Смерти\n{} - {} - {} - {} - {}\n{} - {} - {} - {} - {}\n{} - {} - {} - {} - {}\n{} - {} - {} - {} - {}\n{} - {} - {} - {} - {} \n \n{}: \nИгрок - Герой - Убийства - Помощь - Смерти \n{} - {} - {} - {} - {} \n{} - {} - {} - {} - {} \n{} - {} - {} - {} - {} \n{} - {} - {} - {} - {} \n{} - {} - {} - {} - {}'.format(league_name,radiant_team,dire_team,radiant_team,radiant_score,dire_team,dire_score,winner,str(round(duration)),radiant_team,radiant_players[0],radiant_players[1],radiant_players[2],radiant_players[3],radiant_players[4],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    radiant_players[5],radiant_players[6],radiant_players[7],radiant_players[8],radiant_players[9],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    radiant_players[10],radiant_players[11],radiant_players[12],radiant_players[13],radiant_players[14],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    radiant_players[15],radiant_players[16],radiant_players[17],radiant_players[18],radiant_players[19],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    radiant_players[20],radiant_players[21],radiant_players[22],radiant_players[23],radiant_players[24],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    dire_team, dire_players[0],dire_players[1],dire_players[2],dire_players[3],dire_players[4],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    dire_players[5],dire_players[6],dire_players[7],dire_players[8],dire_players[9],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    dire_players[10],dire_players[11],dire_players[12],dire_players[13],dire_players[14],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    dire_players[15],dire_players[16],dire_players[17],dire_players[18],dire_players[19],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    dire_players[20],dire_players[21],dire_players[22],dire_players[23],dire_players[24])

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    return text


async def on_ready():
    print('Bot connected')
text = getLastMatch()

@client.command(pass_context = True)

async def matchstat(ctx):
    await ctx.send(await getLastMatch())

#Подключение

TOKEN = 'NzE2MzQyNTMzMDk2OTk2ODY0.XtKYEw.1eDvA2F-sB-cTmuG9Q_SPlcIV8c'

client.run(TOKEN)
