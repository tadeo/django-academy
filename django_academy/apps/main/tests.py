"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.main.models import Course
from soupselect import select
from BeautifulSoup import BeautifulSoup

class SimpleTest(TestCase):
    def test_courses_list_present_in_course_detail_page(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        test_course_name = 'Test Course'
        new_course = Course(name=test_course_name, description='lorem ipsum')
        new_course.save()
        response = self.client.get('/courses/%s' % new_course.pk)
        self.assertContains(response, '<ul class="object_index">')
        soup = BeautifulSoup(response.content)
        li_nodes = select(soup, 'ul.object_index li')
        self.assertEquals(test_course_name in str(li_nodes[0]), True)
