
from django.contrib.auth.models import User

user = User.objects.create_user('Eugene', 'rullrow@gmail.com', 'wfadmin123!')

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
user.last_name = 'Lee'
user.save()


