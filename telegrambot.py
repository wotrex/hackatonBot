import requests
import json

class ESportBot():
    def __init__(self):
        self.u = "https://api.telegram.org/bot1105108305:AAEhW5-hfSAxtypvGEelbCk11DNvLXcBXPc/getUpdates"      

    def get_updates(self,offset=None, timeout=30):                
        params = {'timeout': timeout, 'offset': offset}
        self.url = requests.get(self.u, params)
        jsonresponse = json.loads(self.url.text)
        return jsonresponse

    def last_update(self):                                          
        if 'result' in self.get_updates():
            results = self.get_updates()['result']
            if len(results) > 0:
                last_update = results[-1]
            else:
                last_update = None

            return last_update
        else:
            last_update = None
            return last_update
    
    def get_chat_id(self,update):                         
        if 'message' in update:
            chat_id = update['message']['chat']['id']
            return chat_id
        else:
            return None
        if 'edited_message' in update:
            chat_id = update['edited_message']['chat']['id']
            return chat_id
        else:
            return None
    def send_mess(self, chat, text):                 
        params = {'chat_id': chat, 'text': text}
        response = requests.post("https://api.telegram.org/bot1105108305:AAEhW5-hfSAxtypvGEelbCk11DNvLXcBXPc/" + 'sendMessage', params)
        return response
    
    def send_mes(self, chat, text): 
        response = requests.post("https://api.telegram.org/bot1105108305:AAEhW5-hfSAxtypvGEelbCk11DNvLXcBXPc/sendMessage?chat_id={}&text={}".format(chat, text))
        return response
    def get_message(self,update):              
        if 'message' in update:
            if 'text' in update['message']:
                chat_id = update['message']['text']
                return chat_id
            else:
                
                no = "non"
                return no
        else:
            no = "non"
            return no
        if 'edited_message' in update:
            if 'text' in update['edited_message']:
                chat_id = update['edited_message']['text']
                return chat_id
            else:
                no = "non"
                return no
        else:
            no = "non"
            return no
def getMatch(matchid):
    match = requests.get("https://api.opendota.com/api/matches/{}?api_key=19674c39-adc9-4622-8af5-7050103d6964".format(matchid))
    jsonresp = json.loads(match.text)
    return jsonresp
def getProMatch():
    match = requests.get("https://api.opendota.com/api/proMatches?api_key=19674c39-adc9-4622-8af5-7050103d6964")
    jsonresp = json.loads(match.text)
    return jsonresp
leagues = ['RED STAR CUP','World E-sports Legendary League','Oceanic Esports Dota League','中国DOTA2职业联赛','ESL One Birmingham 2020 Online powered by Intel']
def getLastMatch(idchat, last_match, matchStats):
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
    firstBloodTime = matchStats['first_blood_time']
    multi_kills = ''
    for n in range(10):
        if matchStats['players'][n]['multi_kills'] is None:
            break
        if '5' in matchStats['players'][n]['multi_kills']:
            if (matchStats['players'][n]['name']) is None:
                multi_kills = matchStats['players'][n]['personaname'] + " совершил RAMPAGE " + str(matchStats['players'][n]['multi_kills']['5']) + " раз(а)"
            else:
                multi_kills = matchStats['players'][n]['name'] + " совершил RAMPAGE " + str(matchStats['players'][n]['multi_kills']['5']) + " раз(а)"
            break
        elif '4' in matchStats['players'][n]['multi_kills']:
            if (matchStats['players'][n]['name']) is None:
                multi_kills = matchStats['players'][n]['personaname'] + " убил четырёх подряд " + str(matchStats['players'][n]['multi_kills']['4']) + " раз(а)"
            else:
                multi_kills = matchStats['players'][n]['name'] + " убил четырёх подряд " + str(matchStats['players'][n]['multi_kills']['4']) + " раз(а)"
            break
        elif '3' in matchStats['players'][n]['multi_kills']:
            if (matchStats['players'][n]['name']) is None:
                multi_kills = matchStats['players'][n]['personaname'] + " совершил тройное убийство " + str(matchStats['players'][n]['multi_kills']['3']) + " раз(а)"
            else:
                multi_kills = matchStats['players'][n]['name'] + " совершил тройное убийство " + str(matchStats['players'][n]['multi_kills']['3']) + " раз(а)"
            break
    firstBloodPlayer = None
    for n in range(10):
        if matchStats['players'][n]['kills_log'] is None or not matchStats['players'][n]['kills_log']:
            continue
        if int(firstBloodTime) + 1 == int(matchStats['players'][n]['kills_log'][0]['time']):
            if (matchStats['players'][n]['name']) is None:
                firstBloodPlayer = matchStats['players'][n]['personaname']
            else:
                firstBloodPlayer = matchStats['players'][n]['name']
            break
    bot.send_mes(idchat, "\u2b50\u2b50\u2b50Лига:%20{}\u2b50\u2b50\u2b50%0A{}%20против%20{}%0AСилы%20Света:%20{}.%20Счёт:%20{}.%0AСилы%20Тьмы:%20{}.%20Счёт:%20{}.%0AПобедили:%20{}%0AПродолжительность:%20{}%20мин.%0A%0A{}:%0AИгрок%20-%20Герой%20-%20Убийства%20-%20Помощь%20-%20Смерти%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A%0A{}:%0AИгрок%20-%20Герой%20-%20Убийства%20-%20Помощь%20-%20Смерти%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A%0A{}%20совершил%20первое%20убийство%20на%20{}%20минуте%0A{}".format(league_name,radiant_team,dire_team,radiant_team,radiant_score,dire_team,dire_score,winner,str(round(duration)),radiant_team,radiant_players[0],radiant_players[1],radiant_players[2],radiant_players[3],radiant_players[4],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    radiant_players[5],radiant_players[6],radiant_players[7],radiant_players[8],radiant_players[9],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    radiant_players[10],radiant_players[11],radiant_players[12],radiant_players[13],radiant_players[14],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    radiant_players[15],radiant_players[16],radiant_players[17],radiant_players[18],radiant_players[19],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    radiant_players[20],radiant_players[21],radiant_players[22],radiant_players[23],radiant_players[24],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    dire_team, dire_players[0],dire_players[1],dire_players[2],dire_players[3],dire_players[4],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    dire_players[5],dire_players[6],dire_players[7],dire_players[8],dire_players[9],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    dire_players[10],dire_players[11],dire_players[12],dire_players[13],dire_players[14],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    dire_players[15],dire_players[16],dire_players[17],dire_players[18],dire_players[19],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   dire_players[20],dire_players[21],dire_players[22],dire_players[23],dire_players[24],firstBloodPlayer,str(round(firstBloodTime/60)),str(multi_kills)))
    if idchat in benchmarksen:
        benchmarks = []
        for n in range(10):
            benchmarks.append(round((matchStats['players'][n]['benchmarks']['gold_per_min']['pct'])*100,2))
            benchmarks.append(round((matchStats['players'][n]['benchmarks']['xp_per_min']['pct'])*100,2))
            benchmarks.append(round((matchStats['players'][n]['benchmarks']['kills_per_min']['pct'])*100,2))
            benchmarks.append(round((matchStats['players'][n]['benchmarks']['last_hits_per_min']['pct'])*100,2))
            benchmarks.append(round((matchStats['players'][n]['benchmarks']['hero_damage_per_min']['pct'])*100,2))
        bot.send_mes(idchat, "Benchmarks%0A%0A{}:%0AИгрок%20-%20золото%20в%20минуту%20-%20опыт%20в%20минуту%20-%20убийства%20в%20минуту%20-%20добитые%20крипы%20в%20минуту%20-%20урон%20по%20героям%20в%20минуту%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A%0A{}:%0AИгрок%20-%20золото%20в%20минуту%20-%20опыт%20в%20минуту%20-%20убийства%20в%20минуту%20-%20добитые%20крипы%20в%20минуту%20-%20урон%20по%20героям%20в%20минуту%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%0A{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}%20-%20{}".format(radiant_team,radiant_players[0],benchmarks[0],benchmarks[1],benchmarks[2],benchmarks[3],benchmarks[4],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      radiant_players[5],benchmarks[5],benchmarks[6],benchmarks[7],benchmarks[8],benchmarks[9],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      radiant_players[10],benchmarks[10],benchmarks[11],benchmarks[12],benchmarks[13],benchmarks[14],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      radiant_players[15],benchmarks[15],benchmarks[16],benchmarks[17],benchmarks[18],benchmarks[19],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      radiant_players[20],benchmarks[20],benchmarks[21],benchmarks[22],benchmarks[23],benchmarks[24],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      dire_team,dire_players[0],benchmarks[25],benchmarks[26],benchmarks[27],benchmarks[28],benchmarks[29],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      dire_players[5],benchmarks[30],benchmarks[31],benchmarks[32],benchmarks[33],benchmarks[34],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      dire_players[10],benchmarks[35],benchmarks[36],benchmarks[37],benchmarks[38],benchmarks[39],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      dire_players[15],benchmarks[40],benchmarks[41],benchmarks[42],benchmarks[43],benchmarks[44],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      dire_players[20],benchmarks[45],benchmarks[46],benchmarks[47],benchmarks[48],benchmarks[49]))
    return
def update(token, id, **kwargs):
    data = json.dumps(kwargs)
    p = requests.post('https://write.as/api/posts' + "/%s" % id, data=data,
        headers={"Authorization": "Token %s" % token,
                "Content-Type":"application/json"})
    if p.status_code != 200:
        return "Error in updatePost(): %s" % p.json()["error_msg"]
def updateList(members):
    b = ''
    for k in members:
        b += str(k) + ','
    update('54e5b71b-8113-4381-4819-4b6e942e5b25', '3s53eqfuvys0y85q', body = (b))
def updateBench(benchmarksen):
    b = ''
    for k in benchmarksen:
        b += str(k) + ','
    update('54e5b71b-8113-4381-4819-4b6e942e5b25', 'otvkp38orjdkzgyw', body = (b))
heroes = json.loads(requests.get("https://api.opendota.com/api/heroes?api_key=19674c39-adc9-4622-8af5-7050103d6964").text)
r = requests.get("https://write.as/api/posts/3s53eqfuvys0y85q")
rb = requests.get("https://write.as/api/posts/otvkp38orjdkzgyw")
objects = json.loads(r.text)['data']['body']
members = []
benchmarksen = []
k = ''
for o in objects:
    if o != ',':
        k +=str(o)
    else:
        members.append(int(k))
        k = ''
objects = json.loads(rb.text)['data']['body']
for o in objects:
    if o != ',':
        k +=str(o)
    else:
        benchmarksen.append(int(k))
        k = ''
bot = ESportBot()          
offset = None
match_now = 0
while 1:
    bot.get_updates(offset)     
    last_update = bot.last_update()
    last_match = getProMatch()
    matchStats = getMatch(last_match[0]['match_id'])
    if last_match[0]['match_id'] != match_now:
        for m in members:
            getLastMatch(m, last_match,matchStats)
        match_now = last_match[0]['match_id']
    if last_update is None:         
        continue
    last_update_id = last_update['update_id']
    if bot.get_message(last_update) == "/enablenews" or bot.get_message(last_update) == "/enablenews@dotaCyberGameBot":
        if bot.get_chat_id(last_update) in members:
            pass
        else:
            bot.send_mess(bot.get_chat_id(last_update),'Авто рассылка включена')
            members.append(bot.get_chat_id(last_update))
            updateList(members)
    if bot.get_message(last_update) == "/enablebm" or bot.get_message(last_update) == "/enablebm@dotaCyberGameBot":
        if bot.get_chat_id(last_update) in benchmarksen:
            pass
        else:
            bot.send_mess(bot.get_chat_id(last_update),'Benchmarks включены')
            benchmarksen.append(bot.get_chat_id(last_update))
            updateBench(benchmarksen)
    if bot.get_message(last_update) == "/disablebm" or bot.get_message(last_update) == "/disablebm@dotaCyberGameBot":
        if bot.get_chat_id(last_update) in benchmarksen:
            bot.send_mess(bot.get_chat_id(last_update),'Benchmarks выключены')
            del benchmarksen[benchmarksen.index(bot.get_chat_id(last_update))]
            updateBench(benchmarksen)
    if bot.get_message(last_update) == "/disablenews" or bot.get_message(last_update) == "/disablenews@dotaCyberGameBot":
        if bot.get_chat_id(last_update) in members:
            bot.send_mess(bot.get_chat_id(last_update),'Авто рассылка выключена')
            del members[members.index(bot.get_chat_id(last_update))]
            updateList(members)
    if bot.get_message(last_update) == "/lastmatchstats" or bot.get_message(last_update) == "/lastmatchstats@dotaCyberGameBot" or bot.get_message(last_update) == "/alllastmatchstats" or bot.get_message(last_update) == "/alllastmatchstats@dotaCyberGameBot":
        getLastMatch(bot.get_chat_id(last_update), last_match,matchStats)
    offset = last_update_id + 1
