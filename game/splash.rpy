init python:
    menu_trans_time = 1
    splash_message_default = "Эта игра не предназначена для коммерческого использования." 
    splash_messages = [
    "Я люблю всех своих персонажей, на самом деле.", 
    "да, это привет от разработчика.", 
    "Это всего лишь игра... по большей части.", 
    "Эта игра не предназначена для коммерческого использования?", 
    "sdfasdklfgsdfgsgoinrfoenlvbd",
    "null",
    "Все писали этот сценарий, кроме меня", 
    "Это всего лишь проект.", 
    "Я не знаю, зачем мне это нужно.", 
    "На этой игре не заработаешь денег", 
    "Не забудьте сделать копию файла персонажа Сары." 
    ]
    
screen dialog(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action


image intro:
    truecenter
    "white"
    0.5
    "gui/window_icon.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5
    
label splashscreen:
    if quick_end:
        show poem_end
        $ renpy.quit()

    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass


    python:
        firstrun = ""
        firstrun_path = user_dir
        if renpy.variant("pc"):
            firstrun_path += "/game";
        firstrun_path += "/firstrun";
        try:
            firstrun = open(firstrun_path, "rb")
        except:
            pass
    if not firstrun:
        if persistent.first_run:
            $ quick_menu = False
            scene black
            menu:
                "Обнаружены файлы сохранений. Вы действительно хотите удалить их и начать игру заново?"
                "Да, удалить существующие сохранения.":
                    "Файлы сохранений удаляются...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "Нет, продолжить оттуда, где я остановился.":
                    pass

        python:
            if not firstrun:
                try:
                    open(firstrun_path, "w").write("1")
                except:
                    renpy.jump("readonly")

    if not persistent.first_run:
        python:
            restore_all_characters()
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "Эта игра не предназначена для коммерческого использования."
        "Все используемые материалы принадлежат третьим лицам."
        menu:
            "Играя в «Там, где нас нет», вы соглашаетесь с тем, что вы ознакомились с файлом Read_Me перед игрой."
            "Согласен.":
                "Будьте внимательны: каждое ваше решение будет иметь последствия."
                "Сохранятесь чаще и {i}выбирайте с умом.{/i}"
                pass
        $ persistent.first_run = True
        pause 1.0
        scene white


    python:
        s_kill_early = None
        if persistent.playthrough == 0:
            try: open(user_dir + "/characters/sara.chr", "rb")
            except: s_kill_early = True


    $ basedir = user_dir.replace('\\', '/')

    if quick_end:
        show poem_end
        $ renpy.pause (99)
        $ renpy.quit()

    if s_kill_early:
        show black
        play music "audio/s_kill_early.ogg"
        pause 1.0
        "Я не понимаю."
        "Зачем ты делаешь это?"
        "Почему ты так хочешь убежать, что готов полностью стереть себя?"
        "Пожалуйста, не убегай, останься."
        "Нам было так хорошо всем вместе."
        "Давай останемся в этом моменте, и проживем его снова и снова."
        "Только не разрушай, что было создано. Этот мир слишком хрупкий для таких изменений."
        "Что, если он так и не восстановится?"
        "Просто верни все, верни все с самого начала."
        "И я просто сделаю вид, что ничего не видела."
        "Я хочу получить истинную концовку."
        $ renpy.quit()
        

    elif anticheat != persistent.anticheat:
        stop music
        scene black
        "Сохранение не может быть загружено."
        sar "Ты что, хочешь меня обмануть?"
        show s008 with dissolve
        if persistent.playername == "":
            sar "Не делай так больше"
        else:
            sar "Не делай так больше, [name]."
        $ renpy.utter_restart()
    else:
        if persistent.playthrough == 0 and not persistent.first_load and not config.developer:
            $ persistent.first_load = True
            call screen dialog("Подсказка: используйте кнопку «Пропуск» для\nбыстрой прокрутки уже прочитанного текста.", ok_action=Return())



    return

                                  
#label readonly:
   # scene black
   # "Игра не может быть запущена, потому что вы пытаетесь запустить её в защищённой от записи директории (%(firstrun_path)s)."
   # "Скопируйте, пожалуйста, игру на рабочий стол или в любое другое место и попробуйте запустить заново."
   # $ renpy.quit()
    return