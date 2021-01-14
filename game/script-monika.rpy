label rps:
    $ win = 0
    $ lose = 0
    $ rps_beats = [("камень", "ножницы"), ("ножницы", "бумага"), ("бумага", "камень")]
    if win > 0:
        show a407 with dissolve
        al "Да блин!"
        hide a407 with dissolve
    if lose > 0:
        show a419 with dissolve
        al "Опа! Ха!"
        hide a419 with dissolve
    else:
        if win = 2:
            show a423 with dissolve
            show m224 at right with dissolve
            me "Ага! Все, ты обещал!"
            hide a423
            show a426
            al "Да блин, это тебе повезло просто!"
            me "Ничего не знаю, ты обещал."
            hide a426
            show a433
            al "Приятно видеть, что тебя так любят."
            hide a433 with moveoutleft
            "Показательно вздохнув, Алан развернулся и пошел дальше по дорожке."
            hide m224
            show m225 at right
            show m225 at center with move
            mon "По-мужски, значит."
            me "Прости, ну а что мне надо было делать?"
            hide m225
            show m207
            mon "Да нет, ничего. Главное, что сработало."
            hide m207
            show m214
            mon "Спасибо."
            "Я почти физически почувствовал, как у меня за спиной вырастают крылья."
            $ monwheel = true
            hide m214
            show m230
            mon "Боже, неужели он и правда ушел."
            me "Да уж, вот привяжется – не отстанет…"
            return
        if lose = 2:
            show a410 with dissolve
            show m222 at right with dissolve
            al "Хе-хе, смотрите, кто выиграл!"
            hide a410
            show a411
            hide m222
            show m204 at right
            mon "Да ладно, ты умудрился проиграть ему в этой дурацкой игре?!"
            hide a411
            show a402
            al "Эй, попрошу, это вовсе не дурацкая игра!"
            hide a402
            show a403
            al "Это международный способ узнать, кто круче!"
            hide a403
            show a420
            hide m204
            show m237 at right
            al "Я круче."
            hide m237
            show m240 at right
            mon "Слышишь, мистер я круче, давай ты все-таки уйдешь и оставишь нас в покое?"
            hide a420
            show a409
            hide m240
            show m204 at right
            al "Ну нет, я честно выиграл!"
            hide a409
            show a410
            hide m204
            show m242 at right
            al "И теперь никуда вы от меня не денетесь."
            hide a410
            show a419
            "Господи Боже. {w}Да он специально решил над нами поиздеваться."
            return
    menu:
        "Камень!":
            $ rps_player = "камень"
        "Бумага!":
            $ rps_player = "бумага"
        "Ножницы!":
            $ rps_player = "ножницы"

    $ rps_npc = renpy.random.choice(["камень", "бумага", "ножницы"])

    al "Я выбрал %(rps_npc)!"

    if (rps_player, rps_npc) in rps_beats:
        $ win +=1
        show a404 with dissolve
        al "Рано радуешься, просто повезло."
        me "Да-да, конечно."
        hide a404 with dissolve
        jump rps

    elif (rps_npc, rps_player) in rps_beats:
        $ lose += 1
        show a410 with dissolve
        al "Ха! Съел?"
        me "Я еще отыграюсь."
        hide a410 with dissolve
        jump rps

    else:
        show a410 with dissolve
        al "У-у-у, ситуация накаляется!"
        hide a404 with dissolve
        jump rps

screen battletime:
    timer 0.1 repeat True action If(time > 0, true=SetVariable('time', time - 0.02), false = [Hide('battletime'), Jump(timerjump)])    #Первый тайм - пауза между снятием времени, Второй тайм - минус времени     #####     Jump(timerjump)]) - командой этой мы обозначаем каким кодом мы будем вызывать переход если не успеет по времени персонаж сделать выбор

    bar:
     style "timebar"
     value time
     xalign 0.5 yalign 0.2# расположение бара, 0.5 посередине ширины экрана, 0.2 сверху но не на самом краю



screen my_scr:

    timer 1.0 action If(my_timer>1, [SetVariable("my_timer", my_timer-1), Return("smth")], Return("loser")) repeat True

    text u"время - [my_timer] сек." size 30 color "ff0" xalign 0.0 yalign 0.1
    text u"баллы - [score]" size 40 color "c00" xalign 0.5 yalign 0.1
    #text u"повторных нажатий - [counter]" size 20 color "00c"xalign 1.0 yalign 0.1


    key "q" action Return("q")
    key "w" action Return("w")
    key "e" action Return("e")
    key "r" action Return("r")
    key "h" action Return("h")
    key "d" action Return("d")
    key "v" action Return("v")
    key "k" action Return("k")
    key "n" action Return("n")
    key "a" action Return("a")
    key "g" action Return("g")
    key "b" action Return("b")
    key "o" action Return("o")
    key "j" action Return("j")
    key "l" action Return("l")

    key "Q" action Return("Q")
    key "W" action Return("W")
    key "E" action Return("E")
    key "R" action Return("R")
    key "H" action Return("H")
    key "D" action Return("D")
    key "V" action Return("V")
    key "K" action Return("K")
    key "N" action Return("N")
    key "A" action Return("A")
    key "G" action Return("G")
    key "B" action Return("B")
    key "O" action Return("O")
    key "J" action Return("J")
    key "L" action Return("L")

    key "й" action Return(u"й")
    key "ц" action Return(u"ц")
    key "у" action Return(u"у")
    key "к" action Return(u"к")
    key "р" action Return(u"р")
    key "в" action Return(u"в")
    key "м" action Return(u"м")
    key "л" action Return(u"л")
    key "т" action Return(u"т")
    key "ф" action Return(u"ф")
    key "п" action Return(u"п")
    key "и" action Return(u"и")
    key "щ" action Return(u"щ")
    key "о" action Return(u"о")
    key "д" action Return(u"д")

    key "Й" action Return(u"Й")
    key "Ц" action Return(u"Ц")
    key "У" action Return(u"У")
    key "К" action Return(u"К")
    key "Р" action Return(u"Р")
    key "В" action Return(u"В")
    key "М" action Return(u"М")
    key "Л" action Return(u"Л")
    key "Т" action Return(u"Т")
    key "Ф" action Return(u"Ф")
    key "П" action Return(u"П")
    key "И" action Return(u"И")
    key "Щ" action Return(u"Щ")
    key "О" action Return(u"О")
    key "Д" action Return(u"Д")

transform my_transform:
    on show:
        xalign 0.5 yalign 0.5
        alpha 0.0
        parallel:
            linear 0.2 zoom 10.0
        parallel:
            linear 0.1 alpha 1.0
            linear 0.1 alpha 0.0



label balbes2:     ###  Метка куда мы перейдем если не успеем по времени
    hide screen battletime
    hide screen timeout_event2  ### закрываем скрипт наших надписей, что бы они исчезли
    pause 0.1
    "Яне успеваю нажимать на кнопки вовремя..."
    return


label demomo:
    play sound "audio/SAVE_succes.wav"
    scene black
    $ renpy.pause (0.1)
    play sound "audio/mainmenu_select.wav"
    $ renpy.pause (0.1)
    play sound "audio/mainmenu_select.wav"
    $ renpy.pause (0.1)
    play sound "audio/mainmenu_select.wav"
    $ renpy.pause (0.1)
    play sound "audio/SAVE_succes.wav"
    scene end1
    $ renpy.pause (8.0, hard=True)
    menu fight1:
        "Битва":
            scene end2 with dissolve
            $ renpy.pause (3.0)
            scene end3
            $ renpy.pause (3.0)
            "* Q *"
            $ time = 1
            $ timerjump = "balbes"
            $ my_timer = 10
            show screen my_scr
            label loop_one1:
                $ res = ui.interact()
                if res == "loser":
                    hide screen my_scr
                    scene black with dissolve
                    scene room_m with dissolve
                    show s027 with dissolve
                    stop music
                    $ renpy.pause(0.1, hard=True)
                    me "Черт, я проиграл"
                    sar "Ахах, ну ты даешь, давай еще раз!"
                    menu:
                        "Да я сейчас тебя обыграю!":
                            sar "Ну давай, попробуй!"
                        "Давай закончим":
                            sar "Нет уж, я не дам тебе уйти!"
                    jump demomo

                if res not in u"qй":
                    $ renpy.pause(0.1, hard=True)
                    jump loop_one1

                hide text
                show text("[res]") at my_transform

                if res == prev_hit:
                   $ counter += 1
                #else:
                    #$ prev_hit = res
                    #$ counter += 1

                if counter < 3:
                    $ score += (3 - counter)
                $ renpy.pause(0.1, hard=True)

                if score > 130:
                    hide screen my_scr
                    $ renpy.pause(0.1, hard=True)
                    $ renpy.pause(0.0, hard=True)
                    $ renpy.pause(0.0, hard=True)
                    jump far_away
                else:
                    jump loop_one1

    label far_away1:
        hide screen battletime
        hide screen timeout_event2
        scene end5
        $ renpy.pause (1.5)
        scene end6
        "* W *"
        $ time = 1
        $ timerjump = "balbes"
        $ my_timer = 10
        show screen my_scr
        label loop_two1:
            $ res = ui.interact()
            if res == "loser":
                hide screen my_scr
                scene black with dissolve
                scene room_m with dissolve
                show s027 with dissolve
                stop music
                $ renpy.pause(0.1, hard=True)
                me "Черт, я проиграл"
                sar "Ахах, ну ты даешь, давай еще раз!"
                menu:
                    "Да я сейчас тебя обыграю!":
                        sar "Ну давай, попробуй!"
                    "Давай закончим":
                        sar "Нет уж, я не дам тебе уйти!"
                jump demomo

            if res not in u"wц":
                $ renpy.pause(0.1, hard=True)
                jump loop_two1

            hide text
            show text("[res]") at my_transform

            if res == prev_hit:
                $ counter += 1
                #else:
                    #$ prev_hit = res
                    #$ counter += 1

            if counter < 140:
                $ score += (3 - counter)
            $ renpy.pause(0.1, hard=True)

            if score > 260:
                hide screen my_scr
                $ renpy.pause(0.1, hard=True)
                $ renpy.pause(0.0, hard=True)
                $ renpy.pause(0.0, hard=True)
                jump faar_away1

            jump loop_two1

    label faar_away1:
        hide screen battletime
        hide screen timeout_event2
        scene end7
        $ renpy.pause (1.5)
        play sound "sounds/soul_battle_flash.wav"
        scene black
        $ renpy.pause (0.1)
        play sound "sounds/soul_battle_flash.wav"
        scene end8
        "* E *"
        $ time = 1
        $ timerjump = "balbes"
        $ my_timer = 10
        show screen my_scr
        label loop_three1:
            $ res = ui.interact()
            if res == "loser":
                hide screen my_scr
                scene black with dissolve
                scene room_m with dissolve
                show s027 with dissolve
                stop music
                $ renpy.pause(0.1, hard=True)
                me "Черт, я проиграл"
                sar "Ахах, ну ты даешь, давай еще раз!"
                menu:
                    "Да я сейчас тебя обыграю!":
                        sar "Ну давай, попробуй!"
                    "Давай закончим":
                        sar "Нет уж, я не дам тебе уйти!"
                jump demomo

            if res not in u"eу":
                $ renpy.pause(0.1, hard=True)
                jump loop_three1

            hide text
            show text("[res]") at my_transform

            if res == prev_hit:
                $ counter += 1
            #else:
                #$ prev_hit = res
                #$ counter += 1

            if counter < 150:
                $ score += (3 - counter)
                $ renpy.pause(0.1, hard=True)

            if score > 390:
                hide screen my_scr
                $ renpy.pause(0.1, hard=True)
                $ renpy.pause(0.0, hard=True)
                $ renpy.pause(0.0, hard=True)
                jump faaar_away1

            jump loop_three1

    label faaar_away1:
        hide screen battletime
        hide screen timeout_event2
        scene end9 with dissolve
        $ renpy.pause (1.5)
        scene wnd with dissolve
        scene wnd1
        scene black
        $ renpy.pause (0.3)
        scene wnd2
        $ renpy.pause (0.01, hard=True)
        scene wnd3
        $ renpy.pause (0.01, hard=True)
        scene wnd4
        $ renpy.pause (0.01, hard=True)
        scene wnd5
        $ renpy.pause (0.01, hard=True)
        scene wnd6
        $ renpy.pause (0.01, hard=True)
        play sound "sounds/monster_damage_hit.wav"
        scene wnd7
        with vpunch
        $ renpy.pause (2.0, hard=True)
        sar "Да ты совсем разучился играть!"
        sar "Не поддавайся, соберись!"
        "* R H *"
        $ time = 1
        $ timerjump = "balbes"
        $ my_timer = 10
        show screen my_scr
        label loop_four1:
            $ res = ui.interact()
            if res == "loser":
                hide screen my_scr
                scene black with dissolve
                scene room_m with dissolve
                show s027 with dissolve
                stop music
                $ renpy.pause(0.1, hard=True)
                me "Черт, я проиграл"
                sar "Ахах, ну ты даешь, давай еще раз!"
                menu:
                    "Да я сейчас тебя обыграю!":
                        sar "Ну давай, попробуй!"
                    "Давай закончим":
                        sar "Нет уж, я не дам тебе уйти!"
                jump demomo

            if res not in u"rкhр":
                $ renpy.pause(0.1, hard=True)
                jump loop_four1

            hide text
            show text("[res]") at my_transform

            if res == prev_hit:
                $ counter += 1
            else:
                $ prev_hit = res
                $ counter -= 1

            if counter < 160:
                $ score += (3 - counter)
                $ renpy.pause(0.1, hard=True)

            if score > 480:
                hide screen my_scr
                $ renpy.pause(0.1, hard=True)
                $ renpy.pause(0.0, hard=True)
                $ renpy.pause(0.0, hard=True)
                jump faaaar_away1

            jump loop_four1

    label faaaar_away1:
        hide screen battletime
        hide screen timeout_event2
        play sound "sounds/soul_battle_flash.wav"
        scene black with dissolve
        $ renpy.pause (0.1, hard=True)
        play sound "sounds/soul_battle_flash.wav"
        $ renpy.pause (0.1)
        scene x9 with dissolve
        "* D L K *"
        $ time = 1
        $ timerjump = "balbes"
        $ my_timer = 10
        show screen my_scr
        label loop_five1:
            $ res = ui.interact()
            if res == "loser":
                hide screen my_scr
                scene black with dissolve
                scene room_m with dissolve
                show s027 with dissolve
                stop music
                $ renpy.pause(0.1, hard=True)
                me "Черт, я проиграл"
                sar "Ахах, ну ты даешь, давай еще раз!"
                menu:
                    "Да я сейчас тебя обыграю!":
                        sar "Ну давай, попробуй!"
                    "Давай закончим":
                        sar "Нет уж, я не дам тебе уйти!"
                jump demomo

            if res not in u"dвlдkл":
                $ renpy.pause(0.1, hard=True)
                jump loop_five1

            hide text
            show text("[res]") at my_transform

            if res == prev_hit:
                $ counter += 1
            else:
                $ prev_hit = res
                $ counter -= 1

            if counter < 170:
                $ score += (3 - counter)
                $ renpy.pause(0.1, hard=True)

            if score > 1100:
                hide screen my_scr
                $ renpy.pause(0.1, hard=True)
                $ renpy.pause(0.0, hard=True)
                $ renpy.pause(0.0, hard=True)
                jump faaaar_aaway1

            jump loop_five1

    label faaaar_aaway1:
        hide screen battletime
        hide screen timeout_event2
        scene x12 with dissolve
        $ renpy.pause (3.0, hard=True)
        scene x13
        $ renpy.pause (0.01, hard=True)
        scene x14
        $ renpy.pause (0.01, hard=True)
        scene x15
        $ renpy.pause (0.01, hard=True)
        scene x16
        $ renpy.pause (0.01, hard=True)
        scene x17
        $ renpy.pause (0.01, hard=True)
        scene x18
        $ renpy.pause (0.01, hard=True)
        scene x19
        $ renpy.pause (0.01, hard=True)
        scene x20
        $ renpy.pause (0.01, hard=True)
        scene x21
        $ renpy.pause (0.01, hard=True)
        scene x22
        $ renpy.pause (0.01, hard=True)
        scene x23
        $ renpy.pause (0.01, hard=True)
        scene x24
        $ renpy.pause (0.01, hard=True)
        scene x25
        $ renpy.pause (0.01, hard=True)
        scene x26
        $ renpy.pause (0.01, hard=True)
        scene x27
        $ renpy.pause (0.8, hard=True)
        play sound "sounds/battle_item_equip.wav"
        scene x28
        $ renpy.pause (1.0, hard=True)
        scene x29
        "* N A *"
        $ time = 1
        $ timerjump = "balbes"
        $ my_timer = 10
        show screen my_scr
        label loop_six1:
            $ res = ui.interact()
            if res == "loser":
                hide screen my_scr
                scene black with dissolve
                scene room_m with dissolve
                show s027 with dissolve
                stop music
                $ renpy.pause(0.1, hard=True)
                me "Черт, я проиграл"
                sar "Ахах, ну ты даешь, давай еще раз!"
                menu:
                    "Да я сейчас тебя обыграю!":
                        sar "Ну давай, попробуй!"
                    "Давай закончим":
                        sar "Нет уж, я не дам тебе уйти!"
                jump demomo

            if res not in u"nтaф":
                $ renpy.pause(0.1, hard=True)
                jump loop_six1

            hide text
            show text("[res]") at my_transform

            if res == prev_hit:
                $ counter += 1
            else:
                $ prev_hit = res
                $ counter -= 1

            if counter < 180:
                $ score += (3 - counter)
                $ renpy.pause(0.1, hard=True)

            if score > 1000:
                hide screen my_scr
                $ renpy.pause(0.1, hard=True)
                $ renpy.pause(0.0, hard=True)
                $ renpy.pause(0.0, hard=True)
                jump faaaar_aaaway1

            jump loop_six1

    label faaaar_aaaway1:
        hide screen battletime
        hide screen timeout_event2
        scene x30
        $ renpy.pause (0.5, hard=True)
        play sound "sounds/monster_damage_hit.wav"
        scene wnd7 with vpunch
        $ renpy.pause (0.5, hard=True)
        scene x36
        $ renpy.pause (3.0, hard=True)
        play sound "sounds/undyne_spear_appear.wav"
        scene x37 with dissolve
        $ renpy.pause (0.5, hard=True)
        scene x38
        $ renpy.pause (0.1, hard=True)

        "* G B O *"
        $ time = 1
        $ timerjump = "balbes"
        $ my_timer = 10
        show screen my_scr
        label loop_seven1:
            $ res = ui.interact()
            if res == "loser":
                hide screen my_scr
                scene black with dissolve
                scene room_m with dissolve
                show s027 with dissolve
                stop music
                $ renpy.pause(0.1, hard=True)
                me "Черт, я проиграл"
                sar "Ахах, ну ты даешь, давай еще раз!"
                menu:
                    "Да я сейчас тебя обыграю!":
                        sar "Ну давай, попробуй!"
                    "Давай закончим":
                        sar "Нет уж, я не дам тебе уйти!"
                jump demomo

            if res not in u"gпbиoщ":
                $ renpy.pause(0.1, hard=True)
                jump loop_seven1

            hide text
            show text("[res]") at my_transform

            if res == prev_hit:
                $ counter += 1
            else:
                $ prev_hit = res
                $ counter -= 1

            if counter < 190:
                $ score += (3 - counter)
                $ renpy.pause(0.1, hard=True)

            if score > 1600:
                hide screen my_scr
                $ renpy.pause(0.1, hard=True)
                $ renpy.pause(0.0, hard=True)
                $ renpy.pause(0.0, hard=True)
                jump faaaar_aaaaway1

            jump loop_seven1

    label faaaar_aaaaway1:
        hide screen battletime
        hide screen timeout_event2
        if gamesara == True:
            jump aftergame
        if gamealone == True:
            jump aftergame1






label day_mon:
    $ notereason = 0 #целое число, последняя записка//
    $ notefind = 0 #целое число, последняя записка//
    $ notesign = 0 #целое число, последняя записка//

    $ reason1 = False #//дело в размере города//
    $ reason2 = False #//дело в родителях//
    $ reason3 = False #//дело в твоей семье//
    $ monwheel = False #//разговор на колесе//
    $ monrock = False #//будем ли кататься на колесе//
    $ kiss = False #//целовались ли с моникой//
    $ lastmeet = False #//поедем ли мы на репетицию в 4 день//
    $ sBracelet = False #//браслет дружбы//
    $ sPhoto = False #//совместное фото этого года//
    $ sMascot = False #//талисман на удачу//
    $ sPhotoOld = False #//совместное детское фото//
    $ monearly = False #//мы остаемся//
    $ earrings = False #//золотые серьги//

    scene room_m with dissolve
    stop music
    play music "audio/5_monika.ogg"
    "С утра меня разбудил звонок Моники."
    "Он был настолько внезапным, что я забыл проснуться, отвечая на него."
    show m200 with dissolve
    me "Д-да? Что? Кто это?"
    hide m200
    show m210
    mon "Это Моника. Ты что, спишь до сих пор?"
    hide m210
    show m219
    me "М-м-м, нет, нисколько, ни разу… что случилось?"
    me "Сегодня же нет репетиции… {w}Вроде?"
    hide m219
    show m207
    mon "Нет, репетиции сегодня нет, можешь выдохнуть."
    hide m207
    show m201
    mon "Просто вчера мы так и не договорили, ты сказал, что сегодня свободен."
    hide m201
    show m200
    me "Да, но… да, да, я свободен."
    hide m200
    show m224
    mon "Я уж слышу, как ты свободен."
    hide m224
    show m201
    mon "Не знала, что ты сова. Может, тогда встретимся где-нибудь попозже?"
    hide m201
    show m207
    mon "Когда ты там встаешь."
    hide m207
    show m223
    me "Да я… ну, может, часов в двенадцать?"
    hide m223
    show m225
    "Моника издала смешок, и у меня вдруг запылало лицо, как будто я сказал что-то постыдное."
    hide m225
    show m224
    mon "Хорошо, давай в двенадцать."
    me "Давай, м-м-м… да-давай встретимся около центрального парка."
    hide m224
    show m200
    me "Как раз там погуляем и все обсудим. Хорошо?"
    hide m200
    show m219
    mon "Хорошо. Тогда до встречи, соня."
    me "Все, давай, до встречи."
    hide m219 with dissolve
    "Я бросил трубку, не дожидаясь очередных смешков. {w}Кажется, у меня пылали даже уши."
    "Я лег обратно, закутавшись в одеяло, и закрыл глаза."
    "Так странно. Если я не ошибаюсь, каким-то образом я только что пригласил Монику Фишер на свидание."
    "И более того – она согласилась. {w}Поразительно."
    "Нет, на самом деле это вряд ли свидание. Она просто хочет поговорить."
    "Но что, если… {w}А если да?"
    "Надо ли мне как-то приодеться, или это будет выглядеть по-идиотски?"
    "Кажется, обычно девушке покупают цветы на свидания… Но если это не свидание, это тоже будет глупо."
    "Агх, что же делать…"
    scene black with dissolve
    #//локация: темный фон (сон)
    "Погруженный в размышления, я задремал."
    scene room_m with dissolve
    #//локация: наша комната
    "А когда открыл глаза, на часах была половина двенадцатого."
    "Меня буквально подбросило на кровати. Разумеется, ни про какие прихорашивания речь уже не шла."
    "А про цветы и все остальное я напрочь забыл. Не опоздаю – уже хорошо!"
    scene park with dissolve
    #//локация: парк (простой парк)
    stop music
    play music "audio/memories.ogg"
    "Моника ждала меня у входа в парк. {w}При виде меня она приветливо улыбнулась."
    show m224 with dissolve
    mon "Привет еще раз, соня."
    me "Ты что, теперь постоянно будешь так меня называть?"
    hide m224
    show m207
    mon "Нет, но какое-то время придется потерпеть."
    me "Понятно. Ну, у меня были прозвища и пообиднее."
    hide m207
    show m214
    mon "Ну извини, раз это прям обидно…"
    me "Все, закроем тему про сон. Пойдем лучше погуляем по парку."
    hide m214
    show m207
    mon "Пойдем."
    hide m207 with dissolve
    "Какое-то время мы шли молча, переглядываясь друг с другом."
    "Пока Моника не заговорила первой."
    show m216 with dissolve
    mon "Так… значит, ты собрался уезжать."
    me "Ну… да, вроде того."
    hide m226
    show m218
    mon "Надолго? Или насовсем?"
    hide m218
    show m222
    me "Думаю, что насовсем."
    hide m222
    show m213
    mon "Хм. Как-то довольно серьезно."
    hide m213
    show m214
    mon "Похоже на действительно обдуманное решение."
    hide m214
    show m227
    me "Да, так и есть. Я… уже договорился с одним знакомым, остановлюсь у него сначала."
    me "Потом постараюсь устроиться на какую-нибудь подработку, пока не поступлю."
    hide m227
    show m205
    mon "А что тебе мешало остаться здесь, просто подать туда документы?"
    me "Это… сложно объяснить."
    hide m205
    show m224
    mon "Попробуй. Знаешь, я не такая уж и блондинка."
    me "Хах… я и не считал тебя тупой блондинкой."
    hide m224
    show m207
    mon "Приятно слышать."
    hide m207
    show m218
    mon "И все же, почему сейчас?"
    hide m218
    show m228
    mon "Почему обязательно воровать для этого аттестат? Бежать во время выпускного?"
    hide m228
    show m205
    me "Просто выпускной – идеальное время для того, чтобы уехать."
    me "И я не только про цены на билеты, а вообще, это идеально!"
    hide m205
    show m222
    me "Ни у кого не возникает вопросов, зачем я перебираю вещи, кому я звоню, куда я иду, зачем мне сумка с вещами…"
    hide m222
    show m216
    me "Универсальная отмазка – да это для выпускного!"
    me "А потом уже такого не будет."
    hide m216
    show m222
    mon "А зачем вообще такая скрытность? Зачем уезжать, никому ничего не сказав?"
    hide m222
    show m217
    mon "У тебя какие-то проблемы в семье?"
    me "Я… Ну…"
    menu:
        # ВЫБОР РЕПЛИКИ (причина побега)
        # РЕПЛИКА 1/4: маленький город
        "Маленький город":
            $ renpy.fix_rollback()
            $ reason1 = True
            me "Нет, дело не в семье, просто…"
            hide m217
            show m222
            me "Это же маленький город, ну что здесь может быть интересного?"
            me "Я выучил весь его наизусть, когда мне было еще десять. И ничего не поменялось."
            me "Что мои бабушка с дедушкой, что мои родители, что мои тетя с дядей…"
            hide m222
            show m229
            me "Все одно и то же: закончили школу, закончили вуз, устроились на какую-то работу и сидят ее ненавидят."
            me "На выходные надо устроить генеральную уборку, в отпуск обязательно куда-нибудь поехать отдыхать…"
            hide m229
            show m216
            me "А какой смысл? Что дальше?"
            me "Да, конечно, можно сделать все по-своему. Но все же друг друга знают!"
            hide m216
            show m229
            me "И все, почти весь город над тобой смеется, ведь весь город знает, как правильно!"
            hide m229
            show m213
            me "Я не хочу ничего этого, Моника."
            me "Я хочу в большой город, где множество возможностей."
            me "Где постоянно столько всего происходит… настоящего."
            me "Где никого не интересует, кто ты, откуда ты, из чьей ты семьи."
            hide m213
            show m229
            me "Где ты можешь развиваться, делать то, что тебе нравится."
            me "Где можно хоть чего-нибудь добиться нормального, понимаешь?"
            hide m229
            show m230
            mon "Хм. Ну допустим, да, понимаю."
            hide m230
            show m205
            mon "Хоть и не совсем согласна."
            hide m205
            show m216
            mon "В чем-то ты, конечно, прав, не спорю, но ведь…"
            hide m216

        # РЕПЛИКА 2/4: родители решают за меня (причина побега)
        "Родители решают за меня":
            $ renpy.fix_rollback()
            $ reason2 = True
            me "Д-да, можно сказать и так."
            me "Родители всегда все решали за меня. В какую секцию надо идти, в какой кружок записаться…"
            me "У них уже готов список, куда мне надо поступать."
            me "Я хотел уйти в колледж после девятого класса. Уже узнал, в какой."
            hide m217
            show m227
            me "Они даже и слушать не хотели. Что такое колледж, надо идти в вуз!"
            hide m227
            show m229
            me "И вот я здесь, великий выпускник одиннадцатого класса."
            hide m229
            show m223
            me "Мне надоело, Моника, мне так это надоело…"
            hide m223
            show m213
            me "Я хочу решать все сам, это же моя жизнь, почему так."
            me "Я не хочу поступать на какого-то инженера, чтобы потом коротать свою жизнь на каком-нибудь заводе."
            hide m213
            show m216
            me "Кому вообще это надо, только гнить на нелюбимой работе."
            hide m216
            show m214
            mon "А на кого же ты хотел бы?"
            me "На… на программиста."
            me "Я уже выбрал себе три вуза, куда я хочу подать документы. У меня же все отлично получается."
            hide m214
            show m213
            me "Но отец если узнает – прибьет на месте."
            me "Поэтому надо сделать все так, чтобы они не узнали, понимаешь?"
            hide m213
            show m230
            mon "Понимаю… Хотя это и странно."
            hide m230
            show m216
            mon "Просто…"
            hide m216

        # РЕПЛИКА 3/4: не хочу в твою империю (причина побега)
        "Не хочу в твою империю":
            $ reason3 = True
            $ renpy.fix_rollback()
            me "Просто… это может прозвучать грубо, конечно, но…"
            hide m217
            show m223
            me "Но разве в этом городе можно добиться хоть чего-то серьезного, не являясь твоим родственником?"
            hide m223
            show m233
            mon "Что?"
            me "Не обижайся,  но это ведь правда так, разве нет?"
            hide m233
            show m205
            me "Твоя семья, наверное, весь город уже захватила под сферу своего влияния."
            me "Во всех управляющих компаниях, во всех банках, конторах, судах, полицейских участках… да везде найдется кто-нибудь из Фишеров."
            me "Вы там воротите какими-то бешеными состояниями и все делаете так, как вам хочется."
            me "А чего могу добиться, например, я?"
            me "Мы с тобой даже толком не общались, и я уж точно тебе не родственник."
            me "Что я могу, стать лучшим кассиром какой-нибудь \"Четверочки\"? Или лучшим в мире дворником?"
            hide m205
            show m228
            mon "Перестань, это все вовсе не так."
            hide m228
            show m202
            me "Я не в обиду говорю, Моника, правда."
            me "Но если смотреть на вещи объективно, то все хорошие места давно за кем-то уже зарезервированы."
            me "Куда мне тягаться с вами, правда же?"
            hide m202
            show m228
            me "А в большом городе все совсем не так, там куда больше возможностей."
            me "Я смогу устроиться на ту работу, на какую я хочу, и чего-то действительно добиться."
            me "Причем сам, своими силами."
            hide m228
            show m202
            me "Прости, если я тебя задел, просто… ты сама же спросила, почему я захотел уехать."
            hide m202
            show m204
            mon "Ну тебе необязательно было для этого оскорблять всю мою семью, знаешь ли."
            me "Я же не говорю, что…"
            hide m204
            show m230
            mon "Да-да, я поняла, ты просто повторяешь за всеми остальными людьми."
            hide m230
            show m206
            mon "На самом деле все совсем не так, знаешь ли."
            hide m206
            show m234
            mon "На самом деле мои…"
            hide m234

        # РЕПЛИКА 4/4: просто решил, и все (причина побега)
        "Просто решил и все":
            $ reason2 = True
            $ renpy.fix_rollback()
            hide m217
            show m223
            me "Да неважно, просто решил, и все."
            hide m223
            show m219
            mon "Да брось, скажи мне."
            mon "Мне кажется, я уже и так знаю достаточно, договаривай."
            me "Ну правда…"
            hide m219
            show m227
            mon "Что-то в семье, да?"
            hide m227
            show m207
            mon "Ничего страшного, у нас в параллели у многих проблемы в семье."
            hide m207
            show m212
            mon "То есть, конечно, это страшно, это неправильно и все такое…"
            hide m212
            show m201
            mon "Просто в этом нет…"
            hide m201

            #завершение выбора реплики (причина побега)
    show m223
    show a417 at left with moveinleft
    stop music
    play music "audio/went_fishing_caught_a_girl.ogg"
    al "Какие люди! Да без охраны!"
    hide a417 at left
    show a405
    hide m223
    show m232
    mon "Алан!"
    hide a405
    show a400 at left
    hide m232
    show m235
    al "Привет, Моника, привет, [name]."
    hide a400
    show a410 at left
    al "Что это тут у вас, свидание, да?"
    hide m235
    show m208
    mon "Алан, пошел ты к черту, у нас важный разговор!"
    hide a410
    show a418 at left
    hide m208
    show m209
    al "Да-да, конечно, я вижу."
    hide a418
    show a419 at left
    hide m209
    show m222
    al "А куда вы идете?"
    hide m222
    show m221
    me "Алан, сейчас действительно не лучшее время."
    hide a419
    show a415 at left
    al "Да ладно, мы же уже совсем скоро станем бывшими одноклассниками!"
    hide a415
    show a400 at left
    hide m221
    show m208
    mon "Что тебе надо? {w}Хотя знаешь, что – мне плевать!"
    hide a400
    show a419 at left
    hide m208
    show m228
    mon "Иди, куда ты там шел, оставь нас в покое!"
    hide a419
    show a410 at left
    hide m228
    show m202
    al "Моника, ты что, встала не с той ноги сегодня?"
    hide a410
    show a411 at left
    hide m202
    show m204
    al "Или может-"
    hide a411
    show a419 at left
    me "Алан, правда, что ты хотел?"
    hide a419
    show a401 at left
    al "Да ничего я не хотел, увидел вас, подошел поздороваться!"
    hide a401
    show a400 at left
    me "Хорошо, мы с тобой тоже поздоровались, а теперь…"
    hide a400
    show a417 at left
    hide m204
    show m221
    al "А теперь мы можем прогуляться вместе!"
    hide a417
    show a419 at left
    al "Моника, что с лицом?"
    mon "Не могу решить, как именно мне тебя убить."
    hide a419
    show a415 at left
    al "Ой, скажешь тоже!"
    hide a415
    show a418 at left
    "Если так пойдет и дальше, Моника и правда взбесится."
    "Да и мало ли что Алан там придумал… его розыгрыши никогда не бывают безобидными."
    "Надо срочно что-то придумать."
    hide a418
    show a419 at left
    hide m221
    show m222
    me "Алан, слушай…"
    menu:
        # ВЫБОР ДЕЙСТВИЯ (алан отвали номер 1)
        # ДЕЙСТВИЕ 1/2: купить Алану что-нибудь
        "Купить Алану что-нибудь":
            $ renpy.fix_rollback()
            hide a419
            show a400 at left
            me "Может… может, давай я тебе куплю что-нибудь?"
            hide a400
            show a422 at left
            hide m222
            show m216
            me "Какой-нибудь сахарной ваты, может?"
            hide a422
            show a421 at left
            hide m216
            show m218
            al "О, я люблю сахарную вату!"
            hide m218
            show m224
            me "Вот видишь, как отлично."
            hide a421
            show a400 at left
            me "Давай я куплю тебе сахарной ваты, а ты потом пойдешь по своим делам и дашь нам договорить."
            hide a400
            show a405 at left
            hide m224
            show m219
            al "Идет!"
            me "Отлично, идем."
            hide a405 with moveoutleft
            hide a405
            show a400 at left with moveinleft
            hide m219
            show m214
            "Я поймал на себе благодарный взгляд Моники. {w}Впрочем, это было ненадолго."
            hide m214 with dissolve
            "Пока мы искали ларек с сахарной ватой, Алан вел себя настолько нахально, что мне самому захотелось его придушить."
            show a421 at left with dissolve
            show m202 with dissolve
            al "…Кстати, Моника, отличная кофточка!"
            hide m202
            show m237
            mon "Спасибо."
            hide a421
            show a424 at left
            hide m237
            show m205
            al "А ты же была в ней на вечеринке уже! У вас что, дела совсем плохи?"
            hide a424
            show a423 at left
            hide m205
            show m222
            al "Это из-за той громкой истории на заводе?"
            me "Каком заводе?"
            hide a423
            show a419 at left
            hide m222
            show m228
            mon "Понятия не имею. Алан, не знаю, о чем ты, это моя любимая кофта."
            hide a419
            show a410 at left
            al "Да-да, конечно."
            hide m228
            show m237
            mon "Забирай свою вату и проваливай."
            hide a410
            show a418 at left
            al "Значит, любимая кофта, да…"
            hide a418
            show a411 at left
            hide m237
            show m235
            al "Будет очень неловко, если на нее случайно что-нибудь…"
            hide m235
            show m238
            mon "Знаешь, что, отойди от меня!"
            hide a411
            show a417 at left
            hide m238
            show m212
            me "Алан, хватит. Ты же обещал."
            hide a417
            show a422 at left
            hide m212
            show m205
            al "Да перестаньте, весело же!"
            hide a422
            show a425 at left
            al "Выпускной же скоро! Когда еще сможем так повеселиться!"

    # ДЕЙСТВИЕ 2/2: возвать к его совести (алан отвали номер 1)
        "Воззвать к его совести":
            $ renpy.fix_rollback()
            hide a419
            show a400 at left
            hide m222
            show m205
            me "Правда, хватит."
            hide a400
            show a404 at left
            me "Ты же хороший парень, ну подошел, ну поздоровался."
            me "Давай теперь каждый разойдется по своим делам, хорошо?"
            hide a404
            show a403 at left
            hide m205
            show m222
            al "Так у вас что тут, и правда свидание, да?"
            hide a403
            show a411 at left
            hide m222
            show m235
            al "Боишься, что я ее отниму?"
            hide m235
            show m204
            mon "Ой, совсем уж чушь не неси, да."
            hide a411
            show a420 at left
            hide m204
            show m202
            al "Да ты посмотри на нее, она в восторге от моего общества!"
            hide a420
            show a424 at left
            al "Мон, а ведь мы скоро выпустимся! И мы больше не будем одноклассниками!"
            hide a424
            show a423 at left
            al "Я буду так скучать! А ты будешь?"
            hide a423
            show a428 at left
            hide m202
            show m228
            mon "Ага, особенно по твоим розыгрышам."
            hide m228
            show m237
            mon "А знаешь, кто еще будет по ним скучать сильнее всех?"
            hide a428
            show a411 at left
            mon "Моя домработница."
            hide a411
            show a410 at left
            al "Но ты будешь скучать больше, я же знаю."
            hide a410
            show a419 at left
            hide m237
            show m205
            me "Алан, ну серьезно."
            hide a419
            show a420 at left
            al "Не бойся, чувак, я же только придуриваюсь."
            hide a420
            show a422 at left
            hide m205
            show m222
            al "Не нужна она мне, кому она вообще нужна?"
            hide a422
            show a425 at left
            hide m222
            show m222
            mon "Раз я тебе так не нужна, какого хрена ты вообще подошел к нам?"
            hide m222
            show m232
            mon "Иди уже отсюда!"
            hide a425
            show a403 at left
            hide m232
            show m235
            al "Да чего ты злая-то такая? Я же дурачусь!"

            #завершение выбора реплики (алан отвали номер 1)

    hide a403
    hide a425
    show a419 at left
    hide m235
    hide m205
    show m239
    al "Пойдемте лучше где-нибудь покатаемся?"
    hide a419
    show a411 at left
    hide m239
    show m228
    mon "Никуда я с тобой не пойду, идиота ты кусок."
    hide a411
    show a415 at left
    hide m228
    show m202
    al "Брось, я знаю, что ты любишь! Ты любишь цепочную карусель!"
    hide a415
    show a400 at left
    hide m202
    show m205
    me "Давай лучше чуть попозже, у нас правда тут важный разговор…"
    hide a400
    show a425 at left
    hide m205
    show m228
    al "Да я понимаю, что ты, все мы были на твоем месте!"
    me "Спасибо, тогда ты…"
    hide a425
    show a406 at left
    hide m228
    show m240
    al "Нет ничего хуже, чем когда девчонкам вздумалось поговорить!"
    hide a406
    show a429 at left
    hide m240
    show m221
    al "Потом спасибо скажешь! Я ж понимаю!"
    hide a429
    show a430 at left
    me "…Нет, это немного не…"
    hide a430
    show a422 at left
    al "И чего им спокойно не живется? Вечно какие-то разговоры, что-то надо решить, что-то надо делать…"
    hide a422
    show a421 at left
    hide m221
    show m232
    mon "Это не какой-то там пустой разговор, Алан!"
    hide m232
    show m225
    mon "Я же не ты, чтобы говорить про ерунду!"
    hide a421
    show a428 at left
    hide m225
    show m241
    al "Ой, слабовато, Моника, слабовато."
    hide a428
    show a431 at left
    hide m241
    show m221
    mon "Ах ты..!"
    "Кажется, еще немного – и Моника его действительно придушит на месте."
    "Или наша с ней прогулка будет окончательно испорчена…"
    "Надо срочно что-то делать!"
    menu:
        "Решить мирным путем":
            $ renpy.fix_rollback()
            hide a431
            hide m221
            show a419 at left
            show m240
            me "Алан, слушай, можно тебя на минуту?"
            hide a419
            show a425 at left
            al "Да, конечно, что такое?"
            hide a425
            show a411 at left
            hide m240
            show m237
            mon "Ой, а теперь мальчики у нас пошли разговаривать, да?"
            hide a411
            show a410 at left
            hide m237
            show m202
            me "Моника, тише, я попробую все уладить…"
            hide m202
            show m228
            "Моника только фыркнула, скрестив руки на груди."
            hide m228 with dissolve
            hide a410 with dissolve
            "Я отошел вместе с Аланом на пару шагов."
            show a419 with dissolve
            me "Слушай, это и правда очень важный разговор."
            hide a419
            show a418
            me "Нам нужно кое-что… решить до выпускного, это правда важно."
            me "…Постой, что ты делаешь?"
            hide a418
            show a405
            al "Да я вспомнил, что я недавно покупал жвачку-электрошокер, не могу найти…"
            me "Что?!"
            hide a405
            show a424
            al "Ну знаешь, такая якобы упаковка дорогой жвачки, и одна пастилка слегка вытащена."
            hide a424
            show a421
            al "За нее потянешь и получишь разряд!"
            hide a421
            show a404
            al "Где же она, сейчас же самое время!.."
            hide a404
            show a425
            me "Нет, Алан, сейчас точно не самое лучшее время!"
            hide a425
            show a426
            al "Да ладно тебе, что такого?"
            hide a426
            show a411
            al "Во, нашел! Пошли!"
            hide a411
            show a419
            me "Нет, подожди… Алан!"
            show m202 at right with dissolve
            hide a419
            show a400
            al "А вот и мы! Кстати, Моника, хочешь жвачку?"
            hide a400
            show a419
            me "Не бери."
            hide m228
            show m204 at right
            mon "Из твоих рук? Да ни за что."
            hide a419
            show a422
            al "Ну как хочешь."

        # ДЕЙСТВИЕ 2/2: решить вопрос по-мужски (алан отвали номер 2)
        "Решить вопрос по-мужски":
            $ renpy.fix_rollback()
            hide a422
            show a421 at left
            hide m204
            show m218
            me "Так, хватит. Давай разберемся по-мужски."
            hide a421
            show a424 at left
            hide m218
            show m217
            al "По-мужски?"
            hide a424
            show a432 at left
            "Я поднял кулак и красноречиво показал ему."
            me "Да, по-мужски."
            hide a432
            show a425 at left
            hide m217
            show m204
            me "Я выиграю – и ты оставляешь нас в покое."
            hide a425
            show a421 at left
            me "Только честно!"
            hide a421
            show a400 at left
            al "О, я понял, хорошо, давай. Два из трех?"
            me "Идет. На счет три."
            hide a400
            show a414 at left
            hide m204
            show m237
            al "Ага, давай."
            hide m237 with dissolve
            hide a414 with dissolve
            call rps

    if monrock == False:
        hide a419
        show a424
        hide m242
        show m205 at right
        al "Ой, смотрите-смотрите, американские горки работают!"
        hide a424
        show a421
        al "Пойдемте прокатимся!"
        hide m205
        show m204 at right
        mon "Еще чего."
        hide a421
        show a422
        al "Да, конечно, [name], идем!"
        hide a422
        show a430
        hide m204
        show m240 at right
        al "Увидишь, как громко может визжать Моника."
        hide a430
        show a431
        hide m240
        show m238 at right
        mon "Не буду я кататься!"
        hide a431
        show a422
        hide m238
        show m239 at right
        al "Да пойдемте, это же круто! Они в этом году еще не работали!"
        hide m239
        show m240 at right
        me "Оно и видно…"
        hide a422
        show a419
        me "Алан, ты что, не видишь, какая там очередь?"
        hide a419
        show a415
        al "Ну и что, ради американских горок можно и потерпеть!"
        hide a415
        show a416
        hide m240
        show m228 at right
        al "Да пойдемте! Давайте прокатимся хоть разок!"
        hide a416
        show a418
        hide m228
        show m229 at right
        al "И я, так уж и быть, от вас отстану."
        hide a418
        show a419
        hide m229
        show m237 at right
        mon "Не верю ни единому слову."
        hide a419
        show a423
        al "Да честно, ну пойдемте!"
        hide a423 with dissolve
        hide m237 at right with dissolve
        scene park3 with dissolve
        "Он так уговаривал, что непонятно каким образом, но через десять минут мы уже купили билеты"
        "и встали в хвост этой гигантской очереди."
        "Моника, до этого без конца возмущавшаяся, почему-то подозрительно притихла."
        "Я хотел уже было тихо спросить у нее, все ли хорошо, но она меня опередила."
        show a400
        show m204 at right
        with dissolve
        mon "Очередь и правда огромная, Алан, ну ты и…"
        hide a400
        show a420
        al "Зато прокатимся – не пожалеете!"
        hide a420
        show a421
        hide m204
        show m212 at right
        mon "Представляю. Это явно надолго… слушайте, я вас ненадолго покину."
        hide a421
        show a424
        me "Нет, постой, зачем? Куда?"
        hide a424
        show a402
        hide m212
        show m222 at right
        al "Да, куда это ты собралась? Мы билет на тебя купили!"
        hide a402
        show a408
        hide m222
        show m228 at right
        mon "Да сейчас вернусь! Мне…"
        hide a408
        show a424
        hide m228
        show m212 at right
        mon "Мне надо в уборную."
        hide a424
        show a425
        hide m212
        show m231 at right
        mon "[name], сходишь со мной?"
        hide a425
        show a410
        hide m231
        show m204 at right
        al "А ты сама не умеешь, что ли?"
        hide a410
        show a411
        mon "Вот из-за того, что ты такой самый умный, тебя я и не зову."
        hide m204
        show m205 at right
        me "А ты… гм, уверена?"
        hide m205
        show m206 at right
        mon "Просто проводи меня, а то…"
        hide a411
        show a412
        hide m206
        show m213 at right
        mon "Там собак часто выгуливают. Мне страшно одной."
        hide m213
        show m214 at right
        me "Оу. Тогда конечно, пойдем."
        hide a412
        show a420
        hide m214
        show m218 at right
        al "Ладно, идите, я в очереди постою!"
        hide a420
        show a422
        hide m218
        show m219 at right
        al "Давайте побыстрее!"
        "Я только кивнул ему, а Моника уже потащила меня за руку по дорожке в сторону туалетов."
        hide m219
        hide a422
        with dissolve
        scene park2 with dissolve
        "Когда Алан вместе с очередью скрылись за поворотом, мы замедлили шаг."
        "И Моника отпустила мою руку."
        show m207 with dissolve
        mon "Боже, неужели получилось."
        hide m207
        show m227
        me "Что, прости?"
        hide m227
        show m226
        mon "Ну я не знала, как еще от него отвязаться."
        hide m226
        show m228
        mon "Как прилипнет, не отстанет."
        me "То есть тебе что, ни в какую уборную не надо было?"
        hide m228
        show m237
        mon "Нет, конечно. И собак там тоже никаких нет."
        hide m237
        show m234
        mon "Просто уже сил не было никаких его терпеть."
        hide m234
        show m228
        mon "Да и кататься с Аланом на американских горках… {w}уж извините."
        hide m228
        show m235
        mon "У него же вообще мозгов нет, мало ли что он там с ними сделает!"
        hide m235
        show m237
        me "Блин, Моника, но все равно это как-то…"
        me "Нельзя так с людьми. Он же нас там ждет."
        me "А когда подойдет его очередь? Он же будет ждать, сам не пойдет."
        hide m237
        show m206
        mon "И поделом ему, будет знать."
        menu:
            "Я так не могу":
                $ renpy.fix_rollback()
                hide m206
                show m213
                me "Прости, я так не могу. Мне совесть не позволит."
                me "Давай прокатимся на этих несчастных горках, а потом договорим?"
                hide m213
                show m212
                mon "Уф… ладно, так уж и быть."
                hide m212
                show m216
                mon "Если честно, я вообще уже не уверена, что мы поговорим."
                hide m216
                show m217
                me "Почему?"
                hide m217
                show m226
                mon "Да знаешь… с этим балбесом все настроение пропало, вот честно."
                hide m226
                show m227
                mon "Спасибо тебе, что ты мне все рассказал, конечно."
                hide m227
                show m229
                mon "И да, я обещаю, что я никому ничего не скажу, раз это так важно."
                hide m229
                show m204
                mon "А теперь пошли к твоему драгоценному Алану."
                me "Прости."
                hide m204
                show m230
                mon "Да что уж тут скажешь."
                hide m230
                show m244
                mon "Это даже мило, что ты о нем думаешь."
                me "Правда?.."
                hide m244
                show m211
                mon "Нет, конечно, он идиот."
                hide m211
                show m238
                mon "Я и так зла, как незнамо кто, а теперь надо еще к нему обратно тащиться!"
                hide m238
                show m239
                me "Прости еще раз."
                hide m239
                show m204
                mon "Да перестань, сколько можно быть милым, пошли."
                scene park_3 with dissolve
                "Не переставая бурчать, Моника пошла следом за мной обратно к Алану."
                "Однако когда мы подошли к очереди, то оказалось, что Алан там уже не один, а с друзьями."
                "Монику, кажется, на секунду перекосило со злости."
                show a425
                show m222 at right
                with dissolve
                al "О, вы вернулись!"
                hide a425
                show a418
                hide m222
                show m221 at right
                al "Идемте, наша очередь уже скоро!"
                hide a418
                show a431
                hide m221
                show m245 at right
                al "Смотрите, кого я встретил!"
                me "Да уж мы видим."
                hide a431
                show a424
                al "Вы не против, если я с пацанами поеду, да?"
                hide a424
                show a425
                al "Вот ваши билеты, идите сюда, первыми поедете."
                hide a425
                show a420
                al "Ух будет весело!"
                hide a420 with moveoutleft
                hide m245
                show m240 at right
                show m240 at center with move
                me "Да ладно…"
                hide m240
                show m238
                mon "Ой, он же нас ждать будет…"
                hide m238
                show m241
                mon "Ой, мне совесть не позволит…"
                hide m241
                show m242
                mon "Ой, Моника, давай вернемся…"
                hide m242
                show m240
                me "Ну прости, я же не знал, что он тут уже не один."
                me "Может, и правда будет весело."
                hide m240
                show m245
                mon "Да, конечно."
                hide m245 with dissolve
                scene rollercoaster with dissolve
                "Весело… {w}не было."
                "Несмотря на сопротивление Моники, нас с ней каким-то образом усадили за второе место."
                "И, если честно, я очень радовался, что первое уже было занято."
                "Моника визжала так, что чуть не сорвала голос и не оставила меня глухим."
                "Алан с одним из его друзей, сидящие позади нас, тоже кричали не переставая, правда, от восторга."
                "На мертвой петле мне показалось, что мы сейчас улетим ко всем чертям, и я рефлекторно заорал вместе с ними."
                scene park3_a with dissolve
                "Когда мы выходили с горок, Алан уже не обращал на нас никакого внимания, уходя со своими друзьями."
                "Мы остались вдвоем – я, пытающийся выровнять дыхание,"
                "и бледная Моника, прижимающая обе ладони к груди."
                show m246 with dissolve
                mon "Чтобы я… еще… раз…"
                me "Прости. Это из-за меня все."
                hide m246
                show m243
                mon "На самом деле… может, это и весело."
                hide m243
                show m237
                mon "Но на мертвой петле Алан дернул меня за волосы."
                me "Оу… Ты из-за этого так закричала?"
                mon "Да, из-за этого."
                hide m237
                show m228
                mon "Вообще не будь у меня за спиной Алана, это могло быть весело, но…"
                hide m228
                show m229
                me "Да, я понимаю."
                me "Ну, зато теперь он ушел. Может, сходим погуляем?"
                hide m229
                show m231
                me "Или прокатимся на чем-нибудь менее экстремальном."
                hide m231
                show m212
                mon "Ага, на детской карусельке, что ли?"
                hide m212
                show m218
                me "Нет, мы могли бы… прокатиться на цепочной карусели?"
                hide m218
                show m214
                mon "Оу."
                hide m214
                show m244
                mon "Я бы согласилась, правда, но у меня до сих пор сердце колотится, как бешеное."
                hide m244
                show m229
                mon "Да и поздно уже. Наверное, мне лучше пойти домой."
                hide m229
                show m227
                me "Давай я тебя провожу? А то вдруг собаки какие-нибудь…"
                hide m227
                show m224
                mon "Убедительно."
                hide m224
                show m219
                mon "Идем."
                scene city_road with dissolve
                stop music
                play music "audio/a_promise_from_distant_days.ogg"
                "Идти было недалеко, всего пару кварталов. {w}Однако они казались мне настоящей пыткой."
                "Я чувствовал себя ужасно неловко из-за всего произошедшего, мне было почти стыдно перед Моникой."
                "Чертов Алан, надо было все так испортить…"
                "Словно услышав мои мысли, Моника взяла меня за руку. {w}Помедлив, я сжал ее нежную ладонь в своей."
                show m200 with dissolve
                mon "Что ж, а вот и мой дом."
                hide m200
                show m214
                mon "Спасибо, что проводил."
                me "Да не за что… Слушай, прости за сегодня."
                hide m214
                show m223
                me "Правда, мне ужасно жаль, что так получилось."
                hide m223
                show m224
                mon "Не бери в голову,[name]."
                mon "От Алана очень трудно избавиться, когда он решил напакостить."
                hide m224
                show m225
                mon "Мне ли не знать."
                hide m225
                show m235
                mon "Тем более что ничего страшного он и не сделал."
                hide m235
                show m218
                me "Ну может, он не подготовился."
                hide m218
                show m207
                mon "Да, наверное."
                hide m207
                show m214
                mon "Спасибо тебе еще раз за доверие."
                mon "И добрых снов."
                hide m214 with dissolve
                "С этими словами Моника вдруг приподнялась на носочки и коротко поцеловала меня в щеку."
                "У меня перехватило дыхание."
                "Отстранившись, она улыбнулась мне, повернулась и направилась к дому."
                "А я остался стоять, как дурак, глядя ей вслед."
                #локация: дома (вечер)
                scene room_on with dissolve
                "Сам не помню, как я оказался дома. Да и как ужинал, принимал душ и расстилал постель, тоже."
                "Из головы не выходил сегодняшний день."
                "Кто бы мог подумать, что с Моникой окажется так… спокойно."
                "Она действительно классная. И интересная. И красивая, вне сомнений…"
                "Ну конечно, все-таки первая девушка школы."
                "Я подавил вздох. {w}Впервые в жизни я пожалел, что вот-вот уеду."
                "Может, все не так плохо… Может, у нас могло бы что-нибудь получиться."
                "Но теперь я этого уже никогда не узнаю…"
            "Хорошо, идем":
                $ renpy.fix_rollback()
                $ monwheel = True
                me "Ну… ну ладно."
                hide m206
                show m204
                mon "Ничего страшного, зная Алана, он там с кем-нибудь уже задружился."
                me "Да уж, у него явно нездоровая тяга к общению."
                hide m204
                show m219
                mon "Ты хотел сказать, что если он прицепится, то не отвяжешься?"
                hide m219
                show m207
                me "Ну… да, вроде того."
    else:
        $ monwheel = True
        if monwheel == True:
            hide m242
            show m218
            me "Знаешь, что… давай на всякий случай пойдем в другую сторону?"
            hide m218
            show m212
            mon "Согласна."
            hide m212 with dissolve
            "Я кивнул и повел ее в другую сторону парка, ненавязчиво приобняв за талию."
            "Кажется, она не возражала."
            "Боже, неужели это и правда свидание?.."
            scene park with dissolve
            stop music
            play music "audio/Cocoon_illuminated_by_moonlight.mp3"
            show m219 with dissolve
            me "Так… на чем мы остановились?"
            hide m219
            show m214
            mon "Да. Точно."
            hide m214
            show m227
            mon "…"
            hide m227
            show m228
            mon "…"
            hide m228
            show m229
            mon "Блин. Это, наверное, глупо…"
            hide m229
            show m212
            mon "Но мне теперь кажется, что этот урод может вернуться в любой момент."
            me "Оу…"
            hide m212
            show m231
            mon "Давай, может, куда-нибудь еще пойдем?"
            hide m231
            show m217
            me "Например?"
            hide m217
            show m226
            mon "Даже не знаю…"
            "Я вздохнул и возвел глаза к небу. {w}И вдруг придумал."
            hide m226
            show m231
            me "Слушай, может быть, на колесо обозрения?"
            hide m231
            show m218
            mon "Оу."
            hide m218
            show m214
            mon "Мне нравится."
            me "Как раз на нем и продолжим?"
            mon "Да. Очень…"
            hide m214
            show m207
            mon "Очень романтично."
            "Романтично?.. Романтично?!"
            hide m207 with dissolve
            scene park3_a with dissolve
            #локация: можно еще сменить на какую-нибудь, но я хз, мб и не надо х)
            "Идя за Моникой в сторону кассы, я, наверное, раз тридцать повторил про себя это слово с разными интонациями."
            "В результате она не дала мне за себя заплатить, сказав, что нам и так ехать потом."
            "Мда, очень романтично."
            scene wheel_a with dissolve
            stop music
            play music "audio/a_promise_from_distant_days.ogg"
            #локация: колесо оборзения
            "Я не катался на колесе обозрения, наверное, с начальной школы."
            "Я уже и не помнил, как это красиво – когда весь город расстилается перед тобой, как на ладони."
            "Моника взяла нам два круга. Видимо, действительно решила поговорить."
            "Однако первую минуту мы просто молча стояли и смотрели на город."
            "На этот раз я был тем, кто прервал тишину."
            show m200 with dissolve
            me "Так красиво."
            hide m200
            show m214
            mon "Да. Очень."
            hide m214
            show m244
            mon "Я так давно не каталась на колесе обозрения."
            hide m244
            show m247
            me "Я тоже! Последний раз лет в восемь, наверное, катался."
            hide m247
            show m207
            mon "Да, я где-то так же."
            hide m207
            show m201
            mon "Хотя странно, это же так здорово. Ребенком не понимаешь всей этой красоты."
            hide m201
            show m219
            mon "Даже как-то жаль, что я так давно не каталась."
            me "Насколько я знаю, твои родители могут купить тебе персональное колесо обозрения."
            hide m219
            show m207
            mon "Это будет уже не то!"
            hide m207
            show m214
            mon "Ладно, на чем мы..?"
            me "Кажется, ты была со мной не согласна."
            hide m214
            show m200
            mon "Да… Кхм."
            if reason1 == True:
                mon "Я спросила тебя, почему ты уезжаешь, и ты сказал, что в маленьких городах нет ничего интересного."
                me "Ну…"
                hide m200
                show m219
                mon "Давай я скажу, ладно?"
                hide m219
                show m227
                mon "Я хотела сказать, что да, я тебя понимаю."
                me "Правда?"
                hide m227
                show m230
                mon "Да, город действительно маленький, казалось бы, что с него взять."
                hide m230
                show m201
                mon "Но я хочу сказать, что… в этом есть своя прелесть."
                hide m201
                show m252
                mon "Да, ты можешь уехать в большой город. Да, там будет много возможностей."
                hide m252
                show m218
                mon "Но что они тебе дадут?"
                hide m218
                show m229
                mon "Что они изменят?"
                hide m229
                show m236
                mon "Да, тебе будет чем гордиться."
                mon "Ты не просто какой-то там жалкий продавец, а продавцом с большого города!"
                hide m236
                show m234
                mon "Но чем это будет отличаться от продавца в маленьком городе?"
                hide m234
                show m231
                me "Это не то…"
                hide m231
                show m230
                mon "Ладно, допустим, не продавец!"
                hide m230
                show m201
                mon "Ты ведь сдавал информатику? Допустим, ты пойдешь работать программистом."
                hide m201
                show m236
                mon "Да, ты найдешь работу в более крупной фирме, ты будешь там впахивать и получать свои кровно заработанные."
                hide m236
                show m222
                mon "Но что это тебе даст?"
                hide m222
                show m224
                mon "Кроме того, что ты осчастливишь владельца этой фирмы."
                hide m224
                show m227
                mon "Ничего не даст."
                me "Не соглашусь, оно даст мне повыше зарплату."
                hide m227
                show m207
                mon "Ну… да, тут не поспоришь."
                hide m207
                show m214
                mon "Но я о другом."
                hide m214
                show m249
                mon "В маленьком городе у тебя больше возможностей сделать что-то полезное."
                hide m249
                show m250
                mon "Не просто сидеть и делать владельца фирмы богаче, а реально что-то делать, понимаешь?"
                hide m250
                show m229
                mon "Мои родители пашут день и ночь, чтобы сделать жителей этого города счастливее."
                hide m229
                show m237
                mon "Да, они могли бы уехать куда-нибудь и открыть любую коммерческую фирму."
                hide m237
                show m244
                mon "Но они остаются здесь, потому что здесь они могут сделать что-то хорошее."
                hide m244
                show m247
                mon "Они могут сделать жизнь здесь лучше."
                hide m247
            elif reason2 == True:
                mon "Я спросила тебя, почему ты уезжаешь, и ты сказал, что из-за родителей."
                me "Ну…"
                hide m200
                show m219
                mon "Давай я скажу, ладно?"
                hide m219
                show m227
                mon "Я хотела сказать, что да, я тебя понимаю."
                me "Правда?"
                hide m227
                show m214
                mon "Да, конечно."
                hide m214
                show m216
                mon "Мои родители тоже давят на меня."
                hide m216
                show m226
                mon "Иногда даже слишком…"
                hide m226
                show m207
                mon "Да, я знаю, все думают, что мне так повезло, моя семья же так богата!"
                hide m207
                show m212
                mon "Но это не значит, что у меня нет никаких проблем."
                mon "Бывает, что отец на меня ругается, что-то запрещает, злится на меня."
                mon "Я тоже на него злюсь."
                hide m212
                show m216
                mon "Мама часто игнорирует меня, если ей что-то не понравилось."
                hide m216
                show m230
                mon "Я ее тоже игнорирую, отец начинает злиться, все выливается в скандал…"
                hide m230
                show m237
                mon "И виноватой чаще всего оказываюсь я."
                hide m237
                show m236
                mon "Но знаешь…"
                hide m236
                show m250
                mon "Потом, когда я перестаю на них злиться, я вспоминаю, как сильно они меня любят."
                hide m250
                show m249
                mon "Пусть они ругали меня за плохие оценки…"
                hide m249
                show m253
                me "Тебя ругали за плохие оценки?"
                hide m253
                show m207
                mon "Конечно, и еще как!"
                hide m207
                show m214
                mon "У папы вообще бзик какой-то по этому поводу."
                hide m214
                show m201
                mon "Мама столько ему говорила, что я не обязана учиться идеально, но ему все равно."
                hide m201
                show m225
                mon "Его дочь должна быть лучшей везде."
                hide m225
                show m229
                mon "Но знаешь, даже когда я где-то ошибалась…"
                hide m229
                show m227
                mon "Они всегда поддерживали меня."
                hide m227
                show m248
                mon "Или когда я чего-то боялась, спрашивала совета, они могли прочитать мне целую лекцию…"
                hide m248
                show m207
                mon "Но это была полезная лекция. То есть они правда хотели, чтобы я все поняла."
                hide m207
                show m222
                mon "Конечно, у тебя могут быть и другие родители, я не знаю, но…"
                hide m222
                show m214
                mon "Я уверена, они тоже тебя любят."
                hide m214
                show m253
                mon "Как мои родители любят меня."
                hide m253
                show m251
                mon "Да, это не всегда заметно, я знаю."
                hide m251
                show m248
                mon "Мои вот родители работают сутками, чтобы сделать жителей города счастливее."
                hide m248
                show m243
                mon "Сделать жизнь в городе лучше."
                hide m243
                show m247
                mon "И я так безумно горжусь ими и всем, что они делают!"
                hide m247
                show m200
                mon "Я просто обязана сделать все возможное, чтобы продолжить их дело!"
                hide m200
            elif reason3 == True:
                mon "Я спросила тебя, почему ты уезжаешь, и ты сказал, что из-за моей семьи."
                me "Ну я не…"
                hide m200
                show m219
                mon "Давай я скажу, ладно?"
                hide m219
                show m227
                mon "Я хотела сказать, что да, я тебя понимаю."
                me "Правда?"
                hide m227
                show m214
                mon "Да, конечно."
                hide m214
                show m224
                mon "Думаешь, я не в курсе, какими нас считают?"
                hide m224
                show m224
                mon "Фу-фу, Фишеры, везде суют свой нос, все куплено, ла-ла-ла!"
                hide m224
                show m207
                mon "Да даже ты наверняка считал меня зазнайкой!"
                hide m207
                show m214
                me "Да нет вроде…"
                hide m214
                show m210
                mon "Шучу."
                hide m210
                show m227
                mon "На самом деле все совсем не так."
                hide m227
                show m236
                mon "Да, моя семья действительно очень влиятельна, по факту, мы контролируем весь город."
                hide m236
                show m234
                mon "Но это не значит, что мы суем всех своих родственников на управляющие места."
                hide m234
                show m237
                mon "Если кто-то безответственный идиот, то он безответственный идиот!"
                hide m237
                show m248
                mon "У меня есть кузен, который считал, что ему все должны."
                hide m248
                show m201
                mon "Он старше меня на года три или четыре…"
                hide m201
                show m210
                mon "В общем, он в институте вообще ничего не делал и считал, что это норма."
                hide m210
                show m219
                mon "Что его родители все сами сделают, запугают преподов, а его пристроят на сладкое местечко."
                hide m219
                show m225
                mon "Как раз вон место главврача в одной из больниц освободилось, а почему бы сразу не туда?"
                me "Да, я помню, столько разговоров было."
                hide m225
                show m253
                mon "Ну ты помнишь, чем все закончилось?"
                me "Да, кажется…"
                hide m253
                show m218
                me "Вроде бы говорили, что вы испугались поднявшейся шумихи и отдали место кому-то нормальному."
                hide m218
                show m219
                mon "Испугались шумихи, да-да."
                hide m219
                show m207
                mon "Почему бы моим родителям не испугаться шумихи, это же так страшно."
                hide m207
                show m248
                mon "Мой отец вообще озверел, когда узнал про кузена."
                hide m248
                show m225
                mon "Он вылетел из института, как пробка."
                me "Что, серьезно?"
                hide m225
                show m207
                mon "Ну да, он же ничего там не делал."
                hide m207
                show m201
                mon "Сейчас его мой дядя пытается перевоспитать, но как-то не очень получается."
                hide m201
                show m251
                mon "Папа говорит, что надо просто денег лишить на пару лет, и сразу мозги появятся."
                hide m251
                show m248
                mon "Но дядя слишком жалостливый."
                hide m248
                show m253
                mon "Я это к тому, что мои родители не дураки."
                hide m253
                show m234
                mon "Они действительно очень, очень много и усердно работают."
                hide m234
                show m229
                mon "Я иногда могу не видеть их целыми сутками."
                hide m229
                show m231
                mon "Но они это все делают вовсе не для того, чтобы вертеть всеми, как им хочется."
                hide m231
                show m244
                mon "Они это делают, чтобы сделать жителей города счастливее."
                hide m244
                show m247
                mon "Чтобы жизнь здесь стала лучше, понимаешь?"
                hide m247

    show m222
    mon "Посмотри, ведь все стало так по-другому!"
    hide m222
    show m249
    mon "Видишь вон там торговый центр? Раньше там были гаражи, много гаражей."
    hide m249
    show m250
    mon "Несколько рядов сплошных гаражей."
    hide m250
    show m253
    mon "Там постоянно тусили всякие сомнительные личности, постоянно кого-то грабили или еще хуже…"
    hide m253
    show m207
    mon "Отец до сих пор вспоминает, сколько было возни со сносом гаражей, с документами, со всем прочим…"
    hide m207
    show m252
    mon "Но посмотри сейчас."
    hide m252
    show m250
    mon "Сколько-то лет работы – и вместо притона уже стоит красивый торговый центр."
    hide m250
    show m253
    mon "Мало того, что функциональный, так там ведь появились новые рабочие места!"
    hide m253
    show m228
    mon "Или вон там видишь? Ой, плохо видно, сейчас повыше поднимемся…"
    hide m228
    show m227
    mon "Где кинотеатр \"Витязь\", помнишь?"
    me "А, да, помню."
    hide m227
    show m224
    mon "Он ведь совсем недавний, ему, наверное, даже шести лет нет."
    hide m224
    show m214
    mon "Его строили, еще когда я в младшей школе училась."
    hide m214
    show m248
    mon "Там раньше был малолюдный пустырь, говорили, жуткое место."
    hide m248
    show m236
    mon "Якобы хотели сделать сквер, в результате ничего не сделали, пустырь остался."
    hide m236
    show m201
    mon "Отец долго ругался, что там что-то с документами еще было не в порядке."
    hide m201
    show m253
    mon "И тоже – взяли, сделали, построили."
    mon "У людей появился красивый кинотеатр, а также – опять же! – новые рабочие места."
    hide m253
    show m243
    mon "Да даже взять прямо этот парк!"
    hide m243
    show m251
    mon "Еще до моего рождения здесь была огромная свалка."
    hide m251
    show m248
    mon "Мама шутит, что до сих пор чувствует ее запах, они тогда часто сюда приезжали, ее все закрывать не хотели."
    hide m248
    show m244
    mon "Но в итоге отец добился своего, свалку закрыли, участок выровняли, вычистили."
    hide m244
    show m207
    mon "И вот, пожалуйста."
    hide m207
    show m219
    mon "Мы сидим в кабинке в колесе обозрения, и я…"
    hide m219
    show m227
    mon "Рассказываю тебе о том, что это действительно важно."
    hide m227
    show m229
    mon "Да, может, большой город в чем-то лучше, но…"
    hide m229
    show m230
    mon "Но зато здесь действительно можно повлиять на что-то."
    hide m230
    show m201
    mon "Все в наших руках, понимаешь?"
    hide m201
    show m236
    mon "Мы не будем здесь каплями в океане, брошенные и никому не нужные."
    hide m236
    show m250
    mon "Мы можем сделать жизнь наших близких лучше…"
    hide m250
    show m214
    mon "Понимаешь?"
    hide m214
    show m227
    me "Я… Ну, ты-то, конечно, можешь."
    hide m227
    show m217
    me "У тебя и связи, и все на свете."
    hide m217
    show m229
    mon "Ну… да, конечно. {w}Просто…"
    hide m229
    show m230
    mon "Не подумай, я тебя не отговариваю, конечно, это тебе решать, не мне."
    hide m230
    show m233
    mon "Но просто… просто подумай об этом, хорошо?"
    hide m233
    show m231
    mon "Подумай о том, что даже в маленьком городе все может быть совсем иначе…"
    "Ее рука легла мне на плечо, и по мне как будто прошел электрический разряд."
    hide m231
    show m254
    "Я смотрел ей в глаза и думал о том, что она права."
    "И все… возможно, действительно может стать совсем иначе."
    "Возможно, то, что я искал… гораздо ближе, чем мне казалось."
    "Возможно, оно буквально на расстоянии вытянутой руки…"
    hide m254
    show m255
    "Моника смотрела на меня, слабо, будто бы робко улыбаясь."
    "Забавно, я никогда не думал, что она может так робко улыбаться…"
    menu:
        "Поцеловать":
            $ renpy.fix_rollback()
            $ kiss = True
            "Еще не совсем понимая, что делаю, я медленно положил руку поверх ее ладони и слегка сжал ее."
            hide m255 with dissolve
            "А затем, словно решившись, наклонился и поцеловал прямо в эту робкую улыбку."
            scene black with dissolve
            "Она слабо выдохнула мне в губы, обвила мою шею руками, и я позабыл, как дышать."
            "Весь мир вдруг сократился до ее рук в моих волосах и до ее нежных губ."
            "Кажется, я мог бы стоять так вечно."
            "Обнимать ее за тонкую талию, ощущать тонкий и сладкий запах духов…"
            "…и целовать до потери пульса."
            scene wheel_all with dissolve
            "А колесо продолжало отсчитывать круг за кругом, словно ничего и не происходило."
        "Поблагодарить":
            $ renpy.fix_rollback()
            me "Спасибо… {w} Правда, спасибо."
            hide m255
            show m254
            me "Я никогда не думал об этом в таком ключе."
            hide m254
            show m247
            mon "Не за что. Я рада, что натолкнула тебя на какие-то мысли."
            "Где ты была раньше с этими мыслями…"
            hide m247
            show m223
            me "А у тебя хорошо поставлена речь."
            me "Тебе бы оратором каким-нибудь пойти…"
            hide m223
            show m207
            mon "Аххах, я приму это за комплимент!"
            hide m207
            show m214
            me "А, да… это он и был, да."
            me "Не сказал бы, что я умею делать комплименты."
            hide m214
            show m224
            mon "Ничего страшного, зато ты довольно милый."
            me "Эм… {w}ну спасибо, что ли."
            hide m224 with dissolve
            scene wheel_all with dissolve
            #локация: общий вид колеса оборзения
            "А колесо продолжало отсчитывать круг за кругом, словно ничего такого не было."

    "Когда мы вышли из кабины спустя два круга, солнце уже клонилось к закату."
    show m201 with dissolve
    mon "Мне пора домой, уже совсем поздно."
    me "Я тебя провожу. Чтобы собаки не покусали."
    hide m201
    show m225
    mon "Ага, или Алан не утащил."
    hide m225
    show m207
    me "Ну да, Алан куда страшнее собаки."
    hide m207 with dissolve
    "Засмеявшись, Моника взяла меня за руку, уходя к выходу из парка."
    "Чувствуя, как сердце забилось где-то в горле, я сжал ее руку и не сдержал улыбки."
    scene city_road with dissolve
    #локация: дом моники (вечер)
    "На душе было так хорошо, что я даже не заметил, когда мы дошли до ее дома."
    show m253 with dissolve
    mon "Что ж, спасибо, что проводил."
    hide m253
    show m201
    mon "И за вечер тоже спасибо."
    hide m201
    show m210
    mon "День, конечно, не задался, но вечер был чудесным."
    hide m210
    show m214
    me "Да не за что… Я рад, что мы поговорили."
    hide m214
    show m224
    mon "А я рада, что застала тебя на месте кражи со взломом."
    me "С каким взломом? Я ничего не взламывал!"
    hide m224
    show m207
    mon "Ну хорошо, просто на месте кражи!"
    hide m207
    show m253
    me "Ты все время теперь будешь мне это припоминать?"
    hide m253
    show m225
    mon "Ну, \"соня\" уже неактуально, так что… да?"
    hide m225
    show m207
    me "Вот же…"
    if kiss == True:
        "Еще посмеиваясь, Моника приподнялась на носочки и коротко поцеловала меня в губы."
    else:
        "Еще посмеиваясь, Моника приподнялась на носочки и коротко поцеловала меня в щеку."

    "У меня перехватило дыхание."
    hide m207
    show m219
    mon "Добрых снов, [name]."
    me "Добрых… Пока, Моника."
    hide m219
    show m214
    mon "Пока, [name]."
    hide m214 with moveoutright
    "Она в последний раз немного грустно улыбнулась мне, повернулась и направилась к дому."
    "А я остался стоять, как дурак, глядя ей вслед."
    #локация: наш дом
    scene room_n with dissolve
    "Дома я лег спать, даже толком не поужинав, чем немного напугал маму."
    "Я все не мог перестать проматывать в голове сегодняшний день."
    "Особенно… финальную его часть."
    "Боже, мне до сих пор чудился запах ее волос…"
    "Возможно, Моника права… {w}И переезд в другой город – это и правда слишком радикальные меры."
    "Круто, конечно, было бы осознать это все в последний момент…"
    "Но, наверное, это лучше, чем я бы осознал это уже в другом городе."
    "Лучше же..? {w}Аргх!"
    "Я уткнулся лицом в подушку и бессильно застонал."
    jump day_mon2
#КОНЕЦ ТРЕТЬЕГО ДНЯ

label day_mon2:
    scene black with dissolve
    stop music
    play music "audio/dokidoki8.ogg"
    "С утра меня разбудил звонок Моники."
    "Я подскочил на месте, опять забыв проснуться, и ответил с некоторым чувством дежавю."
    show m000 with dissolve
    me "Д-да, что? Привет?"
    hide m000
    show m031
    mon "Привет, соня! Это опять я!"
    hide m031
    show m007
    mon "Звоню пожелать тебе доброго утра!"
    hide m007
    show m019
    me "О Господи… Ты что, теперь каждый будешь мне звонить?"
    hide m019
    show m010
    mon "Нет, только сегодня."
    hide m010
    show m032
    mon "Хотя если ты захочешь, я не против. {w}Я всегда встаю рано."
    me "Я уже догадался…"
    hide m032
    show m033
    mon "Я вот зачем звоню. Можешь не приходить сегодня на репетицию."
    me "…Что? Прости, что?"
    hide m033
    show m010
    mon "Ну а зачем ты мне нужен тут, если ты завтра все равно уедешь?"
    hide m010
    show m014
    mon "Вообще я серьезно."
    hide m014
    show m034
    mon "Я нашла другого мальчика, который будет участвовать в сценке."
    hide m034
    show m230
    mon "Так что… Проведи последний день с близкими? {w}Или просто отдохни."
    hide m230
    show m219
    mon "Я что-нибудь выдумаю, что можно сказать миссис Сантане, чтобы не было подозрительно."
    me "А… А что, так можно было?"
    hide m219
    show m032
    mon "Да, конечно, почему нет?"
    hide m032
    show m024
    mon "Считай это, не знаю… прощальным подарком от меня."
    me "Эм, ну… спасибо?"
    hide m024
    show m014
    mon "Пожалуйста."
    hide m014
    show m010
    mon "А теперь иди и спи сколько влезет, соня."
    hide m010
    show m007
    me "Очень смешно…"
    hide m007
    show m031
    mon "Добрых снов."
    me "Пока, Моника… и спасибо. Правда спасибо."
    hide m031
    show m035
    mon "Правда пожалуйста. Пока, [name]."
    hide m035 with dissolve
    "Она повесила трубку, а я автоматически прижал телефон к груди."
    "Блин, а если… а если я действительно совершил ошибку, так категорично решив уехать?"
    "Что, если я и правда был бы здесь счастлив? Здесь, с Моникой?"
    "Кто же знал, что она окажется такой чуткой и заботливой…"
    "Аргх, как же это все так сложно… {w}Но…"
    "Что, если мы и правда с ней больше никогда не увидимся?"
    "Может, стоит все-таки пойти на репетицию?"
    menu:
        "Поехать на репетицию":
            $ renpy.fix_rollback()
            $ lastmeet = True
            "Да. Да, определенно стоит."
            "Ну что ж. Тогда надо вставать…"
            scene sch_m with dissolve
            #локация: школа
            "Поскольку я все равно еще провалялся какое-то время, я пришел ближе к концу репетиции."
            scene sportzal with dissolve
            #локация: спортзал (либо очередной коридор спортзала)
            "Заходить в спортзал я не стал, остался в коридоре и оттуда наблюдал за всеми."
            "Да что уж за всеми… за Моникой."
            "Ее явно опять доставал Алан, она злилась, пихала его локтем либо ругалась, пока миссис Сантана не видела."
            "А когда во время сценки Моника говорила свои реплики, она вдруг заметила меня."
            "Она осеклась, а затем так искренне улыбнулась, что я понял – я не зря приехал."
            "… {w} После репетиции, когда все начали выходить, я встал так, чтобы меня не увидели."
            "Моника вышла последней, и ее я тихонько окликнул, улыбнувшись."
            me "Эй, я здесь."
            if monwheel == True:
                #ЕСЛИ monwheel = true, то
                "Она оглянулась и прежде, чем я что-то успел сказать, обняла меня за шею."
                "Ненадолго, но этого было достаточно, чтобы губы сами собой растянулись в улыбке."
                show m031 with dissolve
                mon "Привет…"
                hide m031
                show m010
                mon "Что, выспался, соня?"
                hide m010
                show m019
                me "Да, вроде того…"
                me "Как прошла репетиция?"
                hide m019
                show m014
                mon "Хорошо. Даже Алан на удивление вел себя прилично."
                hide m014
                show m006
                mon "Ну, насколько это возможно."
                hide m006
                show m002
                me "Надо же, интересно, почему."
                hide m002
                show m004
                mon "Не знаю и знать не хочу."
                hide m004
                show m031
                mon "Пойдем погуляем?"
                me "В том же парке?"
                hide m031
                show m036
                mon "Ой, думаешь? А если Алан?"
                me "Я буду надеяться, что молния не бьет дважды в одно и то же место."
                hide m036
                show m007
                mon "Аххах… Ну пойдем, рискнем."
                hide m007
                show m014
                me "Идем."
                hide m014 with dissolve
                "Взяв Монику за руку, я повел ее в тот же парк."
                scene park with dissolve
                stop music
                play music "audio/raindrops.ogg"
                #локация: и снова парк
                "К счастью, Алан так и не появился. {w}Хотя признаюсь честно, я начал немного параноить после вчерашнего."
                "Погода была замечательная. Дул прохладный ветерок, светило солнце, где-то пели птицы."
                "Мы с Моникой иногда обменивались ничего не значащими фразами, но в основном молчали, наслаждаясь прогулкой."
                show m030 with dissolve
                mon "Как же здорово сегодня на улице…"
                me "Да… Теперь лето по-настоящему наступило."
                hide m030
                show m031
                mon "Скоро можно будет купаться. Знаешь, что?"
                me "Что?"
                hide m031
                show m032
                mon "А в этих твоих больших городах чаще всего негде купаться."
                hide m032
                show m034
                mon "Либо все настолько грязное, что лучше уж не купаться."
                hide m034
                show m029
                mon "А у нас есть аж целых два чудесных оборудованных пляжа!"
                me "Аргументный аргумент."
                me "Даже не знаю, что тебе возразить."
                hide m029
                show m030
                mon "А что ты мне возразишь, если я права?"
                me "Действительно."
                "Продолжая посмеиваться, я посмотрел на Монику."
                "Солнце красиво переливалось в ее золотистых волосах."
                "Она тоже улыбалась, хоть и немного самодовольно. Но как же ей это шло."
                "Я осознал, что откровенно любуюсь, только когда она засмеялась."
                hide m030
                show m031
                mon "Ну что ты так на меня пристально смотришь?"
                me "Да просто…"
                menu:
                # ВЫБОР ДЕЙСТВИЯ (признаться или нет)
                # ДЕЙСТВИЕ 1/2: признаться в чувствах
                    "Признаться в чувствах":
                        $ renpy.fix_rollback()
                        me "Просто… знаешь…"
                        hide m031
                        show m001
                        mon "Что?"
                        hide m001
                        show m000
                        me "Я всю ночь столько про тебя думал… Мне кажется, я схожу с ума."
                        hide m000
                        show m018
                        me "Но я не могу выкинуть тебя из головы, я думаю про тебя все время."
                        hide m018
                        show m010
                        mon "О… Что, правда?"
                        hide m010
                        show m037
                        me "Ну либо я действительно схожу с ума, причем самым извращенным способом."
                        hide m037
                        show m007
                        mon "Аххах… Ну, в таком случае мы оба сумасшедшие."
                        hide m007
                        show m039
                        mon "Я тоже никак не могу перестать про тебя думать."
                        me "Правда?"
                        hide m039
                        show m035
                        mon "Да…"
                    "Промолчать":
                # ДЕЙСТВИЕ 2/2: промолчать (признаться в любви или нет)
                        $ renpy.fix_rollback()
                        me "Просто… так. Просто смотрю."
                        hide m031
                        show m010
                        mon "Я просто посмотреть?"
                        me "Да-да, именно."
                        hide m010
                        show m030
                        mon "Ясно все с тобой. {w}Кхм…"
                        hide m030
                        show m005
                        mon "Ты знаешь, я… я всю ночь думала про вчерашний день."
                        me "Да? Ты тоже?"
                        hide m005
                        show m038
                        mon "Да, ты тоже? Мне кажется, что я схожу с ума."
                        hide m038
                        show m041
                        mon "Но мне кажется, я не могу выкинуть тебя из головы."
                        hide m041
                        show m042
                        me "Ты… прямо с языка сняла."
                        hide m042
                        show m007
                        mon "Да?"
                        hide m007
                        show m031
                        me "Да. Я тоже не могу, только про тебя и думаю."
                        hide m031
                        show m035
                        mon "Правда?"
                        me "Правда."
                        mon "…"
                        hide m035
                        show m041
                        mon "Я так рада, что ты все-таки приехал…"

                #завершение выбора действия (признаться в любви или нет)
                hide m035
                hide m041
                show m014
                mon "И знаешь, я… я бы не стала спрашивать, но раз ты…"
                hide m014
                show m044
                mon "Раз все так…"
                mon "…"
                hide m044
                show m014
                mon "Раз чувства взаимны, я все же спрошу."
                hide m014
                show m033
                mon "Но я пойму, если ты откажешься."
                me "Я слушаю?"
                hide m033
                show m022
                mon "Я еще никогда ни с кем не чувствовала себя так… спокойно, как с тобой."
                hide m022
                show m024
                mon "Даже вчера, когда я хотела прибить Алана на месте, благодаря тебе я как-то… не знаю."
                hide m024
                show m030
                mon "Знала, что все в порядке."
                hide m030
                show m033
                mon "Что да, Алан тот еще придурок, но твое присутствие меня очень поддерживало."
                hide m033
                show m016
                mon "И я хотела узнать, может, ты…"
                hide m016
                show m044
                mon "Может… {w}Может быть, ты мог бы дать второй шанс этому городу?.."
                hide m044
                show m017
                mon "И мне."
                me "Воу…"
                hide m017
                show m046
                mon "Что скажешь?"
                me "Ну я… м-м-м…"
                menu:
                    "Остаться с Моникой":
                        # ВЫБОР ДЕЙСТВИЯ (остаться с моникой или нет)
                        # ДЕЙСТВИЕ 1/2: остаться с моникой
                        #меняем значение monearly = true и
                        $ renpy.fix_rollback()
                        $ monearly = True
                        "Моника терпеливо ждала моего ответа."
                        "Я помедлил, глядя на нее, затем взял ее руки в свои и коротко кивнул."
                        me "Хорошо."
                        hide m046
                        show m045
                        mon "Что..?"
                        me "Я согласен. Я остаюсь."
                        hide m045
                        show m048
                        me "Только нужно тогда успеть сдать билеты, может, успею…"
                        hide m048
                        show m039
                        mon "Если что, я могу возместить тебе их сумму."
                        me "Да ну тебя."
                        hide m039
                        show m004
                        mon "Я не шучу."
                        hide m004
                        show m014
                        mon "А… а ты не шутишь?"
                        me "Нет, я не шучу."
                        hide m014
                        show m031
                        mon "Ты правда остаешься?"
                        me "Я правда остаюсь."
                        hide m031
                        show m035
                        mon "Ты правда… ох, [name]!"
                        hide m035 with dissolve
                        "Моника с тихим визгом бросилась мне на шею. {w} Я обнял ее в ответ, крепко прижимая к себе."
                        #локация: какой-нибудь просто пейзаж того же парка
                        "Странное дело, но я тоже чувствовал себя гораздо спокойнее."
                        "Как будто все было… правильно."
                        "Мой мир перевернулся с ног на голову за последние несколько дней, но я чувствовал, что теперь все правильно."
                        #локация: дорожка парка?
                        "И когда мы наконец-то отстранились друг от друга и пошли дальше гулять по парку, держась за руки,"
                        "я вдруг понял, что смотрю на мир немного-по другому."
                        "И это тоже…"
                        #локация: вид на город сверху
                        scene city with dissolve
                        "Это тоже было правильным."
                        stop music
                        play music "audio/determination.mp3"
                        scene end with dissolve
                        window hide(None)
                        $ renpy.pause (5)
                        return
                        #КОНЕЦ ИГРЫ
                    # ДЕЙСТВИЕ 2/2: все же уехать (остаться с моникой или нет)
                    "Все же уехать":
                        #меняем значение earrings = true и
                        $ earrings = True
                        $ renpy.fix_rollback()
                        "Моника терпеливо ждала моего ответа."
                        "Я помедлил, глядя на нее, затем взял ее руки в свои и покачал головой."
                        hide m046
                        show m045
                        me "Прости."
                        hide m045
                        show m050
                        me "Я очень долго планировал эту поездку, я не могу просто… взять и выбросить все это."
                        hide m050
                        show m051
                        me "Мне будет очень, очень тебя не хватать."
                        me "Ты даже не представляешь, насколько."
                        hide m051
                        show m052
                        mon "Ничего… я все понимаю."
                        hide m052
                        show m053
                        mon "Я ожидала такого ответа, так что не переживай."
                        hide m053
                        show m054
                        me "Прости, правда. Мне очень жаль…"
                        hide m054
                        show m055
                        me "И очень тяжело это говорить."
                        hide m055
                        show m027
                        mon "… {w}…"
                        hide m027
                        show m030
                        mon "Все в порядке, [name]."
                        hide m030
                        show m039
                        mon "И раз ты все-таки уезжаешь… я хочу дать тебе кое-что с собой."
                        "Моника покопалась в сумочке и достала небольшую коробочку."
                        "Внутри лежала пара золотых сережек с крупными камнями."
                        hide m039
                        show m000
                        mon "Это мои серьги, мне когда-то их подарили, но они очень тяжелые."
                        hide m000
                        show m014
                        mon "Возьми их с собой."
                        hide m014
                        show m016
                        mon "Если вдруг у тебя что-то пойдет не по твоему плану, или, не знаю…"
                        hide m016
                        show m019
                        mon "Если вдруг так получится, что все плохо, и некуда деваться, пусть они тебе помогут."
                        mon "Камни настоящие, так что их можно будет дорого продать."
                        hide m019
                        show m014
                        mon "И возможно, тебе это пригодится однажды."
                        me "Ого…"
                        hide m014
                        show m007
                        mon "Не хочу каркать, конечно…"
                        hide m007
                        show m000
                        me "Ты уверена? Они же явно очень дорогие."
                        hide m000
                        show m014
                        mon "У меня еще есть, не переживай."
                        hide m014
                        show m032
                        mon "Все-таки я же любимая дочка семьи Фишер."
                        hide m032
                        show m029
                        me "Да… сложно забыть об этом."
                        me "Спасибо. Надеюсь, они мне не пригодятся."
                        me "Я бы хотел сохранить что-нибудь на память о тебе."
                        hide m029
                        show m031
                        mon "Что это еще за сентиментальность, я никуда не деваюсь."
                        mon "У тебя есть мой номер, будем созваниваться."
                        hide m031
                        show m030
                        mon "Может, однажды приедешь в гости? Кто знает?"
                        hide m030
                        show m032
                        mon "Может, вообще тебе не понравится, и ты вернешься."
                        me "Спасибо за веру в меня."
                        hide m032
                        show m037
                        mon "Это не вера в тебя, просто вдруг не понравится."
                        hide m037
                        show m033
                        mon "Так что никаких глупостей про вещи на память."
                        hide m033
                        show m019
                        mon "Это все хорошо, но если вдруг что-то случится, смело продавай их."
                        mon "Ничего страшного не будет."
                        "Помедлив, я взял коробочку с сережками. {w}Они и правда были увесистыми."
                        "Я убрал коробочку в рюкзак и со вздохом обнял Монику за плечи."
                        hide m019
                        show m033
                        me "Спасибо тебе еще раз. Ты такая чудесная."
                        hide m033
                        show m035
                        mon "Да, я знаю. Пойдем дальше гулять?"
                        me "Давай… пойдем."
                        "Удивительно, но кто бы знал, как мне будет ее не хватать…"
                        hide m035 with dissolve
                        scene city_road with dissolve
                        #локация: закат
                        "Мы гуляли с Моникой до самого вечера. Я проводил ее до дома, и мы еще долго целовались у двери."
                        "В результате нас спугнула ее домработница, и Монике пришлось уйти."
                        #локация: дом (вечер)
                        scene room_n with dissolve
                        "Домой я пришел, как в тумане."
                        "Неужели на этом все закончится. Неужели вот так все и закончится, не успев даже начаться…"
                        "Наверное, сегодня был самый сложный выбор за последние несколько лет."
                        "Второй день подряд отказаться от ужина не получилось, но как поел, я тоже не помнил."
                        "Просто упал лицом в подушку и почти сразу заснул."
                        #завершение выбора действия (остаться с моникой или нет)
            else:
                #ИНАЧЕ (monwheel = false), то
                "Она оглянулась и широко улыбнулась мне."
                show m001 with dissolve
                mon "Привет, соня. Выспался?"
                hide m001
                show m000
                me "Вроде того, да."
                me "Спасибо, что отмазала меня от репетиции, кстати. Почему я не ходил?"
                hide m000
                show m034
                mon "Потому что у тебя там что-то не так с костюмом на выпускной, и ты поехал искать новый, пока не поздно."
                hide m034
                show m037
                me "Ого. Находчиво, даже и не придерешься."
                hide m037
                show m030
                mon "Ну так."
                hide m030
                show m039
                mon "…"
                hide m039
                show m014
                mon "Я правда очень рада, что ты все-таки приехал. Я уже и не рассчитывала."
                hide m014
                show m032
                mon "Не передумал уезжать?"
                me "Эм, нет, конечно."
                hide m032
                show m007
                mon "Ну, я так и думала."
                hide m007
                show m001
                mon "В любом случае я рада, что могу попрощаться с тобой лично."
                hide m001
                show m000
                me "Как-то ты это все слишком грустно повернула."
                me "Слушай, мне все еще так стыдно за вчерашнее…"
                hide m000
                show m022
                me "Может, еще раз сходим куда-нибудь погулять и продолжим вчерашний разговор?"
                hide m022
                show m023
                me "Только не в этот пресловутый парк."
                hide m023
                show m025
                mon "…А надо ли?"
                me "Что надо ли?"
                hide m025
                show m033
                mon "А надо ли продолжать вчерашний разговор?"
                hide m033
                show m034
                mon "Это ведь уже не важно. Пойдем просто погуляем."
                hide m034
                show m007
                mon "Погода просто чудесная."
                hide m007
                show m019
                me "Ты уверена?"
                me "Ты вчера так гнала Алана, чтобы успеть сказать мне что-то…"
                hide m019
                show m030
                mon "Я думаю, уже поздно что-либо говорить, [name]."
                hide m030
                show m031
                mon "Просто я желаю тебе хорошей жизни в новом городе."
                me "Мы еще только гулять идем, а ты уже прощаешься?"
                hide m031
                show m010
                mon "Ничего, потом еще раз скажу!.."
                hide m010 with dissolve
                #локация: дневное небо
                scene sky with dissolve
                "Она взяла меня под руку, и мы пошли гулять по городу."
                "Потом в кино. {w}Потом опять в парк…"
                scene city_road with dissolve
                stop music
                play music "audio/Say_My_Name.mp3"
                #локация: тот же закат
                "Время пролетело так быстро, что никто из нас не успел понять этого."
                "Когда я проводил Монику до дома, уже почти стемнело."
                "А уж когда я пришел домой, было так поздно, что мама даже отругала меня немного за то, что заставил беспокоиться."
                "Я очень плохо запомнил, что именно она мне говорила. {w}В голове было гулко и пусто."
                "А на душе как будто скребла целая стая кошек."
                "Вот же чертов Алан, что же Моника хотела мне сказать…"
                "Я ведь пытался снова поговорить об этом, но она все время убегала от этой темы."
                "А теперь и правда уже поздно что-либо делать…"
                "Завтра утром поезд. Нужно было сегодня собрать вещи и написать записку родителям,"
                "но у меня не осталось абсолютно никаких сил."
                "Все, что мне удалось сделать – так это поставить будильник на завтра."
                "Я отложил телефон подальше и заснул, едва коснувшись головой подушки."
                scene black with dissolve
        "Остаться дома":
            "Нет, наверное, лучше и правда остаться дома."
            "Заодно хорошенько выспаться, а то завтра так рано вставать…"
            "Да и Моника сама сказала, чтобы мы провели время дома…"
            "С этими мыслями я закрыл глаза и провалился обратно в сон."
            scene black with dissolve
            #локация: черный экран
            if sara > -1:
                "Мне удалось поспать несколько часов, прежде чем мне опять позвонили."
                "На этот раз это была Сара."
                show s012 with dissolve
                sar "Привет! Ты что, проспал репетицию?"
                hide s012
                show s014
                me "М-м… да, вроде того."
                hide s014
                show s026
                sar "Хитрый какой! А я уже к тебе подхожу!"
                hide s026
                show s001
                sar "У меня две коробки пиццы и время до самого вечера!"
                hide s001
                show s000
                me "Ого, я смотрю, ты настроена решительно."
                hide s000
                show s059
                sar "Ну конечно, с кем же еще мне удастся так хорошо наесться пиццы?"
                hide s059
                show s060
                sar "Кстати, одну из них я взяла твою любимую, с креветками."
                hide s060
                show s061
                sar "И еще напитков."
                hide s061
                show s047
                sar "В общем, поднимай свою ленивую сам-знаешь-что и иди меня встречай!"
                me "Оуф, ладно."
                hide s047 with dissolve
                "Повесив трубку, я сладко потянулся и неохотно встал с постели."
                show home_hall with dissolve
                #локация: прихожая
                "Я успел и одеться, и умыться, и даже постель застелить, когда Сара наконец-то дошла до меня."
                show s062 with dissolve
                sar "Приве-е-ет, а вот и я!"
                hide s047
                show s027
                sar "Держи пиццу и иди скорей сюда, я тебя обниму!"
                hide s027
                show s063
                me "Ого, ты чего это?"
                hide s063
                show s005
                sar "Я та-а-ак соскучилась!"
                hide s005
                show s065
                sar "Слушай, я тут подумала, у тебя родители дома?"
                me "Нет, они на работе, а что?"
                hide s065
                show s064
                sar "Может, поиграем в тот файтинг, что ты купил весной?"
                hide s064
                show s012
                sar "Мы так давно в него не играли, а я что-то про него столько думала сегодня."
                hide s012
                show s017
                sar "Давай поиграем напоследок?"
                me "Давай, почему бы и нет?"
                hide s017
                show s005
                sar "А еще у меня сюрприз для тебя."
                hide s005
                show s006
                me "Какой?"
                hide s006
                show s001
                sar "Всему свое время, торопыга!"
                hide s001
                show s014
                sar "Пошли скорее есть."
                me "Признай, ты пришла сюда вовсе не ради меня."
                hide s014
                show s028
                sar "Да блин, она так пахла всю дорогу, что это была просто пытка!"
                hide s028
                show s006
                me "Да-да, конечно!"
                hide s006 with dissolve
                #локация: наша комната
                scene room_m with dissolve
                "Пицца закончилась на удивление быстро. {w}Хотя чего удивительного, здесь же Сара."
                "Мы немного поиграли, посмотрели всякую чушь в соцсетях, поболтали ни о чем."
                "Затем Сара притянула к себе сумку и порылась в ней."
                show s017 with dissolve
                sar "Знаешь, мне… мне даже как-то не верится, что завтра тебя уже не будет."
                hide s017
                show s021
                sar "Может, мы никогда больше уже не соберемся вот так вдвоем."
                me "Сара, ну только не начинай…"
                hide s021
                show s022
                sar "Нет-нет, я ничего не говорю, ничего не начинаю."
                hide s022
                show s029
                sar "Я просто, ну… я взяла несколько предметов из дома."
                ## отсюда и до следующей метки – копировать для концовки сары ##
                hide s029
                show s030
                sar "Хочу, чтобы ты взял что-нибудь с собой на память обо мне."
                hide s030
                show s031
                sar "Это браслет дружбы, который я плела тебе в пятом классе, но ты не захотел его носить."
                hide s031
                show s032
                sar "Ты сказал, что лучше он останется у меня."
                me "Ого, ты хранила его все это время?"
                hide s032
                show s066
                sar "Да, вот он."
                hide s066
                show s059
                sar "А это наше фото с прогулки в конце мая, помнишь?"
                hide s059
                show s006
                sar "Мы кормили голубей, а потом их гоняли."
                hide s006
                show s065
                me "Да… оу, а действительно удачное фото."
                hide s065
                show s066
                sar "Да, я долго выбирала к нему рамочку."
                hide s066
                show s001
                sar "А это наше старое фото. Мы здесь совсем недавно познакомились."
                hide s001
                show s000
                me "Ох, блин, вот это я тут…"
                hide s000
                show s004
                sar "Как сказала бы мама – молодой кабанчик."
                me "Ага, почему бы не взять с собой фото, где мои щеки почти загораживают шею?"
                hide s004
                show s005
                sar "Ну перестань, она классная!"
                hide s005
                show s007
                me "Ты-то? Ну еще бы, ты тут Сара-до-встречи-с-пиццей. {w}А я…"
                hide s007
                show s011
                sar "Ну перестань!"
                hide s011
                show s030
                sar "Так вот. {w}И, наконец…"
                me "О боги, твой талисман на удачу."
                hide s030
                show s031
                sar "Да-да, который я привезла с моря в первом классе."
                hide s031
                show s032
                sar "Он никогда еще меня не подводил."
                sar "С ним я дважды брала первое место на конкурсе танцев в старшей школе."
                hide s032
                show s057
                me "Так что, можно сказать, ты читерила?"
                hide s057
                show s037
                sar "Нет, ну я же не каждый раз им пользовалась, это же талисман, а не лампа джинна."
                hide s037
                show s008
                me "Ты же сама сказала, что он на удачу."
                hide s008
                show s011
                sar "Да, но… ой, что тебе объяснять, опять прикалываешься."
                me "Не без этого, да."
                hide s011
                show s000
                me "Но слушай, он ведь был тебе так дорог…"
                hide s000
                show s030
                me "Да что там, все эти вещи тебе дороги, я не могу просто взять и забрать их у тебя."
                hide s030
                show s040
                sar "Можешь. Я хочу, чтобы они у тебя были."
                hide s040
                show s057
                me "Предлагаю компромисс."
                me "Я беру что-то одно с собой, и остальное остается у тебя. {w}Идет?"
                hide s057
                show s059
                sar "Хм… да, хорошо."
                hide s059
                show s000
                sar "И что ты выберешь?"
                me "Хм, дай-ка подумать…"
                menu:
                    # ВЫБОР ПРЕДМЕТА (сувенир на память)
                    # ПРЕДМЕТ 1/4: браслет дружбы
                    "Браслет дружбы":
                        $ renpy.fix_rollback()
                        $ sBracelet = True
                        me "Я возьму браслет. Все-таки ты плела его для меня."
                        hide s000
                        show s006
                        sar "Я, кстати, очень старалась!"
                        me "Да, я вижу. Правда, на руке носить все равно не буду, уж прости."
                        hide s006
                        show s000
                        sar "Ничего, положишь в кошелек."
                    # ПРЕДМЕТ 2/4: совместное фото этого года (сувенир на память)
                    "Совместное фото этого года":
                        $ renpy.fix_rollback()
                        $ sPhoto = True
                        me "Я возьму наше фото, которое не так страшно будет на людях показать."
                        hide s000
                        show s022
                        me "Так ты всегда будешь у меня на глазах."
                        hide s022
                        show s045
                        sar "Ав, [name]…"
                        hide s045
                        show s040
                        sar "Я буду присматривать за тобой."
                    "Старый талисман Сары":
                        $ renpy.fix_rollback()
                        # ПРЕДМЕТ 3/4: старый талисман сары (сувенир на память)
                        $ sMascot = True
                        me "Давай я возьму талисман. Удача мне точно не помешает."
                        hide s000
                        show s005
                        sar "Он как раз заряжен, я давно им не пользовалась."
                        hide s005
                        show s014
                        sar "Надеюсь, что он тебя приятно удивит."
                        me "Я тоже. Спасибо тебе еще раз."
                        hide s014
                        show s040
                        sar "Не за что, [name]."
                    "Наше детское фото":
                        $ renpy.fix_rollback()
                        # ПРЕДМЕТ 4/4: наше детское фото (сувенир на память)
                        $ sPhotoOld = True
                        me "Я возьму нашу детскую фотографию."
                        hide s000
                        show s022
                        me "Чтобы она умерла вместе со мной, и никто ее не увидел больше."
                        hide s022
                        show s004
                        sar "Да что такого, блин, ну все мы в детстве пухляши!"
                        me "Не настолько же! Я не могу тебе позволить показывать ее всем подряд."
                        hide s004
                        show s067
                        sar "Ой, ну ладно, ладно, убедил."
                        #завершение выбора предмета (сувениры на память)

                hide s067
                hide s040
                hide s000
                show s001
                sar "Что ж, тогда все остальные я убираю…"
                hide s001
                show s000
                me "Да, убирай. Этот тогда остается мне."
                ## вот до сюда можно копировать кусок для сары ##
                "Сара кивнула, складывая все обратно в сумку, как вдруг в дверь позвонили."
                hide s000
                show s022
                "Удивленно переглянувшись с подругой, я пошел открывать."
                hide s022 with dissolve
                scene home_hall with dissolve
                #локация: прихожая
                stop music
                play music "audio/sweet_darkness.ogg"
                show m000 with dissolve
                mon "Привет."
                me "Моника? {w}Что ты здесь делаешь?"
                hide m000
                show m025
                mon "Родители дома?"
                me "Нет?!"
                hide m025
                show m007
                mon "Чего ты кричишь, я зашла попрощаться."
                hide m007
                show m014
                mon "Как ты? Вещи уже собрал?"
                me "Да… нет, еще нет, ко мне…"
                hide m014
                show m018
                me "Кхм. Ко мне Сара зашла тоже попрощаться."
                hide m018
                show m024
                mon "Оу."
                hide m024
                show m058
                mon "Что ж, привет ей, раз так."
                hide m058
                show m039
                mon "А тебе удачной дороги. Надеюсь, у тебя все будет хорошо на новом месте."
                hide m039
                show m014
                me "Спасибо, Моника, я тоже надеюсь."
                me "И я… я правда рад был тебя видеть."
                hide m014
                show m024
                mon "Я тебя тоже."
                hide m024
                show m031
                mon "Что ж, не буду больше вам мешать, дай мне знать, как доедешь?"
                me "Да, конечно, я позвоню тебе?"
                hide m031
                show m014
                mon "Хорошо, я буду ждать."
                if kiss == True:
                    #ЕСЛИ kiss = true, то
                    "Моника помедлила, затем коротко поцеловала меня в губы и обняла."
                    "Я обнял ее в ответ, так крепко, как только мог."
                    hide m014
                    show m027
                    mon "Прощай, [name]"
                    hide m027
                    show m017
                    mon "Доброй дороги."
                    hide m017
                    show m050
                    me "Прощай, Моника…"
                    hide m050
                    show m035
                    "Она улыбнулась мне в последний раз и ушла."
                    hide m035 with dissolve
                    "А я стоял и снова смотрел ей вслед, как самый последний дурак на этом свете."
                else:
                    #ИНАЧЕ (kissa не было), то
                    "Тепло улыбнувшись, словно ничего такого не было, Моника коротко чмокнула меня в щеку."
                    hide m014
                    show m039
                    mon "Удачи тебе, [name]. Прощай."
                    me "Прощай, Моника…"
                    hide m039
                    show m007
                    mon "Жду звонка."
                    hide m007 with dissolve
                    "Подмигнув мне, не переставая улыбаться, Моника развернулась и ушла."
                    "А я остался смотреть ей вслед, как влюбленный идиот."
                    "Черт, почему же все должно было закончиться именно так…"

                scene room_m with dissolve
                #локация: наша комната
                stop music
                play music "audio/dokidoki8.ogg"
                "Когда я вернулся в комнату, Сара сидела на диване и крутила в руках мой так называемый сувенир."
                "В глазах ее стояли слезы."
                show s068 with dissolve
                me "Сара, ты что, плачешь?"
                hide s022
                show s017
                sar "Н-нет…"
                me "Ну Сара, что такое?"
                hide s017
                show s029
                sar "Ни… ничего, просто…"
                hide s029
                show s030
                sar "Ни… ничего, просто…"
                hide s030
                show s039
                sar "Я все еще не могу поверить, что ты уезжаешь!!"
                me "Сара, ну пора бы уже…"
                hide s039
                show s043
                me "Ну… ну не плачь. Давай я еще пиццы закажу?"
                hide s043
                show s044
                sar "Н-не надо."
                hide s044
                show s043
                me "…О Господи, {w}с тобой все в порядке?"
                hide s043
                show s021
                sar "Да, все в порядке."
                hide s021
                show s019
                sar "Тебе и так придется прилично потратиться в дороге, не надо пиццы."
                hide s019
                show s035
                sar "Просто доберись хорошо и звони мне, ладно?"
                hide s035
                show s040
                me "Обязательно."
                me "Сара, запомни – мы останемся друзьями, как и раньше."
                hide s040
                show s030
                me "Просто я буду немного… дальше, чем через два квартала от тебя."
                hide s030
                show s068
                me "Но обещаю, мы не прекратим общаться просто потому, что я уезжаю."
                hide s068
                show s030
                sar "…"
                hide s030
                show s066
                sar "Хорошо… спасибо, [name]."
                hide s066
                show s001
                sar "А кто приходил, кстати?"
                hide s001
                show s000
                me "А… да неважно."
                hide s000
                show s007
                sar "А как тебе удалось уговорить Монику заменить тебя в сценке?"
                hide s007
                show s022
                me "Да просто… помог ей с Аланом, ничего такого."
                hide s022
                show s023
                me "Точно не хочешь пиццу?"
                hide s023
                show s060
                sar "Да, я в порядке, все хорошо."
                hide s060
                show s061
                sar "Ну что, еще разочек сыграем?"
                menu:
                    # ВЫБОР ДЕЙСТВИЯ (включить файтинг)
                    "Играть с Сарой в файтинг":
                        $ renpy.fix_rollback()
                        # ДЕЙСТВИЕ 1/2: сыграть с сарой в файтинг
                        me "Да, конечно. Включай."
                        $ gamesara = True
                        hide s061
                        call demomo
                        show s064
                        sar "Ура! Что ж, опозорим кое-кого еще раз!"
                        label aftergame:
                            scene room_m with dissolve
                            show s011 with dissolve
                            me "Кого ты тут собралась позорить, м-м?"
                            hide s011
                            show s028
                            sar "Так нечестно!"
                            me "Все честно."
                            return
                    "Давай лучше посмотрим фильм":
                        $ renpy.fix_rollback()
                        # ДЕЙСТВИЕ 2/2: давай лучше посмотрим фильм (не надо файтинг)
                        me "Знаешь, я что-то устал. Да и ехать завтра."
                        me "Давай лучше фильм какой-нибудь посмотрим?"
                        hide s061
                        show s004
                        sar "Ты просто боишься, что я тебя на лопатки уложу, да?"
                        me "Очень."
                        hide s004
                        show s005
                        sar "Разумное решение. О, а давай посмотрим тот фильм про космических пиратов?"
                        hide s005
                        show s000
                        me "О, да, тоже про него недавно думал, давай."

                    #завершение выбора действия (че по файтингу)

                scene sky_n with dissolve
                #локация: вечернее небо (можно закат)
                "Вечер завершился мирным просмотром фильмов."
                "Я проводил Сару до дома, по пути зашел в магазин купить чего-нибудь, потом поужинал с родителями…"
                "Все как обычно. {w}Все так, словно ничего не происходило, обычный день."
                "Вот только завтра ничего не будет уже как прежде…"
            else:
                #ИНАЧЕ (<0Са), то
                #локация: черный экран
                scene black with dissolve
                "Я проспал, кажется, целую вечность."
                "Наверное, я решил разом выспаться за все две недели экзаменов."
                scene sky_n with dissolve
                stop music
                play music "audio/meet_me_there.ogg"
                #локация: закатное небо
                "Когда я проснулся, уже вечерело. Голова гудела, словно чугунная."
                "Я вспомнил о нашей ссоре с Сарой, и взгляд сам собой упал на телефон."
                "Может, позвонить ей?.. Не знаю, нравится ли мне идея, что я уеду, не попрощавшись."
                "Она столько поддерживала меня, верила в меня, когда даже я не верил."
                "Да, в последние дни я слишком нервничал из-за всей этой фигни со сценкой и Моникой."
                "Так что, возможно, я и правда мог сильно обидеть ее…"
                "Может, еще не поздно все исправить?"
                menu:
                    "Позвонить Саре":
                        $ renpy.fix_rollback()
                        # ВЫБОР ДЕЙСТВИЯ (миримся или нет)
                        # ДЕЙСТВИЕ 1/2: позвонить саре
                        #то меняем значение очков сары на 0Са и
                        $ sara = 0
                        "Вздохнув, я взял телефон и после недолгого колебания набрал номер Сары."
                        "Она так долго не брала трубку, что я думал, что уже не возьмет."
                        "Но когда я хотел уже отключиться, она все же ответила."
                        show s050 with dissolve
                        sar "Что?"
                        hide s050
                        show s051
                        me "Привет."
                        hide s051
                        show s011
                        sar "Привет. Что тебе надо?"
                        me "Слушай, я, эм…"
                        me "Я хотел извиниться за вчерашнее."
                        hide s011
                        show s008
                        me "Я знаю, ты злишься, и я тоже злюсь, если честно."
                        hide s008
                        show s070
                        me "Но меня уже завтра тут не будет, и я… я не хочу уезжать вот так."
                        hide s070
                        show s071
                        me "Даже не попрощавшись с тобой как следует."
                        hide s071
                        show s041
                        sar "…"
                        hide s041
                        show s072
                        sar "Да, я тоже. Я понимаю."
                        me "Правда?"
                        hide s072
                        show s021
                        me "Давай, может, помиримся потом, когда я уже уеду…"
                        me "В смысле нормально помиримся."
                        hide s021
                        show s019
                        me "А сейчас просто… сделаем вид, что ничего не было."
                        hide s019
                        show s070
                        sar "Хорошо. Давай."
                        hide s070
                        show s023
                        me "Тогда я… как и договаривались, завтра утром подойду к твоему дому?"
                        hide s023
                        show s030
                        sar "Да, хорошо."
                        me "Хорошо. Тогда до завтра?"
                        hide s030
                        show s040
                        sar "До завтра, [name]."
                        hide s040 with dissolve
                        "Я повесил трубку и вздохнул."
                        "Ну что ж, хотя бы так, уже неплохо. {w}Мне будет ее не хватать."
                        "Возможно, даже очень. И ее, и Моники."
                    "Забить на Сару":
                        $ renpy.fix_rollback()
                        # ДЕЙСТВИЕ 2/2: забить на сару (не миримся с сарой)
                        "Ой, да ладно, переживу как-нибудь."
                        "Вон, лучше поиграю во что-нибудь. Или почитаю. Или и то, и то."

                    #завершение выбора действия (миримся или нет)

            "Вздохнув, я пошел раздобыть себе чего-нибудь поесть, но тихо, чтобы не спалили, что я только проснулся."
            "А затем задумался, чем можно пока себя занять."
            jump plays
            label plays:
                stop music
                play music "audio/dance_of_fireflies.ogg"
                "Собственно, почему бы не поиграть немного. Когда еще будет возможность?"
                menu:
                    "Поиграть в файтинг":
                        # ВЫБОР ДЕЙСТВИЯ (а не поиграть ли нам)
                        # ДЕЙСТВИЕ 1/3: поиграть в файтинг
                        #меняем значение game = true
                        $ game = True
                        $ gamealone = True
                        "Ну, собственно, почему бы и нет."
                        jump demomo

                    # ДЕЙСТВИЕ 2/3: поиграть в тетрис (а не поиграть ли нам)
                    "Поиграть в тетрис":
                        #меняем значение game = true
                        $ game = True
                        "Ну, собственно, почему бы и нет."
                        call tetris_start
                        menu:
                            "Поиграть еще":
                                jump tetris_start
                            "Выбрать другую":
                                jump plays
                            "Закончить играть":
                                pass
                    "Почитать лучше":
                        # ДЕЙСТВИЕ 3/3: почитать лучше (а не поиграть ли нам)
                        #меняем значение book = true
                        $ book = True
                        "Хотя… лучше пойду еще поваляюсь и почитаю чего-нибудь."
                        #завершение выбора действия (а не поиграть ли нам)
                if game == True:
                    "В результате мы играли почти до ночи, отвлекаясь разве что на завтрак."
                if book == True:
                    "В результате мы читали до самой ночи, отвлекаясь разве что на завтрак."
                "Мда, какой-то бесполезный вышел день, ну да что поделать."
                "Надо как-то уложить себя теперь обратно спать, ведь завтра очень рано вставать."
                "Ведь надо же еще и вещи собрать, вот черт, я совсем забыл про них…"
                "Ладно, завтра соберу, это недолго."
                "Соберу вещи, напишу родителям записку, а если что, посплю в поезде по дороге."
                "А сейчас надо постараться заснуть."
                "И желательно… не думать о той жизни, которая у меня могла бы быть, будь я чуть смелее…"

            label aftergame1:
                menu:
                    "Поиграть еще":
                        jump demomo
                    "Выбрать другую":
                        jump plays
                    "Закончить играть":
                        pass

    jump day_mon3
#завершение выбора действия (поехать ли на репетицию)
#КОНЕЦ ЧЕТВЕРТОГО ДНЯ

# row - field width
# column - field height
# speed - falling speed
# tops - number of top places
# level - level of difficulty
# mode - presence of a bonus
# impossible - without I tetromino
# for_level - the number of lines for level-up

# Highscore
init -100:
    if persistent.highscore is None:
        $ persistent.highscore = []

init python:

    # Tetromino Symbols
    symb_field = '·'
    symb_red = 'R'
    symb_cyan = 'C'
    symb_blue = 'B'
    symb_green = 'G'
    symb_orange = 'O'
    symb_purple = 'P'
    symb_yellow = 'Y'
    coloring = [symb_red, symb_cyan, symb_blue, symb_green, symb_orange, symb_purple, symb_yellow]

    row = 10
    column = 20

    tops = 10
    level = 1
    for_level = 20
    mode = False
    impossible = False
    speed = 0.4
    speed_limit = 0.05
    speed_acceleration = 0.03

    # Main Class
    class Tetris():
        def __init__(self, speed=.5, level=1, mode=False, bonus=0):
            self.field = ['·']*(row*column)
            self.active = 0
            self.rotate = 0
            self.tetrominos = {1:[1,1, 1,1], 2:[1,1,1,1, 0,0,0,0], 3:[1,0,0, 1,1,1], 4:[0,0,1, 1,1,1], 5:[0,1,1, 1,1,0], 6:[1,1,0, 0,1,1], 7:[0,1,0, 1,1,1] }
            self.next = self.get_tetromino()
            self.tetromino = []
            self.block = True
            self.can_rotation = True
            self.mode = mode
            self.bonus = bonus
            self.lines = 0
            self.lines_counter = 0
            self.point = 0
            self.level = level
            self.start_speed = speed
            self.can_skip = True
            self.speed = self.start_speed
            self.end = False

        def delete_I(self):
            self.tetrominos.pop(2)

        def get_tetromino(self):
            m = []
            for tetromino in self.tetrominos.values():
                m.append(tetromino)
            r = renpy.random.choice(m)
            return r

        def get_tetromino_i(self, i):
            return self.tetrominos.get(i)

        def clear(self, end=False):
            i = 0
            for cell in self.field:
                for color in coloring:
                    if cell == color:
                        self.field[i] = symb_field
                i += 1
            if end:
                self.end_turn()

        def delete(self):
            self.clear(end=True)
            self.bonus -= 1

        def draw_tetromino(self):
            self.clear()
            j = self.tetromino_index_start()
            i = 0
            for cell in self.tetromino:
                if cell:
                    # Tetromino O
                    if self.tetromino == [1,1, 1,1]:
                        self.field[self.active+j] = symb_yellow
                    # Tetromino I
                    elif self.tetromino == [1,1,1,1, 0,0,0,0] or self.tetromino == [0,0,0,0, 1,1,1,1]:
                        self.field[self.active+j] = symb_purple
                    # Tetromino J
                    elif self.tetromino == [1,0,0, 1,1,1] and not self.rotate or self.tetromino == [1,1,1, 0,0,1] and self.rotate == 180:
                        self.field[self.active+j] = symb_blue
                    elif self.tetromino == [1,1, 1,0, 1,0] and self.rotate == 90 or self.tetromino == [0,1, 0,1, 1,1] and self.rotate == 270:
                        self.field[self.active+j] = symb_blue
                    # Tetromino L
                    elif self.tetromino == [0,0,1, 1,1,1] and not self.rotate or self.tetromino == [1,1,1, 1,0,0] and self.rotate == 180:
                        self.field[self.active+j] = symb_orange
                    elif self.tetromino == [1,0, 1,0, 1,1] and self.rotate == 90 or self.tetromino == [1,1, 0,1, 0,1] and self.rotate == 270:
                        self.field[self.active+j] = symb_orange
                    # Tetromino S
                    elif self.tetromino == [0,1,1, 1,1,0] and not self.rotate or self.tetromino == [0,1,1, 1,1,0] and self.rotate == 180:
                        self.field[self.active+j] = symb_green
                    elif self.tetromino == [1,0, 1,1, 0,1] and self.rotate == 90 or self.tetromino == [1,0, 1,1, 0,1] and self.rotate == 270:
                        self.field[self.active+j] = symb_green
                    # Tetromino Z
                    elif self.tetromino == [1,1,0, 0,1,1] and not self.rotate or self.tetromino == [1,1,0, 0,1,1] and self.rotate == 180:
                        self.field[self.active+j] = symb_red
                    elif self.tetromino == [0,1, 1,1, 1,0] and self.rotate == 90 or self.tetromino == [0,1, 1,1, 1,0] and self.rotate == 270:
                        self.field[self.active+j] = symb_red
                    # Tetromino T
                    elif self.tetromino == [0,1,0, 1,1,1] and not self.rotate or self.tetromino == [1,1,1, 0,1,0] and self.rotate == 180:
                        self.field[self.active+j] = symb_cyan
                    elif self.tetromino == [1,0, 1,1, 1,0] and self.rotate == 90 or self.tetromino == [0,1, 1,1, 0,1] and self.rotate == 270:
                        self.field[self.active+j] = symb_cyan

                j = self.tetromino_index_count(j, i)
                i += 1

        def new(self):
            self.line_checker()

            self.rotate = 0
            self.active = self.center()
            self.tetromino = self.next
            self.next = self.get_tetromino()

            self.draw_tetromino()
            self.block = False
            self.can_rotation = True

        def move(self):
            if self.check_let(offset=row*2):
                self.slow()

            if self.check_let():
                self.end_turn()
                return

            self.active += row
            self.draw_tetromino()

        def shift(self, line):
            for l in reversed(range(1, line+1)):
                a = l*row
                b = a+row
                c = (l-1)*row
                d = c+row
                self.field[a:b] = self.field[c:d]
                self.field[c:d] = [symb_field]*row

        def fast(self):
            self.speed = speed_acceleration
        def slow(self):
            self.speed_update()
        def boost(self):
            if self.speed == speed_acceleration:
                self.slow()
            else:
                self.fast()

        def left(self):
            x = self.find_x_cell(left=True)
            if x > 0:
                if not self.check_let(offset=-1-row):
                    self.active -= 1
                    self.draw_tetromino()

        def right(self):
            x = self.find_x_cell(right=True)
            if x < row-1:
                if not self.check_let(offset=1-row):
                    self.active += 1
                    self.draw_tetromino()

        def find_x_cell(self, left=False, right=False):
            m = []
            i = 0
            x = 0
            for cell in self.field:
                for color in coloring:
                    if cell == color:
                        x,y = self.coordinate_index(i)
                        m.append(x)
                i += 1

            if m != []:
                if left:
                    x = min(m)
                elif right:
                    x = max(m)

            return x

        def outward(self):
            j = self.tetromino_index_start()
            k = 0
            for cell in self.tetromino:
                if cell:
                    i = self.active+j
                    x,y = self.coordinate_index(i)
                    xx, yy = self.coordinate()
                    if xx >= row-3:
                        if x == 0:
                            return True
                j = self.tetromino_index_count(j, k)
                k += 1
            return False

        def check_let(self, offset=0):
            j = self.tetromino_index_start()
            k = 0
            for cell in self.tetromino:
                if cell:
                    i = (self.active+j)+row+offset
                    x,y = self.coordinate_index(i)
                    if y <= column-1:
                        for color in coloring:
                            if self.field[i] == color.lower():
                                return True
                    else:
                        return True
                j = self.tetromino_index_count(j, k)
                k += 1
            return False

        def check_let_for_skip(self, offset=0):
            j = self.tetromino_index_start()
            k = 0
            for cell in self.tetromino:
                if cell:
                    i = (self.active+j)+row+offset
                    x,y = self.coordinate_index(i)
                    if y <= column-1:
                        for color in coloring:
                            if self.field[i] == color.lower():
                                return self.active+offset
                    else:
                        return self.active+offset
                j = self.tetromino_index_count(j, k)
                k += 1

        def skip(self):
            self.can_skip = False
            for c in range(column):
                s = self.check_let_for_skip(offset=row*c)
                if s:
                    break

            self.active = s
            self.draw_tetromino()
            self.end_turn()

        def can_skip_reload(self):
            self.can_skip = True

        def tetromino_index_start(self):
            l = len(self.tetromino)
            j = 0 if l == 8 else -1
            return j

        def tetromino_index_count(self, j, i):
            l = len(self.tetromino)

            if self.rotate == 90:
                if i == 1 or i == 3:
                    j += row-2

            elif self.rotate == 180:
                if l == 6:
                    if j == 1:
                        j += row-3
                elif l == 8:
                    j += row-1

            elif self.rotate == 270:
                if i == 1 or i == 3:
                    j += row-2

            else:
                if l == 4:
                    if j == 0:
                        j += row-2
                elif l == 8:
                    pass

                else:
                    if j == 1:
                        j += row-3
            j += 1
            return j

        def coordinate(self):
            i = self.active
            y = i // row
            x = i - y*row
            return x,y

        def coordinate_index(self, i):
            y = i // row
            x = i - y*row
            return x,y

        def hardening(self):
            i = 0
            for cell in self.field:
                for color in coloring:
                    if cell == color:
                        self.field[i] = color.lower()
                i+=1

        def rotation(self):
            l = len(self.tetromino)
            temp = self.tetromino[:]
            temp_rotate = self.rotate

            if l == 8:
                self.rotate = 180 if not self.rotate else False
            elif l == 6:
                if not self.rotate:
                    self.rotate = 90
                    if self.tetromino == [1,0,0, 1,1,1]:
                        self.tetromino = [1,1, 1,0, 1,0]
                    elif self.tetromino == [0,0,1, 1,1,1]:
                        self.tetromino = [1,0, 1,0, 1,1]
                    elif self.tetromino == [0,1,1, 1,1,0]:
                        self.tetromino = [1,0, 1,1, 0,1]
                    elif self.tetromino == [1,1,0, 0,1,1]:
                        self.tetromino = [0,1, 1,1, 1,0]
                    elif self.tetromino == [0,1,0, 1,1,1]:
                        self.tetromino = [1,0, 1,1, 1,0]

                elif self.rotate == 90:
                    self.rotate = 180
                    if self.tetromino == [1,1, 1,0, 1,0]:
                        self.tetromino = [1,0,0, 1,1,1]
                    elif self.tetromino == [1,0, 1,0, 1,1]:
                        self.tetromino = [0,0,1, 1,1,1]
                    elif self.tetromino == [1,0, 1,1, 0,1]:
                        self.tetromino = [0,1,1, 1,1,0]
                    elif self.tetromino == [0,1, 1,1, 1,0]:
                        self.tetromino = [1,1,0, 0,1,1]
                    elif self.tetromino == [1,0, 1,1, 1,0]:
                        self.tetromino = [0,1,0, 1,1,1]

                    self.tetromino = self.tetromino[::-1]

                elif self.rotate == 180:
                    self.rotate = 270
                    if self.tetromino == [1,1,1, 0,0,1]:
                        self.tetromino = [0,1, 0,1, 1,1]
                    elif self.tetromino == [1,1,1, 1,0,0]:
                        self.tetromino = [1,1, 0,1, 0,1]
                    elif self.tetromino == [0,1,1, 1,1,0]:
                        self.tetromino = [1,0, 1,1, 0,1]
                    elif self.tetromino == [1,1,0, 0,1,1]:
                        self.tetromino = [0,1, 1,1, 1,0]
                    elif self.tetromino == [1,1,1, 0,1,0]:
                        self.tetromino = [0,1, 1,1, 0,1]

                else:
                    self.rotate = 0
                    self.tetromino = self.tetromino[::-1]

                    if self.tetromino == [1,1, 1,0, 1,0]:
                        self.tetromino = [1,0,0, 1,1,1]
                    elif self.tetromino == [1,0, 1,0, 1,1]:
                        self.tetromino = [0,0,1, 1,1,1]
                    elif self.tetromino == [1,0, 1,1, 0,1]:
                        self.tetromino = [0,1,1, 1,1,0]
                    elif self.tetromino == [0,1,1, 1,1,0]:
                        self.tetromino = [1,1, 0,0, 1,1]
                    elif self.tetromino == [1,0, 1,1, 1,0]:
                        self.tetromino = [0,1,0, 1,1,1]

            if self.check_let(offset=-row) or self.check_let() or self.outward():
                self.rotate = temp_rotate
                self.tetromino = temp[:]

            self.draw_tetromino()

        def center(self):
            return int(row/2)

        def stats_update(self, line):
            self.lines += line
            self.lines_counter += line
            if self.lines_counter >= for_level:
                self.level += 1
                self.point += 100 * self.level
                self.lines_counter -= for_level
                self.speed_update()
            point = 100 if line == 1 else 300 if line == 2 else 700 if line == 3 else 1500
            self.point += point
            if line == 4 and self.mode:
                self.bonus += 1

        def speed_update(self):
            self.speed = self.start_speed - (self.level*0.01) if self.start_speed - (self.level*0.01) > speed_limit else speed_limit

        def line_checker(self):
            checker = 0
            clear_line = 0
            for line in range(column):
                for cell in range(row):

                    for color in coloring:
                        if self.field[(line*row)+cell] == color.lower():
                            checker += 1

                    if checker == row:
                        self.shift(line)
                        clear_line += 1
                checker = 0

            if clear_line > 0:
                renpy.vibrate(1.0)
                self.stats_update(clear_line)

        def highscore_update(self):
            if persistent.highscore == [] or self.point > persistent.highscore[-1]:
                persistent.highscore.append(self.point)
                persistent.highscore.sort(reverse=True)
                if len(persistent.highscore) > tops:
                    persistent.highscore = persistent.highscore[:tops]

        def end_checker(self):
            for c in range(row):
                for color in coloring:
                    if self.field[row+c] == color.lower():
                        self.end = True
                        break

        def end_turn(self):
            self.slow()
            self.can_rotation = False
            self.hardening()
            self.end_checker()
            self.point += self.level
            self.block = True
            if self.end:
                self.highscore_update()
                renpy.hide_screen('draw_tetris')
                renpy.show_screen('game_over')

        def restart(self):
            self.level = store.level
            self.mode = store.mode
            self.field = ['·']*(row*column)
            self.speed = self.start_speed
            self.active = 0
            self.block = True
            self.can_rotation = True
            self.lines_counter = 0
            self.lines = 0
            self.point = 0
            self.bonus = 0
            self.end = False
            self.speed_update()

    def draw_next(n):
        t = ''
        l = len(n)
        i = 0
        for cell in n:
            if cell:
                # O
                if n == [1,1, 1,1]:
                    t += '{image=yellow.png}'
                # I
                elif n == [1,1,1,1, 0,0,0,0]:
                    t += '{image=purple.png}'
                # J
                elif n == [1,0,0, 1,1,1]:
                    t += '{image=blue.png}'
                # L
                elif n == [0,0,1, 1,1,1]:
                    t += '{image=orange.png}'
                # S
                elif n == [0,1,1, 1,1,0]:
                    t += '{image=green.png}'
                # Z
                elif n == [1,1,0, 0,1,1]:
                    t += '{image=red.png}'
                # T
                elif n == [0,1,0, 1,1,1]:
                    t += '{image=cyan.png}'
            else:
                t += '{image=empty.png}'

            if l == 4:
                if i == 1:
                    t += '\n'
            elif l == 6:
                if i == 2:
                    t += '\n'
            elif l == 8:
                if i == 3:
                    t += '\n'
            i+=1

        return t

    key_left = False
    key_right = False
    import pygame
    class KeyCatcher(renpy.Displayable):
        def render(self,w,h,st,at):
            return Null().render(w,h,st,at)
        def event(self, event, x, y, st):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    store.key_left = True
                elif event.key == pygame.K_RIGHT:
                    store.key_right = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    store.key_left = False
                elif event.key == pygame.K_RIGHT:
                    store.key_right = False

    def brightness(image, b=0.2):
        return im.MatrixColor(image, im.matrix.brightness(b))

image im_key = KeyCatcher()

### TETRIS DRAW SCREEN ###
screen draw_tetris():
    frame xysize 750,940 align .5,.5:
        add 'im_key'
        add '#fff' size 550, 930 xpos 0
        frame xysize 35*row,35*column yalign .5 xalign .37 xanchor .5:
            add 'back.jpg' align .5,.5 size 35*row,35*column

        vbox yalign .5 xalign .37 xanchor .5:
            for clm in range(column):
                hbox:
                    for cell in tetris.field[row*clm : row*(clm+1)]:

                        if cell == symb_red or cell == symb_red.lower():
                            add 'red.png'
                        elif cell == symb_green or cell == symb_green.lower():
                            add 'green.png'
                        elif cell == symb_blue or cell == symb_blue.lower():
                            add 'blue.png'

                        elif cell == symb_yellow or cell == symb_yellow.lower():
                            add 'yellow.png'
                        elif cell == symb_cyan or cell == symb_cyan.lower():
                            add 'cyan.png'
                        elif cell == symb_purple or cell == symb_purple.lower():
                            add 'purple.png'
                        elif cell == symb_orange or cell == symb_orange.lower():
                            add 'orange.png'

                        else:
                            add 'empty.png'

        if renpy.variant("small"):
            $ vboxalign = (1.26, .2)
        else:
            $ vboxalign = (1.18, .2)

        vbox align vboxalign xsize 140:
            text 'NEXT:' xanchor 1.0
            text '%s'%(draw_next(tetris.next)) xanchor 1.0

            null height 60
            text 'LEVEL:' xanchor 1.0
            text '%s'%(tetris.level) xanchor 1.0
            text 'LINES:' xanchor 1.0
            text '%s'%(tetris.lines) xanchor 1.0
            text 'SCORE:' xanchor 1.0
            text '%s'%(tetris.point) xanchor 1.0

            text 'HIGHS:' xanchor 1.0
            $ highscore = persistent.highscore[0] if persistent.highscore != [] else 0
            text '%s'%(highscore) xanchor 1.0

            if tetris.mode:
                null height 50
                text 'BONUS:' xanchor 1.0
                text '%s'%(tetris.bonus) xanchor 1.0

    if renpy.variant("small"):
        button background 'gui/left.png' hover_background brightness('gui/left.png') xysize 250, 250 focus_mask True action Function(tetris.left) align .03,.9
        button background 'gui/right.png' hover_background brightness('gui/right.png') xysize 250, 250 focus_mask True action Function(tetris.right) align .195,.9
        button background 'gui/down.png' hover_background brightness('gui/down.png') xysize 250, 250 focus_mask True action Function(tetris.boost) align .81,.9
        button background 'gui/rotate.png' hover_background brightness('gui/rotate.png') xysize 250, 250 focus_mask True action If(tetris.can_rotation, Function(tetris.rotation)) align .97,.9
        if tetris.bonus:
            button background 'gui/bonus.png' hover_background brightness('gui/bonus.png') xysize 250, 250 focus_mask True action Function(tetris.delete) align .89,.5

    # PC
    else:
        if tetris.can_skip:
            key 'K_RETURN' action Function(tetris.skip)
        else:
            timer .2 action Function(tetris.can_skip_reload)
        if tetris.can_rotation:
            key 'mousedown_1' action Function(tetris.rotation)
            key 'K_UP' action Function(tetris.rotation)
        if tetris.bonus:
            key 'mousedown_2' action Function(tetris.delete)
            key 'K_SPACE' action Function(tetris.delete)

        key 'mousedown_3' action Function(tetris.boost)
        key 'mouseup_3' action Function(tetris.slow)
        key 'K_DOWN' action Function(tetris.boost)

        key 'K_RIGHT' action Function(tetris.right)
        if key_right:
            use keydown_right_move

        key 'K_LEFT' action Function(tetris.left)
        if key_left:
            use keydown_left_move

    use tetromino_animation

screen keydown_right_move():
    timer 0.05 repeat True action Function(tetris.right)
screen keydown_left_move():
    timer 0.05 repeat True action Function(tetris.left)
screen tetromino_animation():
    timer tetris.speed repeat True action If(tetris.block, Function(tetris.new), Function(tetris.move))

### GAME OVER SCREEN ###
screen game_over():
    add '#000'
    vbox align (.5,.45) xsize 500:
        text 'GAME OVER' size 50 xalign .5
        text 'Уровень: [tetris.level]' size 40 xalign .5
        text 'Линии: [tetris.lines]' size 40 xalign .5
        text 'Очки: [tetris.point]' size 40 xalign .5
        null height 20
        $ i = 1
        for highscore in persistent.highscore:
            if highscore == tetris.point:
                text 'top [i]: [highscore]' size 45 xalign .5 color '#f00'
            else:
                text 'top [i]: [highscore]' size 40 xalign .5
            $ i += 1
    textbutton 'Выход' action Hide('game_over'), Jump('tesst') align .5,.9

label tetris_start:

    call screen difficulty_choice

    $ tetris = Tetris(speed=speed, mode=mode, level=level, bonus=0)
    $ tetris.speed_update()
    if impossible:
        $ tetris.delete_I()

    call screen draw_tetris

label tetris_reload:
    $ tetris.restart()
    call screen draw_tetris


init python:
    def set_mode_classic():
        store.row = 10
        store.column = 20
        store.speed = 0.4
    def set_mode_new():
        store.row = 12
        store.column = 25
        store.speed = 0.3
        store.mode = True
    def set_mode_hard():
        store.row = 13
        store.column = 25
        store.speed = 0.2
        store.mode = True
    def set_mode_impos():
        store.row = 15
        store.column = 26
        store.speed = 0.2
        store.impossible = True

screen difficulty_choice():
    vbox align .5,.5 spacing 30:
        button background '#888' hover_background '#fff' xysize 1280,720 action Function(set_mode_classic), Return():
            text 'Играть' align .5,.5 size 60 color '#000'

label day_mon3:
    if monearly == False:
        scene black with dissolve
        stop music
        play music "audio/enigma.mp3"
        "Утром я чувствовал себя, как зомби, которого похоронили накануне зомби-апокалипсиса."
        "Заснуть быстро вчера не получилось, я все не мог выкинуть Монику из головы."
        "Даже сейчас, бегая и пытаясь одновременно чистить зубы и одеваться, {w} да еще и так, чтобы никто не заметил…"
        "…Я думал о ней."
        "Это начинало надоедать. Мне ведь надо было сосредоточиться сейчас совсем на другом!"
        "К примеру, наконец-то собрать вещи. {w}Я взял свою сумку, приготовленную где-то полгода назад."
        "Это должно быть легко, главное – ничего не забыть."
        ## мини-игра со сбором вещей ##
        $ renpy.pause (3)
        "Так, вещи все."
        "Я поставил сумку около двери, а сам сел за стол писать родителям записку."
        "Надо было вчера это сделать, конечно, но… ладно, черт с ним."
        #локация: письменный стол ?
        scene notebook with dissolve
        "Итак, начнем. Дорогие мама и папа…"
        "Блин, как-то слишком банально, наверное. {w}Ой, ну и ладно."
        "Дорогие мама и папа. {w}Если вы это читаете, значит, я уже далеко отсюда."
        "Я решил уехать из города и начать новую жизнь, потому что…"
        "Потому что я… эм…"
        menu:
            "Не вижу будущего здесь":
                $ renpy.fix_rollback()
                $ notereason += 1
                "Потому что я не вижу здесь будущего."
                "Знаю, вам нравится этот город, хоть вы всегда ругаетесь и на него, и на свою работу."
                "Но лично я безумно устал от него."
                "Я знаю здесь уже каждую улочку, каждый поворот. Еще немного, и я буду знать всех голубей поименно."
                "Мне ужасно скучно здесь. Это не то место, где я хотел бы жить."
                "Поэтому я решил, что мне лучше уехать отсюда."
            "Вы давите на меня":
                $ renpy.fix_rollback()
                $ notereason -= 1
                "Потому что я хочу жить так, как я хочу, а не так, как хотите вы."
                "Вы никогда не давали мне той свободы, которой я так хочу."
                "Вы всегда все знали лучше. {w}В какую секцию идти, с кем дружить, куда поступать…"
                "Тогда как мои желания вечно полностью игнорировались."
                "Но это моя жизнь, и я хочу решать, куда я хочу поступать, кем я хочу работать и где я хочу жить."
                "Так что мне надоело. Я хочу жить так, как я хочу! Я хочу самостоятельности, я уже не ребенок!"
                "Вот почему я решил уехать отсюда."
            "Я хочу большего":
                $ renpy.fix_rollback()
                "Потому что я хочу большего, чем этот город может предложить."
                "Серьезно, я не хочу жить в городе, где ремонт старой остановки считается великим событием."
                "Это замечательно, что у вас здесь и работа, и дом, и все на свете, это круто."
                "Но мне нужно больше. Я хочу жить в интересном и большом городе, хочу путешествовать, хочу жить полной жизнью!"
                "А все, чего я хотел бы добиться, здесь попросту невозможно."
                "Так что я принял решение уехать отсюда."

        #завершение выбора причины (прощальная записка)

        "Я ничего не сказал вам, потому что знал, как вы отреагируете."
        "Так что не ищите меня…"
        menu:
            "Все равно не найдете":
                $ notefind -= 1
                $ renpy.fix_rollback()
                "Все равно не найдете, как ни старайтесь."
                "Я уже взрослый, мне не нужна нянька, я сам могу о себе позаботиться."
            "У меня все контролем":
                $ renpy.fix_rollback()
                "Я позвоню сам, как поступлю в вуз, и все немного устаканится."
                "Не волнуйтесь, у  меня все под контролем. Мне есть, на что есть, где остановиться, я не буду бомжевать на улице."
            "Позвоню, как доберусь":
                $ notefind += 1
                $ renpy.fix_rollback()
                "Я позвоню, как доберусь, вы, наверное, к тому времени уже все узнаете. Надеюсь, не будете сильно сердиться…"
                "Если что, мы договорились у знакомого, что я пока поживу у него. Потом поступлю и буду жить в общежитии."
        "Ну что ж, на этом, пожалуй, все…"
        menu:
            "Я люблю вас, простите меня":
                $ notesign -= 1
                $ renpy.fix_rollback()
                "Простите, что не сказал вам сразу. Я просто не мог."
                "Я люблю вас, очень сильно, и уже скучаю."
            "Забудьте обо мне":
                $ renpy.fix_rollback()
                "Так что забудьте обо мне и моем существовании."
                "А лучше вычеркните меня из своей жизни, как будто меня и не было."
            "Не волнуйтесь, я не пропаду":
                $ notesign += 1
                $ renpy.fix_rollback()
                "Не переживайте за меня, особенно ты, мам."
                "Со мной все будет хорошо, я не пропаду."
        "Ваш сын, {w}[name]."
        scene room_m with dissolve
        "Я пробежался по ней глазами и положил на стол на видное место."
        "Кажется, на этом все. Теперь пора ехать."
        "Я взял сумку, высунулся в коридор, убедился, что никого нет, и как можно тише вышел из дома."
        #локация: утренний город 1
        scene city_mor with dissolve
        stop music
        play music "audio/Senaru.mp3"
        "Утренний город встретил меня безлюдными улицами и прохладным свежим ветром."
        "Я неосознанно замедлил шаг, делая глубокий-глубокий вдох."
        "Ну вот и все. Вот он. {w}Последние часы в родном городе."
        "Я не мог понять, жалею я или нет… Какое-то странное чувство поселилось в груди и слабо ныло под ребрами."
        "Я не знал, что с ним делать. Пройдет оно или останется у меня насовсем."
        "Но, может, это было и не так важно…"
        scene city_mor2 with dissolve
        if sara > 0:
            "Пока что я шел по знакомым с детства улицам, повернув к дому Сары."
            #локация: дом сары
            "Она ждала меня, как знала. Как только я подошел к двери, как она распахнула ее, выбежав и обняв меня за шею."
            "Я успел только заметить, что она босиком, и шагнул в прихожую, чтобы не простудилась."
            "Какое-то время мы молча стояли, обнимая друг друга и думая каждый о своем."
            "Отстранились, обменялись улыбками. {w}Почему-то в этой утренней полудреме не нужны были слова."
            "Она поцеловала меня в щеку на прощание, я сжал ее руку и слабо кивнул в ответ."
            "А затем повернулся спиной и пошел в сторону автобусной остановки."
        else:
            "Бросив взгляд в сторону улицы, на которой жила Сара, я пошел в сторону автобусной остановки."
        #локация: автобус
        "В такой ранний час в автобусе была разве что пара человек, не больше."
        "Я занял место рядом с окном и наблюдал, как мимо проносятся дома, деревья, редкие и еще сонные прохожие."
        "Город словно просыпался от долгого сна."
        "Скоро улицы наводнятся людьми и машинами, зашумят слуху привычными звуками, и все будет как обычно."
        "Только меня уже здесь не будет."
        "Я уезжаю. Прямо сейчас. {w}Одна эта мысль вызывала улыбку."
        "Меня здесь больше не будет, а люди остаются. Остаются родители, остаются учителя, одноклассники, Сара…"
        "И Моника тоже остается."
        "В груди снова слегка защемило. Я снова глубоко вздохнул и откинулся на сидение."
        "Дорога предстояла долгая…"
        scene end with dissolve
        window hide(None)
        $ renpy.pause (5)
        return

label epilog_mon:
    scene black with dissolve
    stop music
    play music "audio/Eternal_Anamnesis.mp3"
    "Ближе к вечеру я был уже на месте."
    "Все было хорошо: меня встретил знакомый, как и договаривались, мы поехали к нему, оставили вещи…"
    "…И почти всю ночь гуляли по городу."
    "Он выделил мне отдельную комнату, где я и обустроился на первое время. Все было хорошо."
    "А потом начались проблемы."
    "Накопленных денег хватило ненадолго, а работу найти почему-то никак не получалось."
    "Я утешал себя мыслью, что не может же мне так капитально не везти…"
    "…Когда внезапно знакомый сообщил, что к нему приезжает его девушка из другого города."
    "И мне нужно освободить комнату в ближайшие сроки."
    "Я был в ужасе. {w}Нет, я был просто в панике."
    "Тех подработок, что я находил, хватало только на еду, а никак не на съем квартиры."
    if sPhotoOld == True:
        "С горя я даже купил пару лотерейных билетов, не особо надеясь на удачу, {w}но все без толку."
        "Однако когда я уже совсем отчаялся, знакомый, глядя на мои страдания, сказал, что у него есть предложение."
        "Он рассказал, что у него не так давно умерла бабушка, оставив ему в наследство квартиру на окраине города."
        "Квартира была в ужасном состоянии и отчаянно требовала ремонта."
        "Знакомому же было совершенно не до этого, ему эта квартира вообще не сдалась."
        "И раз такая тупиковая ситуация, он предложил мне пожить на той квартире при условии, что приведу ее в порядок."
        "Разумеется, я согласился. И разумеется, квартира и правда была совершенно убитая."
        "И да, отсюда до центра города добираться было не меньше часа, но кого это волновало?"
        "У меня была квартира! Мне было, где жить!"
        "Я даже мог бы не заселяться в общагу, если подумать…"
    elif earrings == True:
        "С горя я даже купил пару лотерейных билетов, не особо надеясь на удачу, {w}но все без толку."
        "Зачем вообще этот лохотрон продают…"
        "В конце концов, поняв, что иного выхода просто нет, я с тяжестью на сердце продал серьги Моники."
        "На эти деньги удалось снять крохотную комнатку на пару месяцев – как раз до начала учебного года."
        "Я невероятно надеялся, что поступлю хоть куда-нибудь."
    elif sMascot == True:
        "С горя я даже купил пару лотерейных билетов, не особо надеясь на удачу."
        "И не поверил своим глазам, когда один из них оказался выигрышным."
        "Это было поразительно. Талисман Сары и правда работал!"
        "Полученная сумма, конечно, была меньше той, что обещалось в билете,"
        "однако даже ее хватило на то, чтобы переехать в маленькую и уютную студию."
        "И даже, наверное, мне не стоило беспокоиться об общаге."
    else:
        "С горя я даже купил пару лотерейных билетов, не особо надеясь на удачу, {w} но все без толку."
        "В конце концов я честно сказал знакомому, что мне некуда идти. Разве что на улицу."
        "Знакомый примерно догадывался о том, что так и произойдет, так что даже не ругался."
        "Но предупредил, что как только я поступлю, то должен съехать как можно быстрее."
        "Видите ли, у его девушки очень крутой характер."
        "Если честно, я был так рад, что он не выгоняет меня на улицу, что я был готов жить даже с медведицей."
        "Впрочем, примерно так и оказалось…"
        "Его девушка оказалась просто невыносимой. Уже через три дня я думал, что жить на улице не так-то уж и плохо."
        "Мало того, что она меня невзлюбила, наверное, еще до своего приезда, и всячески мне пакостила,"
        "так еще и знакомый постоянно искал с ней уединения, в итоге я приходил домой разве что ночевать."
        "И, пожалуй, никогда в жизни еще я так не хотел поступить в институт."
    "Кстати, об этом. Документы я подавал сразу в три института, чтобы наверняка."
    "Пролететь с этим ну очень не хотелось."
    if sPhoto == True:
        "И каково же было мое изумление, когда меня вдруг зачислили в престижный вуз, куда я вообще наудачу отправлял документы."
        "Это было так круто… Нет, это было потрясающе!"
    elif sPhoto == False:
        "Конечно, в самый крутой вуз в городе я не попал, глупо было даже рассчитывать на такое."
        "Но зато поступил туда, куда, собственно, и ожидал."
    elif sMascot == True:
        "Ничего, зато от моей студии можно было пешком дойти, можно экономить на проезде."
        "Тоже хорошо, не поспоришь же."
    elif sPhotoOld == True:
        "Из квартиры бабушки знакомого, правда, добираться было сложновато."
        "Но зато я жил один, а не в вонючем общежитии."
        "Ладно, на самом деле квартира бабушки тоже не розами пахла, хотя я неделю ее отмывал после переезда."
        "Но это все-таки… было немного другое."
    else:
        "Опять же, как и хотел, почти сразу заселился в общежитие, нашел новых знакомых, хороших и не очень…"
    if saimon > 8:
        "С Саймоном, кстати, я виделся всего пару раз, не более."
        "Так, чисто обменялись новостями да посидели кофе попили."
    else:
        "Саймона, кстати, я больше так и не видел."
    if sara > -1:
        "Зато продолжал общаться с Моникой и Сарой."
    else:
        "Зато очень активно общался с Моникой."
    "Мы постоянно созванивались друг с другом, обменивались новостями."
    "Я надеялся, что однажды смогу приехать в гости. К примеру, на Новый год."
    if notefind == -1:
        "Только вот с родителями мы так и не помирились."
        "Я узнавал про них через знакомых, знал только, что мама ужасно переживает."
        "Но общаться мы не общались."
        "Впрочем, и без этого вся затея с поездкой была под большим вопросом."
    elif notefind == 0:
        "Что касается родителей, с ними мы были в неплохих отношениях."
        "Тоже созванивались, общались… правда, редко, где-то раз в месяц."
        "Да и общались – это громко сказано. Разговоры получались скомканными, короткими и неловкими."
    elif notefind == 1:
        "Что касается родителей, с ними мы были в замечательных отношениях."
        "Мама так волновалась первый месяц, что звонила почти каждый день."
        "Потом, правда, наше общение сократилось до нескольких разговоров в неделю,"
        "но я все равно был рад, что мы все время на связи."
    if notereason == 1:
        "Деньгами они мне не помогали, но я бы и сам не взял. {w}Из гордости."
        "Я ведь уже говорил, что всего хочу добиться сам, своими силами."
        "И я сделаю так, чтобы они могли мной гордиться."
    elif notereason == 0:
        "Деньгами, кстати, они иногда помогали, но я старался не злоупотреблять этим."
        "Все-таки уже не маленький."
    elif notereason == -1:
        "Деньгами они мне, кстати, ни разу не помогли."
        "Ну а что, хотел самостоятельности? Вот тебе и самостоятельность."
        "Но ладно, зато мы хотя бы общались."
    if notesign == -1:
        "С отцом, правда, мы так и не помирились. {w}Он меня так и не простил."
        "Возможно, с поездкой на праздники придется повременить…"
        "Хотя она и так была под большим вопросом."
    else:
        "Отец, правда, не сразу смог меня простить за побег и за то, что я ничего им не сказал."
        "Сначала вообще не хотел со мной разговаривать даже."
        "Но после моего поступления наши отношения с ним начали потихоньку налаживаться."
        "Может, если я приеду на праздники, все станет совсем хорошо…"
        "Хотя, если честно, вся эта затея с поездкой была под большим вопросом."
    if sMascot == True:
        "Ведь я даже летом так и не смог найти постоянную работу, перебивался подработками."
        "А лотерейные деньги надо тратить с умом, а не разбрасываться ими направо и налево."
    else:
        "Ведь я даже летом так и не смог найти постоянную работу, а подработок отчаянно не хватало."
    "Так что параллельно со своим первым учебным месяцев я активно старался заработать везде, где только можно."
    "Вот только сложно найти хоть какую-то работу, днями пропадая на учебе…"
    if sBracelet == True:
        "Однако в конце октября удача неожиданно улыбнулась мне. {w}Даже не так – обняла меня!"
        "Началось с того, что мне позвонила Сара."
        "Ее дальняя родственница, оказывается, работала в крупной фирме и искала на удаленную работу кого-то смышленого."
        "И я как раз подходил по навыкам!"
        "Сара обещала с ней поговорить, и мне даже назначили собеседование."
        "Я ужасно волновался, даже спать накануне не мог. У меня ведь не было образования, я только начал учиться."
        "Она, как оказалось, знала про мою ситуацию, зато не знала, что со мной делать."
        "Ведь она обещала Саре помочь мне."
        "Я сказал ей, что я все понимаю, и было бы глупо брать на такую работу сотрудника без опыта."
        "На что она ответила, что она не поэтому так сомневается, а потому что я великолепно справился с тестовым заданием."
        "В итоге, поскольку я еще учусь, она взяла меня на первое время помощником одного из программистов."
        "Чтобы набирался опыта, да и по времени я бы не успел больше, даже при учете разницы в часовых поясах."
        "Но зато она в шутку сказала, что если я буду стараться, то меня ждет отличная карьера!"
        "Сказать, что я был в шоке, это ничего не сказать. {w}Я был на седьмом небе!"
        "Правда, теперь я спал так мало, что в моих мешках под глазами можно было носить продукты из магазина…"
    else:
        "В итоге я так и бегал по подработкам, свято веря, что вот когда я закончу вуз, все станет совсем по-другому!.."
        "Только бы доучиться и не сойти с ума в процессе…"
    "Но как бы то ни было, я был счастлив."
    "И нисколько не жалел о том, как все получилось."
    stop music
    play music "audio/determination.mp3"
    scene end with dissolve
    window hide(None)
    $ renpy.pause (5)



































