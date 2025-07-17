import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import random
import os
from dotenv import load_dotenv
import json
from datetime import datetime

# .env dosyasından tokenları oku
load_dotenv()
TOKEN = os.getenv('TOKEN')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} olarak giriş yapıldı!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!yardım"))


# Hava durumu komutu (WeatherAPI)
@bot.command()
async def hava(ctx, *, konum: str):
    """Belirtilen konumun hava durumu bilgisini gösterir"""
    try:
        # WeatherAPI'den veri çek
        url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={konum}&lang=tr"
        response = requests.get(url)
        data = response.json()

        if 'error' in data:
            await ctx.send(f"Hata: {data['error']['message']}")
            return

        # Verileri işle
        location = data['location']
        current = data['current']

        # Emoji eşleştirme
        weather_emojis = {
            'Sunny': '☀️',
            'Clear': '🌙',
            'Partly cloudy': '⛅',
            'Cloudy': '☁️',
            'Overcast': '☁️',
            'Mist': '🌫️',
            'Rain': '🌧️',
            'Snow': '❄️',
            'Thunderstorm': '⛈️'
        }

        condition = current['condition']['text']
        emoji = weather_emojis.get(condition, '🌡️')

        # Renk belirleme
        temp = current['temp_c']
        if temp > 30:
            color = 0xFF4500
        elif temp > 20:
            color = 0xFFA500
        elif temp > 10:
            color = 0x00FF00
        else:
            color = 0x1E90FF

        # Embed oluştur
        embed = discord.Embed(
            title=f"{emoji} {location['name']}, {location['country']} Hava Durumu",
            description=f"**{condition}**",
            color=color,
            timestamp=datetime.strptime(location['localtime'], "%Y-%m-%d %H:%M")
        )

        embed.set_thumbnail(url=f"https:{current['condition']['icon']}")
        embed.add_field(name="🌡️ Sıcaklık", value=f"{current['temp_c']}°C", inline=True)
        embed.add_field(name="💨 Hissedilen", value=f"{current['feelslike_c']}°C", inline=True)
        embed.add_field(name="💧 Nem", value=f"%{current['humidity']}", inline=True)
        embed.add_field(name="🌬️ Rüzgar", value=f"{current['wind_kph']} km/s {current['wind_dir']}", inline=True)
        embed.add_field(name="☁️ Bulut", value=f"%{current['cloud']}", inline=True)
        embed.add_field(name="👁️ Görüş", value=f"{current['vis_km']} km", inline=True)

        embed.set_footer(text=f"Son güncelleme: {current['last_updated']}")

        await ctx.send(embed=embed)

    except Exception as e:
        print(f"Hata: {e}")
        await ctx.send("Hava durumu bilgisi alınamadı. Lütfen geçerli bir konum girin.")


# Haber komutu (NewsAPI)

@bot.command()
async def haber(ctx, kategori: str = "genel"):
    """Belirtilen kategoride son dakika haberlerini gösterir"""
    try:
        # Kategoriler ve API ayarları
        KATEGORILER = {
            "genel": "general",
            "spor": "sports",
            "teknoloji": "technology",
            "ekonomi": "business",
            "saglik": "health",
            "eğlence": "entertainment"
        }

        # Kategori kontrolü
        secilen_kategori = KATEGORILER.get(kategori.lower(), "general")

        # API isteği
        url = f"https://newsapi.org/v2/top-headlines?country=us&category={secilen_kategori}&pageSize=5"
        headers = {"X-Api-Key": os.getenv("NEWS_API_KEY")}

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Haberleri işleme
        articles = data.get("articles", [])

        if not articles:
            await ctx.send("Bu kategoride haber bulunamadı.")
            return

        # Embed oluşturma
        embed = discord.Embed(
            title=f"Son Dakika Haberleri ({kategori.capitalize()})",
            color=0x00FF00,
            description=f"NewsAPI ile {len(articles)} haber getirildi"
        )

        for idx, article in enumerate(articles, 1):
            title = article.get("title", "Başlık yok")[:200]
            source = article.get("source", {}).get("name", "Bilinmeyen kaynak")
            url = article.get("url", "#")

            embed.add_field(
                name=f"{idx}. {title}",
                value=f"[{source}]({url})",
                inline=False
            )

        await ctx.send(embed=embed)

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            await ctx.send("API anahtarı geçersiz veya eksik!")
        elif e.response.status_code == 429:
            await ctx.send("API kotası doldu, lütfen daha sonra tekrar deneyin")
        else:
            await ctx.send(f"API hatası: {e.response.status_code}")
    except Exception as e:
        await ctx.send("Haberler alınırken bir hata oluştu")
        print(f"Haber hatası: {e}")


# Diğer komutlar (aşağıdaki komutlar öncekiyle aynı kalacak)
@bot.command()
async def yazitura(ctx):
    sonuc = random.choice(['Yazı', 'Tura'])
    await ctx.send(f'Sonuç: {sonuc}')


@bot.command()
async def zar(ctx):
    sonuc = random.randint(1, 6)
    await ctx.send(f'Zar sonu!cu: {sonuc}')

@bot.command()
async def gercek(ctx):
    gercekler = [
        "Bir yılan 3 yıl boyunca hiçbir şey yemeden yaşayabilir",
        "Dünyanın en küçük ülkesi Vatikan'dır (0.44 km²)",
        "İnsan beyninin %80'i sudan oluşur",
        "Kedilerin her bir kulağında 32 kas vardır",
        "Bal arıları bir günde yaklaşık 2.000 çiçeği ziyaret eder"
    ]
    await ctx.send(f"**İlginç Gerçek:** {random.choice(gercekler)}")


@bot.command()
async def temizle(ctx, miktar: int):
    if miktar > 100:
        await ctx.send("En fazla 100 mesaj silebilirsiniz!")
        return
    await ctx.channel.purge(limit=miktar + 1)
    await ctx.send(f'{miktar} mesaj silindi.', delete_after=3)


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! Gecikme: {round(bot.latency * 1000)}ms')


@bot.command()
async def yardim(ctx):
    embed = discord.Embed(
        title="📜 Bot Komutları",
        description="İşte kullanabileceğiniz komutlar:",
        color=discord.Color.blue()
    )
    embed.add_field(name="!yazitura", value="Yazı tura atar", inline=False)
    embed.add_field(name="!zar", value="1-6 arası zar atar", inline=False)
    embed.add_field(name="!hava <konum>", value="Konumun hava durumunu gösterir", inline=False)
    embed.add_field(name="!haber", value="Son dakika haberleri getirir", inline=False)
    embed.add_field(name="!gercek", value="İlginç bir gerçek gösterir", inline=False)
    embed.add_field(name="!temizle <sayı>", value="Belirtilen sayıda mesaj siler (max 100)", inline=False)
    embed.add_field(name="!ping", value="Bot gecikmesini gösterir", inline=False)
    embed.add_field(name="!yardim", value="Bu yardım mesajını gösterir", inline=False)

    await ctx.send(embed=embed)


bot.run(TOKEN)
