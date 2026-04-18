from django.db import models
from django.utils.text import slugify


class ServiceCategory(models.Model):

    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)

    description = models.TextField(blank=True)

    icon = models.ImageField(upload_to='service_categories/', blank=True, null=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Service(models.Model):

    category = models.ForeignKey(
        ServiceCategory,
        related_name="services",
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=150)

    slug = models.SlugField(unique=True, blank=True)

    description = models.TextField()

    image = models.ImageField(upload_to="services/", blank=True, null=True)

    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    estimated_duration = models.CharField(max_length=50, blank=True)

    is_available = models.BooleanField(default=True)

    is_featured = models.BooleanField(default=False)

    popularity_score = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-popularity_score", "name"]

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ServiceTag(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ServiceTagMapping(models.Model):

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    tag = models.ForeignKey(ServiceTag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.service.name} - {self.tag.name}"