# Nextcord Discord Bot Template

<p align="center">
  <br><b>Useful Links</b></br>
  <a href="https://github.com/nextcord/nextcord">Nextcord Github</a> -
  <a href="https://docs.nextcord.dev/en/stable/api.html">Nextcord API Reference</a> -
  <a href="https://discord.com/developers/applications">Discord Developer</a> -
  <a href="https://support.discord.com/hc/en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline-">Discord Markdown Text</a>
</p>

## Current Commands

### Moderation
- `/ban`
- `/kick`
- `/clear (messages)`

### Info
- `/advanced_userinfo`
- `/basic_userinfo`
- `/serverinfo`
- `/avatar`

### Misc
- `/ping`

## Setup

Follow these steps to set up your Discord bot using this template:

1. Install [Python](https://www.python.org/).

2. Install the required Python packages by running the following command:
- `pip install -r requirements.txt-`

3. Edit the configuration in `/json/configuration.json` to include your bot token and prefix.

4. Run the bot with the following command:
- `python main.py` or `python3 main.py`


## Userinfo Command

To make the Userinfo command work as expected, follow these additional steps:

1. Upload the emojis located in `misc/emojis` to your Discord server. Note that your bot must be in the server to use these emojis.

![Emojis](/misc/images/emojis.png?raw=true "Demo")

2. Obtain the ID of each custom emoji by using the following format: `\:emoji_name:`. This will output something like `<:emoji_name:1132376957959540757>`. Replace `emoji_name` with the name of each emoji.

3. Edit the file `cogs/random/userinfo.py` and modify the following code to include the custom emojis:

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

## Outcome
![Image](/misc/images/advanced_userinfo.png?raw=true "Demo")
