"""
UI Components Module - Contains all Flet UI widgets and layout.

This module defines the visual components for the weather application,
including theme controls, weather display widgets, and input elements.
Designed with modern Apple-inspired aesthetics.
"""

import flet
from flet import icons


DEFAULT_ICON = "03d"

APPLE_LIGHT_BG = "#F5F5F7"
APPLE_DARK_BG = "#1C1C1E"
APPLE_BLUE = "#007AFF"
APPLE_GRAY = "#8E8E93"
APPLE_CARD_BG_DARK = "#2C2C2E"
APPLE_CARD_BG_LIGHT = "#FFFFFF"


def create_theme_toggle(page: flet.Page) -> flet.Container:
    """Create theme toggle buttons with Apple-style design."""

    def set_light_theme(e):
        page.theme_mode = "light"
        page.bgcolor = APPLE_LIGHT_BG
        page.update()

    def set_dark_theme(e):
        page.theme_mode = "dark"
        page.bgcolor = APPLE_DARK_BG
        page.update()

    light_btn = flet.Container(
        content=flet.IconButton(
            icon=icons.LIGHT_MODE,
            icon_color=APPLE_BLUE,
            icon_size=22,
            on_click=set_light_theme,
        ),
        bgcolor=APPLE_CARD_BG_DARK if page.theme_mode == "dark" else "#E5E5EA",
        border_radius=20,
        padding=5,
    )

    dark_btn = flet.Container(
        content=flet.IconButton(
            icon=icons.DARK_MODE,
            icon_color=APPLE_BLUE,
            icon_size=22,
            on_click=set_dark_theme,
        ),
        bgcolor=APPLE_CARD_BG_DARK if page.theme_mode == "dark" else "#E5E5EA",
        border_radius=20,
        padding=5,
    )

    return flet.Container(
        content=flet.Row([light_btn, dark_btn], spacing=4),
        padding=3,
        bgcolor="#E5E5EA" if page.theme_mode == "light" else "#3A3A3C",
        border_radius=25,
    )


def create_weather_icon(icon_code: str = DEFAULT_ICON, size: int = 180) -> flet.Image:
    """Create a weather icon from OpenWeatherMap."""
    return flet.Image(
        src=f"https://openweathermap.org/img/wn/{icon_code}@2x.png",
        width=size,
        height=size,
        fit="contain",
    )


def create_card(controls: list, page: flet.Page, padding: int = 20) -> flet.Container:
    """Create an Apple-style card container."""
    bg = APPLE_CARD_BG_LIGHT if page.theme_mode == "light" else APPLE_CARD_BG_DARK
    return flet.Container(
        content=flet.Column(controls, spacing=12, horizontal_alignment="center"),
        bgcolor=bg,
        border_radius=20,
        padding=padding,
        shadow=flet.BoxShadow(
            spread_radius=0,
            blur_radius=15,
            color=flet.colors.with_opacity(0.1, "black"),
        ) if page.theme_mode == "light" else None,
    )


def create_weather_display_widgets(page: flet.Page) -> dict:
    """Create all weather display widgets with Apple-style typography."""
    text_color = "#000000" if page.theme_mode == "light" else "#FFFFFF"

    return {
        "location": flet.Text(
            value="Search for a city",
            size=18,
            weight="w400",
            color=APPLE_GRAY,
        ),
        "main_temp": flet.Text(
            value="--",
            size=96,
            weight="w200",
            color=text_color,
            font_family="SF Pro Display",
        ),
        "weather_desc": flet.Text(
            value="--",
            size=24,
            weight="w500",
            color=APPLE_GRAY,
        ),
        "weather_icon": create_weather_icon(),
        "feels_like": flet.Text(
            value="Feels like --°",
            size=16,
            weight="w400",
            color=APPLE_GRAY,
        ),
        "sunrise_icon": flet.Icon(icons.SUNNY, color="#FF9500", size=24),
        "sunrise_time": flet.Text(
            value="Sunrise  --:--",
            size=15,
            weight="w400",
            color=text_color,
        ),
        "sunset_icon": flet.Icon(icons.NIGHTLIGHT, color="#5856D6", size=24),
        "sunset_time": flet.Text(
            value="Sunset  --:--",
            size=15,
            weight="w400",
            color=text_color,
        ),
        "humidity_icon": flet.Icon(icons.WATER_DROP, color=APPLE_BLUE, size=22),
        "humidity": flet.Text(
            value="Humidity  --%",
            size=15,
            weight="w400",
            color=text_color,
        ),
        "wind_icon": flet.Icon(icons.AIR, color=APPLE_GRAY, size=22),
        "wind_speed": flet.Text(
            value="Wind  -- m/s",
            size=15,
            weight="w400",
            color=text_color,
        ),
        "pressure_icon": flet.Icon(icons.SPEED, color=APPLE_GRAY, size=22),
        "pressure": flet.Text(
            value="Pressure  -- hPa",
            size=15,
            weight="w400",
            color=text_color,
        ),
    }


def update_widgets_with_weather(widgets: dict, weather_data: dict, page: flet.Page) -> None:
    """Update all weather display widgets with new data."""
    text_color = "#000000" if page.theme_mode == "light" else "#FFFFFF"

    widgets["location"].value = f"{weather_data['name']}, {weather_data['country']}"
    widgets["location"].color = APPLE_GRAY

    widgets["main_temp"].value = f"{weather_data['temp_C']}°"
    widgets["main_temp"].color = text_color

    widgets["weather_desc"].value = weather_data["weather_desc"]
    widgets["weather_icon"].src = f"https://openweathermap.org/img/wn/{weather_data['weather_icon']}@2x.png"

    widgets["feels_like"].value = f"Feels like {weather_data['feels_like_C']}°"

    widgets["sunrise_time"].value = f"Sunrise  {weather_data['sunrise'][:5]}"
    widgets["sunrise_time"].color = text_color

    widgets["sunset_time"].value = f"Sunset  {weather_data['sunset'][:5]}"
    widgets["sunset_time"].color = text_color

    widgets["humidity"].value = f"Humidity  {weather_data['humidity']}%"
    widgets["humidity"].color = text_color

    widgets["wind_speed"].value = f"Wind  {weather_data['wind_speed']} m/s"
    widgets["wind_speed"].color = text_color

    widgets["pressure"].value = f"Pressure  {weather_data['pressure']} hPa"
    widgets["pressure"].color = text_color


def reset_widgets_to_default(widgets: dict, page: flet.Page) -> None:
    """Reset all weather display widgets to their default values."""
    text_color = "#000000" if page.theme_mode == "light" else "#FFFFFF"

    widgets["location"].value = "Search for a city"
    widgets["location"].color = APPLE_GRAY
    widgets["main_temp"].value = "--"
    widgets["main_temp"].color = text_color
    widgets["weather_desc"].value = "--"
    widgets["weather_icon"].src = f"https://openweathermap.org/img/wn/{DEFAULT_ICON}@2x.png"
    widgets["feels_like"].value = "Feels like --°"
    widgets["sunrise_time"].value = "Sunrise  --:--"
    widgets["sunrise_time"].color = text_color
    widgets["sunset_time"].value = "Sunset  --:--"
    widgets["sunset_time"].color = text_color
    widgets["humidity"].value = "Humidity  --%"
    widgets["humidity"].color = text_color
    widgets["wind_speed"].value = "Wind  -- m/s"
    widgets["wind_speed"].color = text_color
    widgets["pressure"].value = "Pressure  -- hPa"
    widgets["pressure"].color = text_color


def create_search_input(on_search: callable, page: flet.Page) -> tuple:
    """Create the city search input field with Apple-style design."""
    bg = "#E5E5EA" if page.theme_mode == "light" else "#3A3A3C"
    text_color = "#000000" if page.theme_mode == "light" else "#FFFFFF"
    hint_color = APPLE_GRAY

    city_input = flet.TextField(
        hint_text="Search city",
        prefix_icon=icons.SEARCH,
        color=text_color,
        hint_style=flet.TextStyle(color=hint_color),
        border_color="transparent",
        filled=True,
        fill_color=bg,
        border_radius=12,
        height=48,
        text_size=16,
        on_submit=on_search,
    )

    search_btn = flet.Container(
        content=flet.Icon(icons.ARROW_FORWARD, color="white", size=22),
        bgcolor=APPLE_BLUE,
        border_radius=12,
        width=48,
        height=48,
        on_click=on_search,
    )

    return city_input, search_btn


def build_main_layout(page: flet.Page, widgets: dict, city_input, search_btn) -> None:
    """Build and add all components to the main page layout."""
    details_row = flet.Row(
        [
            flet.Column(
                [widgets["humidity_icon"], widgets["humidity"]],
                horizontal_alignment="center",
                spacing=6,
            ),
            flet.Column(
                [widgets["wind_icon"], widgets["wind_speed"]],
                horizontal_alignment="center",
                spacing=6,
            ),
            flet.Column(
                [widgets["pressure_icon"], widgets["pressure"]],
                horizontal_alignment="center",
                spacing=6,
            ),
        ],
        spacing=30,
        alignment="center",
    )

    sun_row = flet.Row(
        [
            flet.Column(
                [widgets["sunrise_icon"], widgets["sunrise_time"]],
                horizontal_alignment="center",
                spacing=6,
            ),
            flet.Column(
                [widgets["sunset_icon"], widgets["sunset_time"]],
                horizontal_alignment="center",
                spacing=6,
            ),
        ],
        spacing=50,
        alignment="center",
    )

    weather_card = create_card(
        [
            widgets["location"],
            flet.Row([widgets["weather_icon"], widgets["main_temp"]], alignment="center", spacing=8),
            widgets["weather_desc"],
            widgets["feels_like"],
            flet.Container(height=10),
            sun_row,
            flet.Container(height=10),
            details_row,
        ],
        page,
        padding=24,
    )

    search_row = flet.Row(
        [city_input, search_btn],
        spacing=12,
        alignment="center",
    )

    page.add(
        flet.Container(height=20),
        search_row,
        flet.Container(height=30),
        weather_card,
    )
    page.padding = 20
