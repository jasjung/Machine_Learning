from django.contrib import admin

# Register your models here.
from .models import Choice, Question
# v1
# admin.site.register(Question)

# v2
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
# admin.site.register(Question, QuestionAdmin)

# v3 
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)

# v4 
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)


