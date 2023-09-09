import nextcord
from nextcord.ext import commands
import datetime
import sqlite3

class HappyBirthday(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db_conn = sqlite3.connect('databases/birthdays.db')
        self.db_cursor = self.db_conn.cursor()
        self.create_table()

    def create_table(self):
        self.db_cursor.execute('''
            CREATE TABLE IF NOT EXISTS birthdays (
                user_id INTEGER PRIMARY KEY,
                birthday TEXT
            )
        ''')
        self.db_conn.commit()

    @commands.Cog.listener()
    async def on_ready(self):
        while not self.bot.is_closed():
            today = datetime.date.today()

            self.db_cursor.execute('SELECT user_id FROM birthdays WHERE birthday = ?', (today,))
            users_with_birthday = self.db_cursor.fetchall()

            for user_id in users_with_birthday:
                user = self.bot.get_user(user_id[0])
                if user:
                    try:
                        await user.send('Happy birthday! 🎉')
                    except nextcord.Forbidden:
                        # Handle cases where the bot doesn't have permission to send a DM to the user.
                        pass

            await nextcord.utils.sleep_until(datetime.datetime.now() + datetime.timedelta(days=1))

    @nextcord.slash_command(name="set_bday", description="Set your birthday date (format: DD-MM)")
    async def set_birthday(self, ctx, date: str):
        try:
            birthday = datetime.datetime.strptime(date, '%d-%m').date()
        except ValueError:
            await ctx.send('Invalid date format. Please use DD-MM.')
            return

        user_id = ctx.user.id  # Corrected line

        # Store user's birthday in the database
        self.db_cursor.execute('''
            INSERT OR REPLACE INTO birthdays (user_id, birthday)
            VALUES (?, ?)
        ''', (user_id, birthday))

        self.db_conn.commit()

        await ctx.send(f'{ctx.user.mention}, your birthday has been set to {date}.')


def setup(bot):
    bot.add_cog(HappyBirthday(bot))
