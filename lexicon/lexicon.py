LEXICON: dict[str, str] = {
    'forward': '>>',
    'backward': '<<',
    '/help': '<b>Свиное сердце 2</b>\n\nКнига стихотворений\nАлексея Денисова\n'
             '(в бумажном виде вышла во Владивостоке в 2021 г.)\n\n\n'
             'Пользуйтесь кнопкой Меню!\n'
             'Там оглавление: нажимаешь на строчку - открывается соответствующий стишок.\n'
             'Там же доступ к вашим закладкам.\n'             
             'А чтобы сохранить закладку - жмите на кнопку с номером страницы. '
             'Под каждым стишком есть такая кнопка.\n\n\n'
             'Итак, это бот-читалка. Такой формат распространения книжки. И всё. Не ChatGPT. Но если привыкли уже '
             'общаться с ботами, можете ему написать. Тогда он отправит в ответ рандомный стишок. Бот '
             'не собирает данные, не рассылает спам, не предлагает услуги... Есть, правда, у него одна секретная, '
             'невидимая функция, он считает уникальных подписчиков, чтобы я (автор бота и книжки) знал, '
             'сколько человек им хоть раз воспользовались. Вот, собственно.',
    '/bookmarks': '<b>Это список ваших закладок:</b>',
    'edit_bookmarks': '<b>Редактировать закладки</b>',
    'edit_bookmarks_button': '❌ РЕДАКТИРОВАТЬ',
    'del': '❌',
    'cancel': 'ОТМЕНИТЬ',
    'no_bookmarks': 'У вас пока нет ни одной закладки.\n\nЧтобы '
                    'добавить страницу в закладки - во время чтения '
                    'книги нажмите на кнопку с номером этой '
                    'страницы\n\n/continue - продолжить чтение',
    'cancel_text': '/continue - продолжить чтение'}

LEXICON_COMMANDS: dict[str, str] = {
    '/bookmarks': 'Мои закладки',
    '/help': 'Справка по работе бота',
    '/page_1': 'Я Алексей Денисов...',
    '/page_2': 'как беззаконная комета...',
    '/page_3': 'нет картинок в любимой книжке...',
    '/page_4': 'смерть приходит и проходит...',
    '/page_5': 'кажется не с кем и незачем пить...',
    '/page_6': 'купил мобильник у кавказцев на ВДНХ...',
    '/page_7': 'у вас гляжу тут день сурка...',
    '/page_8': 'хочешь есть? да нет не очень...',
    '/page_9': 'эти дома только кажутся чёрно-белыми...',
    '/page_10': 'станет вечер и поздно чего-то менять...',
    '/page_11': 'день хорошо начат: в спешке...',
    '/page_12': 'что ты там ветер за окном...',
    '/page_13': 'итак, она звалась татьяной...',
    '/page_14': 'Я вас любил, Андрей...',
    '/page_15': 'я ехала пьяная в такси...',
    '/page_16': 'всюду жизнь, как воткнёшь...',
    '/page_17': 'а чистил ли ты ушные...',
    '/page_18': 'ПЕСНЯ',
    '/page_19': 'не дай мне бог сойти с ума...',
    '/page_20': 'то днём весна, а вечером зима...',
    '/page_21': 'а вон январь, как нечто в янтаре...',
    '/page_22': 'он жил и пел себе под нос...',
    '/page_23': 'получил пендельтюром в табло...',
    '/page_24': 'а лучше доминировать давайте...',
    '/page_25': 'А лев поморщился, но съел...',
    '/page_26': 'бе-едный эдвард...',
    '/page_27': 'жук на спине улыбался во сне...',
    '/page_28': 'стал я твёрже и сильно мудрей...',
    '/page_29': 'ДЕНЬ ПОЭЗИИ',
    '/page_30': 'а ну-ка песню нам пропой...',
    '/page_31': 'так я ж сказал поехали...',
    '/page_32': 'депутат тарасюк был ещё жив...',
    '/page_33': 'барсук похоронил корову...',
    '/page_34': 'не говори: не я, так кто...',
    '/page_35': 'Памяти Джорджа Ромеро',
    '/page_36': 'я вдруг увидел, ах, я увидел...',
    '/page_37': 'не пойму чё-то где мои носки...',
    '/page_38': 'ВОЛОСАТЫЕ СТАНСЫ',
    '/page_39': 'пора, мой друг, припорошило...',
    '/page_40': 'видел призрака, был мне тот призрак...',
    '/page_41': 'а у моего брата хороший брат...',
    '/page_42': 'среди миров мерцающих светил...',
    '/page_43': 'ходят голуби по крыше...',
    '/page_44': 'гости даже не съезжались...',
    '/page_45': 'я вашей фотке очень радуюсь...',
    '/page_46': 'я думал о тебе, проезжая царицыно...',
    '/page_47': 'сколько я ходил во магазин...',
    '/page_48': 'СНАРУЖИ И ВНУТРИ',
    '/page_49': 'по бороде меня встречай...',
    '/page_50': 'какой сняжок – колючай! мелкай...',
    '/page_51': 'глуховатый, подслеповатый, с больной спиной...',
    '/page_52': 'что делаешь ты? я рисую годзиллу...',
    '/page_53': 'играли в шахматы, ничья...',
    '/page_54': 'как-то в зное июля...',
    '/page_55': 'дело было в электричке...',
    '/page_56': 'джигурды елды кочумало кно...',
    '/page_57': 'бысть, мысть, охлобысть...',
    '/page_58': 'цмирцмицы! цмирцмицы...',
    '/page_59': 'отупело по утрам, по утрам...',
    '/page_60': 'ГОЛОВА-МАЙОР',
    '/page_61': 'СДТПТ',
    '/page_62': 'ну, типа напиться, влюбиться...',
    '/page_63': 'но что-то будет, надо в это верить...',
    '/page_64': 'я в электричке видел ноги...',
    '/page_65': 'КРЮК',
    '/page_66': 'тихо, василий...'
}
