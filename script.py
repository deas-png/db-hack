import random
from datacenter.models import *

def fix_marks(schoolkid):
	marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3])
	for mark in marks:
		mark.points = 5
		mark.save()
		
def remove_chastisements(schoolkid):
	chastisements = Сhastisement.objects.filter(schoolkid=schoolkid)
	chastisements.delete()

def add_random_commendation(schoolkid, subject_name):
    commendation_list = ['Молодец!','Хорошо!','Отлично!','Гораздо лучше, чем я ожидал!','Ты меня приятно удивил!','Великолепно!','Прекрасно!','Ты меня очень обрадовал!','Именно этого я давно ждал от тебя!','Сказано здорово – просто и ясно!','Ты, как всегда, точен!','Очень хороший ответ!','Талантливо!','Ты сегодня прыгнул выше головы!','Я поражен!','Уже существенно лучше!','Потрясающе!','Замечательно!','Прекрасное начало!','Так держать!','Ты на верном пути!','Здорово!','Это как раз то, что нужно!','Я тобой горжусь!','С каждым разом у тебя получается всё лучше!','Мы с тобой не зря поработали!','Я вижу, как ты стараешься!','Ты растешь над собой!','Ты многое сделал, я это вижу!','Теперь у тебя точно все получится!']
    lessons = Lesson.objects.filter(subject__title=subject_name, group_letter=schoolkid.group_letter, year_of_study=schoolkid.year_of_study)
    teacher = lessons[0].teacher
    created = lessons[0].date
    subject = lessons[0].subject
    text = random.choice(commendation_list)
    Commendation.objects.create(schoolkid=schoolkid,subject=subject,teacher=teacher,created=created,text=text)