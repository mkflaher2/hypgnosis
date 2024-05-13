from app.frontend.callbacks import CallbackHandler
from app.models.control import ControlModel

from nicegui import ui
from os import getenv

def init_page():

    @ui.page("/")
    def root_page():
        ui.page_title('HypGNOSIS')
        with ui.column().classes('w-full items-center'):
            ui.markdown('# HypGNOSIS')

            with ui.row().classes('w-64 items-center'):
                ui.label('Enter 6-digit user code from VR headset')
                code_input = ui.input(
                    label='Enter code',
                    placeholder='000000',
                )

                ui.button(
                    'Enter code',
                    on_click=lambda: ui.navigate.to(f"/control/{code_input.value}")
                )

    @ui.page("/control/{user_id}")
    def control_page(user_id):
        # User-specific data
        control_model = ControlModel()
        control_model.set_user_id(user_id)
        callback_handler = CallbackHandler(control_model)

        # Draw the page
        ui.page_title('HypGNOSIS')

        with ui.column().classes('w-full items-center'):
            ui.markdown('# HypGNOSIS')
            with ui.tabs().classes('w-full') as tabs:
                spiral_tab = ui.tab('Spiral')
            with ui.tab_panels(tabs, value=spiral_tab).classes('w-full items-center'):
                with ui.tab_panel(spiral_tab):
                    slider_width = 'w-2/5'

                    with ui.column().classes('w-full items-center'):
                        with ui.row().classes(slider_width):
                            ui.label('Speed')
                            speed_slider = ui.slider(
                                min=-20, max=20,
                                value=2,
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

    ui.run(port=int(getenv('HYPGNOSIS_UI_PORT')))
