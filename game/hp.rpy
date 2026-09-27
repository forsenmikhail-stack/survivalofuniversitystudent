# Здоровье студента. Максимум 10, шаг штрафа — половина HP.

default hp = 10.0
default hp_max = 10

init python:
    def wrong_answer():
        """Неправильный ответ преподавателю: −0.5 HP."""
        store.hp = max(0.0, round(store.hp - 0.5, 1))
        renpy.notify("Неверный ответ: −0.5 HP")
        return store.hp

    def hp_label():
        if store.hp == int(store.hp):
            return str(int(store.hp))
        return "{:.1f}".format(store.hp)


screen hp_hud():
    zorder 80

    if hp_visible:
        frame:
            xalign 0.985
            yalign 0.03
            background "#00000099"
            padding (18, 12)

            vbox:
                spacing 8

                text "HP [hp_label()] / [hp_max]":
                    size 28
                    color "#f2f2f2"

                hbox:
                    spacing 6
                    for i in range(hp_max):
                        bar:
                            value StaticValue(max(0.0, min(1.0, hp - i)), 1.0)
                            xsize 22
                            ysize 34
                            left_bar Solid("#e05050")
                            right_bar Solid("#2a2a2a")
                            thumb None
                            left_gutter 0
                            right_gutter 0

# HP подключим позже, когда дойдём до сюжета с ответами.
default hp_visible = False

# init python:
#     config.overlay_screens.append("hp_hud")
