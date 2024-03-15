1. Add @BotFather
2. Creat a new bot with command /newbot

    I can help you create and manage Telegram bots. If you're new to the Bot API, please see the manual (https://core.telegram.org/bots).

    You can control me by sending these commands:

    /newbot - create a new bot
    /mybots - edit your bots

    Edit Bots
    /setname - change a bot's name
    /setdescription - change bot description
    /setabouttext - change bot about info
    /setuserpic - change bot profile photo
    /setcommands - change the list of commands
    /deletebot - delete a bot

    Bot Settings
    /token - generate authorization token
    /revoke - revoke bot access token
    /setinline - toggle inline mode (https://core.telegram.org/bots/inline)
    /setinlinegeo - toggle inline location requests (https://core.telegram.org/bots/inline#location-based-results)
    /setinlinefeedback - change inline feedback (https://core.telegram.org/bots/inline#collecting-feedback) settings
    /setjoingroups - can your bot be added to groups?
    /setprivacy - toggle privacy mode (https://core.telegram.org/bots/features#privacy-mode) in groups

    Web Apps
    /myapps - edit your web apps (https://core.telegram.org/bots/webapps)
    /newapp - create a new web app (https://core.telegram.org/bots/webapps)
    /listapps - get a list of your web apps
    /editapp - edit a web app
    /deleteapp - delete an existing web app

    Games
    /mygames - edit your games (https://core.telegram.org/bots/games)
    /newgame - create a new game (https://core.telegram.org/bots/games)
    /listgames - get a list of your games
    /editgame - edit a game
    /deletegame - delete an existing game

https://api.telegram.org/bot7039625967:AAGDIWEqVmTq_ZIkVk52cv8rP2eXRgHHTQQ/getUpdates

```
{
    "ok": true,
    "result": [
        {
            "update_id": 635936688,
            "message": {
                "message_id": 5,
                "from": {
                    "id": 5972474843,
                    "is_bot": false,
                    "first_name": "Jacob",
                    "last_name": "Vu",
                    "username": "jacobvu84"
                },
                "chat": {
                    "id": -4154348388, // GROUP_CHAT_ID
                    "title": "telegram bot api",
                    "type": "group",
                    "all_members_are_administrators": true
                },
                "date": 1710491398,
                "text": "/start",
                "entities": [
                    {
                        "offset": 0,
                        "length": 6,
                        "type": "bot_command"
                    }
                ]
            }
        }
    ]
}
```