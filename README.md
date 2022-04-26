


## Features

- [x] 𝑨𝒖𝒕𝒐 𝒇𝒊𝒍𝒕𝒆𝒓
- [x] 𝑴𝒂𝒏𝒖𝒍 𝒇𝒊𝒍𝒕𝒆𝒓
- [x] 𝑰𝑴𝑫𝑩 𝒔𝒖𝒑𝒑𝒐𝒓𝒕𝒆𝒅
- [x] 𝑨𝒅𝒎𝒊𝒏 𝒄𝒐𝒎𝒎𝒂𝒏𝒅𝒔
- [x] 𝑩𝒓𝒐𝒂𝒅𝒄𝒂𝒔𝒕
- [x] 𝑰𝒏𝒅𝒆𝒙
- [x] 𝑰𝑴𝑫𝑩 𝒔𝒆𝒂𝒓𝒄𝒉
- [x] 𝑰𝒏𝒍𝒊𝒏𝒆 𝒔𝒆𝒂𝒓𝒄𝒉
- [x] 𝑹𝒂𝒏𝒅𝒐𝒎 𝒔𝒕𝒂𝒓𝒕 𝒑𝒊𝒄𝒔
- [x] 𝑰𝒅𝒔 𝒂𝒏𝒅 𝒖𝒔𝒆𝒓 𝒊𝒏𝒇𝒐
- [x] 𝑺𝒕𝒂𝒕𝒔, 𝑼𝒔𝒆𝒓𝒔, 𝑪𝒉𝒂𝒕𝒔, 𝑩𝒂𝒏, 𝑼𝒏𝒃𝒂𝒏, 𝑳𝒆𝒂𝒗𝒆, 𝑫𝒊𝒔𝒂𝒃𝒍𝒆, 𝑪𝒉𝒂𝒏𝒏𝒆𝒍

## Variables

### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/1G1XwEOnxxo)
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/1G1XwEOnxxo)
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel.



## Commands
```
• /logs - to get the rescent errors
• /stats - to get status of files in db.
* /filter - add manual filters
* /filters - view filters
* /connect - connect to PM.
* /disconnect - disconnect from PM
* /del - delete a filter
* /delall - delete all filters
* /deleteall - delete all index(autofilter)
* /delete - delete a specific file from index.
* /info - get user info
* /id - get tg ids.
* /imdb - fetch info from imdb.
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids 
• /index  - to add files from a channel
• /leave  - to leave from a chat.
• /disable  -  do disable a chat.
* /enable - re-enable chat.
• /ban  - to ban a user.
• /unban  - to unban a user.
• /channel - to get list of total connected channels
• /broadcast - to broadcast a message to all Eva Maria users
```
## Deploy
You can deploy this bot anywhere.

<i>**[Watch Deploying Tutorial...](https://youtu.be/fyFKnde_Jz8)**</i>

<details><summary>Deploy To Heroku</summary>
<p>
<br>
<a href="<a href="https://heroku.com/deploy?template=https://github.com/dmxbasil/cl-autofilter-2tree/master">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p>
</details>

<details><summary>Deploy To Railway</summary>
<p>
<br>

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Frailwayapp%2Fexamples%2Ftree%2Fmaster%2Fexamples%2Fflask&envs=ADMINS%2CAPI_HASH%2CAPI_ID%2CAUTH_CHANNEL%2CAUTH_USERS%2CBOT_TOKEN%2CCACHE_TIME%2CCHANNELS%2CCOLLECTION_NAME%2CCUSTOM_FILE_CAPTION%2CDATABASE_NAME%2CDATABASE_URI%2CIMDB%2CLOG_CHANNEL%2CP_TTI_SHOW_OFF%2CPICS%2CSINGLE_BUTTON%2CSUPPORT_CHAT%2CUSE_CAPTION_FILTER&optionalEnvs=CACHE_TIME%2CCOLLECTION_NAME%2CCUSTOM_FILE_CAPTION%2CDATABASE_NAME%2CIMDB%2CP_TTI_SHOW_OFF%2CSINGLE_BUTTON%2CSUPPORT_CHAT%2CUSE_CAPTION_FILTER&ADMINSDesc=Username+or+ID+of+Admin.+Separate+multiple+Admins+by+space.&API_HASHDesc=Get+this+value+from+https%3A%2F%2Fmy.telegram.org+or+https%3A%2F%2Fyoutu.be%2F5eEsvLAKVc0&API_IDDesc=Get+this+value+from+https%3A%2F%2Fmy.telegram.org+or+https%3A%2F%2Fyoutu.be%2F5eEsvLAKVc0&AUTH_CHANNELDesc=ID+of+channel.Make+sure+bot+is+admin+in+this+channel.+Without+subscribing+this+channel+users+cannot+use+bot.&AUTH_USERSDesc=Username+or+ID+of+users+to+give+access+of+inline+search.+Separate+multiple+users+by+space.+Leave+it+empty+if+you+don%27t+want+to+restrict+bot+usage.&BOT_TOKENDesc=Your+bot+token.&CACHE_TIMEDesc=The+maximum+amount+of+time+in+seconds+that+the+result+of+the+inline+query+may+be+cached+on+the+server&CHANNELSDesc=Username+or+ID+of+channel+or+group.+Separate+multiple+IDs+by+space.+File+Channel+id&COLLECTION_NAMEDesc=Name+of+the+collections.+Defaults+to+Telegram_files.+If+you+are+using+the+same+database%2C+then+use+different+collection+name+for+each+bot&CUSTOM_FILE_CAPTIONDesc=A+custom+file+caption+for+your+files.+formatable+with+%2C+file_name%2C+file_caption%2C+file_size%2C+Read+Readme.md+for+better+understanding.&DATABASE_NAMEDesc=Name+of+the+database+in+mongoDB.+For+more+help+watch+this+video+-+https%3A%2F%2Fyoutu.be%2FgBLTsH-IXr0&DATABASE_URIDesc=mongoDB+URI.+Get+this+value+from+https%3A%2F%2Fwww.mongodb.com.+For+more+help+watch+this+video+-+https%3A%2F%2Fyoutu.be%2FgBLTsH-IXr0&IMDBDesc=Imdb%2C+the+view+of+information+when+making+True%2FFalse&LOG_CHANNELDesc=Bot+Logs%2CGive+a+channel+id+with+-100xxxxxxx&P_TTI_SHOW_OFFDesc=Customize+Result+Buttons+to+Callback+or+Url+by+%28True+%3D+url+%2F+False+%3D+callback%29&PICSDesc=Add+some+telegraph+link+of+pictures+.%40MT_telegraph_bot&SINGLE_BUTTONDesc=choose+b%2Fw+single+or+double+buttons+https%3A%2F%2Fgithub.com%2FEvamariaTG%2FEvaMaria%2Fissues%2F22&SUPPORT_CHATDesc=Username+of+a+Support+Group+%2F+ADMIN.+%28+Should+be+username+without+%40+and+not+ID%29&USE_CAPTION_FILTERDesc=Whether+bot+should+use+captions+to+improve+search+results.+%28True+False%29&referralCode=MoTech)

</a>
</p>
</details>

<details><summary>Deploy To VPS</summary>
<p>
<pre>
git clone https://github.com/EvamariaTG/evamaria
# Install Packages
pip3 install -r requirements.txt
Edit info.py with variables as given below then run bot
python3 bot.py
</pre>
</p>
</details>
