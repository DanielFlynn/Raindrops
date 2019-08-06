import unittest
from Raindrops import *

#If the number has a factor of 3, output 'Pling'
#If the number has a factor of 5, output 'Plang'
#If the number has a factor of 7, output 'Plong'
#If the number does not have any of the above as a factor simply return the numbers digits

class RaindropsTest(unittest.TestCase):

    def test_sound_3(self):
        self.assertEqual(raindrops(3),"Pling") #Return is Pling as 3 is a factor of 3

    def test_sound_5(self):
        self.assertEqual(raindrops(5),"Plang") #Return is Plang as 5 is a factor of 5

    def test_sound_7(self):
        self.assertEqual(raindrops(7),"Plong") #Return is Plong as 7 is a factor of 7

    def test_sound_88(self):
        self.assertEqual(raindrops(88),"88") #88 has no factors, so it will return the number as digits

    def test_sound_15(self):
        self.assertEqual(raindrops(15),"PlingPlang") #Return is PlingPlang as 15 is a factor os both 3 & 5

    def test_sound_21(self):
        self.assertEqual(raindrops(21),"PlingPlong") #Return is PlingPlong as 21 is a factor of 3 & 7

    def test_sound_35(self):
        self.assertEqual(raindrops(35), "PlangPlong")#Return is PlangPlong as 35 is a factor os 5 & 7

    def test_sound_105(self):
        self.assertEqual(raindrops(105),"PlingPlangPlong")#Return is PlingPlangPlong as 105 is a factor of 3,5 & 7

