import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-05-22")
        last_service_date = date.fromisoformat("2021-02-16")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-08-31")
        last_service_date = date.fromisoformat("2022-06-23")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())