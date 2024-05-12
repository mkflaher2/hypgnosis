from app.frontend.gui import init_page
from app.frontend.callbacks import CallbackHandler
from app.models.control import ControlModel

if __name__ in  {"__main__", "__mp_main__"}:

    # Dependencies
    control_model = ControlModel()
    callback_handler = CallbackHandler(control_model)

    # Setup NiceGUI
    init_page(control_model, callback_handler)

    print('quitting')
