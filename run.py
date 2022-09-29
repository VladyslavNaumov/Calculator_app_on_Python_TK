import json
from calculator.metal import CalculatorApp

def main(config):
    base_window_cfg = config.get('base')
    base_size = base_window_cfg.get('size')
    base_title = base_window_cfg.get('title')
    settings = config.get('settings')
    base_icon = base_window_cfg.get('icon')
    app = CalculatorApp(base_size, base_title, settings=settings, icon=base_icon)
    app.run()

if __name__ == '__main__':
    with open('config.json', 'r') as fp:
        config = json.load(fp)
        main(config)