# Превью ассетов — потом заменим на сюжет.

# --- Задники ---
image bg corridor = Transform("bg corridor.png", xysize=(1920, 1080))
image bg lecture_hall = Transform("bg lecture_hall.png", xysize=(1920, 1080))
image bg computer_lab = Transform("bg computer_lab.png", xysize=(1920, 1080))
image bg student_room = Transform("bg student_room.png", xysize=(1920, 1080))
image bg bus_stop_waiting = Transform("bg bus_stop_waiting.png", xysize=(1920, 1080))
image bg bus_stop_boarding = Transform("bg bus_stop_boarding.png", xysize=(1920, 1080))
image bg bus_stop_dawn_waiting = Transform("bg bus_stop_dawn_waiting.png", xysize=(1920, 1080))
image bg bus_stop_dawn_boarding = Transform("bg bus_stop_dawn_boarding.png", xysize=(1920, 1080))
image bg chapter_1 = Transform("bg chapter_1.png", xysize=(1920, 1080))

# --- Преподаватели ---
define t_prog = Character("Игорь Семёнович", color="#8fa4b8")
define t_math = Character("Елена Викторовна", color="#c4a484")
define t_proj = Character("Марина Олеговна", color="#6b9e9e")

# --- Студенты ---
define s_kristina = Character("Кристина", color="#9bb8d4")
define s_vika = Character("Вика", color="#7a9e7a")
define s_nastya = Character("Настя", color="#e8b4a0")
define s_vadik = Character("Вадик", color="#e09a5a")
define s_petya = Character("Петя", color="#8a8a9a")
define s_dima = Character("Дима", color="#5a7aa8")

label start:
    # $ hp = 10.0
    # jump hp_demo
    jump chapter_1

label hp_demo:

    scene bg lecture_hall
    with fade

    show teacher_math composed at center
    with dissolve

    t_math "Пробный вопрос. Чему равен предел sin(x) / x, когда x стремится к нулю?"

    menu:
        "Единице":
            show teacher_math calm
            t_math "Верно. HP не трогаю."

        "Нулю":
            $ wrong_answer()
            show teacher_math scold
            t_math "Неверно. Минус половина HP."

        "Бесконечности":
            $ wrong_answer()
            show teacher_math scold
            t_math "Неверно. Минус половина HP."

    if hp <= 0:
        jump hp_fail

    show teacher_math talking
    t_math "Ещё один. Производная x в квадрате?"

    menu:
        "2x":
            show teacher_math calm
            t_math "Верно."

        "x":
            $ wrong_answer()
            show teacher_math frown
            t_math "Нет. Снова минус половина."

        "x в квадрате":
            $ wrong_answer()
            show teacher_math scold
            t_math "Нет. Снова минус половина."

    if hp <= 0:
        jump hp_fail

    show teacher_math composed
    t_math "На этом пробные вопросы закончены. Сейчас HP: [hp_label()]."

    jump preview_teacher_faces

label hp_fail:

    show teacher_math scold
    t_math "HP на нуле. На пересдачу."

    "Пробный провал. В полном сюжете отсюда будет отдельная ветка."

    return

label preview_teacher_faces:

    scene bg chapter_1
    with fade

    "Глава 1. Знакомства."

    scene bg computer_lab
    with fade

    show teacher_prog calm at center
    with dissolve
    t_prog "Спокойное."

    show teacher_prog composed
    with dissolve
    t_prog "Собранное."

    show teacher_prog talking
    with dissolve
    t_prog "Говорящее."

    show teacher_prog frown
    with dissolve
    t_prog "Хмурое."

    show teacher_prog scold
    with dissolve
    t_prog "Хмуро разговаривающее. Лаба снова не компилируется?"

    scene bg lecture_hall
    with dissolve

    show teacher_math calm at center
    with dissolve
    t_math "Спокойное."

    show teacher_math composed
    with dissolve
    t_math "Собранное."

    show teacher_math talking
    with dissolve
    t_math "Говорящее."

    show teacher_math frown
    with dissolve
    t_math "Хмурое."

    show teacher_math scold
    with dissolve
    t_math "Хмуро разговаривающее. Кто опять забыл пределы?"

    scene bg corridor
    with dissolve

    show teacher_project calm at center
    with dissolve
    t_proj "Спокойное."

    show teacher_project composed
    with dissolve
    t_proj "Собранное."

    show teacher_project talking
    with dissolve
    t_proj "Говорящее."

    show teacher_project frown
    with dissolve
    t_proj "Хмурое."

    show teacher_project scold
    with dissolve
    t_proj "Хмуро разговаривающее. Дедлайн проекта был вчера."

    scene bg bus_stop_waiting
    with dissolve
    "Утро. Остановка — студенты ждут автобус."

    scene bg bus_stop_boarding
    with dissolve
    "Автобус подъехал."

    scene bg bus_stop_dawn_waiting
    with dissolve
    "Раннее утро, другой ракурс. Солнце только встаёт — студенты ждут автобус."

    scene bg bus_stop_dawn_boarding
    with dissolve
    "Тот же рассвет. Автобус остановился, все заходят."

    scene bg student_room
    with dissolve
    "Вечер. Комната студента."

    jump preview_students

label preview_students:

    scene bg lecture_hall
    with fade

    show student_kristina simple at center
    with dissolve
    s_kristina "Кристина. Простое."

    show student_kristina dumb
    with dissolve
    s_kristina "Тупое."

    show student_kristina serious
    with dissolve
    s_kristina "Серьёзное."

    show student_kristina happy
    with dissolve
    s_kristina "Весёлое."

    show student_kristina sad
    with dissolve
    s_kristina "Грустное."

    show student_kristina smart
    with dissolve
    s_kristina "Умное."

    hide student_kristina
    show student_vika simple at center
    with dissolve
    s_vika "Вика. Простое."

    show student_vika dumb
    with dissolve
    s_vika "Тупое."

    show student_vika serious
    with dissolve
    s_vika "Серьёзное."

    show student_vika happy
    with dissolve
    s_vika "Весёлое."

    show student_vika sad
    with dissolve
    s_vika "Грустное."

    show student_vika smart
    with dissolve
    s_vika "Умное."

    hide student_vika
    show student_nastya simple at center
    with dissolve
    s_nastya "Настя. Простое."

    show student_nastya dumb
    with dissolve
    s_nastya "Тупое."

    show student_nastya serious
    with dissolve
    s_nastya "Серьёзное."

    show student_nastya happy
    with dissolve
    s_nastya "Весёлое."

    show student_nastya sad
    with dissolve
    s_nastya "Грустное."

    show student_nastya smart
    with dissolve
    s_nastya "Умное."

    hide student_nastya
    show student_vadik simple at center
    with dissolve
    s_vadik "Вадик. Простое."

    show student_vadik dumb
    with dissolve
    s_vadik "Тупое."

    show student_vadik serious
    with dissolve
    s_vadik "Серьёзное."

    show student_vadik happy
    with dissolve
    s_vadik "Весёлое."

    show student_vadik sad
    with dissolve
    s_vadik "Грустное."

    show student_vadik smart
    with dissolve
    s_vadik "Умное."

    hide student_vadik
    show student_petya simple at center
    with dissolve
    s_petya "Петя. Простое."

    show student_petya dumb
    with dissolve
    s_petya "Тупое."

    show student_petya serious
    with dissolve
    s_petya "Серьёзное."

    show student_petya happy
    with dissolve
    s_petya "Весёлое."

    show student_petya sad
    with dissolve
    s_petya "Грустное."

    show student_petya smart
    with dissolve
    s_petya "Умное."

    hide student_petya
    show student_dima simple at center
    with dissolve
    s_dima "Дима. Простое."

    show student_dima dumb
    with dissolve
    s_dima "Тупое."

    show student_dima serious
    with dissolve
    s_dima "Серьёзное."

    show student_dima happy
    with dissolve
    s_dima "Весёлое."

    show student_dima sad
    with dissolve
    s_dima "Грустное."

    show student_dima smart
    with dissolve
    s_dima "Умное."

    "Превью студентов закончено."

    return

label chapter_1:

    scene bg chapter_1
    with fade

    "Глава 1. Знакомства."

    scene bg bus_stop_dawn_waiting
    with dissolve

    "Рассвет. Остановка у универа ещё тихая."

    show student_dima simple at center
    with dissolve

    s_dima "Значит, это здесь. Первый день."

    scene bg bus_stop_dawn_boarding
    with dissolve

    "Автобус останавливается. Дима заходит вместе с остальными."

    scene bg corridor
    with dissolve

    show student_dima serious at center
    with dissolve

    s_dima "Коридор длинный. Аудитория где-то дальше по расписанию."

    scene bg lecture_hall
    with dissolve

    "В аудитории группа уже на местах. Дима садится на свободный стул."

    hide student_dima
    show student_vika serious at center
    with dissolve

    s_vika "Новенький на месте. Я Вика, староста. Расписание на сегодня сверила: сначала знакомимся мы, потом зайдут преподаватели."

    hide student_vika
    show student_nastya simple at center
    with dissolve

    s_nastya "Настя. Мы с Викой с одной школы и сегодня приехали вместе. Если заблудишься в корпусе, лучше спроси её: она вчера весь этаж обошла."

    hide student_nastya
    show student_vika happy at center
    with dissolve

    s_vika "Не преувеличивай. Просто не хочу, чтобы нас в первый день раскидало по чужим аудиториям."

    hide student_vika
    show student_kristina simple at center
    with dissolve

    s_kristina "Кристина. Живу в общежитии напротив. На пары обычно прихожу до звонка и сажусь ближе к доске."

    hide student_kristina
    show student_vadik simple at center
    with dissolve

    s_vadik "Вадик. Я за последней партой у окна. Если что-то объявят в начале пары, могу не услышать, так что лучше пните."

    hide student_vadik
    show student_petya serious at center
    with dissolve

    s_petya "Петя. Я к семестру готовился: конспекты разложил по папкам, всё подписал."

    show student_petya dumb
    with dissolve

    s_petya "Только аудиторию перепутал. На табличке 214, а я два раза прочитал и чуть не ушёл в 314."

    hide student_petya
    show student_nastya serious at center
    with dissolve

    s_nastya "Ты уже в 214. Садись, никуда уходить не надо."

    hide student_nastya
    show student_dima simple at center
    with dissolve

    s_dima "Дима. Только приехал, группу вижу первый раз. Если отстану, буду спрашивать."

    hide student_dima
    show student_vika serious at center
    with dissolve

    s_vika "Тогда все на местах. Сейчас зайдут преподаватели."

    hide student_vika
    show teacher_math composed at center
    with dissolve

    t_math "Елена Викторовна. В этом семестре веду у вас математический анализ и алгебру с геометрией."

    show teacher_math talking
    with dissolve

    t_math "Лекции и семинары по расписанию. Контрольные объявляю заранее. Кто весь семестр молчит и появляется только на зачёте, обычно не сдаёт."

    hide teacher_math
    show teacher_prog calm at center
    with dissolve

    t_prog "Игорь Семёнович. Программирование."

    show teacher_prog talking
    with dissolve

    t_prog "Практики будут в компьютерном классе. Лабораторные сдаёте мне, не друг другу. Если программа не запускается, это ещё не сдача."

    hide teacher_prog
    show teacher_project composed at center
    with dissolve

    t_proj "Марина Олеговна. Проектный практикум."

    show teacher_project talking
    with dissolve

    t_proj "Будете работать вместе со студентами старших курсов. Тема одна на команду, сроки общие. Кто пропадает из общей работы, тянет вниз всех."

    show teacher_project calm
    with dissolve

    t_proj "На сегодня знакомств достаточно. Дальше идём по расписанию."

    hide teacher_project
    with dissolve

    "Первый день только начался."

    return
