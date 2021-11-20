from django.db import models


#user type [admin,subscriber]
#Subscription_type [free,paid,system]

class User_table(models.Model):
	User_ID=models.IntegerField(primary_key=True)
	Username=models.CharField(max_length=200)
	Password=models.CharField(max_length=200)
	User_email=models.EmailField(max_length=200)
	User_Phone=models.CharField(max_length=10)
	Subscription_type=models.CharField(max_length=200)
	Creation_date=models.DateField()
	Name=models.CharField(max_length=200)
	Status=models.CharField(max_length=200)
	User_type=models.CharField(max_length=200)
	
	def __str__(self):
             return "%s %s" % (self.Username, self.Password)


class Contact_table(models.Model):
	Contact_ID=models.IntegerField(primary_key=True)
	Contact_type=models.CharField(max_length=200)
	Full_name=models.CharField(max_length=200)
	First_name=models.CharField(max_length=200)
	Middle_name=models.CharField(max_length=200)
	Last_name=models.CharField(max_length=200)
	Company=models.CharField(max_length=200)
	Designation=models.CharField(max_length=200)
	Emailid=models.EmailField(max_length=200)
	Aadhar=models.CharField(max_length=12)
	Pan_card=models.CharField(max_length=10)
	Phone=models.CharField(max_length=10)
	Location=models.CharField(max_length=200)
	Gender=models.CharField(max_length=10)
	Title=models.CharField(max_length=200)
	Department=models.CharField(max_length=200)
	University=models.CharField(max_length=200)
	Degree=models.CharField(max_length=200)
	Passing_year=models.IntegerField()
	College=models.CharField(max_length=200)
	LinkedIN=models.URLField()
	Facebook=models.URLField()
	Instagram=models.URLField()
	Industry=models.CharField(max_length=200)
	Country=models.CharField(max_length=200)
	State=models.CharField(max_length=200)
	Zip=models.IntegerField()
	Key_Skills=models.CharField(max_length=200)
	Total_Experience=models.CharField(max_length=200)
	Years_in_Business=models.CharField(max_length=200)
	CIN_No=models.CharField(max_length=200)
	Turnover=models.CharField(max_length=200)
	Date_of_Incorporation=models.DateField()
	Employees=models.CharField(max_length=200)
	CTC=models.CharField(max_length=200)
	Notes=models.CharField(max_length=200)
	Remarks=models.CharField(max_length=200)
	
	user_id = models.ForeignKey(User_table, on_delete=models.CASCADE)
	def __str__(self):
            return "%s %s" % (self.First_name, self.Phone)
class Save_search(models.Model):
	search_id=models.IntegerField(primary_key=True)
	Search_Criteria=models.CharField(max_length=200)
	user_id = models.ForeignKey(User_table, on_delete=models.CASCADE)
	
class Limit_table(models.Model):
	limit_id=models.IntegerField(primary_key=True)
	Total_limit=models.IntegerField()
	validation_date=models.DateField()
	balance=models.IntegerField()
	user_id = models.ForeignKey(User_table, on_delete=models.CASCADE)
	
	def __str__(self):
             return "%d  %d" % (self.Total_limit, self.balance)

class view_table(models.Model):
	view_id=models.IntegerField(primary_key=True)
	view_contact=models.IntegerField()
	user_id = models.ForeignKey(User_table, on_delete=models.CASCADE)
	
	def __str__(self):
             return "%d" % (self.view_contact)

class Score_tbl(models.Model):
	Method=models.CharField(max_length=200)
	Status=models.CharField(max_length=1)
	user_id=models.ForeignKey(User_table, on_delete=models.CASCADE)
	Creation_date=models.ForeignKey(User_table, related_name="creation_date_of_record",on_delete=models.CASCADE)
	Score_id=models.CharField(max_length=200)

class Method_tbl(models.Model):
	Score_id=models.ForeignKey(Score_tbl, related_name="score_id_for_matrix", on_delete=models.CASCADE)
	Fields=models.CharField(max_length=200)
	Weightage=models.IntegerField()
	
	
	
	
	
	

