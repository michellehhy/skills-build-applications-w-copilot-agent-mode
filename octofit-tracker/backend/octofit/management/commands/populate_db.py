from django.core.management.base import BaseCommand
from octofit.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), username='john_doe', email='john@example.com', password='password123'),
            User(_id=ObjectId(), username='jane_doe', email='jane@example.com', password='password123'),
            User(_id=ObjectId(), username='alice', email='alice@example.com', password='password123'),
            User(_id=ObjectId(), username='bob', email='bob@example.com', password='password123'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(_id=ObjectId(), name='Team Alpha')
        team2 = Team(_id=ObjectId(), name='Team Beta')
        team1.save()
        team2.save()
        team1.members.add(users[0], users[1])
        team2.members.add(users[2], users[3])

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Running', duration=timedelta(minutes=30)),
            Activity(_id=ObjectId(), user=users[1], activity_type='Cycling', duration=timedelta(minutes=45)),
            Activity(_id=ObjectId(), user=users[2], activity_type='Swimming', duration=timedelta(minutes=60)),
            Activity(_id=ObjectId(), user=users[3], activity_type='Yoga', duration=timedelta(minutes=20)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], score=100),
            Leaderboard(_id=ObjectId(), user=users[1], score=90),
            Leaderboard(_id=ObjectId(), user=users[2], score=80),
            Leaderboard(_id=ObjectId(), user=users[3], score=70),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Morning Run', description='A quick morning run to start the day'),
            Workout(_id=ObjectId(), name='Evening Yoga', description='Relaxing yoga session in the evening'),
            Workout(_id=ObjectId(), name='Swimming Laps', description='Intense swimming workout'),
            Workout(_id=ObjectId(), name='Cycling Adventure', description='Exploring the countryside on a bike'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))