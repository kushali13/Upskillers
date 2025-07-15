import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hacker.settings')
django.setup()

from hackathon.models import Category, Subcategory

# Sample categories and subcategories
categories_data = [
    {
        'name': 'Programming',
        'subcategories': ['Python', 'JavaScript', 'Java', 'C++', 'Web Development', 'Mobile Development']
    },
    {
        'name': 'Design',
        'subcategories': ['UI/UX Design', 'Graphic Design', 'Web Design', 'Logo Design', 'Illustration']
    },
    {
        'name': 'Business',
        'subcategories': ['Marketing', 'Finance', 'Management', 'Entrepreneurship', 'Sales']
    },
    {
        'name': 'Technology',
        'subcategories': ['Artificial Intelligence', 'Machine Learning', 'Data Science', 'Cloud Computing', 'Cybersecurity']
    },
    {
        'name': 'Creative Arts',
        'subcategories': ['Photography', 'Video Editing', 'Music Production', 'Digital Art', 'Animation']
    },
    {
        'name': 'Language',
        'subcategories': ['English', 'Spanish', 'French', 'German', 'Chinese', 'Japanese']
    },
    {
        'name': 'Health & Fitness',
        'subcategories': ['Yoga', 'Nutrition', 'Fitness Training', 'Mental Health', 'Wellness']
    },
    {
        'name': 'Education',
        'subcategories': ['Teaching Methods', 'Curriculum Design', 'Student Assessment', 'Educational Technology']
    }
]

# Create categories and subcategories
for cat_data in categories_data:
    category, created = Category.objects.get_or_create(name=cat_data['name'])
    print(f"{'Created' if created else 'Found'} category: {category.name}")
    
    for sub_name in cat_data['subcategories']:
        subcategory, created = Subcategory.objects.get_or_create(
            name=sub_name,
            category=category
        )
        print(f"  {'Created' if created else 'Found'} subcategory: {subcategory.name}")

print("\n✅ Sample categories and subcategories added successfully!") 