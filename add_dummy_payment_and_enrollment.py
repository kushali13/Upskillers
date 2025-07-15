import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hacker.settings')
django.setup()

from hackathon.models import CustomUser, Course, Payment

# Get a learner and a course (first found)
user = CustomUser.objects.filter(user_type='learner').first()
course = Course.objects.first()

if not user:
    print('No learner user found. Please create a learner user first.')
    exit(1)
if not course:
    print('No course found. Please create a course first.')
    exit(1)

# Create a dummy payment
payment = Payment.objects.create(
    user=user,
    course=course,
    order_id="dummy_order_001",
    payment_id="dummy_payment_001",
    amount=course.price,
    status="Completed"
)

# Enroll the user in the course
course.students_enrolled.add(user)
course.save()

print(f"Dummy payment created and user '{user.username}' enrolled in course '{course.title}'.") 