from django.db import models
from parler.models import TranslatableModel,TranslatedFields


# Create your models here.
class Author(TranslatableModel):
    class RoleChoises(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        WRITER = 'writer', 'Writer'

    image = models.ImageField(upload_to='authors/images/')

    translations = TranslatedFields(
    firts_name = models.CharField(max_length=255),
    last_name = models.CharField(max_length=255),
    bio = models.TextField(),
    role = models.CharField(max_length=255, choices=RoleChoises.choices,default=RoleChoises.ADMIN),
    about_author = models.TextField(),
    )
    
    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return None
    
    def __str__(self):
        return self.safe_translation_getter('first_name','last_name',any_language=True)
    






