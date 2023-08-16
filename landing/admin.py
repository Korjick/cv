from django.contrib import admin

from .models import Experience, Duty, Education, SoftSkill, HardSkill, Language, Referee, Course, Proud


class EducationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'grade', 'institution', 'institution_url', 'started', 'ended')
    search_fields = ('title',)
    empty_value_display = '-пусто-'


class DutyAdmin(admin.ModelAdmin):
    list_display = ('title', 'experience')
    search_fields = ('experience', )
    list_editable = ('experience', )
    empty_value_display = '-пусто-'


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'company', 'company_url', 'started', 'ended', 'location')
    search_fields = ('company', )
    empty_value_display = '-пусто-'


class SoftSkillAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    search_fields = ('title', )
    empty_value_display = '-пусто-'


class HardSkillAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    search_fields = ('title', )
    empty_value_display = '-пусто-'


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'level', )
    search_fields = ('title', )
    empty_value_display = '-пусто-'


class RefereeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'job_title', 'email', 'address')
    search_fields = ('job_title', )
    empty_value_display = '-пусто-'


class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'institution', 'institution_url', 'started', 'ended', )
    search_fields = ('title', )
    empty_value_display = '-пусто-'


class ProudAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title', )
    empty_value_display = '-пусто-'


admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Duty, DutyAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(SoftSkill, SoftSkillAdmin)
admin.site.register(HardSkill, HardSkillAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Referee, RefereeAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Proud, ProudAdmin)
