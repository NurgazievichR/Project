from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField

class Tag(models.Model):
    title = models.CharField('Название',max_length=255, unique=True)
    url = models.SlugField('Ссылка', max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
 

class Category(models.Model):
    ICONS = [
        ('https://radiustheme.com/demo/wordpress/themes/ranna/wp-content/uploads/2020/05/bread-red.png','piece of bread'),
        ('https://radiustheme.com/demo/wordpress/themes/ranna/wp-content/uploads/2020/05/burger-4.png','burger'),
        ('https://radiustheme.com/demo/wordpress/themes/ranna/wp-content/uploads/2020/05/salad.png','vegetables'),
        ('https://radiustheme.com/demo/wordpress/themes/ranna/wp-content/uploads/2020/05/fish-red.png','fish'),
        ('https://radiustheme.com/demo/wordpress/themes/ranna/wp-content/uploads/2020/05/desert-red.png','pie'),
        ('https://radiustheme.com/demo/wordpress/themes/ranna/wp-content/uploads/2020/05/soup-red.png','soup'),
    ]
    ICONS_TWO = [
        ('https://radiustheme.com/demo/wordpress/themes/ranna/wp-content/uploads/2020/05/bread-white.png','piece of bread'),
        ('https://radiustheme.com/demo/wordpress/themes/ranna/wp-content/uploads/2020/05/sandwich-white.png','burger'),
        ('https://radiustheme.com/demo/wordpress/themes/ranna/wp-content/uploads/2020/05/salad-white.png','vegetables'),
        ('https://radiustheme.com/demo/wordpress/themes/ranna/wp-content/uploads/2020/05/fish-white.png','fish'),
        ('https://radiustheme.com/demo/wordpress/themes/ranna/wp-content/uploads/2020/05/desert-write.png','pie'),
        ('https://radiustheme.com/demo/wordpress/themes/ranna/wp-content/uploads/2020/05/soup.png','soup'),
    ]
    title = models.CharField('Название',max_length=255, unique=True)
    image = models.ImageField('Фото', upload_to='category_images/', blank=True)
    icon = models.CharField('Иконка', max_length=100, choices=ICONS, help_text='Желательно выбирать одинаковые иконки')
    icon2 = models.CharField('Иконка2', max_length=100, choices=ICONS_TWO, help_text='Желательно выбирать одинаковые иконки')
    url = models.SlugField('Ссылка', max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    CUISINE = [
        ('Italian','Italian'),
        ('Japanese','Japanese'),
        ('Thai','Thai'),
        ('Russian','Russian'),
        ('Korean','Korean'),
        ('Chinese','Chinese'),
        ('American','American'),
    ]
    DIFFICULTY = [
        ('easy','easy'),
        ('medium','medium'),
        ('difficult','difficult'),
    ]
    TIME = [ tuple(([i,k])) for i,k in enumerate(range(121))]   
    TIME_ = [ tuple(([i,k])) for i,k in enumerate(range(13))]   

    title = models.CharField('Название',max_length=255)
    image = models.ImageField('Фото', upload_to='product_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='children', verbose_name='Категория')
    tag = models.ManyToManyField(Tag, related_name='children', verbose_name='Теги' )
    date = models.DateField(auto_now=True, null=True)
    url = models.SlugField('Ссылка', max_length=255, unique=True)

    recipe = models.CharField('Рецепты', max_length=550, help_text='Пишите рецепт через точка-запятую')
    description = RichTextField('Описание')
    step_one = models.TextField('Шаг 1')
    step_one_photo = models.ImageField('Фото 1', upload_to='product_images/' )
    step_two = models.TextField('Шаг 2')
    step_two_photo = models.ImageField('Фото 2', upload_to='product_images/' )
    step_three = models.TextField('Шаг 3')
    step_three_photo = models.ImageField('Фото 3', upload_to='product_images/' )
    step_four = models.TextField('Шаг 4', blank=True, null=True)
    step_four_photo = models.ImageField('Фото 4', upload_to='product_images/', blank=True, null=True)
    step_five = models.TextField('Шаг 5', blank=True, null=True)
    step_five_photo = models.ImageField('Фото 5', upload_to='product_images/', blank=True, null=True)

    cuisine = models.CharField('Страна', max_length=100, choices=CUISINE)
    difficulty = models.CharField('Сложность', max_length=100, choices=DIFFICULTY)
    prep_time = models.IntegerField('Время подготовки', choices=TIME)
    cook_time = models.IntegerField('Время готовки', choices=TIME)
    serving = models.IntegerField('Обслуживание', choices=TIME_)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукт'
 





