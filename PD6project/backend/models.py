from django.db import models
from django.utils import timezone

NAME_SIZE = 30
PHONE_SIZE = 14
ZIPCODE_SIZE = 5
TYPE_SIZE = 30
MEASURE_SIZE = 6
MEASURE_DECIMAL_SIZE = 6


# Create your models here.
class Client(models.Model):
    # PK
    # client_ID

    client_name = models.CharField(max_length=NAME_SIZE)
    client_type = models.CharField(max_length=NAME_SIZE)

    def __str__(self):
        return self.client_name


class User(models.Model):
    # PK
    # userID

    first_name = models.CharField(max_length=NAME_SIZE)
    last_name = models.CharField(max_length=NAME_SIZE)
    middle_name = models.CharField(max_length=NAME_SIZE)
    job_title = models.CharField(max_length=NAME_SIZE)
    email = models.EmailField()
    office_phone = models.CharField(max_length=PHONE_SIZE)
    cell_phone = models.CharField(max_length=PHONE_SIZE)
    prefix = models.CharField(max_length=NAME_SIZE)

    # FK
    client_ID = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name


class TestStandard(models.Model):
    # PK
    # standard_ID

    standard_name = models.CharField(max_length=NAME_SIZE)
    description = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.standard_name


class Location(models.Model):
    # PK
    # location_ID

    address1 = models.CharField(max_length=NAME_SIZE)
    address2 = models.CharField(max_length=NAME_SIZE)
    city = models.CharField(max_length=NAME_SIZE)
    state = models.CharField(max_length=NAME_SIZE)
    postal_code = models.CharField(max_length=ZIPCODE_SIZE)
    country = models.CharField(max_length=NAME_SIZE)
    phone_number = models.CharField(max_length=PHONE_SIZE)
    fax_number = models.CharField(max_length=PHONE_SIZE)
    # FK
    client_ID = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.address1


class Product(models.Model):
    # PK
    # model_number

    product_name = models.CharField(max_length=NAME_SIZE)
    cell_technology = models.CharField(max_length=NAME_SIZE)
    cell_manufacturer = models.CharField(max_length=NAME_SIZE)
    number_of_cells = models.PositiveIntegerField()
    number_of_cells_in_series = models.PositiveIntegerField()
    number_of_series_strings = models.PositiveIntegerField()
    number_of_diodes = models.PositiveIntegerField()
    product_length = models.DecimalField(decimal_places=MEASURE_SIZE, max_digits=MEASURE_DECIMAL_SIZE)
    product_width = models.DecimalField(decimal_places=MEASURE_SIZE, max_digits=MEASURE_DECIMAL_SIZE)
    product_weight = models.DecimalField(decimal_places=MEASURE_SIZE, max_digits=MEASURE_DECIMAL_SIZE)
    superstrate_type = models.CharField(max_length=TYPE_SIZE)
    superstrate_manufacturer = models.CharField(max_length=NAME_SIZE)
    substrate_type = models.CharField(max_length=TYPE_SIZE)
    substrate_manufacturer = models.CharField(max_length=NAME_SIZE)
    frame_type = models.CharField(max_length=TYPE_SIZE)
    frame_adhesive = models.CharField(max_length=NAME_SIZE)
    encapsulate_type = models.CharField(max_length=TYPE_SIZE)
    encapsulant_manufacturer = models.CharField(max_length=NAME_SIZE)
    junction_box_type = models.CharField(max_length=TYPE_SIZE)
    junction_box_manufacturer = models.CharField(max_length=NAME_SIZE)
    objects = models.Manager()

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['product_name']



class Certificate(models.Model):
    # PK
    # certificate_number

    report_number = models.CharField(max_length=NAME_SIZE)
    issue_date = models.DateField()
    # FK
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    standard_ID = models.ForeignKey(TestStandard, on_delete=models.CASCADE)
    location_ID = models.ForeignKey(Location, on_delete=models.CASCADE)
    model_number = models.ForeignKey(Product, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.report_number

    class Meta:
        ordering = ['report_number']


class TestSequence(models.Model):
    # PK
    # sequence_ID

    sequence_name = models.CharField(max_length=NAME_SIZE)

    def __str__(self):
        return self.sequence_name


class PerformanceData(models.Model):

    max_system_voltage = models.DecimalField(decimal_places=MEASURE_SIZE, max_digits=MEASURE_DECIMAL_SIZE)
    voc = models.DecimalField(decimal_places=MEASURE_SIZE, max_digits=MEASURE_DECIMAL_SIZE)
    isc = models.DecimalField(decimal_places=MEASURE_SIZE, max_digits=MEASURE_DECIMAL_SIZE)
    vmp = models.DecimalField(decimal_places=MEASURE_SIZE, max_digits=MEASURE_DECIMAL_SIZE)
    imp = models.DecimalField(decimal_places=MEASURE_SIZE, max_digits=MEASURE_DECIMAL_SIZE)
    pmp = models.DecimalField(decimal_places=MEASURE_SIZE, max_digits=MEASURE_DECIMAL_SIZE)
    ff = models.DecimalField(decimal_places=MEASURE_SIZE, max_digits=MEASURE_DECIMAL_SIZE)

    # PKFK
    model_number = models.ForeignKey(Product, on_delete=models.CASCADE)
    sequence_ID = models.ForeignKey(TestSequence, on_delete=models.CASCADE)

    def __str__(self):
        return self.max_system_voltage


class Service(models.Model):
    # PK
    # service_ID

    service_name = models.CharField(max_length=NAME_SIZE)
    description = models.TextField()
    is_fi_required = models.BooleanField()
    fi_frequency = models.DecimalField(decimal_places=MEASURE_SIZE, max_digits=MEASURE_DECIMAL_SIZE)

    # FK
    standard_ID = models.ForeignKey(TestStandard, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.service_name

    class Meta:
        ordering = ['service_name']

