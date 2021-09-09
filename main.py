from random import random, randint
import discord
import datetime
import openpyxl as openpyxl
import asyncio
import os
client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print ("Szreav 봇 구동 준비 완료")
    game = discord.Game("!도움말")
    await client.change_presence(status=discord.Status.online, activity=game)

prefix = ("!")

@client.event
async def on_message(message):
    if message.content.startswith(prefix + "안녕"):
        await message.channel.send("안녕하세요, SG서버 공식 관리 봇 Szreav 입니다.")
    if message.content.startswith(prefix + "제작자"):
        await message.channel.send("Ssëüṅg#9197")

    if message.content.startswith(prefix + "서버"):
        i = client.guilds
        await message.channel.send(i)

    if message.content.startswith(prefix + "서은규"):
        await message.channel.send("서은규는 " + message.author.name + " 의 노예랄까..?")
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="서은규의 한마디 ", value="서은규: 아앙 주인님~~", inline=False)
        await message.author.send(embed=embed)

    if message.content.startswith(prefix + "청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메시지를 삭제했습니다.")
    global yes, no, voting, msgid, lit

    if message.content.startswith(prefix + "아바타"):
        user = message.author
        await message.channel.send(f"{message.author.mention} **님의 아바타입니다.**")
        await message.channel.send(user.avatar_url)

    if message.content.startswith("샌즈"):
        sanseasteregg = (message.author.name + " 샌즈!!!!!!")
        await message.channel.send("이스터에그를 찾은 " + message.author.name + "당신은 최고의 샍즈")
        embed = discord.Embed(color=0x7AD7BE)
        embed.add_field(name="와! 샌즈 아 시 는 구 나", value=sanseasteregg, inline=False)
        await message.author.send(embed=embed)

    if message.content.startswith(prefix + "투표"):
        if message.content == "!투표":
            await message.channel.send("투표기능을 사용하려면 !투표/주제/항목1/항목2 와 같은형식으로 해야합니다.")
        else:
            vote = message.content[4:].split("/")
            await message.channel.send("투표 - " + vote[0])
            for i in range(1, len(vote)):
                choose = await message.channel.send("```" + vote[i] + "```")
                await choose.add_reaction(':thumbsup:')

    if message.content.startswith(prefix + "타이머"):
        time = int(message.content[5:])
        print("타이머 시작")
        embed = discord.Embed(colour=discord.Colour.blue(), title = "타이머",)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/884511414042107944/885491454124916787/4854.png_860.png")
        embed.add_field(name="타이머를 {0}초간 작동합니다.".format(time), value="또각또각~")
        await message.channel.send(embed=embed)
        await asyncio.sleep(time)
        embed = discord.Embed(colour=discord.Colour.blue(), title = "타이머",)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/884511414042107944/885491454124916787/4854.png_860.png")
        embed.add_field(name="{0}초가 지났습니다!".format(time), value="타이머가 종료됩니다.")
        await message.channel.send(embed=embed)


    if message.content.startswith(prefix + "채널메시지"):
        if message.author.id == 884504196831924244 or message.channel.permissions_for(message.author).administrator:
            channel = message.content[10:28]
            msg = message.content[29:]
            if channel != 884504196831924244 or channel != 884513923653586986:
                await message.channel.send("해당 채널에는 채널 메시지를 전송 할수 없습니다.")
            else:
                await client.get_channel(int(channel)).send(msg)
                await message.channel.send("'" + msg + "'(이)라고 채널메시지를 보냈습니다.")
        else:
            await message.channel.send("채널메시지 기능은 서버의 관리자만 사용할 수 있습니다.")

    if message.content.startswith(prefix + "내정보"):
        await message.channel.send(message.author.name + " 님의 정보")
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color = 0x7AD7BE)
        embed.add_field(name="이름:", value=message.author.name, inline=False)
        embed.add_field(name="디스플레이(현재채널) 닉네임:  ", value=message.author.display_name, inline=False)
        embed.add_field(name="가입일:  ", value=str(date.year) + "년 " + str(date.month) + "월 " + str(date.day) + "일 ", inline=False)
        embed.add_field(name="아이디: ", value=message.author.id, inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith(prefix + "도움말"):
      embed = discord.Embed(description=f'>>> [**Szreav 봇 초대하기**](https://discord.com/api/oauth2/authorize?client_id=884795213992820737&permissions=8&scope=bot)', colour=0x2F3136)
      embed.add_field(name="주의사항", value=f"``모든 명령어는 Szreav의 접두사 ''!'' 를 사용하여야 합니다 예시(!도움말 , !타이머)``", inline= False)
      embed.add_field(name="도움말", value=f"``Szreav봇의 정보와 명령어 등을 알려 줍니다.``", inline= False)
      embed.add_field(name="굴려", value=f"``랜덤 주사위를 굴립니다. ``", inline= False)
      embed.add_field(name="아바타", value=f"``자신의 프로필 사진 (아바타) 를 출력합니다. ``", inline= False)
      embed.add_field(name="내정보", value=f"``명령어를 보낸 유저의 디스코드 정보를 전송합니다.``", inline= False)
      embed.add_field(name="청소", value=f"``지정한 수 만큼 채널에 메시지를 삭제합니다``", inline= False)
      embed.add_field(name="서버", value=f"``서버코드를 출력합니다.``", inline= False)
      embed.add_field(name="타이머", value=f"``타이머를 시작합니다. 예시(!타이머 5 => 타이머 5초 실행)``", inline= False)      
      embed.add_field(name="확률", value=f"``1~100의 숫자중 77이 당첨되면 상금 ''천원''이 주어지는 도박게임입니다.``", inline= False)
      embed.add_field(name="미친확률", value=f"``1~1000의 숫자중 777이 당첨되면 상금 ''오천원''이 주어지는 도박게임입니다.``", inline= False)
      embed.add_field(name="Szreav", value=f"``Szreav봇의 정보를 알려줍니다``", inline= False)
      embed.set_author(name=f"{message.author.name} 님에게 전송된 도움말",icon_url=message.author.avatar_url)
      await message.reply(embed=embed,content='Szreav봇의 도움말입니다!', mention_author=True)


    if message.content.startswith(prefix + "Szreav"):
      embed = discord.Embed(description=f'', colour=0x7AD7BE)
      embed.set_author(name=f"{message.author.name} 님의 도움말",icon_url=message.author.avatar_url)
      embed.add_field(name="현재 Szreav봇 핑", value=f">>> {int((client.latency * 1000))}'ms", inline = False)
      embed.add_field(name="제작 기간", value=f">>> 2021-08-12 ~", inline = False)
      embed.add_field(name="사용 모듈", value=f">>> **[discord.py](https://discordpy.readthedocs.io/)** / **[Python](https://www.python.org/)** / **[Hcskr](https://github.com/331leo/hcskr_python)** 를 이용해 제작된 봇입니다", inline = False)
      embed.add_field(name="프로필 정보", value=f"- Szreav봇 \n>>> 디스코드 : Ssëüṅg#9197", inline = False)
      await message.reply(embed=embed,content='님에게 전송된 Szreav봇 정보', mention_author=True)

    if message.content.startswith(prefix + "확률"):
        percent_value = randint(1, 100)
        embed = discord.Embed(colour=0x7AD7BE)
        await message.channel.send("77이 뽑히면 잭팟!")
        embed.add_field(name='1%의 확률!', value=percent_value, inline=False)
        await message.channel.send(embed=embed)
        if percent_value == 77:
            await message.channel.send(message.author.name + " 잭팟 당첨!!!! :moneybag: ")
            luckyguy = (message.author.name + " 1%의 확률을 뚫으셨습니다! 당첨금 : 1000원")
            embed = discord.Embed(color=0x7AD7BE)
            embed.add_field(name="1%의 확룔!:four_leaf_clover: ", value=luckyguy, inline=False)
            await message.author.send(embed=embed)
        else:
            await message.channel.send(message.author.name + " 아쉽게도 1%의 확률을 이기지 못했습니다... ")

    if message.content.startswith(prefix + "미친확률"):
        percent_value = randint(1, 1000)
        embed = discord.Embed(colour=0x7AD7BE)
        await message.channel.send("777이 뽑히면 잭팟!")
        embed.add_field(name='1%의 확률!', value=percent_value, inline=False)
        await message.channel.send(embed=embed)
        if percent_value == 777:
            await message.channel.send(message.author.name + " 잭팟 당첨!!!! :moneybag: ")
            luckyguy = (message.author.name + " 1%의 확률을 뚫으셨습니다! 당첨금 : 5000원")
            embed = discord.Embed(color=0x7AD7BE)
            embed.add_field(name="1%의 확룔!:four_leaf_clover: ", value=luckyguy, inline=False)
            await message.author.send(embed=embed)
        else:
            await message.channel.send(message.author.name + " 아쉽게도 1%의 확률을 이기지 못했습니다... ")



    if message.content.startswith(prefix + "굴려"):
        dice_value = randint(1, 6)
        await message.channel.send("랜덤 주사위를 굴립니다~~")
        if dice_value == 1:
            pic = ("https://cdn.discordapp.com/attachments/884504196831924244/885467230932967424/6294.png_1200.png")
        if dice_value == 2:
            pic = ("https://cdn.discordapp.com/attachments/884504196831924244/885467230932967424/6294.png_1200.png")
        if dice_value == 3:
            pic = ("https://cdn.discordapp.com/attachments/884504196831924244/885467230932967424/6294.png_1200.png")
        if dice_value == 4:
            pic = ("https://cdn.discordapp.com/attachments/884504196831924244/885467230932967424/6294.png_1200.png")
        if dice_value == 5:
            pic = ("https://cdn.discordapp.com/attachments/884504196831924244/885467230932967424/6294.png_1200.png")
        if dice_value == 6:
            pic = ("https://cdn.discordapp.com/attachments/884504196831924244/885467230932967424/6294.png_1200.png")
        embed = discord.Embed(colour=0x7AD7BE)
        embed.add_field(name='랜덤 주사위의 숫자는??', value=dice_value, inline=False)
        embed.set_thumbnail(url="https://discord.com/channels/707587767130914818/707762913556955216/707762960394878986")
        await message.channel.send(embed=embed)


        
access_token = os.environ['BOT_TOKEN']       
client.run(access_token)
