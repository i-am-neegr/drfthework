import unittest
from unittest.mock import patch, Mock
from rest_framework import status

class LessonTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Mock()  # Mock the client completely
        self.user = Mock(email="admin@sky.com", pk=1)
        self.course = Mock(name="Python course", description="Python course jun", owner=self.user, pk=1)
        self.lesson = Mock(name="Python lesson", description="Python course", course=self.course, owner=self.user, pk=1)
        self.client.force_authenticate = Mock(return_value=None)

    @patch('django.urls.reverse')  # Mock the reverse function
    def test_lesson_list(self, mock_reverse):
        # Mock the URL returned by reverse
        mock_reverse.return_value = '/materials/lessons/'
        url = mock_reverse("materials:lesson_list")
        mock_response = Mock(status_code=status.HTTP_200_OK, json=Mock(return_value={
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "name": self.lesson.name,
                    "picture": None,
                    "description": self.lesson.description,
                    "link": "",
                    "owner": self.user.pk,
                    "course": self.course.pk,
                }
            ]
        }))
        self.client.get = Mock(return_value=mock_response)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "name": self.lesson.name,
                    "picture": None,
                    "description": self.lesson.description,
                    "link": "",
                    "owner": self.user.pk,
                    "course": self.course.pk,
                }
            ]
        })

if __name__ == '__main__':
    unittest.main()