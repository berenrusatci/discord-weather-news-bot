<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multi-Purpose Discord Bot README</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
            line-height: 1.6;
            color: #24292e;
            max-width: 800px;
            margin: 0 auto;
            padding: 30px;
        }
        h1, h2, h3 {
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
            font-weight: 600;
        }
        code {
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
            background-color: rgba(27,31,35,0.05);
            padding: 0.2em 0.4em;
            margin: 0;
            font-size: 85%;
            border-radius: 3px;
        }
        pre code {
            display: block;
            padding: 16px;
            overflow: auto;
            font-size: 85%;
            line-height: 1.45;
            border-radius: 6px;
        }
        a {
            color: #0366d6;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-top: 1em;
            display: block;
            overflow: auto;
        }
        th, td {
            border: 1px solid #dfe2e5;
            padding: 8px 12px;
            text-align: left;
        }
        th {
            background-color: #f6f8fa;
            font-weight: 600;
        }
        ul, ol {
            padding-left: 2em;
        }
    </style>
</head>
<body>

    <h1>Multi-Purpose Discord Bot</h1>

    <p>This project is a multi-purpose Discord bot developed using Python and the <code>discord.py</code> library. It offers various features such as querying weather information, listing the latest news, performing simple moderation tasks, and providing several fun commands.</p>

    <h2>✨ Features</h2>
    <ul>
        <li><strong>Weather Forecast:</strong> Fetches real-time weather data for a specified location from <a href="https://www.weatherapi.com/" target="_blank" rel="noopener noreferrer">WeatherAPI</a> and presents it as a rich embed message.</li>
        <li><strong>Latest News:</strong> Lists the top 5 latest news articles from various categories like general, sports, and technology using <a href="https://newsapi.org/" target="_blank" rel="noopener noreferrer">NewsAPI</a>.</li>
        <li><strong>Fun Commands:</strong>
            <ul>
                <li><code>!coinflip</code>: Flips a coin.</li>
                <li><code>!roll</code>: Rolls a random 1-6 sided die.</li>
                <li><code>!fact</code>: Displays an interesting fact.</li>
            </ul>
        </li>
        <li><strong>Moderation:</strong>
            <ul>
                <li><code>!clear &lt;amount&gt;</code>: Deletes a specified number of messages from the channel (max 100).</li>
            </ul>
        </li>
        <li><strong>Utility Commands:</strong>
            <ul>
                <li><code>!ping</code>: Shows the bot's current latency.</li>
                <li><code>!help</code>: Displays a help menu with all commands and their descriptions.</li>
            </ul>
        </li>
    </ul>

    <h2>🛠️ Setup and Installation</h2>
    <p>Follow the steps below to run the bot on your own server.</p>

    <h3>1. Prerequisites</h3>
    <ul>
        <li><a href="https://www.python.org/downloads/" target="_blank" rel="noopener noreferrer">Python 3.8</a> or higher.</li>
        <li>A Discord account and administrator permissions on a server where you want to add the bot.</li>
    </ul>

    <h3>2. Clone the Project</h3>
    <p>Clone the project to your local machine:</p>
    <pre><code>git clone https://github.com/your-username/discord-bot-project.git
cd discord-bot-project</code></pre>

    <h3>3. Install Dependencies</h3>
    <p>Create a <code>requirements.txt</code> file to manage the project's Python dependencies.</p>
    <p><strong>Contents of <code>requirements.txt</code>:</strong></p>
    <pre><code>discord.py
python-dotenv
requests</code></pre>
    <p>Then, install these libraries using <code>pip</code>:</p>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h3>4. Obtain API Keys and Bot Token</h3>
    <p>The bot requires three keys/tokens to function:</p>
    <ol>
        <li><strong>Discord Bot Token:</strong>
            <ul>
                <li>Go to the <a href="https://discord.com/developers/applications" target="_blank" rel="noopener noreferrer">Discord Developer Portal</a>.</li>
                <li>Click "New Application" to create a new application.</li>
                <li>Navigate to the "Bot" tab and click "Add Bot".</li>
                <li><strong>IMPORTANT:</strong> In the "Privileged Gateway Intents" section, enable the <strong>MESSAGE CONTENT INTENT</strong>. This is necessary for the bot to read messages.</li>
                <li>Click "Reset Token" to get your bot's token and copy it to a safe place.</li>
            </ul>
        </li>
        <li><strong>WeatherAPI Key:</strong>
            <ul>
                <li>Sign up at <a href="https://www.weatherapi.com/signup.aspx" target="_blank" rel="noopener noreferrer">WeatherAPI</a>.</li>
                <li>After logging in, get your free API key from your dashboard.</li>
            </ul>
        </li>
        <li><strong>NewsAPI Key:</strong>
            <ul>
                <li>Register at <a href="https://newsapi.org/register" target="_blank" rel="noopener noreferrer">NewsAPI</a>.</li>
                <li>After logging in, you will be provided with your unique API key.</li>
            </ul>
        </li>
    </ol>

    <h3>5. Create the Configuration File</h3>
    <p>In the project's root directory, create a file named <code>.env</code> and paste your keys into it as follows:</p>
    <pre><code>TOKEN=YOUR_DISCORD_BOT_TOKEN_HERE
WEATHER_API_KEY=YOUR_WEATHERAPI_KEY_HERE
NEWS_API_KEY=YOUR_NEWSAPI_KEY_HERE</code></pre>

    <h3>6. Launch the Bot</h3>
    <p>Once everything is set up, run the following command in your terminal to start the bot:</p>
    <pre><code>python bot.py</code></pre>
    <p><em>(Note: This assumes your Python file is named <code>bot.py</code>.)</em></p>
    <p>If you see the message <code>Logged in as YOUR_BOT_NAME!</code> in the terminal, your bot is successfully online.</p>

    <h2>🚀 Commands and Usage</h2>
    <p>The bot's command prefix is set to <code>!</code>.</p>
    <table>
        <thead>
            <tr>
                <th>Command</th>
                <th>Description</th>
                <th>Example Usage</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>!help</code></td>
                <td>Displays the help menu with all commands.</td>
                <td><code>!help</code></td>
            </tr>
            <tr>
                <td><code>!weather &lt;location&gt;</code></td>
                <td>Fetches weather information for the specified location.</td>
                <td><code>!weather London</code></td>
            </tr>
            <tr>
                <td><code>!news [category]</code></td>
                <td>Lists the latest news. (Default: general)</td>
                <td><code>!news technology</code></td>
            </tr>
            <tr>
                <td><code>!coinflip</code></td>
                <td>Flips a coin.</td>
                <td><code>!coinflip</code></td>
            </tr>
            <tr>
                <td><code>!roll</code></td>
                <td>Rolls a random die between 1 and 6.</td>
                <td><code>!roll</code></td>
            </tr>
            <tr>
                <td><code>!fact</code></td>
                <td>Provides a random interesting fact.</td>
                <td><code>!fact</code></td>
            </tr>
            <tr>
                <td><code>!clear &lt;amount&gt;</code></td>
                <td>Deletes a specified number of messages (max 100).</td>
                <td><code>!clear 10</code></td>
            </tr>
            <tr>
                <td><code>!ping</code></td>
                <td>Shows the bot's current latency.</td>
                <td><code>!ping</code></td>
            </tr>
        </tbody>
    </table>
    <p><strong>Note:</strong> Valid categories for the <code>!news</code> command are: <code>general</code>, <code>sports</code>, <code>technology</code>, <code>business</code>, <code>health</code>, <code>entertainment</code>.</p>

    <h2>⚙️ Technologies Used</h2>
    <ul>
        <li><a href="https://www.python.org/" target="_blank" rel="noopener noreferrer">Python</a></li>
        <li><a href="https://discordpy.readthedocs.io/en/stable/" target="_blank" rel="noopener noreferrer">discord.py</a></li>
        <li><a href="https://docs.python-requests.org/en/latest/" target="_blank" rel="noopener noreferrer">Requests</a></li>
        <li><a href="https://www.weatherapi.com/" target="_blank" rel="noopener noreferrer">WeatherAPI</a></li>
        <li><a href="https://newsapi.org/" target="_blank" rel="noopener noreferrer">NewsAPI</a></li>
    </ul>

</body>
</html>
