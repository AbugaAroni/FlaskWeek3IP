import unittest
from app.models import Pitch

class TestPitch(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitches class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_Pitch = Pitch(1234,'My pitch','Motivational','You can do it dont give up')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_Pitch,Pitch))
