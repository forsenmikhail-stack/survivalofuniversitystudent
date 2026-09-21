# Превью ассетов — потом заменим на сюжет.

# --- Задники ---
image bg corridor = Transform("bg corridor.png", xysize=(1920, 1080))
image bg lecture_hall = Transform("bg lecture_hall.png", xysize=(1920, 1080))
image bg computer_lab = Transform("bg computer_lab.png", xysize=(1920, 1080))
image bg student_room = Transform("bg student_room.png", xysize=(1920, 1080))
image bg bus_stop_waiting = Transform("bg bus_stop_waiting.png", xysize=(1920, 1080))
image bg bus_stop_boarding = Transform("bg bus_stop_boarding.png", xysize=(1920, 1080))

# --- Преподаватели ---
define t_prog = Character("Игорь Семёнович", color="#8fa4b8")
define t_math = Character("Елена Викторовна", color="#c4a484")
define t_proj = Character("Марина Олеговна", color="#6b9e9e")

label start:
    jump preview_teacher_faces

label preview_teacher_faces:

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

    scene bg student_room
    with dissolve
    "Вечер. Комната студента."

    "Превью ассетов закончено."

    return
