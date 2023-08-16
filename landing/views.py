from django.shortcuts import render

from .models import Experience, Education, SoftSkill, HardSkill, Language, Course, Proud, Referee


def index(request):
    experiences = Experience.objects.order_by('-started')
    educations = Education.objects.order_by('-started')
    soft_skills = SoftSkill.objects.all()
    hard_skills = HardSkill.objects.all()
    languages = Language.objects.all()
    courses = Course.objects.order_by('-started')
    prouds = Proud.objects.all()
    referees = Referee.objects.all()
    context = {
        'experiences': experiences,
        'educations': educations,
        'soft_skills': soft_skills,
        'hard_skills': hard_skills,
        'languages': languages,
        'courses': courses,
        'prouds': prouds,
        'referees': referees
    }
    return render(request, 'landing/index.html', context)