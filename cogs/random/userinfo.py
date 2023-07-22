import nextcord
from nextcord.ext import commands
from nextcord.utils import format_dt


class UserinfoCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(name="basic_userinfo", description="Get basic information on a user")
    async def basicuserinfo(self, interaction: nextcord.Interaction, user: nextcord.User):
        await interaction.response.send_message(f"Name: {user.name}\nID: {user.id}\nAccount created at: {user.created_at}")
        
    @nextcord.slash_command(name="advanced_userinfo", description="More advanced userinfo command")
    async def advanceduserinfo(self, interaction: nextcord.Interaction, user: nextcord.User):
        bot = str(user.bot).replace("False", "User").replace("True", "Bot")
        created = format_dt(user.created_at, "R")
        joined = format_dt(interaction.user.joined_at, "R")
        roles = [role.mention for role in user.roles if role.name != "@everyone"]
        role = str(roles).replace("[", "").replace("]", "").replace("'", "").replace(",", " ")
        status = str(user.status).replace("dnd", "<:dnd_badge:1132382322218508349> DND").replace("online", "<:online_badge:1132382196590714880> Online").replace("idle", "<:idle_badge:1132382200155881603> Idle").replace("offline", "<:offline_badge:1132382195097550868> Offline")

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

        embed = nextcord.Embed(color=nextcord.Color.blurple())
        embed.set_author(name=user.name, icon_url="https://cdn3.emoji.gg/emojis/2986-discord-username.png")
        embed.set_thumbnail(url=user.avatar)
        embed.set_footer(text=user.id, icon_url="https://cryptologos.cc/logos/space-id-id-logo.png")
        embed.add_field(name="User Mention", value=user.mention, inline=True)
        embed.add_field(name="User or Bot?", value=bot, inline=True)
        embed.add_field(name="Account Created", value=created, inline=True)
        embed.add_field(name="User Status", value=status, inline=True)
        embed.add_field(name="Server Position", value=f"{interaction.guild.members.index(user)}/{len(interaction.guild.members)}", inline=True)
        embed.add_field(name="Joined Server", value=joined, inline=True)
        embed.add_field(name="User Badges", value=badges, inline=True)
        embed.add_field(name="User Roles", value=role, inline=False)

        await interaction.response.send_message(embed=embed)
        

def setup(bot):
    bot.add_cog(UserinfoCog(bot))