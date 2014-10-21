from django.test import TestCase
from projects.models import Project
from teams.models import Team
from django.db import IntegrityError
from django.core.exceptions import ValidationError

class TestProjectName(TestCase):
    def setUp(self):
        self.name = "test_project_name"
        self.second_name = "test_second_project_name"
        self.invalid_long_length_name = "a" * 65
        self.team_name = "test_team_name"
        self.lang = "python"
        self.ver = "2.7.8"

        self.project = Project.objects.create_project(
            name = self.name,
        )
        self.second_project = Project.objects.create_project(
            name = self.second_name,
    
        )

    def test_create_project_must_contain_name(self):
        try:
            project = Project.objects.create_project(
                properties = ('python','2.7.8')
            )
        except TypeError:
            pass

    def test_create_project_name_min_length_1(self):
        try:
            project = Project.objects.create_project(
                name = ""
            )
        except ValidationError:
            pass

    def test_project_name_max_length_64(self):
        try:        
            Project.objects.create_project(
                name = self.invalid_long_length_name,
            )
        except ValidationError:
            pass

    def test_get_all_projects(self):
        projects = Project.objects.all()
        self.assertEqual(projects[0].name, self.project.name)
        self.assertEqual(projects[1].name, self.second_project.name)

# Integrity
    def test_project_should_have_unique_name(self):
        try:
           Project.objects.create_project(
                name = self.name, 
            )
        except IntegrityError:
            pass

# Assert
    def test_get_project_equal_to_project_targetted(self):
        get_project = Project.objects.get_project(self.project.id)
        self.assertEqual(
                self.project, 
                get_project, 
                "get_project should be equal to target project",
        )
           
