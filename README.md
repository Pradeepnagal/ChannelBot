
### Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?)

1. Tap on above button and fill `API_ID`, `API_HASH`, `BOT_TOKEN` (and `MUST_JOIN`).
2. Then tap "Deploy App" below it. Wait till deploying is complete (will take atmost 2 minutes).
3. After deploying is complete, tap on "Manage App"
4. Check the logs to see if your bot is ready!

### Local Deploying

1. Clone the repo
   ```markdown
   git clone https://github.com/StarkBotsIndustries/ChannelBot
   ```
   
2. Get a DATABASE_URL. If you don't know how, deploy using Heroku Button only or delete database things as it's not a compulsion.
   
3. Edit `Config.py` and fill the needed variables

4. Enter the directory
   ```markdown
   cd ChannelBot
   ```
5. Run the file
   ```markdown
   python3 channelbot.py
   ```

## Environment Variables

#### Mandatory Vars

- `API_ID` - Get this from [my.telegram.org](https://my.telegram.org/auth)
- `API_HASH` - Get this from [my.telegram.org](https://my.telegram.org/auth)
- `BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather)
- `DATABASE_URL` - Will be automatically added by Heroku.
- `MUST_JOIN` - Username/ID of your telegram channel/group.

## Functions


1) Automatically add caption
2) Automatically post sticker after every message.
3) Add URL buttons to every message.
4) Various settings like Edit Mode, Caption Mode and Webpage Preview

