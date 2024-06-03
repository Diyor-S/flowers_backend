# Generated by Django 5.0.2 on 2024-06-03 10:49

import common.utils
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number1', models.CharField(max_length=20, validators=[common.utils.validate_phone_number], verbose_name='phone number1')),
                ('phone_number2', models.CharField(max_length=20, validators=[common.utils.validate_phone_number], verbose_name='phone number2')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('address', models.CharField(max_length=150, verbose_name='address')),
                ('work_time', models.CharField(max_length=120, verbose_name='work time')),
            ],
            options={
                'verbose_name': 'Contacts',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('phone_number', models.CharField(max_length=120, validators=[common.utils.validate_phone_number], verbose_name='phone number')),
                ('status', models.CharField(choices=[('new', 'new'), ('accepted', 'accepted'), ('progress', 'progress'), ('cancelled', 'cancelled'), ('finished', 'finished')], default='new', max_length=20)),
                ('address', models.CharField(max_length=150, verbose_name='address')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('phone_number', models.CharField(max_length=20, validators=[common.utils.validate_phone_number], verbose_name='phone number')),
                ('question', models.TextField(verbose_name='question')),
            ],
            options={
                'verbose_name': 'Questions',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='category title')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='category image')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='product title')),
                ('special_offers', models.CharField(max_length=100, verbose_name='special offers')),
                ('occasion', models.CharField(max_length=100, verbose_name='occasion')),
                ('for_whom', models.CharField(max_length=200, verbose_name='for whom')),
                ('description', models.TextField(verbose_name='description')),
                ('status', models.BooleanField(default=True, verbose_name='status')),
                ('quantity', models.IntegerField(default=1, verbose_name='quantity')),
                ('price', models.IntegerField(verbose_name='price')),
                ('old_price', models.IntegerField(verbose_name='old price')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='product image')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.CharField(choices=[('cash', 'cash'), ('card', 'card'), ('card_private_bank', 'card private bank')], default='cash', max_length=50, verbose_name='payment')),
                ('delivery', models.CharField(choices=[('pick-up', 'pick-up'), ('delivery', 'delivery')], default='delivery', max_length=50, verbose_name='delivery')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='core.order', verbose_name='order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='core.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Order Product',
                'verbose_name_plural': 'Order Products',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='product images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='core.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Product Images',
                'verbose_name_plural': 'Product Images',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(verbose_name='review')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='core.product', verbose_name='product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='subcategory title')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='core.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'Sub Category',
                'verbose_name_plural': 'Sub Categories',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='core.subcategory', verbose_name='subcategory'),
        ),
        migrations.CreateModel(
            name='TogetherPurchased',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_product', to='core.product', verbose_name='product')),
                ('related_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_products', to='core.product', verbose_name='related products')),
            ],
            options={
                'verbose_name': 'Together Purchased',
                'verbose_name_plural': 'Together Purchased',
            },
        ),
    ]
