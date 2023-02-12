# python3 -m venv .folder  - команда в терменале для создания папки где будут лежать библиотеки

# from progress.bar import Bar
# from isOdd import isOdd #проверка на нечетность

# print(isOdd(0)) 
# print(isOdd(2)) 

################ прогресс-бар ###############


# bar = Bar('Processing', max=20)
# import time
# for i in range(20):
#     time.sleep(0.01)
#     # Do some work
#     bar.next()
# bar.finish()


################ эмоджи ###############
# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))

############### графики ###############

# import matplotlib.pyplot as plt
# import numpy as np

# Fixing random state for reproducibility
# import matplotlib.pyplot as plt
# import numpy as np
# list = [1, 2, 3 ,2, 7]
# plt.plot(list)
# plt.show()

######### бот телеги ################

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *




app = ApplicationBuilder().token("5962550647:AAF6M-uVCbMkcVJzXfhFMqLaPo1IUQ-vZNs").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.run_polling()
