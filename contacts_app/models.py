from django.db import models
from django.contrib.auth.models import User

#user type [admin,subscriber]
#Subscription_type [free,paid,system]

class Contact(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	contact_type=models.CharField(max_length=200, null=True)
	full_name=models.CharField(max_length=200, null=True)
	first_name=models.CharField(max_length=200, null=True)
	middle_name=models.CharField(max_length=200, null=True)
	last_name=models.CharField(max_length=200, null=True)
	company=models.CharField(max_length=200, null=True)
	designation=models.CharField(max_length=200, null=True)
	emailid=models.EmailField(max_length=200, null=True)
	aadhar=models.CharField(max_length=12, null=True)
	pan_card=models.CharField(max_length=10, null=True)
	phone=models.CharField(max_length=10, null=True)
	location=models.CharField(max_length=200, null=True)
	gender=models.CharField(max_length=10, null=True)
	title=models.CharField(max_length=200, null=True)
	department=models.CharField(max_length=200, null=True)
	university=models.CharField(max_length=200, null=True)
	degree=models.CharField(max_length=200, null=True)
	passing_year=models.CharField(max_length=200, null=True)
	college=models.CharField(max_length=200, null=True)
	linkedin=models.URLField(null=True)
	facebook=models.URLField(null=True)
	instagram=models.URLField(null=True)
	industry=models.CharField(max_length=200, null=True)
	country=models.CharField(max_length=200, null=True)
	state=models.CharField(max_length=200, null=True)
	pin_code=models.CharField(max_length=200, null=True)
	key_skills=models.CharField(max_length=200, null=True)
	total_experience=models.CharField(max_length=200, null=True)
	years_in_business=models.CharField(max_length=200, null=True)
	cin_no=models.CharField(max_length=200, null=True)
	turnover=models.CharField(max_length=200,default="0", null=True)
	date_of_incorporation=models.CharField(max_length=200,null=True)
	employees=models.CharField(max_length=200, null=True)
	ctc=models.CharField(max_length=200, null=True)
	notes=models.CharField(max_length=200, null=True)
	remarks=models.CharField(max_length=200, null=True)
	status=models.CharField(max_length=200, null=True)
 
	
class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200, null=True)
    email = models.EmailField()
    subscription_type = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=13, null=True)

class SaveSearch(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	search_criteria=models.CharField(max_length=200)

	
class Limit(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	total_limit=models.CharField(max_length=200)
	validation_date=models.DateField()
	balance=models.CharField(max_length=200)
	
	def __str__(self):
             return "%d  %d" % (self.total_limit, self.balance)

class View(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	view_contact=models.CharField(max_length=200)
	
	def __str__(self):
             return "%s" % (self.view_contact)

class Score(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	method=models.CharField(max_length=200)
	status=models.CharField(max_length=1)
	creation_date=models.ForeignKey(User, related_name="creation_date_of_record",on_delete=models.CASCADE)

class Method(models.Model):
	score=models.ForeignKey(Score, related_name="score_id_for_matrix", on_delete=models.CASCADE)
	fields=models.CharField(max_length=200)
	weightage=models.CharField(max_length=200)
	
	
	
	
	
	

