from app.models.control import Color

from nicegui import ui
from os import getenv

def spiral_control(control_model, callback_handler):

    slider_width = 'w-2/5'

    with ui.column().classes('w-full items-center'):
        with ui.row().classes(slider_width):
            ui.label('Speed')
            speed_slider = ui.slider(
                min=-10, max=10,
                value=1,
                step=0.01,
                on_change=callback_handler.update_state
            ).bind_value(control_model, 'speed') \
            .props('label-always')
        with ui.row().classes(slider_width):
            ui.label('R')
            r_slider = ui.slider(
                min=0, max=1,
                value=1,
                step=0.01,
                on_change=callback_handler.update_state
            ).bind_value(control_model.color, 'r') \
            .props('label-always')

        with ui.row().classes(slider_width):
            ui.label('G')
            g_slider = ui.slider(
                min=0, max=1,
                value=1,
                step=0.01,
                on_change=callback_handler.update_state
            ).bind_value(control_model.color, 'g') \
            .props('label-always')

        with ui.row().classes(slider_width):
            ui.label('B')
            b_slider = ui.slider(
                min=0, max=1,
                value=1,
                step=0.01,
                on_change=callback_handler.update_state
            ).bind_value(control_model.color, 'b') \
            .props('label-always')

        with ui.row().classes(slider_width):
            ui.label('A')
            a_slider = ui.slider(
                min=0, max=1,
                value=1,
                step=0.01,
                on_change=callback_handler.update_state
            ).bind_value(control_model.color, 'a') \
            .props('label-always')

def init_page(control_model, callback_handler):

    @ui.page('/')
    def show():
        ui.page_title('HypGNOSIS')
        with ui.column().classes('w-full items-center'):
            ui.markdown("# HypGNOSIS")
            with ui.tabs().classes('w-full') as tabs:
                spiral_tab = ui.tab('Spiral')
            with ui.tab_panels(tabs, value=spiral_tab).classes('w-full items-center'):
                with ui.tab_panel(spiral_tab):
                    spiral_control(control_model, callback_handler)

    ui.run(port=int(getenv('HYPGNOSIS_UI_PORT')))
