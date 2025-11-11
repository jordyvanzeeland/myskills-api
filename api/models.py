from django.db import models

class Employment(models.Model):
    id = models.AutoField(primary_key=True)
    employer = models.CharField(max_length=255, null=False, blank=False)
    function = models.CharField(max_length=255, null=False, blank=False)
    dateStart = models.DateTimeField(max_length=100, null=False, blank=False)
    dateEnd = models.DateTimeField(max_length=100, null=False, blank=False)

class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    dateStart = models.DateTimeField(max_length=100, null=False, blank=False)
    dateEnd = models.DateTimeField(max_length=100, null=False, blank=True)

class SkillsType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)

class Skills(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    type = models.ForeignKey(SkillsType, on_delete=models.CASCADE)

class EmploymentSkills(models.Model):
    id = models.AutoField(primary_key=True)
    employmentid = models.ForeignKey(Employment, on_delete=models.CASCADE)
    skillid = models.ForeignKey(Skills, on_delete=models.CASCADE)
    skillStartDate = models.DateTimeField(max_length=100, null=False, blank=True)

class ProjectSkills(models.Model):
    id = models.AutoField(primary_key=True)
    projectid = models.ForeignKey(Projects, on_delete=models.CASCADE)
    skillid = models.ForeignKey(Skills, on_delete=models.CASCADE)
    skillStartDate = models.DateTimeField(max_length=100, null=False, blank=True)