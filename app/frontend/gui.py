from app.models.control import Color

from nicegui import ui

def init_page(control_model, callback_handler):

    @ui.page('/')
    def show():
        ui.page_title('HypGNOSIS')
        with ui.column().classes('w-full items-center'):
            ui.markdown("# HypGNOSIS")
            with ui.row().classes('w-1/3'):
                ui.label('Speed')
                speed_slider = ui.slider(
                    min=-10, max=10,
                    value=1,
                    step=0.01,
                    on_change=callback_handler.update_state
                ).bind_value(control_model, 'speed') \
                .props('label-always')
            with ui.row().classes('w-1/3'):
                ui.label('R')
                r_slider = ui.slider(
                    min=0, max=1,
                    value=1,
                    step=0.01,
                    on_change=callback_handler.update_state
                ).bind_value(control_model.color, 'r') \
                .props('label-always')

            with ui.row().classes('w-1/3'):
                ui.label('G')
                g_slider = ui.slider(
                    min=0, max=1,
                    value=1,
                    step=0.01,
                    on_change=callback_handler.update_state
                ).bind_value(control_model.color, 'g') \
                .props('label-always')

            with ui.row().classes('w-1/3'):
                ui.label('B')
                b_slider = ui.slider(
                    min=0, max=1,
                    value=1,
                    step=0.01,
                    on_change=callback_handler.update_state
                ).bind_value(control_model.color, 'b') \
                .props('label-always')

            with ui.row().classes('w-1/3'):
                ui.label('A')
                a_slider = ui.slider(
                    min=0, max=1,
                    value=1,
                    step=0.01,
                    on_change=callback_handler.update_state
                ).bind_value(control_model.color, 'a') \
                .props('label-always')

    ui.run()
