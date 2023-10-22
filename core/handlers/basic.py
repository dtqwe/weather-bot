from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
import core.keyboards.reply as kb
import aiohttp

from core.utils.utils import weather_descriptions_russian, precipitation_probabilities_russian

owm_api_key = '471a41a84c5d5aa8b0ad5864e45eaa3f'

router = Router()
    
@router.message(F.text == '/start')
async def on_start(message: Message):
    await message.answer(f'👋 Привет, <b>{message.from_user.first_name}</b>! Я бот, который предоставляет информацию о 🌦️ <b>погоде</b>. Чтобы узнать все команды, используй команду /help.', parse_mode='HTML')

@router.message(F.text == '/help')
async def on_help(message: Message):
    await message.answer('<b>Для получения погоды, используйте команду /weather город или воспользуйтесь удобным интерфейсом с выбором, набрав команду /wt.</b>', parse_mode='HTML')

@router.message(F.text == '/wt')
async def wt(message: Message):
    await message.answer('Выбери страну ниже:', reply_markup=kb.main)

# ------------------------------- RUSSIA ------------------------------------
@router.message(F.text == '🇷🇺Россия')
async def wt_ru(message: Message):
    await message.answer('Выбери город:', reply_markup=kb.cityOfRu)

@router.callback_query(F.data == 'moscow')
async def moscow(callback: CallbackQuery):
    await handle_weather_callback(callback, 'Москва')

@router.callback_query(F.data == 'piter')
async def piter(callback: CallbackQuery):
    await handle_weather_callback(callback, 'Санкт-Петербург')

@router.callback_query(F.data == 'kazan')
async def kazan(callback: CallbackQuery):
    await handle_weather_callback(callback, 'Казань')

@router.callback_query(F.data == 'omsk')
async def omsk(callback: CallbackQuery):
    await handle_weather_callback(callback, 'Омск')

@router.callback_query(F.data == 'backToMainfromRu')
async def backToMainfromRu(callback: CallbackQuery):
    await callback.answer('Назад')
    await callback.message.answer('Назад', reply_markup=kb.main)
# ------------------------------------ END RUSSIA ---------------------------

# ------------------------------------ KAZAKHSTAN ---------------------------
@router.message(F.text == '🇰🇿Казахстан')
async def wt_kz(message: Message):
    await message.answer('Выбери город:', reply_markup=kb.cityOfKz)

@router.callback_query(F.data == 'astana')
async def astana(callback: CallbackQuery):
    await handle_weather_callback(callback, 'Астана')

@router.callback_query(F.data == 'almaty')
async def almaty(callback: CallbackQuery):
    await handle_weather_callback(callback, 'Алматы')

@router.callback_query(F.data == 'petro')
async def petro(callback: CallbackQuery):
    await handle_weather_callback(callback, 'Петропавловск')

@router.callback_query(F.data == 'aktobe')
async def aktobe(callback: CallbackQuery):
    await handle_weather_callback(callback, 'Актобе')

@router.callback_query(F.data == 'backToMainfromKz')
async def backToMainfromKz(callback: CallbackQuery):
    await callback.answer('Назад')
    await callback.message.answer('Назад', reply_markup=kb.main)
# ------------------------------------ END KAZAKHSTAN -----------------------

# ------------------------------------ Ukraine ------------------------------
@router.message(F.text == '🇺🇦Украина')
async def wt_ua(message: Message):
    await message.answer('Выбери город:', reply_markup=kb.cityOfUa)

@router.callback_query(F.data == 'kiev')
async def kiev(callback: CallbackQuery):
    await handle_weather_callback(callback, 'Киев')

@router.callback_query(F.data == 'odessa')
async def odessa(callback: CallbackQuery):
    await handle_weather_callback(callback, 'Одесса')

@router.callback_query(F.data == 'lvov')
async def lvov(callback: CallbackQuery):
    await handle_weather_callback(callback, 'Львов')

@router.callback_query(F.data == 'dnepr')
async def dnepr(callback: CallbackQuery):
    await handle_weather_callback(callback, 'Днепр')

@router.callback_query(F.data == 'backToMainfromUa')
async def backToMainfromUa(callback: CallbackQuery):
    await callback.answer('Назад')
    await callback.message.answer('Назад', reply_markup=kb.main)
# ------------------------------------ END UKRAINE --------------------------

# ------------------------------------ BELARUS ---------------------------
@router.message(F.text == '🇧🇾Беларусь')
async def wt_by(message: Message):
    await message.answer('Выбери город:', reply_markup=kb.cityOfBy)

@router.callback_query(F.data == 'minsk')
async def minsk(callback: CallbackQuery):
    await handle_weather_callback(callback, 'Минск')

@router.callback_query(F.data == 'gomel')
async def gomel(callback: CallbackQuery):
    await handle_weather_callback(callback, 'Гомель')

@router.callback_query(F.data == 'vitebsk')
async def vitebsk(callback: CallbackQuery):
    await handle_weather_callback(callback, 'Витебск')

@router.callback_query(F.data == 'brest')
async def brest(callback: CallbackQuery):
    await handle_weather_callback(callback, 'Брест')

@router.callback_query(F.data == 'backToMainfromBy')
async def backToMainfromBy(callback: CallbackQuery):
    await callback.answer('Назад')
    await callback.message.answer('Назад', reply_markup=kb.main)
# ------------------------------------ END BELARUS -----------------------


@router.message(F.text.startswith('/weather'))
async def get_weather(message: Message):
    try:
        city = message.text.split(' ', 1)[1]
        weather_info = await get_weather_details(city)
        if weather_info:
            temperature = weather_info['temperature']
            min_temperature = weather_info['min_temperature']
            max_temperature = weather_info['max_temperature']
            humidity = weather_info['humidity']
            wind_speed = weather_info['wind_speed']
            weather_description = weather_info['weather_description']
            precipitation_probability = weather_info['precipitation_probability']

            weather_text = f'Погода в  🏙️ {city}:\n'
            weather_text += f'Текущая температура: 🌡️ {temperature}°C\n'
            weather_text += f'Минимальная температура: {"❄️" if min_temperature <= 0 else "☀️"} {min_temperature}°C\n'
            weather_text += f'Максимальная температура: {"☀️" if max_temperature >= 0 else "❄️"} {max_temperature}°C\n'
            weather_text += f'Влажность: 💧 {humidity}%\n'
            weather_text += f'Скорость ветра: 🌬️ {wind_speed} м/с\n'
            weather_text += f'Описание погоды: {weather_description}\n'
            weather_text += f'Вероятность осадков: 🌂 {precipitation_probability}\n'

            await message.answer(weather_text)
        else:
            await message.answer('Информация о погоде недоступна')
    except IndexError:
        await message.answer('Вы не указали город!')

async def handle_weather_callback(callback: CallbackQuery, city_name):
    await callback.answer(f'Вы выбрали {city_name}')
    city = city_name
    weather_info = await get_weather_details(city)

    if weather_info:
        temperature = weather_info['temperature']
        min_temperature = weather_info['min_temperature']
        max_temperature = weather_info['max_temperature']
        humidity = weather_info['humidity']
        wind_speed = weather_info['wind_speed']
        weather_description = weather_info['weather_description']
        precipitation_probability = weather_info['precipitation_probability']

        weather_text = f'Погода в  🏙️ {city}:\n'
        weather_text += f'Текущая температура: 🌡️ {temperature}°C\n'
        weather_text += f'Минимальная температура: {"❄️" if min_temperature <= 0 else "☀️"} {min_temperature}°C\n'
        weather_text += f'Максимальная температура: {"☀️" if max_temperature >= 0 else "❄️"} {max_temperature}°C\n'
        weather_text += f'Влажность: 💧 {humidity}%\n'
        weather_text += f'Скорость ветра: 🌬️ {wind_speed} м/с\n'
        weather_text += f'Описание погоды: {weather_description}\n'
        weather_text += f'Вероятность осадков: 🌂 {precipitation_probability}\n'

        await callback.message.answer(weather_text, reply_markup=None)
    else:
        await callback.message.answer('Информация о погоде недоступна', reply_markup=None)


# функция для получения подробной информации о погоде
async def get_weather_details(city):
    async with aiohttp.ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={owm_api_key}&units=metric'
        async with session.get(url) as response:
            data = await response.json()
            if data.get('main') and data['main'].get('temp'):
                temperature = data['main']['temp']
                min_temperature = data['main']['temp_min']
                max_temperature = data['main']['temp_max']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']

                weather_description = weather_descriptions_russian.get(data['weather'][0]['description'], 'нет данных')
                precipitation_probability = precipitation_probabilities_russian.get(data.get('pop', 'N/A'), 'нет данных')

                return {
                    'temperature': round(temperature),
                    'min_temperature': round(min_temperature),
                    'max_temperature': round(max_temperature),
                    'humidity': humidity,
                    'wind_speed': wind_speed,
                    'weather_description': weather_description,
                    'precipitation_probability': precipitation_probability
                }
            else:
                return None  # Информация о погоде недоступна