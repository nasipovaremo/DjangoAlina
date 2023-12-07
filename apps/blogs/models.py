from django.db import models



class Blog(models.Model):
    title = models.CharField(
        max_length=123,
        verbose_name="Name",
    )
    description = models.TextField(
        verbose_name="описание",
    )

    image = models.ImageField(
        upload_to="blogs/",
        verbose_name="Фото"
    )

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"