from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Resume, Skill, Company, PreviousJob
import datetime

class ResumeAPITest(APITestCase):
    def setUp(self):
        self.skill_name = "Django"
        self.success_summary = "Survived the amazon jungle"
        self.owner = User.objects.create_user(
            username='john.doe', 
            password='secret',
            first_name='John',
            last_name='Doe',
            email='john.doe@gmail.com'
        )
        self.resume = Resume.objects.create(
            owner = self.owner,
            success_summary = self.success_summary
        )
        self.skill = Skill.objects.create(
            resume=self.resume,
            name="Python"
        )
        self.company = Company.objects.create(
            name="ACME Corp",
            location="Remote",
            description="Testing"
        )
        self.previous_job = PreviousJob.objects.create(
            resume=self.resume,
            company=self.company,
            position="Developer",
            start_date=datetime.date(2020, 1, 1),
            description="Working hard"
        )

    def test_resumes_list(self):
        url = reverse('resume-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if results is in data (for paginated responses) or direct list
        data = response.data.get('results') if isinstance(response.data, dict) else response.data
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['owner'], self.owner.id)

    def test_educations_list(self):
        url = reverse('education-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_skills_list(self):
        url = reverse('skill-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_skill_create(self):
        data = {
            'resume' : self.resume.id,
            'name' : 'Django'
        }
        url = reverse('skill-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Django')

    def test_update_resume(self):
        data = {
            'owner' : self.owner.id,
            'success_summary' : 'Updated summary'
        }
        url = reverse('resume-detail', args=[self.resume.id])
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success_summary'], 'Updated summary')

    def test_delete_resume(self):
        url = reverse('resume-detail', args=[self.resume.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_previous_jobs(self):
        url = reverse('previousjob-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_skill(self):
        data = {
            'resume' : self.resume.id,
            'name' : 'Updated skill'
        }
        url = reverse('skill-detail', args=[self.skill.id])
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated skill')