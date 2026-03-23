from django.db import models

# Create your models here.

class Customer(models.Model):
    lastName = models.CharField(max_length=200)
    firstName = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    postalCode = models.CharField(max_length=200)

    def __str__(self):
        return self.firstName + " " + self.lastName

class Car(models.Model):
    serialNumber = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    colour = models.CharField(max_length=200)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    SaleName = models.CharField(max_length=200)

    def __str__(self):
        return self.serialNumber

class Salesperson(models.Model):
    lastName = models.CharField(max_length=200)
    firstName = models.CharField(max_length=200)

    def __str__(self):
        return self.firstName + " " + self.lastName

class SalesInvoice(models.Model):
    invoiceNum = models.DecimalField(max_digits=10, decimal_places=0)
    date = models.DateTimeField("date sold")
    carID = models.ForeignKey(Car, on_delete=models.CASCADE)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salespersonID = models.ForeignKey(Salesperson, on_delete=models.CASCADE)

    def __str__(self):
        return self.invoiceNum
    
class ServiceTicket(models.Model):
    serviceTicketNumber = models.CharField(max_length=200)
    carID = models.ForeignKey(Car, on_delete=models.CASCADE)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dateReceived = models.DateTimeField("date received")
    comments = models.CharField(max_length=200)
    dateReturned = models.DateTimeField("date returned")

class Mechanic(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)

    def __str__(self):
        return self.firstName + " " + self.lastName
    

class Service(models.Model):
    serviceName = models.CharField(max_length=200)
    hourlyRate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.serviceName

class ServiceMechanic(models.Model):
    serviceTicketID = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    serviceID = models.ForeignKey(Service, on_delete=models.CASCADE)
    mechanicID = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=5, decimal_places=0)
    comment = models.CharField(max_length=200)
    rate = models.DecimalField(max_digits=6, decimal_places=2)

class Parts(models.Model):
    partNumber = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    purchasePrice = models.DecimalField(max_digits=10, decimal_places=2)
    retailPrice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.serviceName

class PartsUsed(models.Model):
    partID = models.ForeignKey(Parts, on_delete=models.CASCADE)