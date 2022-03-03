from pyexpat import model
from xml.dom.domreg import registered
from django.contrib import admin

# Register your models here.

# typically user models don't need to
# be registered

# but as the user is created as a model
# that's why it needs to be registered

from . models import User

admin.site.register(User)

