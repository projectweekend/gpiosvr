from unittest import mock

from falcon import testing
import pytest

from . utils import create_app


PIN_CONFIG = [('red', 5), ('blue', 13)]


def mock_led_factory(pin_num):
    m = mock.MagicMock()
    m.is_lit = False
    m.pin = pin_num
    return m


@pytest.fixture()
def client():
    app = create_app(pin_config=PIN_CONFIG, led_factory=mock_led_factory)
    return testing.TestClient(app)


def test_get_led_exists(client):
    for label, pin in PIN_CONFIG:
        result = client.simulate_get('/{0}'.format(label))
        assert result.json['pin'] == pin
        assert result.json['is_lit'] is False
