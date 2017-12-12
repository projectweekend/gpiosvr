import falcon

from .resources import Control, Detail


def create_app(pin_config, led):
    """
    This returns a Falcon application that is ready to use with Gunicorn.
    `pin_config`: An iterable of pin number/route label pairs
    `port`: A port number where this server will listen
    """

    leds = {label: led(pin) for label, pin in pin_config}

    app = falcon.API()
    app.add_route('/{label}', Detail(leds=leds))
    app.add_route('/{label}/{action}', Control(leds=leds))

    return app
