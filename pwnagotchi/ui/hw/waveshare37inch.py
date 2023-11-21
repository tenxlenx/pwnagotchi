import logging

import pwnagotchi.ui.fonts as fonts
from pwnagotchi.ui.hw.base import DisplayImpl


class Waveshare37inch(DisplayImpl):
    def __init__(self, config):
        super(Waveshare37inch, self).__init__(config, 'waveshare37inch')
        self._display = None

    def layout(self):
        fonts.setup(10, 9, 10, 35, 25, 9)
        self._layout['width'] = 480 # 264
        self._layout['height'] = 280 # 176
        self._layout['face'] = (66, 27)
        self._layout['name'] = (5, 73)
        self._layout['channel'] = (0, 0)
        self._layout['aps'] = (28, 0)
        self._layout['uptime'] = (415, 0)
        self._layout['line1'] = [0, 14, 480, 14]
        self._layout['line2'] = [0, 267, 480, 267]
        self._layout['friend_face'] = (0, 250)
        self._layout['friend_name'] = (40, 250)
        self._layout['shakes'] = (0, 267)
        self._layout['mode'] = (455, 267)
        self._layout['status'] = {
            'pos': (38, 93),
            'font': fonts.status_font(fonts.Medium),
            'max': 40
        }
        return self._layout

    def initialize(self):
        logging.info("initializing waveshare 3.7 inch display")
        from pwnagotchi.ui.hw.libs.waveshare.v37inch.epd3in7 import EPD
        self._display = EPD()
        self._display.init()
        self._display.Clear(0xFF)

    def render(self, canvas):
        buf = self._display.getbuffer(canvas)
        self._display.display(buf)

    def clear(self):
        self._display.Clear(0xff)
