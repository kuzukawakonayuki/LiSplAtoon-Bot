import discord
import requests
import json
import datetime
import time
import schedule
import asyncio

def Stage_Get():
    url = "https://spla2.yuu26.com/schedule"
    headers = {"User-Agent": "LiSplAtoon-Bot/ver0.1(twitter@kuzukawa_lisa)"}
    response = requests.get(url,headers=headers)
    dic = json.loads(response.text)
    dic = dic['result']
    
    url = "https://spla2.yuu26.com/coop/schedule"
    headers = {"User-Agent": "LiSplAtoon-Bot/ver0.1(twitter@kuzukawa_lisa)"}
    response = requests.get(url,headers=headers)
    dic_coop = json.loads(response.text)
    dic_coop = dic_coop['result']

    coop_now = dic_coop[0]
    coop_next = dic_coop[1]

    held_time = coop_now["start"]
    held_time = held_time[11:13]
    held_now = datetime.datetime.now()
    held_now = held_now.strftime("%H")

    if held_now == held_time:
        held = '開催中'
        held_next = '次回'
    else:
        held = '次回'
        held_next = 'その次'

    coop_now_weapons = coop_now["weapons"]
    coop_next_weapons = coop_next["weapons"]
    coop_now_send = '【' + coop_now["stage"]["name"] + '】\n' + coop_now["start"] + 'から　　　\n' + coop_now["end"] + 'まで\n' + '▲▽支給ブキ▽▲' + '\n・' + coop_now_weapons[0]["name"] + '\n・' + coop_now_weapons[1]["name"] + '\n・'+ coop_now_weapons[2]["name"] + '\n・'+ coop_now_weapons[3]["name"] + '\n'
    coop_next_send = '【' + coop_next["stage"]["name"] + '】\n' + coop_next["start"] + 'から\n' + coop_next["end"] + 'まで\n' + '▲▽支給ブキ▽▲' + '\n・' + coop_next_weapons[0]["name"] + '\n・' + coop_next_weapons[1]["name"] + '\n・'+ coop_next_weapons[2]["name"] + '\n・'+ coop_next_weapons[3]["name"] + '\n'

    regular = dic["regular"]
    regular_now = regular[0]
    regular_next = regular[1]
    regular_now_send = '【' + regular_now["rule"] + '】\n-' + regular_now["maps"][0] + '\n-' + regular_now["maps"][1] + '\n' + regular_now["start"] + 'から　　　\n' + regular_now["end"] + 'まで\n'
    regular_next_send = '【' + regular_next["rule"] + '】\n-' + regular_next["maps"][0] + '\n-' + regular_next["maps"][1] + '\n' + regular_next["start"] + 'から\n' + regular_next["end"] + 'まで\n'

    gachi = dic["gachi"]
    gachi_now = gachi[0]
    gachi_next = gachi[1]
    gachi_now_send = '【' + gachi_now["rule"] + '】\n-' + gachi_now["maps"][0] + '\n-' + gachi_now["maps"][1] + '\n' + gachi_now["start"] + 'から　　　\n' + gachi_now["end"] + 'まで\n'
    gachi_next_send = '【' + gachi_next["rule"] + '】\n-' + gachi_next["maps"][0] + '\n-' + gachi_next["maps"][1] + '\n' + gachi_next["start"] + 'から\n' + gachi_next["end"] + 'まで\n'

    league = dic["league"]
    league_now = league[0]
    league_next = league[1]
    league_now_send = '【' + league_now["rule"] + '】\n-' + league_now["maps"][0] + '\n-' + league_now["maps"][1] + '\n' + league_now["start"] + 'から　　　\n' + league_now["end"] + 'まで\n'
    league_next_send = '【' + league_next["rule"] + '】\n-' + league_next["maps"][0] + '\n-' + league_next["maps"][1] + '\n' + league_next["start"] + 'から\n' + league_next["end"] + 'まで\n'

    return [held, coop_now_send, held_next, coop_next_send, regular_now_send, regular_next_send, gachi_now_send, gachi_next_send, league_now_send, league_next_send]

client = discord.Client()

@client.event
async def on_ready():
    print('login_OK')
    print('{0.user}'.format(client))
    print(client.user.id)
    print('------------------------')
    asyncio.ensure_future(stage_send())

async def stage_send():
    channel = client.get_channel(547058723907174432)
    stages = Stage_Get()
    embed = discord.Embed(title="サーモンラン", color=0xffff00)
    embed.add_field(name=stages[0], value=stages[1])
    embed.add_field(name=stages[2], value=stages[3])
    await channel.send(embed=embed)
    embed = discord.Embed(title="レギュラーマッチ", color=0x00ff00)
    embed.add_field(name="現在", value=stages[4])
    embed.add_field(name="次回", value=stages[5])
    await channel.send(embed=embed)
    embed = discord.Embed(title="ガチマッチ", color=0xff8c00)
    embed.add_field(name="現在", value=stages[6])
    embed.add_field(name="次回", value=stages[7])
    await channel.send(embed=embed)
    embed = discord.Embed(title="リーグマッチ", color=0xff00ff)
    embed.add_field(name="現在", value=stages[8])
    embed.add_field(name="次回", value=stages[9])
    await channel.send(embed=embed)

client.run('NTQ3Mzg3NzQwNDQyOTg0NDQ4.D02COQ.SRT1fXlvKs-CaXBe6uUNqo0NuDE')



