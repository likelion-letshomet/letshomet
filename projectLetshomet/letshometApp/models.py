from django.db import models

# Create your models here.
class LetsHometDb(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
            return self.title

    def summary(self):
        return self.body[:1]
        
#회원 --> email 추가
class User(models.Model):
    id = models.CharField(max_length = 20,primary_key = True)
    password = models.CharField(max_length = 30)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length= 30,null=True)
    gender = models.CharField(max_length = 30,null=True)
    age = models.IntegerField(null=True)
    

#추천 게시글 (null = True 는 오류 나는걸 막기위함)
class Recommend_Post(models.Model): 
    post_num = models.IntegerField(primary_key = True,auto_created=True)
    title = models.CharField(max_length = 30)
    context = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length = 30,null=True)
    like_num = models.IntegerField(null=True)
    post_url1 = models.CharField(max_length=500, null=True)## change imageField --> url 	
    post_url2 = models.CharField(max_length=500, null=True)## change imageField --> url 	
    post_url3 = models.CharField(max_length=500, null=True)## change imageField --> url 	
#구독 현황 바구니 추가

#*********title 외래키로 변경
class Subscribe_Cart(models.Model):
    cart_num = models.IntegerField(primary_key = True,auto_created=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    
    post_num = models.ForeignKey('Recommend_Post',on_delete=models.CASCADE)
    post_title = models.ForeignKey('Recommend_Post',on_delete=models.CASCADE,related_name='%(class)s_requests_created',null=True)


#홈트 현황관리 완주율 popup db
class Homet_Status(models.Model):
    subscribe_title = models.ForeignKey('Subscribe_Cart',on_delete=models.CASCADE)
    week = models.IntegerField()
    days = models.ImageField()

#후기 게시글
class Review_Post(models.Model):
    post_num = models.IntegerField(primary_key = True,auto_created=True)
    title = models.CharField(max_length = 30)
    context = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

#후기 게시글 댓글
class Review_Comment(models.Model):
    comment_num = models.IntegerField(primary_key = True,auto_created=True)
    context = models.TextField()
    post_num = models.ForeignKey('Review_Post',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

#추천 게시글 댓글
class Recommend_Comment(models.Model):
    comment_num = models.IntegerField(primary_key = True,auto_created=True)
    context = models.TextField()
    post_num = models.ForeignKey('Recommend_Post',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)