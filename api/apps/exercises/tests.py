from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from apps.exercises.models import Exercise, Difficulty


class ExerciseAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.difficulty = Difficulty.objects.create(name='Beginner')
        cls.exercise = Exercise.objects.create(name="SM Bench Press",
                                               difficulty=cls.difficulty)

    def test_retrieve_exercise(self):
        """
        Ensure we can retrieve an existing exercise object.
        """
        url = reverse('exercise-detail', kwargs={'pk': self.exercise.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Exercise.objects.count(), 1)
        self.assertEqual(response.data, {
            'id': 1,
            'name': 'SM Bench Press',
            'difficulty': {
                'id': 1,
                'name': 'Beginner'
            },
            'created': self.exercise.created.isoformat().replace('+00:00', 'Z')
        })

    def test_list_exercises(self):
        """
        Ensure we can list all exercise objects.
        """
        Exercise.objects.create(name="Pull-ups",
                                difficulty=self.difficulty)
        Exercise.objects.create(name="Barbell Bench Hip Thrust",
                                difficulty=self.difficulty)

        url = reverse('exercise-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Exercise.objects.count(), 3)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['name'], 'SM Bench Press')
        self.assertEqual(response.data[1]['name'], 'Pull-ups')
        self.assertEqual(response.data[2]['name'], 'Barbell Bench Hip Thrust')

    def test_exercise_str_method(self):
        """
        Ensure the __str__ method of Exercise returns the name.
        """
        self.assertEqual(str(self.exercise), "SM Bench Press")

    def test_unique_exercise_names_per_difficulty(self):
        Exercise.objects.create(name="Lunges", difficulty=self.difficulty)

        # Attempt to create a duplicate
        with self.assertRaises(Exception):
            Exercise.objects.create(name="Lunges", difficulty=self.difficulty)
