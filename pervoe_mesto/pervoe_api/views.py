from django.shortcuts import render
from django.http import JsonResponse
from telegram import Bot
from telegram.error import TelegramError

from django.http import HttpResponse
from django.views import View
from django.core.files import File

import os, re

from .forms import ClientForm, PriceForm, CalculatorForm
from .models import Apartment

TELEGRAM_BOT_TOKEN = '5599450991:AAH4w_cTs1h3UpLxJyMKL0bPGQ8-5SQBGZ0'
TELEGRAM_GROUP_CHAT_ID = '-4082298212'

def send_telegram_message(chat_id, message):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    message = 'ПЕРВОЕ МЕСТО \n\n' + message

    try:
        bot.send_message(chat_id=chat_id, text=message)
        return True
    except TelegramError as e:
        print(f"Error sending Telegram message: {e}")
        return False

def index(request):
    contact_form = ClientForm()
    price_form = PriceForm()
    calculator_form = CalculatorForm()

    apartments = Apartment.objects.all()
    if request.method == 'POST':
        form_type = None

        if 'phone_contact' in request.POST:
            form_type = 'contact'
        elif 'name' in request.POST:
            form_type = 'calculator'
        elif 'question-1__count_flat[]' in request.POST:
            form_type = 'quiz'
        elif 'apartment' in request.POST:
            form_type = 'apartment'    
        elif 'phone' in request.POST:
            form_type = 'phone'

        if form_type:
            return handle_form_submission(request, form_type, price_form)

    return render(request, 'index.html', {'contact_form': contact_form, 
                                          'price_form': price_form, 
                                          'calculator_form': calculator_form,
                                          'apartments':apartments,})

def handle_form_submission(request, form_type, price_form):
    if form_type == 'contact':
        return handle_contact_form(request)
    elif form_type == 'calculator':
        return handle_calculator_form(request)
    elif form_type == 'quiz':
        return handle_quiz_form(request)
    elif form_type == 'phone':
        return handle_phone_form(request, price_form)
    elif form_type == 'apartment':
        return handle_apartment_form(request)
    else:
        return JsonResponse({'success': False, 'message': 'Форма неверная', 'errors': dict(request.POST)})

def handle_contact_form(request):
    if 'Заявка на звонок' in request.POST['from']:
        phone_number = request.POST['phone_contact']
        msg = f'Обратный звонок\n\n Телефон: {phone_number}'
        send_telegram_message(TELEGRAM_GROUP_CHAT_ID, msg)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'Форма неверная', 'errors': dict(request.POST)})

def handle_apartment_form(request):
    selected_options = {
        'from': request.POST['from'],
        'apartment': request.POST['apartment'],
        'phone': request.POST['phone'],
    }
    
    msg = ''
    msg = f'Понравилась квартира\n\n'
    msg += f'Откуда: {selected_options["from"]}\n'
    msg += f'Квартира: {selected_options["apartment"]}\n'
    msg += f'Телефон: {selected_options["phone"]}'
    print(msg)
    send_telegram_message(TELEGRAM_GROUP_CHAT_ID, msg)
    return JsonResponse({'success': True})

def handle_calculator_form(request):
    if 'Ипотека' in request.POST['from']:
        state = ''
        from_form = request.POST['from']
        price = request.POST['price']
        first_payment = request.POST['first_payment']
        credit_term = request.POST['credit_term']

        if 'state' in request.POST:
            state = request.POST['state']
        elif 'family' in request.POST:
            state = request.POST['family']
        elif 'it' in request.POST:
            state = request.POST['it']

        if 'mother' in request.POST:
            state += ' и ' + request.POST['mother']

        bank = request.POST['bank']
        percents = request.POST['percents']
        payment = request.POST['payment']
        sum_value = request.POST['sum']

        name = request.POST['name']
        phone = request.POST['phone']

        msg = f'{from_form}\nСумма кредита: {price}\nПервый платеж: {first_payment}\nСрок кредита: {credit_term}\nПоддержка: {state}\nБанк: {bank} || Процент:{percents}\nПлатеж по калькулятору: {payment}\nФинальная сумма кредита: {sum_value}\n\nФИО: {name}\nТелефон: {phone}'
        send_telegram_message(TELEGRAM_GROUP_CHAT_ID, msg)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'Форма неверная', 'errors': dict(request.POST)})

def handle_quiz_form(request):
    selected_options = {
        'from': request.POST['from'],
        'count_flat': request.POST.getlist('question-1__count_flat[]'),
        'area': request.POST.getlist('question-2__area[]'),
        'decor': request.POST.getlist('question-3__decor[]'),
        'time': request.POST.getlist('question-4__time[]'),
        'mortgage': request.POST.getlist('question-5__mortgage[]'),
        'phone': request.POST['phone'],
    }

    msg = f'Запрос на подбор квартиры\n\n'
    msg += f'Откуда: {selected_options["from"]}\n'
    msg += f'Количество комнат: {", ".join(selected_options["count_flat"])}\n'
    msg += f'Площадь: {", ".join(selected_options["area"])}\n'
    msg += f'Отделка: {", ".join(selected_options["decor"])}\n'
    msg += f'Срок сдачи: {", ".join(selected_options["time"])}\n'
    msg += f'Ипотека: {", ".join(selected_options["mortgage"])}\n'
    msg += f'Телефон: {selected_options["phone"]}'
    
    send_telegram_message(TELEGRAM_GROUP_CHAT_ID, msg)
    return JsonResponse({'success': True})

def handle_phone_form(request, price_form):
    price_form = PriceForm(request.POST)
    if price_form.is_valid():
        phone_number = price_form.cleaned_data['phone']
        form_value = price_form.cleaned_data['from_value']
        type_messenger = request.POST['type']
        msg = f'{form_value}\n\nНомер телефона: {phone_number}\nМессенджер {type_messenger}'
        send_telegram_message(TELEGRAM_GROUP_CHAT_ID, msg)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'Форма неверная', 'errors': dict(price_form.errors)})
    


class ApartmentsUpdaterView(View):
    def get(self, request, *args, **kwargs):
        # Путь к папке, в которой хранятся изображения квартир разных типов
        aparts_path_types = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static', 'images', 'apparts')

        # Имя файла для ведения журнала
        log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'apartments_creation_log.txt')

        # Счетчик созданных квартир
        total_created = 0

        # Обход папок с разными типами квартир
        for room_type_folder in os.listdir(aparts_path_types):
            room_type_path = os.path.join(aparts_path_types, room_type_folder)
            # Извлекаем room_type из имени папки
            room_type_mapping = {
                '0_room': 'Студия',
                '1_room': '1-комнатная',
                '2_room': '2-комнатная',
                '3_room': '3-комнатная',
            }
            room_type = room_type_mapping.get(room_type_folder, '4-комнатная')

            # Обход файлов внутри каждой папки
            for file in os.listdir(room_type_path):
                file_path = os.path.join(room_type_path, file)
                # Извлекаем информацию из имени файла с использованием обновленного регулярного выражения
                match = re.search(r'(\d+\.\d+)', file)
                print(match)
                if match:
                    # Извлекаем размер квартиры из регулярного выражения
                    area = float(match.group(1))

                    # Проверяем, существует ли квартира с такими параметрами
                    if not Apartment.objects.filter(room_type=room_type, area=area).exists():
                        # Создаем новую квартиру
                        apartment = Apartment(room_type=room_type, area=area)

                        # Сохраняем изображение
                        with open(file_path, 'rb') as f:
                            apartment.image.save(file, File(f))

                        print(f"Created apartment: {apartment}")

                        # Увеличиваем счетчик созданных квартир
                        total_created += 1

        # Записываем информацию в журнал
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"Total apartments created: {total_created}\n")

        return HttpResponse("Apartments creation complete.")
