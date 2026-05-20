################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    if main_menu:

        hbox:
            style_prefix "main_nav"
            xalign 0.5
            yalign 1.0
            yoffset -60
            spacing 14

            textbutton _("Start") action Start()
            textbutton _("Continue") action Continue(confirm=False) sensitive renpy.newest_slot() is not None
            textbutton _("Load") action ShowMenu("load")
            textbutton _("Preferences") action ShowMenu("preferences")
            textbutton _("About") action ShowMenu("about")
            textbutton _("Credits") action ShowMenu("creditos")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                textbutton _("Help") action ShowMenu("help")

            if renpy.variant("pc"):
                ## The quit button is banned on iOS and unnecessary on Android and Web.
                textbutton _("Quit") action Quit(confirm=not main_menu)

    else:

        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.5

            spacing gui.navigation_spacing

            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")
            textbutton _("Load") action ShowMenu("load")
            textbutton _("Preferences") action ShowMenu("preferences")

            if _in_replay:
                textbutton _("End Replay") action EndReplay(confirm=True)
            else:
                textbutton _("Main Menu") action MainMenu()

            textbutton _("About") action ShowMenu("about")
            textbutton _("Credits") action ShowMenu("creditos")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                ## Help isn't necessary or relevant to mobile devices.
                textbutton _("Help") action ShowMenu("help")

            if renpy.variant("pc"):
                ## The quit button is banned on iOS and unnecessary on Android and Web.
                textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")

style main_nav_button is navigation_button
style main_nav_button_text is navigation_button_text

style main_nav_button:
    # No menu inferior, não forçamos largura igual para evitar "buracos".
    size_group None

style main_nav_button_text:
    size 52


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add Solid("#000000")
    add Transform("images/RAÍZES LOGO.png", xalign=0.5, yalign=0.5, zoom=1)

    ## Sem overlay escuro no menu principal.

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

style main_menu_version_text:
    color "#d7bd7c"


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    # Fundo preto para todas as telas de menu.
    add Solid("#000000")

    # Barra separadora horizontal, antes do menu inferior.
    add Solid(gui.game_menu_separator_color):
        xalign 0.5
        yalign 1.0
        yoffset -180
        xsize 1720
        ysize gui.game_menu_separator_width

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            if main_menu:
                null width 0
            else:
                frame:
                    style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background None

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 75
    right_margin 20
    top_margin 15

style game_menu_viewport:
    xsize config.screen_width
    ymaximum 620

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style return_button:
    xalign 1.0
    xoffset -40
    yalign 0.0
    yoffset 35
