from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from .managers import CategoryManager
from utils.views import group_queryset
from parler.models import TranslatableModel,TranslatedFields
from parler.managers import TranslatableManager
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.translation import gettext_lazy as _
from user.models import Author


class Category(TranslatableModel):
    slug = models.SlugField(verbose_name=_('slug'),unique=True, blank=True, null=True)
    translations = TranslatedFields(
        name = models.CharField(verbose_name=_('nomi'),max_length=255),
    )



    custom = CategoryManager()
    objects = TranslatableManager()
    
    

    def save(self, *args, **kwargs):
        if not self.slug and self.translations.name:
            self.slug = slugify(self.translations.name)
            counter = 1
            original_slug = self.slug
            while Category.custom.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    @property
    def get_group_blogs(self):
        return group_queryset(3, self.blog_set.all())

    @property
    def get_group_blogs_2(self):
        return group_queryset(2, self.blog_set.all())

    @property
    def get_group_blogs_6(self):
        return group_queryset(6, self.blog_set.all())
    
    
    @property
    def get_group_blogs_3(self):
        return group_queryset(3, self.blog_set.all())


    def __str__(self):
        return self.safe_translation_getter('name',any_language=True)
    
    class Meta:
        verbose_name = _("Kategoriya")
        verbose_name_plural = _("Kategoriyalar")

class Tag(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(verbose_name=_('nomi'),max_length=255)
    )

    def __str__(self):
        return self.safe_translation_getter('name',any_language=True)
    class Meta:
        verbose_name = _('Teg')
        verbose_name_plural = _("Teglar")

class Blog(TranslatableModel):
    class StatusEnum(models.TextChoices):
        PUBLISHED = 'published'
        DRAFT = 'draft'
    
    translations = TranslatedFields(
        title = models.CharField('Title', max_length=200),
        text = CKEditor5Field('Text',config_name='extends'),
        image = models.ImageField(verbose_name=_("Rasm"), upload_to='blog_images/',default="/media/blog_images/2f225e734996023d3f435e021fd40bc4_DOjbh4J.webp")
    )



    category = models.ForeignKey(Category, verbose_name=_("Kategoriya"), on_delete=models.SET_NULL, null=True)
    status = models.CharField(verbose_name=_("Status"), max_length=255, choices=StatusEnum.choices, default=StatusEnum.DRAFT)
    like = models.ManyToManyField(User, verbose_name=_("Like"), related_name="like", blank=True)
    seen = models.ManyToManyField(User, verbose_name=_("Korilgan"), related_name="seens", blank=True)
    tags = models.ManyToManyField(Tag, verbose_name=_("Hesh teg"))
    datetime = models.DateTimeField(verbose_name=_("Sana vaqt"), auto_now_add=True)
    

    @property
    def imageURL(self):
        image = self.safe_translation_getter('image', any_language=True)
        if image:
            return image.url
        return None


    def __str__(self):
        return self.safe_translation_getter('title',any_language=True)
    
    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Bloglar")


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE,null=True, blank=True, related_name='replies')

    def __str__(self):
        return f"{self.blog} - {self.user} - {self.text[:20]}"






