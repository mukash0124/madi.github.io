# Generated by Django 4.1.3 on 2023-02-12 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=13)),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('description', models.CharField(default='Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nihil saepe exercitationem error fugiat ipsum quis, sed harum placeat possimus, consequatur accusantium. Cum eius molestias numquam consequatur? Placeat culpa sit ipsa vero ea, accusantium modi qui neque excepturi? Perferendis recusandae suscipit laboriosam fuga doloremque ullam beatae inventore quis! Non aspernatur tempora dolorem accusantium at corporis ducimus deleniti id officia cum ea ab quis animi voluptatum, nostrum culpa pariatur eligendi vel, unde, inventore dicta doloribus porro repellat esse. Debitis, sint non! Magni maiores nesciunt, odio nostrum corporis nulla saepe maxime praesentium, quos libero fugit! Nesciunt recusandae numquam voluptas laudantium nisi enim nostrum rerum accusamus nam velit excepturi porro perferendis expedita modi id, nobis veritatis. Atque exercitationem obcaecati reiciendis nisi accusamus pariatur quia. Modi dolorum perferendis sequi incidunt alias iusto sit iure suscipit sapiente, officia natus perspiciatis minus delectus cumque quis exercitationem labore corporis. Ea maiores itaque, quia corporis aut sed vitae quam expedita, quas asperiores ad? Natus impedit, asperiores at consequuntur nam voluptas quos accusamus quidem tempora. Earum, repudiandae! Ipsam, ullam praesentium. Illum laudantium modi ratione repellendus deleniti dolor commodi dolorum illo ducimus, adipisci rem voluptas voluptatum libero vero reprehenderit explicabo. Temporibus ad consequuntur in est laborum ex totam laboriosam maiores id.', max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
