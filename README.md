
# Multi-Purpose Discord Bot

This project is a multi-purpose Discord bot developed using Python and the `discord.py` library. It offers various features such as querying weather information, listing the latest news, performing simple moderation tasks, and providing several fun commands.

## ✨ Features

  - **Weather Forecast:** Fetches real-time weather data for a specified location from [WeatherAPI](https://www.weatherapi.com/) and presents it as a rich embed message '!hava <city>'
  - **Latest News:** Lists the top 5 latest news articles from various categories like general, sports, and technology using [NewsAPI](https://newsapi.org/) '!haber <category>'
  - **Fun Commands:**
      - `!yazitura`: Flips a coin.
      - `!zar`: Rolls a random 1-6 sided die.
      - `!gercek`: Displays an interesting fact.
  - **Moderation:**
      - `!temizle <amount>`: Deletes a specified number of messages from the channel (max 100).
  - **Utility Commands:**
      - `!ping`: Shows the bot's current latency.
      - `!help`: Displays a help menu with all commands and their descriptions.

## 🛠️ Setup and Installation

Follow the steps below to run the bot on your own server.

### 1\. Prerequisites

  - [Python 3.8](https://www.python.org/downloads/) or higher.
  - A Discord account and administrator permissions on a server where you want to add the bot.

### 2\. Clone the Project

Clone the project to your local machine:

```bash
git clone https://github.com/your-username/discord-bot-project.git
cd discord-bot-project
```

### 3\. Install Dependencies

Create a `requirements.txt` file to manage the project's Python dependencies.

**Contents of `requirements.txt`:**

```
discord.py
python-dotenv
requests
```

Then, install these libraries using `pip`:

```bash
pip install -r requirements.txt
```

### 4\. Obtain API Keys and Bot Token

The bot requires three keys/tokens to function:

1.  **Discord Bot Token:**

      - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
      - Click "New Application" to create a new application.
      - Navigate to the "Bot" tab and click "Add Bot".
      - **IMPORTANT:** In the "Privileged Gateway Intents" section, enable the **MESSAGE CONTENT INTENT**. This is necessary for the bot to read messages.
      - Click "Reset Token" to get your bot's token and copy it to a safe place.

2.  **WeatherAPI Key:**

      - Sign up at [WeatherAPI](https://www.weatherapi.com/signup.aspx).
      - After logging in, get your free API key from your dashboard.

3.  **NewsAPI Key:**

      - Register at [NewsAPI](https://newsapi.org/register).
      - After logging in, you will be provided with your unique API key.

### 5\. Create the Configuration File

In the project's root directory, create a file named `.env` and paste your keys into it as follows:

```env
TOKEN=YOUR_DISCORD_BOT_TOKEN_HERE
WEATHER_API_KEY=YOUR_WEATHERAPI_KEY_HERE
NEWS_API_KEY=YOUR_NEWSAPI_KEY_HERE
```

### 6\. Launch the Bot

Once everything is set up, run the following command in your terminal to start the bot:

```bash
python bot.py
```

*(Note: This assumes your Python file is named `bot.py`.)*

If you see the message `Logged in as YOUR_BOT_NAME!` in the terminal, your bot is successfully online.

## 🚀 Commands and Usage

The bot's command prefix is set to `!`.

| Command | Description | Example Usage |
|---|---|---|
| `!help` | Displays the help menu with all commands. | `!help` |
| `!weather <location>` | Fetches weather information for the specified location. | `!weather London` |
| `!news [category]` | Lists the latest news. (Default: general) | `!news technology` |
| `!coinflip` | Flips a coin. | `!coinflip` |
| `!roll` | Rolls a random die between 1 and 6. | `!roll` |
| `!fact` | Provides a random interesting fact. | `!fact` |
| `!clear <amount>` | Deletes a specified number of messages (max 100). | `!clear 10` |
| `!ping` | Shows the bot's current latency. | `!ping` |

**Note:** Valid categories for the `!news` command are: `general`, `sports`, `technology`, `business`, `health`, `entertainment`.

## ⚙️ Technologies Used

  - [Python](https://www.python.org/)
  - [discord.py](https://discordpy.readthedocs.io/en/stable/)
  - [Requests](https://docs.python-requests.org/en/latest/)
  - [WeatherAPI](https://www.weatherapi.com/)
  - [NewsAPI](https://newsapi.org/)
