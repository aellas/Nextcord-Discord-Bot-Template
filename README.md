# Nextcord Bot Template

<p align="center">
<br><b>Useful Links</b></br>
        <a href="https://github.com/nextcord/nextcord">Nextcord Github</a> - <a href="https://docs.nextcord.dev/en/stable/api.html">Nextcord API Reference</a> - <a href="https://discord.com/developers/applications">Discord Developer</a> - <a href="https://support.discord.com/hc/en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline-">Discord Markdown Text</a>
</p>

# Commands
<br><b>Moderation</b></br>
`/ban` `/kick` `/clear (messages)`

<br><b>Info</b></br>
`/advanced_userinfo` `/basic_userinfo` `/serverinfo` `/avatar`

<br><b>Misc</b></br>
`/ping`

# Setup
+ Install [Python](https://www.python.org/)
+ Install requirements `pip intall -r requirements.txt`
+ Edit `/json/configuration.json` and add your [token, prefix & owner_name]
+ Run project `python main.py`

# Userinfo Command
+ Upload the emojis located in `misc/emojis` and add each custom emoji to your discord server (bot must be in server to use)
![Image](/misc/images/emojis.png?raw=true "Demo")
+ Grab each emoji's ID, you can do this by using `\:emoji_name:` this will output `<:emoji_name:1132376957959540757>` (change emoji_name to the name you set for each emoji)
+ Edit `cogs/random/userinfo.py` and edit this code
```python
        badges = ""
        if user.public_flags.staff:
            badges += "<:discord_staff:1132379154654957669> "
        if user.public_flags.partner:
            badges += "<:partner:1132378094855004160> "
        if user.public_flags.hypesquad:
            badges += "<:hypesquad:1132378611635191828> "
        if user.public_flags.bug_hunter:
            badges += "<:discord_staff:1132379154654957669> "
        if user.public_flags.bug_hunter_level_2:
            badges += "<:bughunter_level2:1132378990787694733> "
        if user.public_flags.hypesquad_bravery:
            badges += "<:hypesquad_bravery:1132377049026269334> "
        if user.public_flags.hypesquad_brilliance:
            badges += "<:hypesquad_balance:1132376844436521012> "
        if user.public_flags.hypesquad_balance:
            badges += "<:hypsesquad_balance:1132374887428800606> "
        if user.public_flags.early_supporter:
            badges += "<:early_supporter:1132376957959540757> "
        if user.public_flags.active_developer:
            badges += "<:active_developer:1132377229914026106> "
        if user.public_flags.discord_certified_moderator:
            badges += "<:moderator:1132378418055483562> "
        if user.public_flags.verified_bot_developer:
            badges += "<:verified_bot_developer:1132379960674357248> "
```
+ Replace each emoji with your `<:emoji_name:1132376957959540757>`

## Outcome
![Image](/misc/images/advanced_userinfo.png?raw=true "Demo")






