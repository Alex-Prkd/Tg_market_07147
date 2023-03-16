from aiogram.utils import executor

from view.handler import dp


if __name__ == '__main__':
    executor.start_polling(dp)