from django.db import models
import datetime

# Create your models here.
class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted    = models.BooleanField(default=False)

class Records(BaseModel):
    class Meta:
        db_table = 'records'
    record_name = models.CharField("Record Name", max_length=100, null=True, blank=True)
    state = models.CharField("State", max_length=100, null=True, blank=True)
    dist = models.CharField("District", max_length=100, null=True, blank=True)
    institution_type = models.CharField("Institution Type",  max_length=255, blank=True, null=True)
    institution_name = models.CharField("Institution Name", max_length=255, null=True, blank=True)
    petitioner_name = models.CharField("Petitioner Name", max_length=255, null=True, blank=True)
    case_type = models.CharField("Case Type", max_length=255, null=True, blank=True)
    case_number = models.CharField("Case Number", max_length=255, null=True, blank=True)
    file_number = models.CharField("File Number", max_length=255, null=True, blank=True)
    counter_filed = models.BooleanField(default=False)
    cf_lr = models.CharField("CF letter no", max_length=100, null=True, blank=True)
    cf_dt = models.DateField(blank=True, null=True,default=datetime.date.today)
    date_of_order = models.DateField(blank=True, null=True,default=datetime.date.today)
    memorandum_sought = models.BooleanField(default=False)
    ms_lr = models.CharField("Memorandum sought letter no", max_length=100, null=True, blank=True)
    ms_dt = models.DateField(blank=True, null=True,default=datetime.date.today)
    memorandum_received = models.BooleanField(default=False)
    mr_lr = models.CharField("Memorandum Reveived letter no", max_length=100, null=True, blank=True)
    mr_dt = models.DateField(blank=True, null=True,default=datetime.date.today)
    status_of_comp = models.CharField("Status of compliance", max_length=100, null=True, blank=True)
    sc_lr = models.CharField("Status of comp letter no", max_length=100, null=True, blank=True)
    sc_dt = models.DateField(blank=True, null=True,default=datetime.date.today)
    fao_filed = models.BooleanField(default=False)
    fao_lr = models.CharField("FAO letter no", max_length=100, null=True, blank=True)
    fao_dt = models.DateField(blank=True, null=True,default=datetime.date.today)
    def __str__(self):
        return self.record_name

class State(BaseModel):
    class Meta:
        db_table = 'state'
    state_name = models.CharField("State", max_length=100, null=True, blank=True)
    def __str__(self):
        return self.state_name

class District(BaseModel):
    class Meta:
        db_table = 'district'
    dist_name = models.CharField("District", max_length=100, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return self.dist_name

class InstitutionType(BaseModel):
    class Meta:
        db_table = 'institution_type'
    institution_type = models.CharField("Institution Type", max_length=100, null=True, blank=True)
    def __str__(self):
        return self.institution_type

class InstitutionName(BaseModel):
    class Meta:
        db_table = 'institution_name'
    institution_name = models.CharField("Institution Name", max_length=100, null=True, blank=True)
    institution_type = models.ForeignKey(InstitutionType, on_delete=models.CASCADE)
    def __str__(self):
        return self.institution_name

class CaseType(BaseModel):
    class Meta:
        db_table = 'case_type'
    case_type = models.CharField("Case Type", max_length=100, null=True, blank=True) 
    def __str__(self):
        return self.case_type
    
     