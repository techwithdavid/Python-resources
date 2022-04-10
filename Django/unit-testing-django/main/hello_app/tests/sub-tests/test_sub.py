from django.test import TestCase

class AnimalTestCase(TestCase):
    def setUp(self):
        pass

    def test_animals_can_speak(self):
        number_one = 1
        self.assertEqual(1, number_one)