from rest_framework import serializers
from .models import *

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', 'level']

class ResumeSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    avg_rating = serializers.ReadOnlyField() 
    
    class Meta:
        model = Resume
        fields = '__all__'
        
class PreviousJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousJob
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'