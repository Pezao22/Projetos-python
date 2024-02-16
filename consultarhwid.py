import discord, re, asyncio , requests
from discord.ext import commands
from datetime import datetime
import aiomysql

intents = discord.Intents.all()
intents.members = True
canalId = ''# adicione o ID do canal a utilizar 
api_key = ''# Adicione sua key
bot = commands.Bot(command_prefix='!', intents=intents)

# Configuração da conexão com o banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'db': 'pvp',
}

def iplocate(ip_address):
    url = f'https://www.iplocate.io/api/lookup/{ip_address}?apikey={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        results = response.json()
        return results
    else:
        print(f"Error: {response.status_code}")
        return None


async def connect_to_db():
    try:
        connection = await aiomysql.connect(**db_config)
        return connection
    except Exception as e:
        print(f'Erro ao conectar ao banco de dados: {e}')
        return None

@bot.event
async def on_message(message):
    # Verifica se a mensagem foi enviada na sala com o ID 1157856876118159400
    if message.channel.id == canalId and not message.author.bot:
        content = message.content.strip()
        connection = None  # Inicializa connection como None
        await message.delete()
        try:
            if (content.isdigit() and len(content) <= 6):
                embed = discord.Embed(
                    title=f"Realizando Buscas Aguarde ...",
                    color=discord.Color.green()
                )
                embed.add_field(
                        name=f"------------------------------\n",
                        value=f"**Buscando:** {content}",
                        inline=False
                    )
                embed.set_footer(
                    text="Esta mensagem será deletada em 10 segundos."
                )
                embed.set_image(url="https://c.tenor.com/aH2oWlpX664AAAAC/lupa-ojo.gif")
                # Envie o embed como mensagem
                response = await message.channel.send(embed=embed)
                await asyncio.sleep(10)
                await response.delete()
                # Tenta estabelecer a conexão com o banco de dados
                connection = await connect_to_db()

                if connection is not None:
                    async with connection.cursor() as cursor:
                        # Verifica se o token existe na tabela bans
                        await cursor.execute("""
                            SELECT
                                users.*,
                                bans.user_id,
                                bans.token AS ban_token,
                                bans.reason,
                                bans.staff_id,
                                identities.name
                            FROM users
                            LEFT JOIN bans ON users.id = bans.user_id
                            LEFT JOIN identities ON users.id = identities.user_id
                            WHERE users.id = %s;
                        """, (content,))

                        resultados = await cursor.fetchall()

                        if resultados:
                            # Obtendo os nomes das colunas a partir da descrição do cursor
                            columns = [column[0] for column in cursor.description]

                            # Organizando o resultado como uma lista de dicionários
                            rows = [dict(zip(columns, row)) for row in resultados]
                            db = rows[0]

                            embed = discord.Embed(
                                title=f"Resultados Encontrados ID: {content}",
                                color=discord.Color.green()
                            )
                            tokens = db.get('token', '').split(',')  # Pode ajustar o separador conforme necessário
                            tokenlist = '\n'.join(f'{token.strip()}' for token in tokens)
                            geoResult = ''
                            if db['endpoint'] is not None and db['endpoint'] != '0.0.0.0':
                                geoResult = iplocate(db['endpoint'])
                            
                            formato_desejado = "%d/%m/%Y %H:%M:%S"
                            data_hora_formatada = db['last_login'].strftime(formato_desejado)
                            embed.add_field(
                                name=f"---------- ** PLAYER INFO ** -----------\n",
                                value=f"**ID: {db['id']}**\n **Nome: **{db['name']} \n**STEAM:** {db['steam']}\n**DISCORD: ** {db['discord']}\n**IP: ** {db['endpoint']}\n**ULTIMO LOGIN: ** {data_hora_formatada}\n**Tokens** {tokenlist}",
                                inline=False
                            )

                            if geoResult and isinstance(geoResult, dict):
                                embed.add_field(
                                    name=f"---------- ** REDE INFO ** -----------\n",
                                    value=f"**IP: {geoResult['ip']}**\n **CIDADE: **{geoResult['city']}\n**UF:** {geoResult['subdivision']} \n**PAIS:** {geoResult['country']}\n**CORDS: ** Lat: {geoResult['latitude']} - Long: {geoResult['longitude']}\n**PROVEDOR: ** {geoResult['org']}\n**PROXY: ** {geoResult['threat']['is_proxy']}",
                                    inline=False
                                )
                            
                            if db['user_id']:
                                embed.add_field(
                                        name=f"---------- ** BAN INFO ** ---------------\n",
                                        value=f"**ID: {db['user_id']}**\n**Motivo:** {db['reason']}\n**Token** {db['ban_token']}\n**Banido Por: ** {db['staff_id']}",
                                        inline=False
                                    )
                            else:
                                embed.add_field(
                                        name=f"---------- ** BAN INFO ** -----------\n",
                                        value=f"Nao foi encontrado banimentos para esse ID",
                                        inline=False
                                    )

                            # for resultado in resultados:
                            #     user_id, token, motivo, duration, time, staff = resultado
                            #     embed.add_field(
                            #         name=f"------------------------------\n",
                            #         value=f"**ID: {user_id}**\n**Motivo:** {motivo}\n**Banido Por: ** {staff}",
                            #         inline=False
                            #     )
                                # Adiciona a última linha informando que a mensagem será deletada
                            # embed.set_footer(
                            #     text="Esta mensagem será deletada em 30 segundos."
                            # )
                            embed.set_thumbnail(url="https://i.gifer.com/HzL.gif")
                            #embed.set_image(url="https://i.gifer.com/HzL.gif")
                            # Envie o embed como mensagem
                            response = await message.channel.send(embed=embed)
                            # await asyncio.sleep(30)
                            # await response.delete()
            elif (re.match(r'^[0-9a-fA-F]+$', content) or re.match(r'^\["[0-9a-fA-F]+",("[0-9a-fA-F]+")*\]$', content)) and len(content) == 64:                

                embed = discord.Embed(
                    title=f"Realizando Buscas Aguarde ...",
                    color=discord.Color.green()
                )
                embed.add_field(
                        name=f"------------------------------\n",
                        value=f"**Buscando:** {content}",
                        inline=False
                    )
                embed.set_footer(
                    text="Esta mensagem será deletada em 10 segundos."
                )
                embed.set_image(url="https://c.tenor.com/aH2oWlpX664AAAAC/lupa-ojo.gif")
                # Envie o embed como mensagem
                response = await message.channel.send(embed=embed)
                await asyncio.sleep(10)
                await response.delete()
                # Tenta estabelecer a conexão com o banco de dados
                connection = await connect_to_db()

                if connection is not None:
                    async with connection.cursor() as cursor:
                        # Verifica se o token existe na tabela bans
                        await cursor.execute("SELECT * FROM bans WHERE token = %s OR token = %s OR token LIKE %s OR SUBSTRING_INDEX(token, ':', -1) = %s", (content, f'"{content}"', f'%"{content}"%', content))
                        resultados = await cursor.fetchall()

                        if resultados:
                            embed = discord.Embed(
                                title=f"Resultados Encontrados\n\n{content}",
                                color=discord.Color.green()
                            )

                            for resultado in resultados:
                                user_id, token, motivo, duration, time, staff = resultado
                                embed.add_field(
                                    name=f"------------------------------\n",
                                    value=f"**ID: {user_id}**\n**Motivo:** {motivo}\n**Banido Por: ** {staff}",
                                    inline=False
                                )
                                # Adiciona a última linha informando que a mensagem será deletada
                            # embed.set_footer(
                            #     text="Esta mensagem será deletada em 30 segundos."
                            # )
                            embed.set_thumbnail(url="https://i.gifer.com/HzL.gif")
                            #embed.set_image(url="https://i.gifer.com/HzL.gif")
                            # Envie o embed como mensagem
                            response = await message.channel.send(embed=embed)
                            # await asyncio.sleep(30)
                            # await response.delete()
                        else:
                            embed = discord.Embed(
                                title=f"Nenhum resultado encontrado",
                                color=discord.Color.green()
                            )
                            embed.add_field(
                                    name=f"------------------------------\n",
                                    value=f"**HWID:** {content}\n\n** Não foi encontrado em nosso bando de dados e o BIGFOOT ficou boladão **",
                                    inline=False
                                )
                            embed.set_footer(
                                text="Esta mensagem será deletada em 20 segundos."
                            )
                            embed.set_image(url="https://i.gifer.com/Db5f.gif")
                            # Envie o embed como mensagem
                            response = await message.channel.send(embed=embed)
                            await asyncio.sleep(20)
                            await response.delete()
                else:
                    embed = discord.Embed(
                        title=f"Conexão com banco de dados perdida",
                        color=discord.Color.green()
                    )
                    embed.add_field(
                            name=f"------------------------------\n",
                            value=f"**Deu Ruim e o BIGFOOT sai correndo ..**",
                            inline=False
                        )
                    embed.set_footer(
                        text="Esta mensagem será deletada em 20 segundos."
                    )
                    embed.set_thumbnail(url="https://i.gifer.com/7BPp.gif")
                    # Envie o embed como mensagem
                    response = await message.channel.send(embed=embed)
                    await asyncio.sleep(20)
                    await response.delete()
            else:
                embed = discord.Embed(
                        title=f"Formato do token Inválido",
                        color=discord.Color.green()
                    )
                embed.add_field(
                        name=f"------------------------------\n",
                        value=f"**Coloque apenas o token sem nenhum outro caracter especial para que a consulta seja realizada com exito**",
                        inline=False
                    )
                embed.set_footer(
                    text="Esta mensagem será deletada em 10 segundos."
                )
                embed.set_image(url="https://i.gifer.com/7QM0.gif")
                # Envie o embed como mensagem
                response = await message.channel.send(embed=embed)
                await asyncio.sleep(10)
                await response.delete()
        except Exception as e:
            print(e)
        finally:
            if connection is not None:
                connection.close()  # Fecha a conexão


bot.run()#ADICIONEIO SUA TOKEN
