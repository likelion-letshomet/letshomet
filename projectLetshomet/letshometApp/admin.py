from django.contrib import admin
from .models import LetsHometDb
from .models import User
from .models import Recommend_Post
from .models import Subscribe_Cart
from .models import Review_Post
from .models import Review_Comment
from .models import Recommend_Comment

# Register your models here.
admin.site.register(LetsHometDb)
admin.site.register(User)
admin.site.register(Recommend_Post)
admin.site.register(Subscribe_Cart)
admin.site.register(Review_Post)
admin.site.register(Review_Comment)
admin.site.register(Recommend_Comment)
