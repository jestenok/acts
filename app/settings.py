SAVE_FOLDER = 'C:/Users/Jestenok/Documents/work/acts/data'


MONTH_NUMBER_MAP = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
}

ORG_CREDS = {
    'ДЭ': {
        'name': 'ООО «Дентал Эдюкейшн»',
        'full_name': 'Общество с ограниченной ответственностью «Дентал Эдюкейшн»',
        'inn': '7702464542',
        'director': 'Гофштейн Евгений Владимирович',
        'director_whos': 'Гофштейна Евгения Владимировича',
        'directors_position_whos': 'генерального директора',
        'contract_number': '0109/1',
        'contract_date': '01.09.2023',
    },
    'ГЭ': {
        'name': 'ООО «Геософт Эндолайн»',
        'full_name': 'Общество с ограниченной ответственностью «Геософт Эндолайн»',
        'inn': '7702401616',
        'director': 'Гофштейн Евгений Владимирович',
        'director_whos': 'Гофштейна Евгения Владимировича',
        'directors_position_whos': 'генерального директора',
        'contract_number': 'б/н',
        'contract_date': '04.04.2022',
    },
    'Савченкова': {
        'name': 'ИП Савченкова В.А.',
        'full_name': 'Индивидуальный Предприниматель Савченкова Валентина Афанасьевна,',
        'inn': '770200919807',
        'director': 'Савченкова Валентина Афанасьевна',
        'director_whos': 'Савченковой Валентины Афанасьевны',
        'directors_position_whos': 'индивидуального предпринимателя',
        'contract_number': '0109/2',
        'contract_date': '01.09.2023',
    }
}

ORG_DIR_SERVICE = {
    'ГЭ': [
        # ['internal-client', 'Внутренний клиент'],
        ['salary', 'Сервис расчета зарплаты'],
        ['dash', 'Сервис дашбордов'],
        ['defects', 'Сервис замены брака'],
    ],
    'ДЭ': [
        ['utils-library', 'Общая библиотека'],  # ГЭ
        ['doc', 'Общая документация'],
        ['confirmations', 'Сервис подтверждений'],
        ['goods', 'Сервис работы с товарами'],
        ['payment-systems', 'Сервис платежных систем'],
    ],
    'Савченкова': [
        ['server', 'Работа с сервером'],  # ГЭ
        ['clients', 'Сервис работы с клиентами'],
        ['auth', 'Сервис авторизации'],
        ['personal-store', 'Сервис личного склада'],
        # ['paykeeper', 'Сервис оплаты'],
        # ['payment-systems', 'Сервис оплаты'],
    ],
}

BLACK_WORDS = [
    'fix',
    'test',
    'merge',
    'init',
    'bugfix',
    'bug',
    'registry',
    'localhost',
    'update',
    'багфикс'
]