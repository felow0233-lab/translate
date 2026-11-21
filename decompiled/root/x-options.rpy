
















define config.name = _("Mushoku Tensex")





define gui.show_name = True




define config.version = "0.10.0"





define gui.about = _p("""
""")






define build.name = "MushokuTensex"








define config.has_sound = True
define config.has_music = True
define config.has_voice = True
























define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 200





default preferences.afm_time = 15
















define config.save_directory = "MushokuTensex-1749654846"






define config.window_icon = "gui/window_icon.png"






init python:






















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/**.rpy', None)  



    build.classify('game/**.png', 'archive')  
    build.classify('game/**.jpg', 'archive')  
    build.classify('game/**.ogg', 'archive')  
    build.classify('game/**.mp3', 'archive')  
    build.classify('game**', 'archive')       


    build.archive("data", "all")  




    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
