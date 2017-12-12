import json

import falcon


class LED:

    def __init__(self, leds):
        self._leds = leds

    def led(self, label):
        led = self._leds.get(label)
        if led is None:
            raise falcon.HTTPNotFound()
        return led

    @staticmethod
    def _led_to_json(led):
        return json.dumps({
            'pin': led.pin,
            'is_lit': led.is_lit
        })


class Detail(LED):

    def on_get(self, req, res, label):
        res.body = self._led_to_json(self.led(label))


class Control(LED):

    allowed_actions = ('on', 'off', 'toggle')

    def on_post(self, req, res, label, action):
        led = self.led(label)
        if action not in self.allowed_actions:
            raise falcon.HTTPNotFound()

        getattr(led, action)()
        res.body = self._led_to_json(led)
