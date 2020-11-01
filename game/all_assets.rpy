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
default chapter = 1

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
     define al = Character("Алан", color="#ff4040")
     define sar = Character("Сара", color="9de0b4")
     define sai = Character("Саймон", color="#dbd7d2")
     define mon = Character("Моника", color="#faf87d")
     define nn = Character("???", color="#fce79f")
     define g = Character("[name]", color="#ffffff")
     define bul = Character("Разработчик", color="#7d72c2")

            
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

    image train ="images/bg/train.jpg"
    image gorod ="images/bg/gorod.jpg"
    image darksky ="images/bg/darksky.jpg"
    image schhall ="images/bg/schoolhallway1.jpg"
    image schhall2 ="images/bg/schoolhallway2.jpg"
    image schhalln ="images/bg/schoolhallway_night.jpg"
    image schstairs ="images/bg/schoolstairs.jpg"
    image forest_night ="images/bg/forest_night.png"
    image cityroad ="images/bg/city_road.jpg"
    image schbuild ="images/bg/school_building.jpg"
    image schbulid2 ="images/bg/school_building2.jpg"
    image city2 ="images/bg/city2.jpg"
    image city ="images/bg/city.jpg"
    image class1 ="images/bg/class1.jpg"
    image class2 ="images/bg/class2.jpg"
    image class3 ="images/bg/class3.jpg"
    image schbath ="images/bg/sch_bath.jpg"
    image tos ="images/menu/tos.jpg"
    
    
    
    image black = "#000000"
    image dark = "#000000e4"
    image darkred = "#110000c8"
    image white = "#ffffff"
    image end:
        truecenter
        "gui/end_ru.png"
    image poem_end:
        truecenter
        "images/menu/poem.jpg"

   
################ Sprites #####################


    image sai angry ="images/saimon/saiangr.png"    #Саймон
    image sai blink ="images/saimon/saiblink.png"
    image sai calm ="images/saimon/saicalm.png"
    image sai hap ="images/saimon/saihappy.png"
    image sai laugh ="images/saimon/sailaugh.png"
    image sai sad ="images/saimon/saisad.png"
    image sai smart ="images/saimon/saismart.png"
    image sai smirk ="images/saimon/saismirk.png"
    image sai surp ="images/saimon/saisurprised.png"
    

    image sar angry ="images/sara/saraangry.png"      #Сара
    image sar calm ="images/sara/saracalm.png"
    image sar crazy ="images/sara/saracrazy.png"
    image sar cry ="images/sara/saracry.png"
    image sar off ="images/sara/saraoffend.png"
    image sar hap ="images/sara/sarahappy.png"
    image sar sad ="images/sara/sarasad.png"
    image sar scared ="images/sara/sarascared.png"
    image sar smile ="images/sara/sarasmile.png"
    image sar surp ="images/sara/sarasurprised.png"
    
    image mon angry ="images/monika/monangry.png"      #Моника
    image mon crazy ="images/monika/moncrazy.png"
    image mon hap ="images/monika/monhappy.png"
    image mon norm ="images/monika/monnorm.png"
    image mon sad ="images/monika/monsad.png"
    image mon scared ="images/monika/monscared.png"
    image mon smirk ="images/monika/monsmirk.png"
    image mon surp ="images/monika/monsurprised.png"
    image mon kill ="images/monika/monkill.png"
    image mon vangry ="images/monika/monverangry.png"

    
    image al angry ="images/alan/alanangry.png"      #Алан
    image al calm ="images/alan/alancalm.png"
    image al dis ="images/alan/alandis.png"
    image al shy ="images/alan/alanshy.png"
    image al hap ="images/alan/alanhappy.png"
    image al sad ="images/alan/alansad.png"       
    image al smile ="images/alan/alansmile.png"
    image al surp ="images/alan/alansurprised.png"          
   
    
    
    
    
################ CG #####################

   
    
    
    
    
    
    

