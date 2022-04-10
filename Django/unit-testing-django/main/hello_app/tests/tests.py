from django.test import TestCase

class AnimalTestCase(TestCase):
    def setUp(self):
        pass

    def test_animals_can_speak(self):
        number_two = 2
        self.assertEqual(2, number_two)