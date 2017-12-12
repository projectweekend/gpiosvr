import json


class LED:

    def __init__(self, leds):
        self._leds = leds

    def led(self, label):
        led = self._leds.get(label)
        if led is None:
            message = 'label does not exist: {0}'.format(label)
            raise falcon.HTTPNotFound(message)
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
            message = 'action does not exist: {0}'.format(label)
            raise falcon.HTTPNotFound(message)

        getattr(led, action)()
        res.body = self._led_to_json(led)
