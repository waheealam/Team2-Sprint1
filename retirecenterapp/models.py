from django.db import models
from django.utils import timezone
from phone_field import PhoneField
from django.contrib.auth.models import User

class Profile(models.Model):
    RoleTypes = (('admin','Admin'),('maint','Maintenance'),('staff', 'Staff'),('resident', 'Resident'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(null=True,max_length=30)
    last_name = models.CharField(null=True,max_length=30)
    email = models.EmailField(null=True,unique=True)
    role = models.CharField(choices=RoleTypes,max_length=254)
    phone = PhoneField(blank=True, help_text='User phone number')
    altcontact = models.EmailField(null=True,max_length=254)
    REQUIRED_FIELDS = ['first_name','last_name','email','role','phone']

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.id)

class Apartment(models.Model):
    aptBuilding = models.CharField(max_length=50)
    aptRoomNum = models.IntegerField()
    aptFloor = models.IntegerField()

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.id)

class Apt_Resident(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    AptID = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    startDate = models.DateField()

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.id)

class Order(models.Model):
    PriorityOptions = (('High','High'),('Medium','Medium'),('Low', 'Low'))
    StatusOptions = (('New','New'),('Assigned','Assigned'),('In Progress', 'In Progress'),('Closed', 'Closed'))
    ProbType = (('Plumbing','Plumbing'),('Electrical','Electrical'),('Appliance', 'Appliance'),('Other', 'Other'))
    aptID = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    ordDescription = models.TextField()
    created_date = models.DateField()
    ordPriority = models.CharField(choices=PriorityOptions,default='Low', max_length=50)
    ordStatus = models.CharField(choices=StatusOptions,default='New', max_length=50)
    ordProbType = models.CharField(choices=ProbType, max_length=50)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.id)

class Assign_Order(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.id)

class OrderComment(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    commDate = models.DateField(editable=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.id)