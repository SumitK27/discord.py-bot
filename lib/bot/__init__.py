from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase

PREFIX = "+"
OWNER_IDS = [468490331135016961]

class Bot(BotBase):
	def __init__(self):
		self.PREFIX = PREFIX
		self.ready = False
		self.guild = None
		self.scheduler = AsyncIOScheduler()

		super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

	def run(self, version):
		self.VERSION = version

		with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
			self.TOKEN = tf.read()

		print("Running Bot...")
		super().run(self.TOKEN, reconnect=True)

	async def on_connect(self):
		print("Bot Connected!!!")

	async def on_disconnect(self):
		print("Bot Disconnected!!!")

	async def on_ready(self):
		if not self.ready:
			self.ready = True
			self.guild = self.get_guild(715185011229327410)
			print("Bot Ready")
		else:
			print("Bot Reconnected")	

	async def on_message(self, message):
		pass

bot = Bot()
