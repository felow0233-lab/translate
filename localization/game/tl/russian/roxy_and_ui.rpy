# Mushoku Tensex 0.10.0 — русская локализация интерфейса и безопасной сцены Рокси.
# Не меняет игровые переменные, условия или переходы.

translate russian strings:
    old "Back"
    new "Назад"

    old "History"
    new "История"

    old "Skip"
    new "Пропустить"

    old "Auto"
    new "Авто"

    old "Save"
    new "Сохранить"

    old "Q.Save"
    new "Быстрое сохранение"

    old "Q.Load"
    new "Быстрая загрузка"

    old "Prefs"
    new "Настройки"

    old "Start"
    new "Начать"

    old "Load"
    new "Загрузить"

    old "Preferences"
    new "Настройки"

    old "End Replay"
    new "Завершить повтор"

    old "Main Menu"
    new "Главное меню"


    old "Quit"
    new "Выход"

    old "Skip introduction"
    new "Пропустить вступление"

    old "Watch introduction"
    new "Посмотреть вступление"

    old "You feel tired and decide to rest for the day."
    new "Ты устал и решил отдохнуть до конца дня."

    old "💗 Call Girl"
    new "💗 Позвать девушку"

    old "🌾 Go to the Barn"
    new "🌾 Пойти в сарай"

    old "Call Aisha"
    new "Позвать Айшу"

    old "Call Zenith"
    new "Позвать Зенит"

    old "Call Roxy"
    new "Позвать Рокси"

    old "Call Lilia"
    new "Позвать Лилию"

    old "Call Norn"
    new "Позвать Норн"

    old "Call [s_dog_name]"
    new "Позвать [s_dog_name]"

    old "🛒 Village Shop"
    new "🛒 Деревенская лавка"

    old "🔨 Blacksmith's Forge"
    new "🔨 Кузница"

    old "🍺 Tavern"
    new "🍺 Таверна"

    old "⚔️ Hunt the Slime Girl"
    new "⚔️ Охотиться на слизневую девушку"

    old "💜 Approach the mysterious girl (!)"
    new "💜 Подойти к загадочной девушке (!)"

    old "Call Sylphie"
    new "Позвать Сильфи"

    old "🏰 Enter the Castle"
    new "🏰 Войти в замок"

    old "🕵️ Black Merchant"
    new "🕵️ Чёрный торговец"












translate russian roxy_pre_menu:
    scene bg taverna with fade

    "Ты входишь в таверну. В воздухе витает тёплый запах эля и жареного мяса."

    rudeus "(Хм? Кто это там сидит совсем один в дальнем углу?)"

    show roxy normal at center, slide_fade
    with dissolve

    rudeus "(...Хм. Милая. Даже очень милая.)"

    rudeus "(Интересно, что она здесь делает совсем одна?)"

    show roxy:
        ease 0.5 xalign 0.8

    show rudeus normal at my_left, slide_fade

    rudeus "Привет. Не возражаешь, если я немного посижу с тобой?"

    roxy "Ой! Э-э... к-конечно, присаживайся..."

    rudeus "И что такая девушка делает в подобном месте в одиночестве?"

    roxy "Я-я не просто «девушка»... Вообще-то, я обучаю магии."

    rudeus "(Учитель магии? Да ещё и такая милая... Хех, мне повезло.)"

    rudeus "Учитель магии, значит? Впечатляет."

    roxy "Я-знаю, что могу выглядеть не слишком убедительно, но в магии я действительно разбираюсь."

    rudeus "Я ни капли в этом не сомневаюсь. И сколько будет стоить твоё обучение?"

    roxy "Я беру 25 золотых монет за один урок."

    rudeus "Справедливая цена. Честно говоря, мне бы очень пригодился такой учитель."

    menu:
        "Нанять её учителем":
            rudeus "Отлично, ты принята. Добро пожаловать, учитель."

            roxy "П-правда?! Ты серьёзно?"

            "Лицо Рокси озаряется радостью, и она широко улыбается."

            roxy "Большое спасибо! Обещаю, я стану для тебя отличным учителем!"

            $ contratou_roxy = True
            $ roxy_evento = 1
            $ renpy.notify("Ты нанял Рокси учителем магии!")
            jump locais
