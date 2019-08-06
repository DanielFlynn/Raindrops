import unittest
from Raindrops import *

#If the number has a factor of 3, output 'Pling'

#If the number has a factor of 5, output 'Plang'

#If the number has a factor of 7, output 'Plong'

#If the number does not have any of the above as a factor simply return the numbers digits

class RaindropsTest(unittest.TestCase):

    def test_sound_3(self):
        self.assertEqual(raindrops(3),"Pling")

    def test_sound_5(self):
        self.assertEqual(raindrops(5),"Plang")

    def test_sound_7(self):
        self.assertEqual(raindrops(7),"Plong")

    def test_sound_88(self):
        self.assertEqual(raindrops(88),"88")