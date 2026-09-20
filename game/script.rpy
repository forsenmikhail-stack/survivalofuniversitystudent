# Превью преподавателей и эмоций.

define t_prog = Character("Игорь Семёнович", color="#8fa4b8")
define t_math = Character("Елена Викторовна", color="#c4a484")
define t_proj = Character("Марина Олеговна", color="#6b9e9e")

label start:
    jump preview_teacher_faces

label preview_teacher_faces:

    scene black
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
    t_prog "Хмуро разговаривающее."

    hide teacher_prog
    show teacher_math calm at center
    with dissolve
    t_math "Спокойное / собранное / говорящее / хмурое / хмуро разговаривающее — те же эмоции."

    hide teacher_math
    show teacher_project calm at center
    with dissolve
    t_proj "Проектный практикум — спрайты готовы."

    "Отрисовка преподавателей."

    return
