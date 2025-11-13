from rest_framework import serializers
from .models import Employment, EmploymentSkills, Projects, ProjectSkills, Skills, SkillsType

class EmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employment
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class SkillsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillsType
        fields = '__all__'

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class EmploymentSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentSkills
        fields = '__all__'

class ProjectSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSkills
        fields = '__all__'