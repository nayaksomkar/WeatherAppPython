"""
Weather Application - Main Entry Point

A desktop weather application built with Flet that displays current weather
information for any city using the OpenWeatherMap API.

Usage:
    python main.py
"""

import flet

from weather_api import get_weather, is_api_configured
from ui_components import (
    create_theme_toggle,
    create_weather_display_widgets,
    create_search_input,
    build_main_layout,
    update_widgets_with_weather,
    reset_widgets_to_default,
    APPLE_DARK_BG,
    APPLE_BLUE,
)


def main(page: flet.Page) -> None:
    """Initialize and configure the main application page."""
    page.theme_mode = "dark"
    page.theme = flet.Theme(color_scheme_seed="#000000")
    page.bgcolor = APPLE_DARK_BG
    page.title = "Weather App"

    if not is_api_configured():
        api_warning = flet.Container(
            content=flet.Row(
                [
                    flet.Icon(name=flet.icons.INFO_OUTLINE, color="#FFFFFF", size=20),
                    flet.Text(
                        value="API key not configured. Showing demo data. Add your OpenWeatherMap API key in config.py for real weather data.",
                        color="#FFFFFF",
                        size=13,
                        weight="w400",
                    ),
                ],
                spacing=10,
                vertical_alignment="center",
            ),
            bgcolor="#FF9500",
            padding=15,
            border_radius=12,
            margin=10,
        )
        page.add(api_warning)

    widgets = create_weather_display_widgets(page)
    theme_row = create_theme_toggle(page)

    def on_city_search(e) -> None:
        """Handle city search from button click or Enter key."""
        city_name = city_input.value.strip()

        if not city_name:
            page.update()
            return

        reset_widgets_to_default(widgets, page)
        page.update()

        weather_data = get_weather(city_name)

        if weather_data.get("success"):
            update_widgets_with_weather(widgets, weather_data, page)
        else:
            error_message = weather_data.get("error_message", "Unknown error")
            widgets["weather_desc"].value = error_message
            reset_widgets_to_default(widgets, page)

        page.update()

    city_input, search_btn = create_search_input(on_city_search, page)

    build_main_layout(page, widgets, city_input, search_btn)
    page.update()


if __name__ == "__main__":
    flet.app(target=main)
