import flet
from flet import(
    Page,
    IconButton,
    icons,
    Row

)

def main(page: Page):
    page.theme_mode = 'dark'
    page.update()

    def set_dark_theme(e):
        page.theme_mode = 'dark'
        page.update()

    def set_light_theme(e):
        page.theme_mode = 'light'
        page.update()

        

    light_theme = IconButton(
        icon=icons.SUNNY,
        icon_size=20,
        tooltip='light theme',
        on_click=set_light_theme
    )

    dark_theme = IconButton(
        icon=icons.NIGHTLIGHT,
        icon_size=20,
        tooltip='light theme',
        on_click=set_dark_theme
    )

    theme_change = Row([light_theme,dark_theme,])

    page.add(theme_change)


flet.app(target=main)