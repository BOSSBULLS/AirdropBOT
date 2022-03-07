# --------------------------------------------- #
# Plugin Name           : DiscordAirdropBot     #
# Author Name           : fabston               #
# File Name             : config.py             #
# --------------------------------------------- #

# Enable / disable the airdrop
airdrop_live = True

# Discord
bot_token = ""  # More: https://www.writebots.com/discord-bot-token/
bot_command_prefix = "!"
log_channel = 945410461569003582  # Channel ID. Example: 654874484842692660
admins = ["901783028286754816", "791364020543291432", "923279250663030814", "677348212759330826"]
airdrop_cap = 500  # Max airdrop submissions that are being accepted

# MySQL Database
mysql_host = "localhost"
mysql_db = "DiscordAirdropBot"
mysql_user = "AirdropUser"
mysql_pw = "BBULS"

texts = {
    "airdrop_start": "The airdrop didn't start yet. Please come back later.",
    "airdrop_max_cap": "ℹ️ The airdrop reached its max cap.",
    "airdrop_walletused": "⚠️ That address has already been used. Use a different one.",
    "airdrop_confirmation": "✅ Your address has been added to airdrop list.",
}
