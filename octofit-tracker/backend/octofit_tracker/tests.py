from django.test import TestCase

# Create your tests here.
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
	def test_create_user(self):
		user = User.objects.create(username='testuser', email='test@example.com', first_name='Test', last_name='User')
		self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
	def test_create_team(self):
		team = Team.objects.create(name='Test Team')
		self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
	def test_create_activity(self):
		user = User.objects.create(username='testuser', email='test@example.com', first_name='Test', last_name='User')
		activity = Activity.objects.create(user=user, activity_type='Running', duration=30, calories_burned=200, date='2026-02-13')
		self.assertEqual(activity.activity_type, 'Running')

class WorkoutModelTest(TestCase):
	def test_create_workout(self):
		user = User.objects.create(username='testuser', email='test@example.com', first_name='Test', last_name='User')
		workout = Workout.objects.create(user=user, workout_type='Yoga', suggested=True, date='2026-02-13')
		self.assertTrue(workout.suggested)

class LeaderboardModelTest(TestCase):
	def test_create_leaderboard(self):
		team = Team.objects.create(name='Test Team')
		leaderboard = Leaderboard.objects.create(team=team, points=100, rank=1)
		self.assertEqual(leaderboard.rank, 1)
