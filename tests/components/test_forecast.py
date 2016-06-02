"""The tests for the forecast.io component."""
import os
import unittest
from unittest.mock import MagicMock

from homeassistant.components.sensor import forecast
from homeassistant import core as ha, loader
import homeassistant.util.dt as date_util
from homeassistant.const import TEMP_CELSIUS

class TestForecastSetup(unittest.TestCase):
    """Test the forecast.io module."""

    def test_setup_no_latitude(self):
        """Test config."""
        hass = ha.HomeAssistant()
        hass.config.config_dir = os.path.join(os.path.dirname(__file__), "config")
        # hass.config.latitude = 32.87336
        hass.config.longitude = -117.22743
        hass.config.time_zone = date_util.get_time_zone('US/Pacific')
        hass.config.temperature_unit = TEMP_CELSIUS
        loader.prepare(hass)
        self.assertFalse(forecast.setup_platform(hass, hass.config.as_dict(), MagicMock()))
