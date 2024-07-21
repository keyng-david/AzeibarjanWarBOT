import config
from src.enemy import Enemy

start_NoneRegisterMessage = "🌀 Не так давно отгремели последние залпы орудий и лязганье кованной стали." \
                            "  🏛 <b>Цирта</b> пала. Жители всех соседних земель наконец смогут вздохнуть с облегчением." \
                            " Никто более не забирает мужей у их семей на поле брани. Голод миновал." \
                            " Всё возвращается на круги своя. Войне пришел конец. Однако, не все очаги зла подавлены." \
                            " Всем обитателям еще предстоит долгая и тяжелая борьба за светлое будущее Эпсилиона…\n\n" \
                            "<b>Epsilion War-</b> <i>увлекательная MMORPG с возможностью персонального и кланового развития персонажа," \
                            " PvP и PvE контентом в открытом и развивающемся мире.</i>"

start_game_inlineButton = "✅ Начать игру"

# Изменять можно лишь смайлики !!!
courses = {"white_sheep": ["🧙🏼‍♂", "Ağqoyunlular"], "black_sheep": ["🥷🏻", "Qaraqoyunlular"],
           "shirvansha": ["💂🏻", "Şirvanşahlar"]}

start_choose_course_preview = """
<i>Тебе предстоит выбрать одну из трех рас, облик которой ты примешь на просторах Эпсилиона</i>

<b>🏼‍♂ Ağqoyunlular</b>: "Верные жители гордой 🏛 <b>Кавеллы</b>. Их вера сильна, а кровь - кипит в жилах."
<b>🥷🏻 Qaraqoyunlular</b>: "Самый древний народ Эпсилиона. Жители 🏛 <b>Аквелии</b> явно знают что-то большее, чем дано простому смертному." 
<b>💂🏻 Şirvanşahlar</b>: "Храбрый и гордый город 🏛 <b>Дранг Гар</b> воспитал не одно поколение сильнейших воинов. Им всегда нужны новобранцы." 

Делай свой выбор!"""

start_choose_course = ["🧙🏼‍♂ Ağqoyunlular", "🥷🏻 Qaraqoyunlular", "💂🏻 Şirvanşahlar"]

startHi = "<b>Приветствуем нового жителя 🕌 Baki</b>"

startWriteName = """
<b>Пришла пора представиться.</b>

Напиши своё имя"""

# Если человек не будет писать ник на протяжении 5мин, то это сообщение прийдет
startWriteNameIfWaiting = """
<i>У каждого героя - должно быть свое имя</i>
                    
Отправь в чат - свой ник и начнем приключение!"""

startYourNameIsInvalid = """
❗ Неправильное имя, увы...

Ты можешь написать только буквы азейбарджанского, английского алфавита и цифры, без специальных знаков. Длина имени не более 16 символов."""

availableSymbols = "abcdefghijklmnopqrstuvwxyzАBСÇDEƏFGĞHXIijКQLMNОÖРRSŞТUÜVYZ1234567890".lower()

startYourNameIsBusy = "❗ Увы, это имя уже занято. Попробуй другое"

startRegistrationComplite = f"""
Добро пожаловать!
В это неспокойное для всех время Эпсилион нуждается в новом герое!
Твоя история берет начало в городе: 🕌 <b>Baki</b>.
Неси гордо своё имя и прославляй свой род!"""

startCompliteRegInline = "✅ Понял"


hero_buttots_keyb = ["👨‍🦱 Персонаж", "🧮 Характеристики", "🎒 Экипировка", "♻ Ресурсы", "🧬 Параметры", "🎏 Боевые приемы",
                     "🔙 Назад"]


fight_users_buttons = ["🗡 Бой 1 на 1", hero_buttots_keyb[6]]


menuMainButtonsList = ["🗺 Карта", "🙋🏻‍♂ Жители", "🚩 Герой", "📯 Клан", "📜 Квесты", "📟 Меню", "🏆 Рейтинг", "❓ Помощь",
                       "⚔ Найти врагов"]

bakiCity = "🕌 Baki"

bakiDesc = "Bakı şəhərində siz şöhrətə gedən çətin yolda sizə kömək edəcək 🙋🏻‍♂️sakinləri tapa bilərsiniz. Onlardan  🎒 geyim ucun  paltar/silah, ala  bilərsiniz. Gücünüzü bərpa etmək üçün sizə dadlı plov veriləcək, sizə ətirli çay , qozlu ballı paxlava veriləcək. Siz həmçinin missiya götürə bilərsiniz, missiyani tamamladıqdan sonra bir mükafat - təcrübə qazanacaqsınız. Bir məşqçi ilə də məşq edə bilərsiniz, o sizə döyüş sənətlərini öyrədəcək."

main_chat = "azeibarjanwar_chat/14"
shop_chat = "azeibarjanwar_chat/15"
news_chat = "azeibarjanwar_chat/16"

chat_list = ["Общий чат", "Торговый чат", "Новости"]



hero_item_list = ["💰 <b>Золото:</b> ", "🎫 <b>Купон:</b> ", "⭐ <b>Уровень:</b> ", "✨ <b>Опыт:</b> ",
                  "🎗️ <b>Şöhrət:</b> ", "🎖 <b>Орден:</b> ", "🏵️ <b>Коллекция:</b> ", "🧬 <b>Очков параметров: </b>",
                  "➕ <b>Бонус к опыту:</b> ", "➕ <b>Бонус к золоту:</b> ", "➕ <b>Бонус к регенерации:</b> ",
                  "<b>🔑 NFT Ключ: </b>"]

hero_information_title = ["<b>🧮 Характеристики</b>", "<b>❤ Здоровье: </b>", "🗡 <b>Атака: </b>", "🔰 <b>Защита: </b>",
                          "<b>🥊 Крит: </b>", "<b>🧬 Параметры героя: </b>", "<b>♥ Выносливость: </b>", "<b>✊ Сила: </b>",
                          "<b>💫 Ловкость: </b>", "<b>🧿 Интуиция: </b>", "⚡️ <b>Уворот: </b>"]

glory_rank_list = ["Yeni başlayan", "Əsgər", "Çavuş", "Usta", "Lentinant", "Kapitan", "General", "Qəhrəman",
                   "Cəsarətli", "Quldur", "Soyuq qanlı", "Vəzir", "Kral"]

city_desc = """
В городе ты можешь найти местных жителей, у которых можно купить различную экипировку и снаряжение. Также, ты можешь помочь им с решением различных вопросов и задач. Они в долгу не останутся. 

К кому ты хочешь зайти в гости?"""

nps_baki_list = ["💰 Торговец Центур", "👨‍🔬 Алхимик Зефельд", "🥋 Тренер А-Эль", "🪄 Шаман", "🔙 В город"]
npc_karabah_list = ["💰 Торговец Мелхиор", "👨‍🔬 Алхимик Зенит", "⚒ Кузнец Кучики", "🥋 Тренер Айдзен", "🪄 Шаман"]
npc_gandja_list = ["💰 Торговец Ноктюрн", "👨‍🔬 Алхимик Кабуто", "⚒ Кузнец Тессай", "🥋 Тренер Урахара", "🪄 Шаман"]

dealer_button_list = ["🗡 Оружие", "🛡 Броня", "💎 Ювелирные изделия", "♻ Ресурсы"]
trainer_button_list = ["🎏 Боевые приемы", "🎏 Активные приемы", "🎏 Изученные приемы", "🔵 Сменить прием №", "⬅ Герой"]

ael_info = ["🥋 <b>Тренер А-Эль</b>",
            "Со времен войны А-Эль овладел всеми видами оружия. Он может показать тебе пару ловких приемов.",
            "Могу предложить для изучения: "]

trainers = {
    "baki": [f"<b>{nps_baki_list[2]}</b>",
             "Со времен войны А-Эль овладел всеми видами оружия. Он может показать тебе пару ловких приемов.",
             "Могу предложить для изучения: ", "ael"],
    "karabah": [f"<b>{npc_karabah_list[3]}</b>",
                "Я мастерски владею многими видами средневекового оружия.",
                "Позволь мне продемонстрировать несколько приемов, которые могут оказаться полезными в схватке: ", "aidzen"],
    "gandja": [f"<b>{npc_gandja_list[3]}</b>",
               "Благодаря моему опыту как древнего воина, я могу владеть любым видом оружия. ",
               "Я могу показать тебе пару ловких трюков, которые помогут в битве с врагами: ", "urahara"]
}

dealers = {
    "baki": [f"<b>{nps_baki_list[0]}</b>",
             "Торговая лавка Центура открыта для всех. У него ты можешь приобрести экипировку.",
             "Что хочешь купить?", "centur"],
    "karabah": [f"<b>{npc_karabah_list[0]}</b>",
                "Мелхиор опытный торговец с разными товарами по хорошей цене.",
                "Что хочешь купить?", "melihor"],
    "gandja": [f"<b>{npc_gandja_list[0]}</b>",
               "Ноктюрн уже с давних пор торгует, и имеет широкий асортимент.",
               "Что хочешь купить?", "nokturn"]
}


alhimics = {
    "baki": [f"<b>{nps_baki_list[1]}</b>",
             "Зефельд - мастер своего дела и готов помочь вам с различными алхимическими нуждами.",
             "Он может предложить следующие услуги: "],
    "karabah": [f"<b>{npc_karabah_list[1]}</b>",
                "Зенит - опытный алхимик, готов помочь вам со всеми алхимическими нуждами.",
                "Он может предложить следующие услуги: "],
    "gandja": [f"<b>{npc_gandja_list[1]}</b>",
               "Кабуто - опытный алхимик, который поможет вам в алхимических задачах.",
               "Он может предложить следующие услуги: "]
}

blacksmits = {
    "karabah": [f"<b>{npc_karabah_list[2]}</b>",
                "Кучики - опытный кузнец, готов помочь вам своими знаниями в кузнечном деле.",
                "Я могу предложить следующие услуги: ", "kuchiki"],
    "gandja": [f"<b>{npc_gandja_list[2]}</b>",
               "Тессай - опытный кузнец, который поможет вам в создании сложных экипировок.",
               "Я могу предложить следующие услуги: ", "tessai"]
}


dealer_weapon_button_list = ["🗡 Мечи", "🪓 Топоры", "⚔ Кинжалы"]
dealer_protect_button_list = ["🎩 Шлемы", "🎽 Доспехи", "🛡 Щиты", "🧤 Перчатки", "🥾 Сапоги", "🌂 Аксессуары"]
dealer_product_button_list = ["📿 Колье", "💍 Кольца"]

waepon_info_list = ["❇ <b>Тип предмета</b>: ", "🎴 <b>Оружие:</b> ", "☢ <b>Качество:</b> ", "💎 <b>Редкость:</b> ",
                    "<b>Бонусы предмета:</b> ", "🗡 <b>Атака:</b> ", "❤ <b>Здоровье:</b> ", "🥊 <b>Крит:</b> ",
                    "<b>Требования к одежде:</b> ", "⭐ <b>Уровень:</b> ", "✊ <b>Сила:</b> ", "♥ <b>Выносливость:</b> ",
                    "<b>Цена:</b> "]

waepon_types_list = ["🔪 Оружие", "Меч", "Топор", "Кинжал", "Шлем", "Доспех", "Щит", "Перчатки", "Сапоги", "Колье",
                     "Кольцо"]

item_types_list = ["sword", "axe", "dagger", "helmet", "armor", "shield", "gloves", "boots", "necklace", "ring"]

trick_need_waepon_actions = {item_types_list[i]: waepon_types_list[1:][i].lower() for i in range(0, 9)}

empty = "Пусто"

buy_item_title = ["{} Купить", "{} Изучить"]

item_types = ["🔪 <b>Оружие:</b> ", "🎩 <b>Шлем:</b> ", "🎽 <b>Доспех:</b> ", "🧤 <b>Перчатки:</b> ", "🥾 <b>Сапоги:</b> ",
              "🛡 <b>Щит:</b> ", "💍 <b>Кольцо:</b> ", "📿 <b>Колье:</b> ", "🌂 <b>Аксессуар:</b> "]

item_actions_inventory = ["✅ Надеть", "❌ Снять", "⚒ Заточить", hero_buttots_keyb[-1], "❌ Нет",
                          "❗ У тебя нет подходящей 🩸 Крови шахида. Она выпадает с монстров, также их можно найти в мешках с ресурсами."]

use_weapon = "<i>Надетая экипировка:</i>"

get_you_cant_buy_it = "❗️ Недостаточно средств. В инвентаре - {} валюты."


async def get_you_buy(item, action):
    actions = ["купили", "изучили"]
    return f"Вы успешно {actions[action]} {item}."


last_page = "Это последняя страница!"
first_page = "Это первая страница!"

you_cant_use = ["⭐ Уровень", "✊ Сила", "♥ Выносливость", "🧿 Интуиция", "💫 Ловкость",
                "❗️ Невозможно надеть предмет. Недостаточно очков навыков:\n",
                "❗️ <b>Невозможно использовать прием.</b>\nНедостаточно очков:\n\n"]

you_successfully_use_it = ["Вы успешно надели ", "Вы успешно сняли ", "<b>Вы успешно добавили прием в слот ✔</b>",
                           "<b>Вы успешно сняли прием</b>"]


async def you_want_to_up_it(item_title):
    return [f"Ты уверен что хочешь заточить <b>{item_title}</b> на 1?",
            f"Ты успешно заточил <b>{item_title}</b> на 1 🎉"]


health_up = ["💖 Ваше здоровье восстановлено на 50%. Можно отправляться в бой",
             "💖 Ваше здоровье полностью восстановлено"]

req = "Требования: "


async def trainer_tricks_list(tricks: list):
    text = trainer_button_list[0] + "\n\n"

    count = 1
    for i in tricks:
        text += f"{'⚪' if i is None else '🔵'} Боевой прием №{count}: "
        text += "<code>-свободный слот-</code>\n\n" if i is None else f"<b>{i.title}</b>\n{i.description}\n\n"
        count += 1
    return text


you_not_have_any_tricks = '❗ Нет доступных приемов.'

trick = ["Текущий прием:", "Прием:", "<b>Снять прием:</b>", "<b>Для установки:</b>"]

not_aviable = "Приема с таким индетификатором не существует!"

location_inf = ["🔸 <b>Уровень монстров:</b> ", "📯 <b>Владельцы:</b> ", "👥 <b>Şəhərdə onlayn oyunçular:</b>"]

transitions_names = ["🏜 Пустошь",
                     "🏞 Устье реки",
                     "🏕 Дом в лесу",
                     "🏛 Карабах",
                     bakiCity,
                     "🔥 Очаг сопротивления",
                     "☠️ Проклятые земли",
                     "⛺️ Лагерь фанатиков",
                     "🏛 Гянджа",
                     "🛖Юрт",
                     "🛕Гала",
                     "🌋  Скала Бесбармак ",
                     "⚔️ Колизей"
                     ]


to_location = "🔙 К локации"

city_list = ["baki", "karabah", "gandja", "coliseum"]

cancel_transition = "🚫 Отменить переход"

down_desc = "В локации можно встретить врагов. Кто же будет следующим?"

map_description = """
Ты открываешь 🗺 <b>Карту.</b>
Хмм, куда мы отправимся на этот раз?

<i>Легенда карты:
🏛 - Город
Остальное - Зоны охоты</i>"""

you_cant_transit = """
    ❗️ <i>Для перемещения в эту локацию, у тебя маленький уровень. Достигни {} уровня и возвращайся. Посмотреть уровень можно в меню 🚩 <b>Герой.</b></i>"""

transit_action = """
    Пункт назначения: <b>{}</b>.

👣 <b>Осталось времени: </b> (~{} сек.)

❓ Между городами и локациями есть расстояние."""

you_in_transit = "Ты находишься в пути. Скоро будешь на месте"

you_in_find = "Идет поиск соперника"

find_fight_canceled = "Поиск боя отменен"

start_find_enemy = "🔭 Начался поиск противника"

where_you_will_to_hit = "Куда будешь бить?"
what_you_want_to_defaet = "Что будешь блокировать?"


async def you_finded_enemy(enemy: Enemy):
    return f"""
Вот ты и встретил своего врага.

Твоим соперником будет <b>{enemy.name}</b> 🔸{enemy.lvl} ❤ ({enemy.max_hp}/{enemy.max_hp}).

<i>{enemy.description}</i>

<b>{where_you_will_to_hit}</b>"""


fight_actions_buttons = ["В голову", "В грудь", "В живот", "В пояс", "В ноги", "Голова, грудь", "Грудь, живот",
                         "Живот, пояс", "Пояс, ноги", "Ноги, голова", "Сбежать"]

surrender = "Сдаться"

fight_actions = {fight_actions_buttons[i]: i for i in range(0, len(fight_actions_buttons))}

fight_info = ["Ход", "бьет", "И попадает в <b>блок</b>", "И наносит ", "урона", " 🥊 <b>крит</b> на 💥 ",
              "пропускает удар соперника"]


async def is_block(num_attack: int, num_block: int, type: str, is_losed=False):
    async def check_is_blocked():
        item_attack = fight_actions_buttons[num_attack].split()[1]
        item_attack = "голова" if item_attack == "голову" else item_attack

        items_block = fight_actions_buttons[num_block]
        items_block = items_block.replace(",", "").lower().split()

        return item_attack in items_block

    if type == "npc":
        return False if is_losed else await check_is_blocked()
    else:
        return "lose_time" if is_losed else await check_is_blocked()


take_life = "💀 Принять участь"
take_reward = "✅ Забрать нaграду"
to_hunt_loc = "В зону охоты"


async def get_fight_result(res_list, enemy: Enemy) -> list:
    if res_list == [False, True]:
        return [f"Тебя убил: <b>{enemy.name}</b>\n\nТы был отправлен восстанавливаться в город", take_life, True]
    elif res_list == [True, False]:
        return [f"📍 Ты победил своего врага -  <b>{enemy.name}</b> 🔸{enemy.lvl} 💔", take_reward, False]
    else:
        return ["Бой завершился у вас <b>ничья</b>. 🎌\n\nТы был отправлен восстанавливаться в город", take_life, True]


string_you_not_have_hp = "Недостаточно здоровя чтобы отправится в бой! минимально нужно 50%!"

wait_res_move = "Ожидаем завершения хода..."

are_you_sure_run = """
<b>Ты уверен что хочешь попытаться сбежать?</b>

❓ С вероятностью в 30% есть шанс успешно сбежать с поля боя без потерь (шанс успешного побега уменьшается каждый ход). Если не повезет - соперник моментально убьет ударом в спину"""


are_you_sure_surrender = """
<b>Ты уверен что хочешь сдаться?</b>

Ты моментально одержишь поражение в бою!"""




you_successfully_runed = "Ты успешно сбежал от врага без потерь"
you_losed_run = "Попытка сбежать - <b>провалилась</b>, cоперник догнал и <b>убил</b>"

yes_or_no = ["Да", "Нет"]

string_time_sec = "⏳ До конца хода осталось {} секунд."

string_for_use_need = "<b>Для использования необходим </b>"

not_aviable_inp = "<b>Неверный ввод!</b>"

skip = "Пропустить"

# Очень важно чтобы эти названия совпадали с названиями приемов в БД (tricks - title) в противном случае работать не будет.
tricks_titles = [
    "По наитию (4 🗡)",
    "Без чувств (4 🛡)",
    "Помощь духов (3 🗡)",
    "Подручное средство (6🛡)",
    "Удар воина (3 🗡)",
    "Храбрый кулак (4 🛡)",
    "Удар дракона (5 🗡)",
    "Удар с головой (6🛡)",
    "Удар молнии (5 🗡)",
    "Чапалах (4 🛡)",
    "Шаринган (6 🗡)",
    "Прогиб (4 🗡)",
    "Гашгалдаг (2 🛡)",
    "Удар шахида(4 🛡)",
    "Удар Берсерка (6 🗡)"
]

use_trick_round_text = " использует кoбинацию "

use_trick = "{} использует комбинацию <b>{}</b>\n<code>{}</code>\n\n"

top_titles = ["✨ По опыту", "💰 По богатству", "📯 Топ кланов", "⚔️ Топ PVP", "🏵 По славе", "⚔️ Клановые войны",
              hero_buttots_keyb[6]]

top_titles_in_messages = ["✨ Рейтинг по опыту", "💰 Рейтинг по богатству", "🏵 Рейтинг по славе",
                          "⚔️ Рейтинг по PVP очкам", "📯 Рейтинг кланов по PVP очкам"]

your_rate = "<b>Твое место в рейтинге:</b>"


async def get_point_desc(lvl: int, array: list):
    from_10_lvl = "(c 10 уровня)"

    return f"""
🧬 <b>Параметры героя:</b>

🧬 Параметры позволяют сделать каждого героя уникальным, увеличивая характеристики.
За каждый уровень дается 🧬 3 очка.

✊ <b>Сила:</b> {array[0]}
♥ <b>Выносливость:</b> {array[1]}
💫 <b>Ловкость:</b> {array[2]} {from_10_lvl if lvl < 10 else ""}
🧿 <b>Интуиция:</b> {array[3]} {from_10_lvl if lvl < 10 else ""}

🧬 <b>Очков параметров:</b> {array[4]}"""


point_buttons = ["🧬 Распределить", "🔄 Сброс параметров", trainer_button_list[4]]


async def get_point_distribute_text(array: list):
    return f"""
<b>🧬 Распределение параметров</b>

Каждый параметр дает определенные характеристики героя:

<b>✊ Сила:</b> 
+3 к атаке 

<b>♥ Выносливость</b>: 
+15 единиц здоровья

<b>💫 Ловкость:</b>
+7 к криту

<b>🧿 Интуиция:</b>
+7 к увороту 

<b>✊ Сила: {array[0]}
♥ Выносливость: {array[1]}
💫 Ловкость: {array[2]}
🧿 Интуиция: {array[3]}</b>

<b>🧬 Очков параметров: {array[4]}</b>"""


distribute_points_inline_text = ["✊ В силу", "♥ В выносливость", "💫 В ловкость", "🧿 В интуицию"]

push_points_dict = {"power": "Ты успешно увеличил ✊ силу", "force": "Ты успешно увеличил ♥ выносливость",
                    "dexterity": "Ты успешно увеличил 💫 ловкость", "intuition": "Ты успешно увеличил 🧿 интуицию"}

points_is_null = "❗️ Свободные очки параметров закончились"

where_push_point = "Куда распределить 🧬 1 очко параметров?"

points_is_null_2 = """
<b>🧬 Распределение параметров</b>

❓ Свободные очки параметров закончились. Следующие очки параметров можно получить увеличив уровень героя или путем сброса всех параметров"""

resource = "Ресурс"

reset_params_no_have = """
<b>🔄 Сброс параметров</b>

❓ Для сброса очков параметров требуется:

<b>🎟 Сертификат cброса параметров</b>

Их можно получить, выполнив определенные квесты, выторговав у игроков или купив за печеньки."""

reset_params_have = reset_params_no_have + "\n\nТы уверен что хочешь сбросить параметры?"

successfull_reseted = """
🧬 Очки параметров успешно сброшены c помощью - 🎟 Сертификат cброса параметров

Предметы и приемы неподходящие под новые параметры были сброшены"""

reset_params = "Сбросить параметры"

no_have_item_actions = ["🎫 Купить в магазине", "🗣 Спросить на рынке"]

you_not_have_this_item_now = "<b>У вас больше нет этого предмета!</b>"

resources_text = """
<b>♻ Ресурсы</b>

<i>❓ Ресурсы обычно используются для крафта, но могут быть другие применения</i>"""

item_types_res = ["crafter", "recepie", "scroll", "potion", "collection_and_order"]
item_types_res_trade = ["crafter_trade", "recepie_trade", "scroll_trade", "potion_trade", "collection_and_order_trade"]

item_types_str = {"crafter": "⚒ Крафтовые", "recepie": "📄 Рецепты", "scroll": "📃 Свитки", "potion": "🧪 Зелья"}

to_res = "♻ К ресурсам"

menu_chield_message = """
<b>📟 Меню</b>

<i>❓ В меню можно изменить настройки персонажа, получить дополнительные награды для развития, приобрести и потратить печеньки, а также заняться торговлей.</i>"""

event = "🐚 Событие"

menu_chield_buttons_text = [event, "🎫 Купоны", "💱 Торговля", "🎎 Рефералы",
                            hero_buttots_keyb[6], "⚙  Настройки"]


async def get_setting_message(nickname, course):
    return f"""
<b>⚙ Настройки</b>

<b>Ник игрока:</b> {nickname}
<b>Раса:</b> {courses[course][0]} {courses[course][1]}

<i>❓ В меню настроек ты можешь сменить имя и расу своего персонажа. Для этих действий нужен специальный предмет, который может выпасть с некоторых монстров. Также, сертификат можно получить по итогам квеста, за участие в специальных событиях, либо приобрести его за печеньки в магазине.</i>"""


settings_buttons_text = ["🗑 Удалить персонажа", "🆔 Сменить имя", "👼 Сменить расу", "⬅️ В меню"]

delete_hero = "УДАЛИТЬ ПЕРСОНАЖА"

delete_hero_message = f"""
<b>Ты действительно хочешь удалить своего персонажа?</b>

⚠️ Весь твой прогресс будет <b>аннулирован</b>, учитываясь уровень, характеристики, предметы, и вообще <b>весь</b> прогресс персонажа.

<i>- Если ты состоишь в клане, но при этом не владеешь им, то ты автоматически выйдешь с него.
- Если ты <b>владелец</b> клана, удалить аккаунт <b>не получится</b>, нужно передать права владения на клан другому пользователю!</i>

- После удаления персонажа, <b>начнется</b> регистрация нового!

<b>Чтобы подтвердить удаление персонажа, введи:</b>
{delete_hero}"""

cancel_del = "🚫 Отменить действие"

canceled_del_hero = "✅ Удаление персонажа успешно <b>отменено!</b>"

not_successfull_input_del_hero = "❌ <b>Неудачное</b> удаление персонажа. <b>Неправильный ввод!</b>"

successfull_input_del_hero = "✅ <b>Ваш персонаж был успешно удален!</b>"

not_have_need_item = "❗️ Для выполнения действия в инвентаре нет необходимого предмета -"
reset_name_button = "Cменить"
you_have_need_item = "У тебя есть нужный предмет. Совершить действие?"
send_new_nickname = "Успешно. А теперь <b>отправь</b> новый никнейм!"

action_canceled = "❌ Действие успешно <b>отменено</b>"

name_changed = "✅ Имя было успешно <b>изменено!</b>"
course_changed = "✅ Расса была успешно <b>изменена!</b>"

get_new_lvl_text = "🎉 Ура! Ты получил {} 🔸 уровень, твое ❤ здоровье полностью восстановлено.\n\nПолучено: 🧬 3 очка параметров"

get_received_reward = """
<b>Получено в награду:</b>
✨ Опыта: {} {}
💰 Золота: {} {}
{}"""

help_message_buttons = [menuMainButtonsList[7], "🗂 База знаний", "📚 Гайды", "📭 Связь", "⚠️ Правила",
                        hero_buttots_keyb[6]]

info_help_text = """
<b>❓ Помощь</b>

⚔️ <b>Azerbaijan War</b> - самая масштабная MMORPG на просторах Telegram.

✳️ Здесь тебе предстоит сражаться за территории. <b>Защищать земли от монстров.</b> Заниматься ремеслом. 

🌐  Получить информацию об основах игры можно здесь: перейти (https://teletype.in/@epsilionwar/By8CGP_2r/)

<i>Если хочешь узнать больше или что то не понятно, пиши в чат @epsilion_chat  или читай 📚 Гайды.</i>"""

data_help_message = """
<b>🗂 База знаний</b>

Здесь можно узнать информацию о монстрах, экипировке и ресурсах, существующих в этом мире.

Что ты хочешь найти?"""

data_help_buttons_text = ["🦄 Найти монстров", "🎒 Найти экипировку", "♻ Найти ресурсы", "🎏 Найти боевые приемы"]
data_help_answers_text = ["поиск монстров: ", "поиск экипировки: ", "поиск ресурсов: ", "поиск комбо: ",
                          "поиск игрока: "]
rarity = "💎 Редкость:"

mob_desc_main_word = ["<b>📋 Страница монстра</b>\n\n", "<b>📋 Страница экипировки</b>\n\n",
                      "<b>📋 Страница ресурса</b>\n", "<b>📋 Страница приема</b>\n\n", "<b>📋 Страница клана</b>\n\n"]

mob_desc_zona_hunt = "<b>🗺 Зона охоты:</b>"

guide_links = ["https://teletype.in/@epsilionwar/By8CGP_2r",
               "https://teletype.in/@epsilionwar/rJ0b7DuhS",
               "https://teletype.in/@epsilionwar/rklF6Du2r",
               "https://teletype.in/@epsilionwar/rylSiBqeI",
               "https://teletype.in/@epsilionwar/Hyrmw6ohr",
               "https://teletype.in/@epsilionwar/S1-bUU9gI",
               "https://teletype.in/@epsilionwar/nU7ghVaCt"]

guide_message = f"""
<b>📚 Гайды</b>

Актуальные гайды по игре:

<b>🌐 Все гайды</b> <a href='{guide_links[0]}'>перейти</a>

<b>⌨️ Интерфейс и управление ботом</b> <a href='{guide_links[1]}'>перейти</a>

<b>⚔️ Боевая система</b> <a href='{guide_links[2]}'>перейти</a>

<b>🎏 Боевые приемы</b> <a href='{guide_links[3]}'>перейти</a>

<b>🎒 Экипировка</b> <a href='{guide_links[4]}'>перейти</a>

<b>⚒ Крафт и улучшения</b> <a href='{guide_links[5]}'>перейти</a>

<b>⛏ Ремесло</b> <a href='{guide_links[6]}'>перейти</a> """

rules_message = """
<b>⚠️ Правила</b>

Использования автоматических средств для игры - запрещено законами EpsilionWar. 

Использование твинков для получения экономической/реферальной выгоды - запрещено законами EpsilionWar.

Подробнее: https://teletype.in/@epsilionwar/HkPsNEfZL"""

support_text = "<b>📭 Связь</b>\n\nДля связей с администрацией проекта писать сюда https://t.me/Mehechio"

for_use = "Для использования:"

count = "шт"

instruction = "Инструкция по созданию вещи."

you_not_have_need_item = "❗️ Предмета нет в инвентаре"

potion_been_used = "<b>Предмет был успешно использован, вы получили:</b>"

potion_res_info = {
    "current_hp": hero_information_title[1], "bonus_xp": hero_item_list[8],
    "regen_hp": hero_item_list[10], "bonus_gold": hero_item_list[9]
}

trade_message = """
<b>💱 Торговля</b>

Обменивать можно:
- 💰 Золото
- 🍪 Печеньки
- 🎒 Экипировку
- ♻️ Ресурсы

Для начала торговли, выбери кому хочешь предложить трейд через кнопку поиска.

<i>Или воспользуйся командой /trade Ник</i>

⚠️ Торговать можно только с игроками, находящимися в том же городе где и ты.

<a href='t.me/azeibarjanwar_chat/15'>Торговый чат</a>"""

find_user = "🔎 Найти игрока"

user_profile = "<b>📋 Профиль игрока</b>"

# TODO: доделать после добавления пвп сражений
async def get_find_user_desc(user_id, nickname, lvl, glory, course, glory_rank):
    return f"""
{user_profile}

{courses[course][0]}️ <a href='tg://user?id={user_id}'>{nickname}</a> 🔸{lvl}

🏵 Слава: {glory} ({glory_rank})

⚔️ Убийств в PVP: 0
☠️ Смертей в PVP: 0"""


offer_trade = "💱 Предложить торговлю"

user_not_in_your_location = "⚠️ Пользователь уже не в вашей локации!"

offer_sended = "✅ Предложение об торговле было <b>отправлено</b>"

offer_accept_or_no = ["✅ Принять предложение", "❌ Отклонить предложение"]
clan_accept_or_no = ["✅ Принять запрос", "❌ Отклонить запрос"]

invite_to_offer = ["Игрок", "пригласил к участию в торговле", " Началась торговля с ",
                   "✅ Предложение было успешно отклонено", "отклонил предложение об торговле! ❌",
                   "⚠️ Игрок не может принять торг!"]

choise_for_offer = f"{menu_chield_buttons_text[2]}\n\n❓ Выбери то, что хочешь предложить для обмена"
buttons_trade_callbaks = ["accept_actions_offer", "gold_offer", "coupons_offer", "equip_offer", "resources_offer"]

buttons_trade = ["🔒 Подтвердить", "💰 Добавить золото", "🎫 Добавить купоны", "🎒 Добавить экипировку",
                 "♻ Добавить ресурсы"]

cancel_trading = "🚫 Отменить торговлю"

trade_canceled = "💱 Торговля была успешно остановлена."
trade_canceled_user_2 = "остановил торговлю."

choise_which_resouser_trade = f"<b>{hero_buttots_keyb[3]}</b>\n\nВыбери, какие ресурсы хочешь передать"
choise_which_equip_trade = f"<b>{hero_buttots_keyb[2]}</b>\n\nВыбери, какую экипировку хочешь передать"


async def get_coupons_or_gold_buttons(item_type: str) -> dict:
    if item_type in ["gold", "coupon"]:
        if item_type == "gold":
            res_info = {"symbol": "💰", "title": "Золота", "callback": "gold", "limits": config.GOLD_LIMITS}
        else:
            res_info = {"symbol": "🎫", "title": "Купонов", "callback": "coupon", "limits": config.COUPON_LIMITS}

        result = {f"{res_info['symbol']} {value} {res_info['title']}": f"{res_info['callback']}_offer_{value}" for value
                  in res_info['limits']}

        return result
    else:
        raise TypeError


how_much_gold_trade = f"<b>{menu_chield_buttons_text[2]}</b>\n\nВыбери, сколько 💰 золота хочешь передать\n\n" + "Доступно в инвентаре: 💰 {} золота "
how_much_coupon_trade = f"<b>{menu_chield_buttons_text[2]}</b>\n\nВыбери, сколько 🎫 купонов хочешь передать\n\n" + "Доступно в инвентаре: 🎫 {} купонов "

not_enough_currency = "У вас недостаточно валюты чтобы добавить в трейд!"

successfull_add_currency = "Успешно добавлено {} {} в трейд!"

successfull_add_to_trade = "Успешно добавлено!"

you_offer_to_trade = "Ты предлагаешь для обмена:"

not_offers = "<i>Предложений нет</i>"

you_confirmed_to_offer = f"{menu_chield_buttons_text[2]}\n\n🕑 Ты подтвердил готовность к сделке. Ожидай второго игрока"

user_confirm_offer_ready = "{} подтвердил готовность к сделке"

user_offers = "Игрок {} предлагает:"

there_is_a_trade = "Идет торг."

offer_resultat_buttons = ["✅ Согласен", "🔒 Изменить"]

go_changes_offer = "{} - готовит изменения в своем предложение. Подожди его новых условий."

user_confirm_offer_resultat = "{} согласился на сделку"

wait_while_user_2_go_changes = "❗️ Подожди пока второй игрок предложит новые условия"

offer_successfully_end = "Сделка успешно завершена!"

trade_is_disabled = "❗️ Прошлая сделка уже завершилась!"

clan_default_buttons = ["🔍 Найти клан", "➕ Создать клан", "❌ Отменить заявку", hero_buttots_keyb[6]]

my_votes = "📬 Мои приглашения"

none_clan_message = """
<b>📯 Клан</b>

Пока у тебя нет клана. Ты можешь найти единомышленников или создать свой!

<i>❓ Клан поможет тебе разобраться в игре, сделает тебя сильнее и даст компанию для покорения мира Azeibarjan War 💪</i>"""

clan_create_message = f"""
⚔️ Клан - это не только место соединения друзей, но и большая мощь на просторах мира Epsilion War. Кланы занимаются политикой, экономическим развитием и ведут свою расу к победе. Организация - превыше всего!

Стоимость создания - {config.CLAN_COST}💰.

📯 Готов ли ты стать лидером и повести за собой своих товарищей?"""

clan_creation_requirements = "❗️ Введите название клана :\n\nНазвание клана должно содержать не менее чем 20 букв, название клана не должено содержать спецсимволов и цифр)"

clan_name_is_unaviable = "⚠️ Неверное название клана!\n\nНазвание клана должно содержать не менее чем 20 букв, название клана не должено содержать спецсимволов и цифр"

clan_name_is_busy = "⚠️ Название клана уже занято, увы.\n\nПопробуй другое имя!"

clan_choice_emoji = "Выберите значок клана :"

creating_clan_is_canceled = "Создание клана успешно отменено ✅"

clan_successfully_created = "❗️Клан успешно создан !"

clan_buttons = [
    "📋 Список участников клана",
    "🛒 Магазин клана",
    "❌ Покинуть клан",
    "⚙️ Настройки клана"
]

clan_casarm = " 📯 Казарма клана {}"

clan_users_casarm = "⛓ В казарме вашего клана {} человек."

check_clan_users_button = ["👤 Смотреть участников клана", "Участники клана: "]

cancel_clan_create = "Отменить создание клана?"

user_not_in_your_clan = "Игрок не в вашем клане!"

user = "Игрок {} - {}"

clan_user_actions = ["🧷 Назначить заместителем", "🖇 Снять права заместителя", "🔐 Отдать права главы клана",
                     "❌ Кикнуть с клана"]

get_user_status = {
    0: "Учасник",
    1: "Заместитель",
    2: "Глава"
}

user_successfully_was_cicked = "Пользователь был успешно <b>кикнут</b> с клана ✅"

you_was_cicked = "❗️ Увы, вы были <b>исключены</b> с клана {}."

something_went_wrong = "Что-то пошло не так.."

successfully_set_pre_head = "✅ Игрок успешно <b>назначен</b> заместителем клана."
successfully_unset_pre_head = "✅ У игрока успешно были <b>сняты</b> заместителем клана."

you_was_set_pre_head = "✅ Вас <b>повысили</b>, теперь вы заместитель клана {}!"
you_was_uset_pre_head = "❗️ Увы, ваши права заместителя клана {} были <b>сняты</b>. "

successfully_set_head = "✅ Игроку успешно были <b>пререданы</b> права главы клана. Вы были <b>переназначены</b> как заместитель."
successfully_unset_head = "✅ Вам были <b>переданы</b> права главы клана {}. Теперь вы имеете полный доступ!"

you_was_leav = "✅ Вы успешно вышли с клана {}."
you_cant_leav = "❌ <b>Невозможно покинуть клан</b> будучи главой. Перейдате права главы клана или удалите клан чтобы выйти."
you_cant_delete_person = "❌ <b>Невозможно удалить персонажа будучи главой.</b> Перейдате права главы клана или удалите клан чтобы удалить персонажа."

clan_shop_message = f"""
{clan_buttons[1]}

Здесь можно купить зелья дешевле на 10% чем у алхимиков."""

list_aviable_clans = "<b>📯 Список доступных кланов</b>"

clan_list_actions = [
    "Клан: <b>{}</b>",
    "<b>👥 Игроков:</b> {}",
    "<b>👑 Лидер:</b> {}",
    "<b>📤 Подать заявку:</b> /clan_req_{}"
]

players = "👥 Игроков: {}"

search_clan = ["🔎 Найти клан для вступления", "Поиск клана: "]

clan_power = "<b>♨️ Сила клана: {}</b>"
user_power = "♨️ Сила игрока: {}"

you_already_in_clan = "❗️ Вы уже в клане!"

you_already_have_invite_join = "❗️ Вы уже отправляли запрос в клан! чтобы отправить запрос на вступление, нужно отменить прошлый."

clan_is_not_have = "❗️ Такого клана не существует!"

clan_count_users_is_too_much = "❗️ В клане не хватает мест, попробуй позднее"

you_send_invite_to_clan = "Ты подал заявку в клан {}"

send_req_to_clan = "📪 Подать заявку в клан"

clan_req_is_canceled = "✅ Заявка в клан {} была успешно отменена."

clan_req_is_not_have = "❗️ Вы не отправляли заявок в клан!"

sostav = "👥 <b>Состав:</b> ({}/{})"

pre_heads = "🎩 <b>Заместители</b>: {}"

control_clan_invites_buttons = ["📬 Управление приглашениями", "📊 Запросы на вступление", "🗞 Отправить приглашение", "📯 Назад"]
not_have_acces = "❗️ <b>У вас нет прав для этой функции.</b>\n\nНужны права заместителя или главы. "
not_have_acces_head = "❗️ <b>У вас нет прав для этой функции.</b>\n\nНужны главы клана. "

clan_control_message = f"<b>{control_clan_invites_buttons[0]}</b>\n\n" \
                       f"Здесь можно принять запрос на приглашение в клан или отправить его."

clan_send_invite = f"<b>{control_clan_invites_buttons[2]}</b>\n\n" \
                   f"Тут ты можешь отправить игроку приглашение в клан."

clan_invite = "📯 Отправить приглашение в клан"

not_can_send_invite = "❗️ Пользователь уже в клане, попробуйте позже!"

clan_invite_sended = "✅ Приглашение в клан было успешно отправлено игроку {}"

cant_you_before_send_invite = "❗️ Вы уже отправляли приглашение в клан этому игроку!"

my_invites_empty_message = f"""
<b>{my_votes}</b>

💁‍♂️ Пока у тебя нет приглашений в клан

❓ Попробуй найти клан сам"""

my_requests_empty_message = f"""
<b>{control_clan_invites_buttons[1]}</b>

💁‍♂️ Пока у вашего клана нет запросов на вступление в клан

❓ Попробуй пригласить пользователя сам."""

is_your_invites = "📃 Доступные приглашения в клан на текущий момент:"
is_your_requests = "📃 Доступные запросы на вступление в клан на текущий момент:"

clan_invite_declined = "✅ Приглашение в клан {} было успешно отклонено"
clan_invite_accepted = "✅ Приглашение в клан {} было успешно принято!"

clan_req_accepted = "✅ Запрос на вступление в клан было успешно принят! В рядах вашего клана новый участник: {}"
clan_req_declined = "✅ Запрос на вступление в клан {} было успешно отклонен!"

you_was_accepted_to_clan = "🎊 Ты успешно вступил в клан {}."

you_was_declined_to_clan = "❌ Увы, ваша заявка на вступление в клан {} была отклонена."

user_desc_attrs = ["<b>👥 Игрок:</b> {}", "<b>⭐ Уровень:</b> {}", "<b>♨️ Сила:</b> {}", "<b>🏵 Слава:</b> {} ({})"]

not_in_clan = "❗️ Для выполнения этого действия нужно быть в клане."

clan_settings_message = f"""
<b>{clan_buttons[3]}</b>

Тут можно настроить параметры клана. 
"""

clan_settings_buttons = {"🖼 Сменить эмодзи": "change-emoji", "✏️ Изменить название": "change-title", "🚫 Удалить клан": "delete-clan"}

emoji_choised = "{} Эмодзи клана было успешно изменено."

emoji_was_buy = "{} Эмодзи было куплено за {}."

clan_change_title_message = f"<b>✏️ Изменить название клана</b>\n\n<i>Стоимость смены названия клана - {config.CHANGE_CLAN_TITLE_COST}💰</i>\n\n<b>Сменить название?</b>"

successfully_changed_clan_title = "✅ Название клана было успешно изменено на {}."

are_you_sure_delete_clan = "<b>🚫 Удалить клан</b>\n\n<i>Если ты удалишь клан, то весь прогресс, игроки выйдут, значки клана будут удалены.</i>\n\n<b>Ты уверен что хочешь удалить клан?</b>"

clan_deleted = "<b>Ваш клан был успешно удален.</b>"

coupons_message = """
<b>🎫 Купоны</b>

<b>🎫 Купоны</b> - особая валюта, с помощью нее можно получить уникальные вещи или бонусы.

❓ Купоны даются за реферальную программу и некоторые квесты. Также есть шанс выпадения купонов со всех убитых монстров"""

coupons_buttons = ["🎫 Магазин", "🎫 Пополнить", settings_buttons_text[3]]

shop_message = "{}\n\nЧто ты хочешь купить?"

coupon_buy_message = "🎫 {} купонов - {} руб."

coupons_shop = {
    "🌟 Премиум": "c_premium",
    "💚 Регенерация": "c_regeneration",
    "✨ Опыт": "c_xp",
    "💰 Золото": "c_gold",
    "🔑 Ключи": "c_keys",
    "🎟 Прочее": "c_other"
}

coupons_titles = {coupons_shop[key]: key for key in coupons_shop.keys()}

successfully_used_bag = "<b>Мешок с золотом был успешно использован.</b>\n\n<i>+{} золота 💰</i>"

effect_been_used = "<b>🧿 Бонусы которые дает этот предмет были уже получены с помощью другого предмета.</b>\n\n<i>Дождитесь пока время действия предмета закончится, чтобы использовать этот.</i>"

dont_fuld = "❗ Не стоит флудить !"

enemy_drop = "Награда за убийство:\n✨ <b>Опыт:</b> {}\n💰 <b>Золото:</b> {} \n\n<i>Дроп ресурсов:</i>\n {}"
quest_reward = "Награда за выполнение квеста:"

take_quest = "✔️ Взять квест"
cancel_quest = "✖️ Отменить квест"

quest_taked = "✔️ Квест был взят"
quest_canceled = "✖️ Квест был отменен"

you_getted_reward_quest = "❗ Вы уже получали награду за квест!"

referal_message = """
<b>🎎 Рефералы</b>

Приглашай друзей чтобы быстрее развиваться и веселее проводить время, усиль свою расу новыми бойцами!
За каждого приведенного игрока, ты получишь: 
💚 Бонус регенерации 24ч
✨ Зелье +50% к опыту 

Ты пригласил: <b>{}</b> игроков. 
Посмотреть приглашенных: /get_reflist

<b>Скинь другу свою уникальную ссылку и получи бонусы:</b>
"""

invite_to_game = "🔎 Позвать в игру"

invite_game_message = """
⚔️ Настало время играть в MMO нового поколения прямо из telegram!
Присоединяйся в ряды моей армии
{}"""

you_have_new_referal = "По твоей реферальной ссылке перешел человек!\n<b>Ты получил:</b>\n💚 Бонус регенерации 24ч\n✨ Зелье +50% к опыту "

freinds_list_empty = f"<b>🎎 Список приглашенных друзей:</b>\n\nУ тебя пока нет приглашенных друзей.."

freinds_list_not_empty = "<b>🎎 Список приглашенных друзей:</b>"

admin_button = "🔑 Админ панель"

admin_buttons = ["🐚 Изменить событие", hero_buttots_keyb[6]]

change_event_buttons = ["📃 Описание события", "📄 Список команд", cancel_del, "🏁 Завершить создание"]

not_have_event = "<i>Пока что нет событий.</i>"

event_info_desc = "Игровое событие, которое вы видите, будет меняться в зависимости от внутреннего мира игры, а также внешних событий реального мира."

event_rewards = "<b>Награды события:</b>"

event_buttons = ["🎁 Получить награду события", "✅ Награда за событие была успешно получена"]

event_reward_been_taked = "Награда за событие была уже получена."
event_reward_now_taked = "Вы успешно получили награду за событие!"


you_finded_opponent = f"""
Вот ты и встретил своего врага.

Твоим соперником будет {{}}

<b>{where_you_will_to_hit}</b>"""


async def gfr(res_type, clan_war_active):
    pvp_points_reward = "\n" + user_power.format(
        ' + ' + str(config.PVP_POINTS_REWARD_ONLINE)) if clan_war_active else ""
    pvp_points_discard = "\n" + user_power.format(
        ' - ' + str(config.PVP_POINTS_DISCARD_ONLINE)) if clan_war_active else ""
    if res_type == "default_win":
        return f"Ты победил своего противника!\n<b>Твоя награда:</b>{pvp_points_reward}\n{hero_item_list[4]} +{config.GLORY_REWARD_ONLINE}"
    elif res_type == "surrender_win":
        return f"Твой противник сдался.\n<b>Твоя награда:</b>{pvp_points_reward}\n{hero_item_list[4]} +{config.GLORY_REWARD_ONLINE}"
    elif res_type == "default_lose":
        return f"Твой противник победил.\n<b>Ты потерял:</b>{pvp_points_discard}\n{hero_item_list[4]} -{config.GLORY_DISCARD_ONLINE}"
    elif res_type == "surrender_lose":
        return f"Ты сдался, противник победил.\n<b>Ты потерял:</b>{pvp_points_discard}\n{hero_item_list[4]} -{config.GLORY_DISCARD_ONLINE}"
    else:
        return f"Бой завершился у вас <b>ничья</b>. 🎌\n\nТы был отправлен восстанавливаться в город"


two_users_skip_move = "<i>⏳ Оба игрока пропустили ход, поэтому значения были выбраны случайно.</i>"

clan_war_will_be_x = f"\nКлановые войны {{}} через <b>{{}}д {{}}ч {{}}мин</b>\n"
clan_war_is_will_be_started = "начнутся"
clan_war_is_will_be_over = "закончатся"

heirs = "👑 Наследники: {}"

clan_wars_start_on = "🌙 Klan müharibəsinin başlanğıcı: ({}) ⚔️"
clan_wars_over_on = "🌙 Klan müharibəsinin sonu: ({}) ⚔️"

clan_reward_res = "<b>Ваш клан занял {} место в клановой войне. Вы получили такие награды:</b>\n"

clan_war_rewards = {
    1: clan_reward_res.format(1) + "3х 🔑 NFT Ключ\n300 💰 Золота\n2х Бонус регенерация 💚 3 дня \n8x 🩸 Кровь шахида",
    2: clan_reward_res.format(2) + "2х 🔑 NFT Ключ\n200 💰 Золота\n1х Бонус регенерация 💚 3 дня \n5x 🩸 Кровь шахида",
    3: clan_reward_res.format(3) + "1х 🔑 NFT Ключ\n150 💰 Золота\n3x 🩸 Кровь шахида",
}

opponent_use_dodge = " <i>(⚡️ уворот соперника на {} урона)</i>"

lvls = {31: "SS", 32: "SSS"}

choice_name = "Выбери имя"

shaman_desc = f"<b>{nps_baki_list[3]}</b>\n\nЯ обладаю уникальной способностью открывать запертые сундуки. \n\n<i>🔑 Количество ключей:</i> {{}}"

boxes_rarity_list = {"siravi_box": "🪬 Сирави сундук", "epic_box": "🔮 Эпический сундук",
                     "legendary_box": "💎 Легендарный сундук"}

box_raruty = "Сундук редкости {}"
box_open_cost = "<b>🔑 Стоимость открытия: {} ключей.\n🎒 У вас в инвентаре {}.</b>"
box_resources_drop = "<i>Дроп</i>:"

box_open = "🔐 Открыть сундук"

box_is_opening = f"<b>{nps_baki_list[3]}</b>\n\n<i>Желаю удачи!</i>\n\nОткрываю сундук: {{}}"

box_was_opened = f"<b>{nps_baki_list[3]}</b>\n\nСундук был открыт, и тебе выпал: {{}}"

what_you_want_to_create = "<i>Что ты хочешь изготовить?</i>"

to_craft = "⚒ Скрафтить"

need_resouces_for_craft = "<b>Необходимые ресурсы для крафта:</b>"

you_dont_have_need_resources = "У вас недостаточно необходимых ресурсов для крафта!"
successfull_created = "Предмет {} успешно создан."


user_not_in_bot = "Пользователь пока не был зарегистрирован в боте."
