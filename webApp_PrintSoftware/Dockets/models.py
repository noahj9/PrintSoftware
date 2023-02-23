from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from invitations.utils import get_invitation_model
from multiselectfield import MultiSelectField

# for sending invitation to new users
# Invitation = get_invitation_model()

class Client(models.Model): #database table to hold all client names
    name = models.CharField(max_length = 100)
    def __unicode__(self):
        return u"%i" % self.name

    def __str__(self):
        return self.name
    

class Contact(models.Model): #for contact names, each contact belongs to a client, each client can have >1 contact
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    client = models.ForeignKey(Client, null = True, on_delete=models.SET_NULL)
    def __unicode__(self):
        return u"%i" % self.name
    def __str__(self):
        return self.name

class Csr(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return u"%i" % self.name    
    def __str__(self):
        return self.name
class Rep(models.Model):
    name = models.CharField(max_length=100)
    csr = models.ForeignKey(Csr, null = True, on_delete=models.SET_NULL) #foreign key means each rep can have a CSR, null means it isnt mandatory, on delete will set value to null instead of deletion
    def __unicode__(self):
        return u"%i" % self.name
    def __str__(self):
        return self.name    

class Machine(models.Model):
    name = models.CharField(max_length=100)
    ink = models.BooleanField(default=True)
    def __unicode__(self):
        return u"%i" % self.name
    def __str__(self):
        return self.name

class Ink(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return u"%i" % self.name    
    def __str__(self):
        return self.name

class Proof(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return u"%i" % self.name    
    def __str__(self):
        return self.name

class Stock(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return u"%i" % self.name    
    def __str__(self):
        return self.name

class Terms(models.Model):
    term = models.CharField(max_length=200)
    def __unicode__(self):
        return u"%i" % self.term    
    def __str__(self):
        return self.term

class Deposit(models.Model):
    deposit = models.CharField(max_length=200)
    def __unicode__(self):
        return u"%i" % self.deposit    
    def __str__(self):
        return self.deposit

class Docket(models.Model): #contains all the data for a docket to be stored in the database
    customer_name = models.ForeignKey(Client, null = True, on_delete=models.SET_NULL)
    date = models.DateField(default=datetime.date.today) #custom field form widgets
    date_required = models.DateField()
    flexibility = models.CharField(max_length = 100)
    contact = models.ForeignKey(Contact, null = True, on_delete=models.SET_NULL)
    terms = models.ForeignKey(Terms, null = True, on_delete=models.SET_NULL)
    customer_PO = models.CharField(max_length = 100)
    quote = models.CharField(max_length=100, null=True)
    deposit = models.ForeignKey(Deposit, null = True, on_delete=models.SET_NULL)
    deposit_amount = models.CharField(max_length=100, blank=True, null=True)
    rep = models.ForeignKey(Rep, null = True, on_delete=models.SET_NULL)
    csr = models.ForeignKey(Csr, null = True, on_delete=models.SET_NULL)
    reception_notes = models.TextField(blank=True)
    #
    #section 1
    quantity_1 = models.CharField(max_length = 100)
    description_1 = models.CharField(max_length = 100)
    finished_size_1 = models.CharField(max_length = 100)
    stock1_1 = models.CharField(max_length = 100)
    stock1_2 = models.CharField(max_length = 100, null = True, blank = True)
    stock1_3 = models.CharField(max_length = 100, null = True, blank = True)
    machine_1 = MultiSelectField(choices = list(Machine.objects.all().values_list("name", "name")))
    run_quantity_1 = models.CharField(max_length = 100, blank = True)
    sheet_size_1 = models.CharField(max_length = 100)
    run_size_1 = models.CharField(max_length = 100)
    proof_1 = models.CharField(max_length = 100)
    inks1_1 = models.CharField(max_length = 100, blank = True)
    inks1_other1 = models.CharField(max_length=100, blank = True)
    inks1_2 = models.CharField(max_length = 100, blank = True)
    inks1_other2 = models.CharField(max_length=100, blank = True)
    inks1_3 = models.CharField(max_length = 100, blank = True)
    inks1_other3 = models.CharField(max_length=100, blank = True)
    instructions_1 = models.TextField(blank=True)
    bindery_1 = models.CharField(max_length = 100)
    file_1 = models.CharField(max_length = 100)
    price_comission_1 = models.CharField(max_length = 100)
    shipping_1 = models.CharField(max_length = 100)
    #
    #
    #section 2
    quantity_2 = models.CharField(max_length = 100, blank = True)
    description_2 = models.CharField(max_length = 100, blank = True)
    finished_size_2 = models.CharField(max_length = 100, blank = True)
    stock2_1 = models.CharField(max_length = 100, null = True, blank = True)
    stock2_2 = models.CharField(max_length = 100, null = True, blank = True)
    stock2_3 = models.CharField(max_length = 100, null = True, blank = True)
    machine_2 = MultiSelectField(choices = list(Machine.objects.all().values_list("name", "name")), blank = True)
    run_quantity_2 = models.CharField(max_length = 100, blank = True)
    sheet_size_2 = models.CharField(max_length = 100, blank = True)
    run_size_2 = models.CharField(max_length = 100, blank = True)
    proof_2 = models.CharField(max_length = 100, null = True, blank = True)
    inks2_1 = models.CharField(max_length = 100, blank = True)
    inks2_other1 = models.CharField(max_length=100, blank = True)
    inks2_2 = models.CharField(max_length = 100, blank = True)
    inks2_other2 = models.CharField(max_length=100, blank = True)
    inks2_3 = models.CharField(max_length = 100, blank = True)
    inks2_other3 = models.CharField(max_length=100, blank = True)
    instructions_2 = models.TextField(blank=True)
    bindery_2 = models.CharField(max_length = 100, blank = True)
    file_2 = models.CharField(max_length = 100, blank = True)
    price_comission_2 = models.CharField(max_length = 100, blank = True)
    shipping_2 = models.CharField(max_length = 100, blank = True)
    #
    #section 3
    quantity_3 = models.CharField(max_length = 100, blank = True)
    description_3 = models.CharField(max_length = 100, blank = True)
    finished_size_3 = models.CharField(max_length = 100, blank = True)
    stock3_1 = models.CharField(max_length = 100, null = True, blank = True)
    stock3_2 = models.CharField(max_length = 100, null = True, blank = True)
    stock3_3 = models.CharField(max_length = 100, null = True, blank = True)
    machine_3 = MultiSelectField(choices = list(Machine.objects.all().values_list("name", "name")), blank = True)
    run_quantity_3 = models.CharField(max_length = 100, blank = True)
    sheet_size_3 = models.CharField(max_length = 100, blank = True)
    run_size_3 = models.CharField(max_length = 100, blank = True)
    proof_3 = models.CharField(max_length = 100, null = True, blank = True)
    inks3_1 = models.CharField(max_length = 100, blank = True)
    inks3_other1 = models.CharField(max_length=100, blank = True)
    inks3_2 = models.CharField(max_length = 100, blank = True)
    inks3_other2 = models.CharField(max_length=100, blank = True)
    inks3_3 = models.CharField(max_length = 100, blank = True)
    inks3_other3 = models.CharField(max_length=100, blank = True)
    instructions_3 = models.TextField(blank=True)
    bindery_3 = models.CharField(max_length = 100, blank = True)
    file_3 = models.CharField(max_length = 100, blank = True)
    price_comission_3 = models.CharField(max_length = 100, blank = True)
    shipping_3 = models.CharField(max_length = 100, blank = True)


    def __int__(self):
        return self.id


