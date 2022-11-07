import json
from calculator.metal import CalculatorApp

def main(config):
    base_window_cfg = config.get('main_window_settings')
    base_size = base_window_cfg.get('geometry')
    base_title = base_window_cfg.get('title')
    base_icon = base_window_cfg.get('icon')
    operation_settings = config.get('operation_settings')
    app = CalculatorApp(base_size, base_title, icon=base_icon,  operation_settings=operation_settings)
    app.run()

if __name__ == '__main__':
    with open('config.json', 'r') as fp:
        config = json.load(fp)
        main(config)