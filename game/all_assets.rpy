############## Defaults ######################

init python:
    # инициализация постоянных данных при первом запуске 
    if persistent.ends is None:
        persistent.ends = []
    # функция. запоминаем, что мы прошли концовку, вносим в список, если ее там не было.
    def end(name):
        if not name in persistent.ends:
            persistent.ends.append(name)
            
 ###### Для секрет концовки:
            ##if len(persistent.ends) >= колво рутов:
           ## jump secret  

          ## после каждой концовки добавлять $ end(1) 

default basedir = user_dir
default persistent.playthrough = 0
default persistent.anticheat = 0
default anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.playername = ""
default player = persistent.playername
default quick_end = False

## Таймер ##
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # Устанавливает постепенное появление и исчезновение бара и требуется только один раз в скрипте

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # Это  вертикальная черта таймера.
    
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
    
    
## Глитч эффект    
    
init python:

    from random import Random
    from __builtin__ import map as fixMap

    class Glitch(renpy.Displayable, Random, NoRollback):

        def __init__(self, pic, speed_multipler=.5):
            super(Glitch, self).__init__()
            self.pic = renpy.easy.displayable(pic)
            self.cached_pics = []
            self.speed_multipler = float(speed_multipler)

        def visit(self):
            return [i[0] for i in self.cached_pics] + [self.pic]

        def create_cache(self):
            self.cached_pics = [self.get_random_recolor() for i in xrange(500)]

        def get_random_crop(self):
            width, height = fixMap(
                lambda x: self.rndInt((self.random() * x * .1)),
                self.base_size
            )
            width *= 10
            x, y = fixMap(
                lambda x: self.rndInt(self.uniform(.0, (x[1] - x[0]))),
                zip((width, height), self.base_size)
            )
            return (
                LiveCrop((x, y, width, height), self.pic),
                (x, y),
                (width, height)
            )

        def get_random_recolor(self):
            crop, pos, size = self.get_random_crop()
            return (
                Transform(
                    LiveComposite(
                        size,
                        (0, 0),
                        crop,
                        (0, 0),
                        AlphaMask(
                            Solid(
                                tuple(self.randint(0, 200) for i in xrange(4))
                            ),
                            crop
                        )
                    ),
                    xzoom=self.uniform(1., 1.5),
                    yzoom=self.uniform(.5, 1.),
                ),
                pos,
                size
            )

        @staticmethod
        def rndInt(val):
            return int(round(float(val)))

        def render(self, width, height, st, at):

            pic_rend = renpy.render(self.pic, width, height, st, at)
            w, h = self.base_size = fixMap(self.rndInt, pic_rend.get_size())
            if not self.cached_pics:
                self.create_cache()
            renderObj = renpy.Render(w, h)
            if self.randint(0, 9):
                renderObj.blit(pic_rend, (0, 0))
            for i in xrange(self.randint(0, 50)):
                pic, pos, old_size = self.choice(self.cached_pics)
                oldX, oldY = old_size
                surface = renpy.render(pic, width, height, st, at)
                sizeX, sizeY = surface.get_size()
                x, y = pos
                x -= (float((sizeX - oldX)) / 2.)
                y -= (float((sizeY - oldY)) / 2.)
                x += (sizeX * self.uniform(-.2, .2))
                renderObj.blit(
                    renpy.render(pic, width, height, st, at),
                    tuple(fixMap(self.rndInt, (x, y)))
                )
            renpy.redraw(self, (self.random() * self.speed_multipler))
            return renderObj

## Выявление имени компьютера

init python:
    import os
    player = os.environ.get('USERNAME',
        os.environ.get('USER',
        os.environ.get('LNAME',
        os.environ.get('LOGNAME','Player'))))

## Взаимодействия с папкой Characters
    
python early:        
    if renpy.android:
        user_dir = os.environ["ANDROID_PUBLIC"]
    else:
        user_dir = config.basedir
    if not os.path.exists(user_dir + "/characters/"):
        try: 
            os.mkdir(user_dir + "/characters/")
        except: 
             pass
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        import os
        try: 
            os.remove(user_dir + "/characters/" + name + ".chr")
        except:
            pass
    def restore_all_characters():
        try:
            open(user_dir + "/characters/sara.chr", "rb")
        except: 
            open(user_dir + "/characters/sara.chr", "wb").write(renpy.file("sara.chr").read())
        try:
            open(user_dir + "/characters/alan.chr", "rb")
        except: 
            open(user_dir + "/characters/alan.chr", "wb").write(renpy.file("alan.chr").read())
        try:
            open(user_dir + "/characters/saimon.chr", "rb")
        except: 
            open(user_dir + "/characters/saimon.chr", "wb").write(renpy.file("saimon.chr").read())
        try:
            open(user_dir + "/characters/monika.chr", "rb")
        except:
            open(user_dir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())

## Стили шрифта

init -1 python:
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    config.automatic_images_minimum_components = 1
    config.automatic_images = [' ', '_', '/']
    config.automatic_images_strip = ['images']
    style.default.font = "fonts/laCartoonerie.ttf"
    style.default.size = 22


init python:
    def unarchive(original_filename, new_filename):
        import os
        import os.path
        
        new_filename = config.basedir + "/" + new_filename
        dirname = os.path.dirname(new_filename)
        
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        
        orig = renpy.file(original_filename)
        new = file(new_filename, "wb")
        
        new.write(orig.read())
        
        new.close()
        orig.close()

define persistent.trans_ending = True
default persistent.clearall = None
    


################## Characters ####################

init:
     define al = Character("Алан", color="#c0c0c0")
     define sar = Character("Сара", color="#ffc0cb")
     define sai = Character("Саймон", color="#ad661f")
     define mon = Character("Моника", color="#faf87d")
     define me = Character("[name]", color="#ffffff")
     define bul = Character("Разработчик", color="#7d72c2")
     define tch = Character("Миссис Сантана", color="#9d81ba")
     define mom = Character("Мама", color="#9d81ba")
     define rb = Character("Ребекка", color="#9e6b54")

            
############## ПЕРЕМЕННЫЕ ###############

init:
    $ sara = 0
    $ alan = 0
    $ saimon = 0
    $ monika = 0
    $ alone = 0 
    $ secret = 0
    $ timer_range = 0
    $ timer_jump = 0
    
############## BackGrounds ###################
init:

    image sch_m ="images/bg/school_morning.jpg"
    image sch_a ="images/bg/school_afternoon.jpg"
    image sch_n ="images/bg/school_night.jpg"
    image class_m ="images/bg/school_class_m.jpg"
    image class_a ="images/bg/school_class_a.jpg"
    image class_n ="images/bg/school_class_n.jpg"
    image stairs ="images/bg/school_stairs.jpg"
    image hall_lo ="images/bg/hallway_lighton.jpg"
    image hall_m ="images/bg/hallway_m.jpg"
    image hall_n ="images/bg/hallway_n.jpg"
    image hall_a ="images/bg/hallway_a.jpg"
    image teachers_a ="images/bg/teachers_a.jpg"
    image teachers_m ="images/bg/teachers_m.jpg"
    image teachers_n ="images/bg/teachers_n.jpg"
    image cafe_m ="images/bg/cafe_m.jpg"
    image smotr ="images/bg/smotrovaya.jpg"
    image town_n ="images/bg/nighttown.jpg"
    image street_sum ="images/bg/summer_street.jpg"
    image mon_house ="images/bg/monika_house.jpg"
    image mon_kit ="images/bg/monika_kitchen.jpg"
    image mon_kiton ="images/bg/monika_kitchen_on.jpg"
    image mon_bath ="images/bg/monika_bathroom.jpg"
    image mon_hall ="images/bg/monika_hall.jpg"
    image sportzal ="images/bg/sportzal.jpg"
    image true_end ="images/bg/monika_bg_glitch.png"
    image stolovaya ="images/bg/dining_hall.jpg"
    image busstop ="images/bg/busstop.jpg"
    image bus ="images/bg/int_bus.jpg"
    image secr_m ="images/secret_place_m2.jpg"
    image secr_a ="images/secret_place_a2.jpg"
    image secr ="images/secret_place1.jpg"
    image tropa ="images/bg/tropa.jpg"
    image room_m ="images/bg/room_m.jpg"
    image room_on ="images/bg/room_on.jpg"
    image room_n ="images/bg/room_n.jpg"
    image kino ="images/bg/kino.jpg"
    image park ="images/bg/park.jpg"
    image park_n ="images/bg/park_n.jpg"



    image tos ="images/menu/tos.jpg"
    
    
    
    image black = "#000000"
    image dark = "#000000e4"
    image darkred = "#110000c8"
    image white = "#ffffff"
    image end:
        truecenter
        "gui/end.png"
    image poem_end:
        truecenter
        "images/menu/poem.jpg"

   
################ Sprites #####################

    image a000 ="images/alan/alan000.png"
    image a001 ="images/alan/alan001.png"
    image a002 ="images/alan/alan002.png"    #Алан
    image a003 ="images/alan/alan003.png"
    image a004 ="images/alan/alan004.png"
    image a005 ="images/alan/alan005.png"
    image a006 ="images/alan/alan006.png"
    image a007 ="images/alan/alan007.png"
    image a008 ="images/alan/alan008.png"
    image a009 ="images/alan/alan009.png"
    image a010 ="images/alan/alan010.png"
    image a011 ="images/alan/alan011.png"
    image a012 ="images/alan/alan012.png"
    image a013 ="images/alan/alan013.png"
    image a014 ="images/alan/alan014.png"
    image a015 ="images/alan/alan015.png"
    image a100 ="images/alan/alan100.png"
    image a101 ="images/alan/alan101.png"
    image a103 ="images/alan/alan103.png"
    image a104 ="images/alan/alan104.png"
    image a105 ="images/alan/alan105.png"
    image a106 ="images/alan/alan106.png"
    image a107 ="images/alan/alan107.png"
    image a108 ="images/alan/alan108.png"
    image a109 ="images/alan/alan109.png"
    image a110 ="images/alan/alan110.png"
    image a111 ="images/alan/alan111.png"
    image a112 ="images/alan/alan112.png"
    image a113 ="images/alan/alan113.png"
    image a114 ="images/alan/alan114.png"
    image a115 ="images/alan/alan115.png"
    image a200="images/alan/alan200.png"
    image a201="images/alan/alan201.png"
    image a202="images/alan/alan202.png"
    image a203="images/alan/alan203.png"
    image a204="images/alan/alan204.png"
    image a205="images/alan/alan205.png"
    image a206="images/alan/alan206.png"
    image a207="images/alan/alan207.png"
    image a208="images/alan/alan208.png"
    image a209="images/alan/alan209.png"
    image a210="images/alan/alan210.png"
    image a211="images/alan/alan211.png"
    image a212="images/alan/alan212.png"
    image a213="images/alan/alan213.png"
    image a214="images/alan/alan214.png"
    image a215="images/alan/alan215.png"
    image a216="images/alan/alan216.png"
    image a217="images/alan/alan217.png"
    image a218="images/alan/alan218.png"
    image a219="images/alan/alan219.png"
    image a220="images/alan/alan220.png"
    image a221="images/alan/alan221.png"
    image a222="images/alan/alan222.png"
    image a223="images/alan/alan223.png"
    image a224="images/alan/alan224.png"
    image a225="images/alan/alan225.png"
    image a226="images/alan/alan226.png"
    image a227="images/alan/alan227.png"
    image a228="images/alan/alan228.png"
    image a229="images/alan/alan229.png"
    image a400="images/alan/alan400.png"
    image a401="images/alan/alan401.png"
    image a402="images/alan/alan402.png"
    image a403="images/alan/alan403.png"
    image a404="images/alan/alan404.png"
    image a405="images/alan/alan405.png"
    image a406="images/alan/alan406.png"
    image a407="images/alan/alan407.png"
    image a408="images/alan/alan408.png"
    image a409="images/alan/alan409.png"
    image a410="images/alan/alan410.png"
    image a411="images/alan/alan411.png"
    image a412="images/alan/alan412.png"
    image a413="images/alan/alan413.png"
    image a414="images/alan/alan414.png"
    image a415="images/alan/alan415.png"
    image a416="images/alan/alan416.png"
    image a417="images/alan/alan417.png"
    image a418="images/alan/alan418.png"
    image a419="images/alan/alan419.png"
    image a420="images/alan/alan420.png"
    image a421="images/alan/alan421.png"
    image a422="images/alan/alan422.png"
    image a423="images/alan/alan423.png"
    image a424="images/alan/alan424.png"
    image a425="images/alan/alan425.png"
    image a426="images/alan/alan426.png"
    image a427="images/alan/alan427.png"
    image a428="images/alan/alan428.png"
    image a429="images/alan/alan429.png"
    image a430="images/alan/alan430.png"
    image a431="images/alan/alan431.png"
    image a432="images/alan/alan432.png"
    image a433="images/alan/alan433.png"

    image s000 ="images/sara/sara000.png"   #Сара
    image s001 ="images/sara/sara001.png"
    image s002 ="images/sara/sara002.png"
    image s003 ="images/sara/sara003.png"
    image s004 ="images/sara/sara004.png"
    image s005 ="images/sara/sara005.png"
    image s006 ="images/sara/sara006.png"
    image s007 ="images/sara/sara007.png"
    image s008 ="images/sara/sara008.png"
    image s009 ="images/sara/sara009.png"
    image s010 ="images/sara/sara010.png"
    image s011 ="images/sara/sara011.png"
    image s012 ="images/sara/sara012.png"
    image s013 ="images/sara/sara013.png"
    image s014 ="images/sara/sara014.png"
    image s015 ="images/sara/sara015.png"
    image s016 ="images/sara/sara016.png"
    image s017 ="images/sara/sara017.png"
    image s018 ="images/sara/sara018.png"
    image s019 ="images/sara/sara019.png"
    image s020 ="images/sara/sara020.png"
    image s021 ="images/sara/sara021.png"
    image s022 ="images/sara/sara022.png"
    image s023 ="images/sara/sara023.png"
    image s024 ="images/sara/sara024.png"
    image s025 ="images/sara/sara025.png"
    image s026 ="images/sara/sara026.png"
    image s027 ="images/sara/sara027.png"
    image s028="images/sara/sara028.png"
    image s029="images/sara/sara029.png"
    image s030="images/sara/sara030.png"
    image s031="images/sara/sara031.png"
    image s032="images/sara/sara032.png"
    image s033="images/sara/sara033.png"
    image s034="images/sara/sara034.png"
    image s035="images/sara/sara035.png"
    image s036="images/sara/sara036.png"
    image s037="images/sara/sara037.png"
    image s038="images/sara/sara038.png"
    image s039="images/sara/sara039.png"
    image s040="images/sara/sara040.png"
    image s041="images/sara/sara041.png"
    image s042="images/sara/sara042.png"
    image s043="images/sara/sara043.png"
    image s044="images/sara/sara044.png"
    image s045="images/sara/sara045.png"
    image s046="images/sara/sara046.png"
    image s047="images/sara/sara047.png"
    image s048="images/sara/sara048.png"
    image s049="images/sara/sara049.png"
    image s050="images/sara/sara050.png"
    image s051="images/sara/sara051.png"
    image s052="images/sara/sara052.png"
    image s053="images/sara/sara053.png"
    image s054="images/sara/sara054.png"
    image s055="images/sara/sara055.png"
    image s056="images/sara/sara056.png"
    image s056="images/sara/sara056.png"
    image s057="images/sara/sara057.png"
    image s058="images/sara/sara058.png"
    image s059="images/sara/sara059.png"
    image s060="images/sara/sara060.png"
    image s061="images/sara/sara061.png"
    image s062="images/sara/sara062.png"
    image s063="images/sara/sara063.png"
    image s064="images/sara/sara064.png"
    image s065="images/sara/sara065.png"
    image s066="images/sara/sara066.png"
    image s067="images/sara/sara067.png"
    image s068="images/sara/sara068.png"
    image s069="images/sara/sara069.png"
    image s070="images/sara/sara070.png"
    image s071="images/sara/sara071.png"
    image s072="images/sara/sara072.png"
    image s100 ="images/sara/sara100.png"
    image s101 ="images/sara/sara101.png"
    image s102 ="images/sara/sara102.png"
    image s103 ="images/sara/sara103.png"
    image s104 ="images/sara/sara104.png"
    image s105 ="images/sara/sara105.png"
    image s106 ="images/sara/sara106.png"
    image s107 ="images/sara/sara107.png"
    image s108 ="images/sara/sara108.png"
    image s109 ="images/sara/sara109.png"
    image s110 ="images/sara/sara110.png"
    image s111 ="images/sara/sara111.png"
    image s112 ="images/sara/sara112.png"
    image s113 ="images/sara/sara113.png"
    image s114 ="images/sara/sara114.png"
    image s115 ="images/sara/sara115.png"
    image s116 ="images/sara/sara116.png"
    image s117 ="images/sara/sara117.png"
    image s118 ="images/sara/sara118.png"
    image s119 ="images/sara/sara119.png"
    image s120 ="images/sara/sara120.png"
    image s121 ="images/sara/sara121.png"
    image s122 ="images/sara/sara122.png"
    image s123 ="images/sara/sara123.png"
    image s124 ="images/sara/sara124.png"
    image s125 ="images/sara/sara125.png"
    image s126 ="images/sara/sara126.png"
    image s127 ="images/sara/sara127.png"

    image m000="images/monika/mon000.png"
    image m001="images/monika/mon001.png"
    image m002="images/monika/mon002.png"   # Моника
    image m003="images/monika/mon003.png"
    image m004="images/monika/mon004.png"
    image m005="images/monika/mon005.png"
    image m006="images/monika/mon006.png"
    image m007="images/monika/mon007.png"
    image m008="images/monika/mon008.png"
    image m009="images/monika/mon009.png"
    image m010="images/monika/mon010.png"
    image m011="images/monika/mon011.png"
    image m012="images/monika/mon012.png"
    image m013="images/monika/mon013.png"
    image m014="images/monika/mon014.png"
    image m015="images/monika/mon015.png"
    image m016="images/monika/mon016.png"
    image m017="images/monika/mon017.png"
    image m018="images/monika/mon018.png"
    image m019="images/monika/mon019.png"
    image m020="images/monika/mon020.png"
    image m021="images/monika/mon021.png"
    image m022="images/monika/mon022.png"
    image m023="images/monika/mon023.png"
    image m024="images/monika/mon024.png"
    image m025="images/monika/mon025.png"
    image m026="images/monika/mon026.png"
    image m027="images/monika/mon027.png"
    image m028="images/monika/mon028.png"
    image m029="images/monika/mon029.png"
    image m030="images/monika/mon030.png"
    image m020="images/monika/mon020.png"
    image m021="images/monika/mon021.png"
    image m022="images/monika/mon022.png"
    image m023="images/monika/mon023.png"
    image m024="images/monika/mon024.png"
    image m025="images/monika/mon025.png"
    image m026="images/monika/mon026.png"
    image m027="images/monika/mon027.png"
    image m028="images/monika/mon028.png"
    image m029="images/monika/mon029.png"
    image m030="images/monika/mon030.png"
    image m031="images/monika/mon031.png"
    image m032="images/monika/mon032.png"
    image m033="images/monika/mon033.png"
    image m034="images/monika/mon034.png"
    image m035="images/monika/mon035.png"
    image m036="images/monika/mon036.png"
    image m037="images/monika/mon037.png"
    image m038="images/monika/mon038.png"
    image m039="images/monika/mon039.png"
    image m040="images/monika/mon040.png"
    image m041="images/monika/mon041.png"
    image m042="images/monika/mon042.png"
    image m043="images/monika/mon043.png"
    image m044="images/monika/mon044.png"
    image m045="images/monika/mon045.png"
    image m046="images/monika/mon046.png"
    image m047="images/monika/mon047.png"
    image m048="images/monika/mon048.png"
    image m049="images/monika/mon049.png"
    image m050="images/monika/mon050.png"
    image m051="images/monika/mon051.png"
    image m052="images/monika/mon052.png"
    image m053="images/monika/mon053.png"
    image m054="images/monika/mon054.png"
    image m055="images/monika/mon055.png"
    image m056="images/monika/mon056.png"
    image m057="images/monika/mon057.png"
    image m058="images/monika/mon058.png"
    image m100="images/monika/mon100.png"
    image m101="images/monika/mon101.png"
    image m102="images/monika/mon102.png"
    image m103="images/monika/mon103.png"
    image m104="images/monika/mon104.png"
    image m105="images/monika/mon105.png"
    image m106="images/monika/mon106.png"
    image m107="images/monika/mon107.png"
    image m108="images/monika/mon108.png"
    image m109="images/monika/mon109.png"
    image m110="images/monika/mon110.png"
    image m111="images/monika/mon111.png"
    image m112="images/monika/mon112.png"
    image m113="images/monika/mon113.png"
    image m114="images/monika/mon114.png"
    image m115="images/monika/mon115.png"
    image m116="images/monika/mon116.png"
    image m117="images/monika/mon117.png"
    image m118="images/monika/mon118.png"
    image m119="images/monika/mon119.png"
    image m120="images/monika/mon120.png"
    image m200="images/monika/mon200.png"
    image m201="images/monika/mon201.png"
    image m202="images/monika/mon202.png"
    image m203="images/monika/mon203.png"
    image m204="images/monika/mon204.png"
    image m205="images/monika/mon205.png"
    image m206="images/monika/mon206.png"
    image m207="images/monika/mon207.png"
    image m208="images/monika/mon208.png"
    image m209="images/monika/mon209.png"
    image m210="images/monika/mon210.png"
    image m211="images/monika/mon211.png"
    image m212="images/monika/mon212.png"
    image m213="images/monika/mon213.png"
    image m214="images/monika/mon214.png"
    image m215="images/monika/mon215.png"
    image m216="images/monika/mon216.png"
    image m217="images/monika/mon217.png"
    image m218="images/monika/mon218.png"
    image m219="images/monika/mon219.png"
    image m220="images/monika/mon220.png"
    image m221="images/monika/mon221.png"
    image m222="images/monika/mon222.png"
    image m223="images/monika/mon223.png"
    image m224="images/monika/mon224.png"
    image m225="images/monika/mon225.png"
    image m226="images/monika/mon226.png"
    image m227="images/monika/mon227.png"
    image m228="images/monika/mon228.png"
    image m229="images/monika/mon229.png"
    image m220="images/monika/mon220.png"
    image m221="images/monika/mon221.png"
    image m222="images/monika/mon222.png"
    image m223="images/monika/mon223.png"
    image m200="images/monika/mon200.png"
    image m201="images/monika/mon201.png"
    image m202="images/monika/mon202.png"
    image m203="images/monika/mon203.png"
    image m204="images/monika/mon204.png"
    image m205="images/monika/mon205.png"
    image m206="images/monika/mon206.png"
    image m207="images/monika/mon207.png"
    image m208="images/monika/mon208.png"
    image m209="images/monika/mon209.png"
    image m210="images/monika/mon210.png"
    image m211="images/monika/mon211.png"
    image m212="images/monika/mon212.png"
    image m213="images/monika/mon213.png"
    image m214="images/monika/mon214.png"
    image m215="images/monika/mon215.png"
    image m216="images/monika/mon216.png"
    image m217="images/monika/mon217.png"
    image m218="images/monika/mon218.png"
    image m219="images/monika/mon219.png"
    image m220="images/monika/mon220.png"
    image m221="images/monika/mon221.png"
    image m222="images/monika/mon222.png"
    image m223="images/monika/mon223.png"
    image m224="images/monika/mon224.png"
    image m225="images/monika/mon225.png"
    image m226="images/monika/mon226.png"
    image m227="images/monika/mon227.png"
    image m228="images/monika/mon228.png"
    image m229="images/monika/mon229.png"
    image m230="images/monika/mon230.png"
    image m231="images/monika/mon231.png"
    image m232="images/monika/mon232.png"
    image m233="images/monika/mon233.png"
    image m234="images/monika/mon234.png"
    image m235="images/monika/mon235.png"
    image m236="images/monika/mon236.png"
    image m237="images/monika/mon237.png"
    image m238="images/monika/mon238.png"
    image m239="images/monika/mon239.png"
    image m240="images/monika/mon240.png"
    image m241="images/monika/mon241.png"
    image m242="images/monika/mon242.png"
    image m243="images/monika/mon243.png"
    image m244="images/monika/mon244.png"
    image m245="images/monika/mon245.png"
    image m246="images/monika/mon246.png"
    image m247="images/monika/mon247.png"
    image m248="images/monika/mon248.png"
    image m249="images/monika/mon249.png"
    image m250="images/monika/mon250.png"
    image m251="images/monika/mon251.png"
    image m252="images/monika/mon252.png"
    image m253="images/monika/mon253.png"
    image m254="images/monika/mon254.png"
    image m255="images/monika/mon255.png"

    image sa000="images/saimon/sai000.png"   # Саймон
    image sa001="images/saimon/sai001.png"
    image sa002="images/saimon/sai002.png"
    image sa003="images/saimon/sai003.png"
    image sa004="images/saimon/sai004.png"
    image sa005="images/saimon/sai005.png"
    image sa006="images/saimon/sai006.png"
    image sa007="images/saimon/sai007.png"
    image sa008="images/saimon/sai008.png"
    image sa009="images/saimon/sai009.png"
    image sa010="images/saimon/sai010.png"
    image sa011="images/saimon/sai011.png"
    image sa012="images/saimon/sai012.png"
    image sa013="images/saimon/sai013.png"
    image sa014="images/saimon/sai014.png"
    image sa015="images/saimon/sai015.png"
    image sa016="images/saimon/sai016.png"

    image tch000="images/teacher/tch000.png"   # Учительница
    image tch001="images/teacher/tch001.png"
    image tch002="images/teacher/tch002.png"
    image tch003="images/teacher/tch003.png"
    image tch004="images/teacher/tch004.png"
    image tch005="images/teacher/tch005.png"
    image tch006="images/teacher/tch006.png"
    image tch007="images/teacher/tch007.png"
    image tch008="images/teacher/tch008.png"

    image rbk000="images/rebekka/rbk000.png"   #  Ребекка
    image rbk001="images/rebekka/rbk001.png"
    image rbk002="images/rebekka/rbk002.png"
    image rbk003="images/rebekka/rbk003.png"
    image rbk004="images/rebekka/rbk004.png"
    image rbk005="images/rebekka/rbk005.png"
    image rbk006="images/rebekka/rbk006.png"

    image mom000="images/mama/mom000.png"   # Мама
    image mom001="images/mama/mom001.png"
    image mom002="images/mama/mom002.png"
    image mom003="images/mama/mom003.png"
    image mom004="images/mama/mom004.png"
################ CG #####################

   
    
    
    
    
    
    

