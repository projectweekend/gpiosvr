import falcon
from gpiozero import LED


def server(pin_config, port):
    """
    This returns a Falcon application that is ready to use with Gunicorn.
    `pin_config`: An iterable of pin number/route label pairs
    `port`: A port number where this server will listen
    """

    leds = {label: LED(pin) for label, pin in pin_config}

    app = falcon.API()
    app.add_route('/{label}', _DetailResource(leds=leds))
    app.add_route('/{label}/{action}', _ControlResource(leds=leds))

    return app


class _LEDResource:

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


class _DetailResource(_LEDResource):

    def on_get(self, req, res, label):
        res.body = self._led_to_json(self.led(label))


class _ControlResource(_LEDResource):

    allowed_actions = ('on', 'off', 'toggle')

    def on_post(self, req, res, label, action):
        if action not in self.allowed_actions:
            message = 'action does not exist: {0}'.format(label)
            raise falcon.HTTPNotFound(message)
        led = self.led(label)
        getattr(led, action)()
        res.body = self._led_to_json(led)
