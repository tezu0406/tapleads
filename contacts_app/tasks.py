from celery import shared_task

from .models import Contact, User, Score, UserData, Method, Field

@shared_task(bind=True)
def recalculate(x, user_id):
    contacts = Contact.objects.all()
    user = User.objects.get(id=user_id)
    user_data = UserData.objects.get(user=user)
    fields = Field.objects.filter(method=user_data.current_method)
    for contact in contacts:
        value = 0
        for field in fields:
            if(getattr(contact, field.name) != None):
                value += field.weightage
        score = Score.objects.filter(contact=contact, user=user).first()
        if score == None:
            score = Score(contact=contact, user=user)
        score.value = value
        score.save()