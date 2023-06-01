from aiogram import Router, Bot
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, CallbackQuery, pre_checkout_query, successful_payment, LabeledPrice, FSInputFile, \
    InputMediaPhoto, InputMediaDocument
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from config_data.config import load_config, PHOTOS
from keyboards import user_keyboards
from keyboards.keyboard_utils import get_inline_keyboard
from lexicon.lexicon_ru import LEXICON_RU

router = Router()

import os


class GetUserInfo(StatesGroup):
    new_user = State()
    service = State()  # Тип косметической процедуры
    master = State()  # Специалист, к которому происходит запись
    date = State()  # Дата посещения
    time = State()  # Время посещения
    name = State()  # Имя, которое ввел клиент
    phone = State()  # Телефон клиента
    pay = State()  # Оплатил ли клиент процедуру сразу (True/False)
    pay_yes = State()  #
    pay_no = State()


class GetCommentInfo(StatesGroup):
    text = State()
    user_name = State()
    save = State()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    menu = [
        ('Да, хочу!', 'menu1'),
    ]
    folder = 'files'
    image = 'imagestart.jpg'
    file = FSInputFile(f'{folder}/{image}')
    keyboard = get_inline_keyboard(menu, buttons_in_row=2)

    await message.answer_photo(
        photo=file,
        caption='Привет. Хочешь узнать о роботе?',
        reply_markup=keyboard
    )


@router.callback_query(Text(contains=['menu1']))
async def menu1(callback: CallbackQuery):
    menu = [
        ('Далее =>', 'menu2'),
    ]
    folder = 'files'
    image = 'image01.jpg'
    keyboard = get_inline_keyboard(menu, buttons_in_row=2)
    file = FSInputFile(f'{folder}/{image}')
    photo = InputMediaPhoto(media=file)
    await callback.message.edit_media(media=photo, reply_markup=keyboard)


@router.callback_query(Text(contains=['menu2']))
async def menu2(callback: CallbackQuery):
    menu = [
        ('<= Назад', 'menu1'),
        ('Далее =>', 'menu3'),
    ]
    folder = 'files'
    image = 'image02.jpg'
    keyboard = get_inline_keyboard(menu, buttons_in_row=2)
    file = FSInputFile(f'{folder}/{image}')
    photo = InputMediaPhoto(media=file)
    await callback.message.edit_media(media=photo, reply_markup=keyboard)


@router.callback_query(Text(contains=['menu3']))
async def menu3(callback: CallbackQuery):
    menu = [
        ('<= Назад', 'menu2'),
        ('Далее =>', 'menu4'),
    ]
    folder = 'files'
    image = 'image03.jpg'
    keyboard = get_inline_keyboard(menu, buttons_in_row=2)
    file = FSInputFile(f'{folder}/{image}')
    photo = InputMediaPhoto(media=file)
    await callback.message.edit_media(media=photo, reply_markup=keyboard)


@router.callback_query(Text(contains=['menu4']))
async def menu4(callback: CallbackQuery):
    menu = [
        ('<= Назад', 'menu3'),
        ('Далее =>', 'menu5'),
    ]
    folder = 'files'
    image = 'image04.jpg'
    keyboard = get_inline_keyboard(menu, buttons_in_row=2)
    file = FSInputFile(f'{folder}/{image}')
    photo = InputMediaPhoto(media=file)
    await callback.message.edit_media(media=photo, reply_markup=keyboard)


@router.callback_query(Text(contains=['menu5']))
async def menu5(callback: CallbackQuery):
    menu = [
        ('<= Назад', 'menu4'),
        ('Далее =>', 'menu6'),
    ]
    folder = 'files'
    image = 'image05.jpg'
    keyboard = get_inline_keyboard(menu, buttons_in_row=2)
    file = FSInputFile(f'{folder}/{image}')
    photo = InputMediaPhoto(media=file)
    await callback.message.edit_media(media=photo, reply_markup=keyboard)


@router.callback_query(Text(contains=['menu6']))
async def menu6(callback: CallbackQuery):
    menu = [
        ('<= Назад', 'menu5'),
        ('Далее =>', 'menu7'),
    ]
    folder = 'files'
    image = 'image06.jpg'
    keyboard = get_inline_keyboard(menu, buttons_in_row=2)
    file = FSInputFile(f'{folder}/{image}')
    photo = InputMediaPhoto(media=file)
    await callback.message.edit_media(media=photo, reply_markup=keyboard)


@router.callback_query(Text(contains=['menu7']))
async def menu7(callback: CallbackQuery):
    menu = [
        ('<= Назад', 'menu6'),
        ('Далее =>', 'menu8'),
    ]
    folder = 'files'
    image = 'image07.jpg'
    keyboard = get_inline_keyboard(menu, buttons_in_row=2)
    file = FSInputFile(f'{folder}/{image}')
    photo = InputMediaPhoto(media=file)
    await callback.message.edit_media(media=photo, reply_markup=keyboard)


@router.callback_query(Text(contains=['menu8']))
async def menu8(callback: CallbackQuery):
    menu = [
        ('<= Назад', 'menu7'),
        ('Далее =>', 'menu9'),
    ]
    folder = 'files'
    image = 'image08.jpg'
    keyboard = get_inline_keyboard(menu, buttons_in_row=2)
    file = FSInputFile(f'{folder}/{image}')
    photo = InputMediaPhoto(media=file)
    await callback.message.edit_media(media=photo, reply_markup=keyboard)


@router.callback_query(Text(contains=['menu9']))
async def menu9(callback: CallbackQuery):
    menu = [
        ('HERMES', 'Hermes'),
        ('EVE', 'Eve'),
    ]
    folder = 'files'
    image = 'image09.jpg'
    keyboard = get_inline_keyboard(menu, buttons_in_row=2, back_menu=True)
    file = FSInputFile(f'{folder}/{image}')
    photo = InputMediaPhoto(media=file, caption='Какого торгового советника ты хочешь приобрести?')
    await callback.message.edit_media(media=photo, reply_markup=keyboard)


@router.callback_query(Text(contains=['Hermes']))
async def menuBroker(callback: CallbackQuery):
    menu = [
        ('<= Назад', 'menu9'),
        ('Я зарегистрировался', 'binance'),
    ]
    folder = 'files'
    doc = 'register_broker.pdf'
    text = 'Необходимо пройти по ссылке (https://my.roboforex.com/en/?a=zoyq) и зарегистрироваться на брокере'
    keyboard = get_inline_keyboard(menu, buttons_in_row=2)
    file = FSInputFile(f'{folder}/{doc}')
    doc = InputMediaDocument(media=file, caption=text)
    await callback.message.edit_media(media=doc, reply_markup=keyboard)


@router.callback_query(Text(contains=['binance']))
async def menu_binance(callback: CallbackQuery):
    menu = [
        ('<= Назад', 'Hermes'),
        ('Я пополнил', 'ypc'),
    ]
    folder = 'files'
    doc = 'binance.pdf'
    text = 'Пополнить брокерский счёт ROBOFOREX\n' \
           'Можно с любой криптобиржи\n' \
           'Мы рекомендуем через BINANCE'
    keyboard = get_inline_keyboard(menu, buttons_in_row=2)
    file = FSInputFile(f'{folder}/{doc}')
    doc = InputMediaDocument(media=file, caption=text)
    await callback.message.edit_media(media=doc, reply_markup=keyboard)


@router.callback_query(Text(contains=['ypc']))
async def menu_ypc(callback: CallbackQuery):
    menu = [
        ('<= Назад', 'binance'),
        ('Я зарегистрировался', 'terminal'),
    ]
    folder = 'files'
    doc = 'register_ypc.pdf'
    text = 'Необходимо пройти по ссылке\n' \
           '(https://my.forex-box.com/aff.php?aff=10151 \n ' \
           'и зарегистрировать Удаленный рабочий стол'
    keyboard = get_inline_keyboard(menu, buttons_in_row=2)
    file = FSInputFile(f'{folder}/{doc}')
    doc = InputMediaDocument(media=file, caption=text)
    await callback.message.edit_media(media=doc, reply_markup=keyboard)


@router.callback_query(Text(contains=['terminal']))
async def menu_terminal(callback: CallbackQuery):
    menu = [
        ('<= Назад', 'binance'),
        ('Я установил', 'get_message'),
    ]
    folder = 'files'
    doc = 'install_terminal.pdf'
    text = '1. Необходимо Подключиться к УРС.\n' \
           '2.Установить терминал - согласно инструкции.'
    keyboard = get_inline_keyboard(menu, buttons_in_row=2)
    file = FSInputFile(f'{folder}/{doc}')
    doc = InputMediaDocument(media=file, caption=text)
    await callback.message.edit_media(media=doc, reply_markup=keyboard)


@router.callback_query(Text(contains=['get_message']))
async def menu_terminal(callback: CallbackQuery):
    menu = [
        ('<= Назад', 'terminal'),
        ('Я подготовил', 'send_message'),
    ]
    folder = 'files'
    image = 'imagestart.jpg'
    text = 'Подготовьте данные, образец ниже 👇🏽\n' \
           'Фамилия Имя\n' \
           'Номер торгового счета\n' \
           'Имя пользователя телеграм.\n\n' \
           'Пример сообщения:\n' \
           'Иванов Иван\n' \
           '35534257\n' \
           '@ivanov55'
    keyboard = get_inline_keyboard(menu, buttons_in_row=2)
    file = FSInputFile(f'{folder}/{image}')
    doc = InputMediaPhoto(media=file, caption=text)
    await callback.message.edit_media(media=doc, reply_markup=keyboard)


@router.callback_query(Text(contains=['send_message']))
async def menu_terminal(callback: CallbackQuery):
    menu = [
        ('<= Назад', 'get_message'),
        ('Я подготовил', 'send_key'),
    ]
    folder = 'files'
    image = 'imagestart.jpg'
    text = 'Необходимо нажать кнопку:' \
           '[📨 Отправить данные📨 ]' \
           'После нажатия откроется диалог:\n' \
           'Куда необходимо отправть данные\n'  \
           'подготовленные в предыдущем сообщении.\n' \
           'Если вы пропустили данное сообщение нажмите кнопку [⬅️ Назад]'
    keyboard = get_inline_keyboard(menu, buttons_in_row=2)
    file = FSInputFile(f'{folder}/{image}')
    doc = InputMediaPhoto(media=file, caption=text)
    await callback.message.edit_media(media=doc, reply_markup=keyboard)


@router.callback_query(Text(contains=['send_key']))
async def menu_terminal(callback: CallbackQuery):
    menu = [
        ('<= Назад', 'send_message'),
        ('Я подготовил', 'send_key'),
    ]
    folder = 'files'
    image = 'imagestart.jpg'
    text = 'Необходимо нажать кнопку:\n' \
           '[📨 Отправить данные📨 ]\n' \
           'После нажатия откроется диалог:\n' \
           'Куда необходимо отправть данные\n' \
           'подготовленные в предыдущем сообщении.\n' \
           'Если вы пропустили данное сообщение нажмите кнопку [⬅️ Назад]'
    keyboard = get_inline_keyboard(menu, buttons_in_row=2)
    file = FSInputFile(f'{folder}/{image}')
    doc = InputMediaPhoto(media=file, caption=text)
    await callback.message.edit_media(media=doc, reply_markup=keyboard)









# --------------------------------------------------------------------------

# Этот хэндлер срабатывает на команду
@router.message(Text(contains=['START_KEYBOARD']))
async def process_help_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/help'],
    )


# # --------------------------------------------------------------------------
#
#
# @router.callback_query(Text(contains=['О нас']))
# async def about(callback: CallbackQuery):
#     services = Service.objects.all()
#     text = LEXICON_RU['about']
#     for service in services:
#         text = f'{text}\n- {service.name}'
#     await callback.message.edit_text(
#         text=text,
#         reply_markup=user_keyboards.start_keyboard()
#     )
#
#
# # --------------------------------------------------------------------------
#
#
# @router.callback_query(Text(text=['Мои записи']))
# async def get_my_schedules(callback: CallbackQuery):
#     user_id = callback.message.from_user.id
#     try:
#         user = User.objects.get(telegram_id=user_id)
#         user_id = user.pk
#         user_text = f'<b>{user.name} ({user.phone}</b>)\n'
#     except User.DoesNotExist:
#         user_text = 'Вы не зарегистрированы'
#         user_id = None
#     my_schedules = Schedule.objects.filter(user_id=user_id).order_by('-date', 'timeslot')
#     for my_schedule in my_schedules:
#         _, time_my_schedule = TIMESLOT_LIST[my_schedule.timeslot]
#         my_schedule_text = f'Дата: {my_schedule.date}. Время: {time_my_schedule}\n' \
#                            f'Услуга: {my_schedule.services.name}\n' \
#                            f'Мастер: {my_schedule.specialist.name}\n'
#         user_text += '----------------------\n'
#         user_text += my_schedule_text
#     await callback.message.edit_text(
#         text=user_text,
#         reply_markup=user_keyboards.start_keyboard(),
#         parse_mode='HTML'
#     )
#
#
# # --------------------------------------------------------------------------
#
#
# @router.callback_query(Text(contains=['Оставить отзыв']))
# async def set_text_comment(callback: CallbackQuery, state: FSMContext):
#     await callback.message.edit_text(
#         text='Напишите отзыв:'
#     )
#     await state.set_state(GetCommentInfo.text)
#
#
# @router.message(GetCommentInfo.text)
# async def set_user_name_comment(message: Message, state: FSMContext):
#     text = message.text
#     await state.update_data(text=text)
#     await message.answer(
#         text='Ваше имя:'
#     )
#     await state.set_state(GetCommentInfo.save)
#
#
# @router.message(GetCommentInfo.save)
# async def save_comment(message: Message, state: FSMContext):
#     user_name = message.text
#     user_data = await state.get_data()
#     await state.update_data(user_name=user_name)
#     comment = Comment.objects.create()
#     comment.text = user_data['text']
#     comment.user_name = user_name
#     comment.save()
#
#     await message.answer(
#         text='Спасибо об отзыве о нашем салоне красоты!',
#         reply_markup=user_keyboards.start_keyboard()
#
#     )
#     await state.clear()
#
#
# # --------------------------------------------------------------------------
#
#
# @router.callback_query(Text(text=['call_us']))
# async def call_us(callback: CallbackQuery):
#     # keyboard =
#     await callback.message.edit_text(
#         text='Мы рады звонку в любое время\n8(800) 555 35 35',
#         reply_markup=user_keyboards.start_keyboard()
#     )
#
#
# @router.callback_query(Text(contains=['Записаться']))
# async def sign_up(callback: CallbackQuery, state: FSMContext):
#     await callback.message.edit_text(
#         text=LEXICON_RU['rules'],
#         reply_markup=user_keyboards.agree_keyboard()
#     )
#     user_id = int(callback.message.from_user.id)
#     await state.update_data(user_id=user_id)
#     await state.set_state(GetUserInfo.new_user)
#
#
# @router.callback_query(GetUserInfo.new_user)
# async def get_service_type(callback: CallbackQuery, state: FSMContext):
#     await callback.message.edit_text(
#         text='Выберите услугу:',
#         reply_markup=user_keyboards.type_service_keyboard()
#     )
#     await state.update_data(service=callback.data)
#     await state.set_state(GetUserInfo.service)
#     await callback.answer()
#
#
# @router.callback_query(GetUserInfo.service)
# async def get_master(callback: CallbackQuery, state: FSMContext):
#     service = callback.data.split()[1]
#     await state.update_data(service=service)
#
#     await callback.message.edit_text(
#         text='К какому мастеру вы хотите записаться?',
#         reply_markup=user_keyboards.masters_keyboard(service)
#     )
#     await state.set_state(GetUserInfo.master)
#     await callback.answer()
#
#
# @router.callback_query(GetUserInfo.master)
# async def get_procedure_date(callback: CallbackQuery, state: FSMContext):
#     master = callback.data.split()[1]
#     await state.update_data(master=master)
#
#     await callback.message.edit_text(
#         text='Выберите дату:',
#         reply_markup=user_keyboards.date_work_master_keyboard(master)
#     )
#     await state.set_state(GetUserInfo.date)
#     await callback.answer()
#
#
# @router.callback_query(GetUserInfo.date)
# async def get_procedure_time(callback: CallbackQuery, state: FSMContext):
#     date = callback.data.split()[1]
#     user_data = await state.get_data()
#     await state.update_data(date=date)
#
#     master_id = user_data['master']
#     await callback.message.edit_text(
#         text='Выберите время:',
#         reply_markup=user_keyboards.time_work_master_keyboard(master_id, date)
#     )
#     await state.set_state(GetUserInfo.time)
#     await callback.answer()
#
#
# @router.callback_query(GetUserInfo.time)
# async def get_user_name(callback: CallbackQuery, state: FSMContext):
#     time_slot = callback.data.split()[1]
#     await state.update_data(time_slot=time_slot)
#
#     await callback.message.edit_text(
#         text='Введите свое имя:'
#     )
#     await state.set_state(GetUserInfo.name)
#     await callback.answer()
#
#
# @router.message(GetUserInfo.name)
# async def get_phone_number(message: Message, state: FSMContext):
#     name = message.text
#     await state.update_data(name=name)
#
#     await message.answer(
#         text='Введите ваш номер телефона для связи:'
#     )
#     await state.set_state(GetUserInfo.phone)
#
#
# @router.message(GetUserInfo.phone)
# async def process_phone(message: Message, state: FSMContext):
#     phone = message.text
#     await state.update_data(phone=phone)
#     user_data = await state.get_data()
#     date = user_data['date']
#     await message.answer(
#         text=f'Спасибо за запись! До встречи {date} по адресу address.\nХотите оплатить сразу?',
#         reply_markup=user_keyboards.pay_keyboard()
#     )
#     await state.set_state(GetUserInfo.pay)
#
#
# @router.callback_query(Text(contains=['pay_no']))
# async def check_pay(callback: CallbackQuery, state: FSMContext):
#     user_data = await state.get_data()
#     user, created = User.objects.get_or_create(telegram_id=user_data['user_id'])
#     if created:
#         user.name = user_data['name']
#         user.telegram_id = user_data['user_id']
#         user.phone = user_data['phone']
#         user.save()
#     date = user_data['date']
#     time_slot = user_data['time_slot']
#     await state.update_data(pay=False)
#     schedule = Schedule.objects.create(date=user_data['date'],
#                                        timeslot=user_data['time_slot'],
#                                        user=user,
#                                        specialist_id=int(user_data['master']),
#                                        services_id=int(user_data['service'])
#                                        )
#     schedule.save()
#     await callback.message.edit_text(
#         text=f"Спасибо за запись! До встречи {date} {time_slot} по адресу address",
#         reply_markup=user_keyboards.start_keyboard()
#     )
#     await state.clear()
#
#
# @router.callback_query(Text(contains=['pay_yes']))
# async def process_storage_conditions(message: Message, bot: Bot, state: FSMContext):
#     user_data = await state.get_data()
#     service = Service.objects.get(pk=user_data['service'])
#     price = [LabeledPrice(label=str(service.name), amount=int(service.price * 100))]
#     await state.update_data(amount=service.price)
#     await bot.send_invoice(
#         message.from_user.id,
#         title=service.name,
#         description='Оплата косметической поцедуры.',
#         provider_token=load_config().payment_token.p_token,
#         currency='rub',
#         photo_url=PHOTOS[f'{service.name}'],
#         is_flexible=False,
#         prices=price,
#         start_parameter='example',
#         payload='test-invoice-payload'
#     )
#
#     await state.set_state(GetUserInfo.pay_yes)
#
#
# @router.pre_checkout_query(lambda query: True)
# async def pre_checkout_query(pre_checkout_q: pre_checkout_query.PreCheckoutQuery, bot: Bot):
#     await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)
#
#
# @router.message()
# async def successful_payment(message: Message, state: FSMContext):
#     if message.successful_payment:
#         user_data = await state.get_data()
#         user, created = User.objects.get_or_create(telegram_id=user_data['user_id'])
#         if created:
#             user.name = user_data['name']
#             user.telegram_id = user_data['user_id']
#             user.phone = user_data['phone']
#             user.save()
#         schedule = Schedule.objects.create(
#             date=user_data['date'],
#             timeslot=user_data['time_slot'],
#             user=user,
#             specialist_id=int(user_data['master']),
#             services_id=int(user_data['service']),
#             pay=True,
#             amount=user_data['amount']
#         )
#         schedule.save()
#         date = user_data['date']
#         time_slot = user_data['time_slot']
#         _, time_my_schedule = TIMESLOT_LIST[time_slot]
#         await message.answer(
#             text=f"Спасибо за запись! До встречи {date} {time_my_schedule} по адресу address",
#             reply_markup=user_keyboards.start_keyboard()
#         )
#         await state.clear()
