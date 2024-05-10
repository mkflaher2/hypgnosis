from app.models.control import Color

from nicegui import ui

def init_page(control_model, callback_handler):

    @ui.page('/')
    def show():
        ui.page_title('HypGNOSIS')
        with ui.column().classes('w-full items-center'):
            ui.markdown("# HypGNOSIS")
            with ui.row():
                direction_toggle = ui.toggle(
                    {1: "Clockwise", 2: "Counter-clockwise"},
                    value=1,
                    on_change=callback_handler.update_state
                ).bind_value(control_model, 'direction')
            with ui.row():
                ui.label('Speed')
                speed_slider = ui.slider(
                    min=0, max=10,
                    step=0.1,
                    on_change=callback_handler.update_state
                ).bind_value(control_model, 'speed')
            with ui.row():
                ui.label('R')
                r_slider = ui.slider(
                    min=0, max=1,
                    step=0.1,
                    on_change=callback_handler.update_state
                ).bind_value(control_model.color, 'r')
            with ui.row():
                ui.label('G')
                g_slider = ui.slider(
                    min=0, max=1,
                    step=0.1,
                    on_change=callback_handler.update_state
                ).bind_value(control_model.color, 'g')
            with ui.row():
                ui.label('B')
                b_slider = ui.slider(
                    min=0, max=1,
                    step=0.1,
                    on_change=callback_handler.update_state
                ).bind_value(control_model.color, 'b')
            with ui.row():
                ui.label('A')
                a_slider = ui.slider(
                    min=0, max=1,
                    step=0.1,
                    on_change=callback_handler.update_state
                ).bind_value(control_model.color, 'a')

    ui.run()
