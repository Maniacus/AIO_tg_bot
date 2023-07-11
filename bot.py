from config_data.config import load_config


config = load_config('.env')

#print(config.tg_bot)

bot_token = config.tg_bot.token           # Сохраняем токен в переменную bot_token
superadmin = config.tg_bot.admin_ids[0]   # Сохраняем ID админа в переменную superadmin

print(bot_token)
print(superadmin)