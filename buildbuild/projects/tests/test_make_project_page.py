from django.test import TestCase
from django.test.client import Client
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from projects.views import MakeProjectView
from projects.models import Project

from teams.models import Team

class MakeProjectPageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.name = "buildbuild_project"
        self.team_name = "buildbuild_team"
        self.team = Team.objects.create_team(name = self.team_name)
        
        # need to find more eloquent way to test redirect url.
        self.TEST_SERVER_URL = "http://testserver"

        respanse = self.client.post("/makeproject/", {
            "name":self.name,
        })
 

    def test_get_make_project_page_request_should_return_200(self):
        response = self.client.get("/makeproject/")
        self.assertEqual(response.status_code, 200)

    def test_check_uniqueness_of_project_name(self):
        try:
            respanse = self.client.post("/makeproject/", {
                "name":self.name,
            })
        except IntegrityError:
            pass
    """
    def test_post_available_project_information_return_302(self):
        response = self.client.post("/makeproject/", {
            "name": self.name,
            })
        self.assertEqual(response.status_code, 302)

    def test_post_available_information_redirect_to_home(self):
        response = self.client.post("/makeproject/", {
             "name": self.name,
            })
        self.assertEqual(response["Location"], self.TEST_SERVER_URL + "/")
    """
