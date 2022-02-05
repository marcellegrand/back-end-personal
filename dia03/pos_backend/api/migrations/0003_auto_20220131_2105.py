# Generated by Django 3.2 on 2022-02-01 02:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_pedido_pedidoplatos'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoPlato',
            fields=[
                ('pedidoplato_id', models.AutoField(primary_key=True, serialize=False)),
                ('pedidoplato_cant', models.IntegerField(default=1, verbose_name='cantidad')),
            ],
        ),
        migrations.AlterField(
            model_name='pedido',
            name='mesa_id',
            field=models.ForeignKey(db_column='mesa_id', on_delete=django.db.models.deletion.RESTRICT, related_name='PedidoMesa', to='api.mesa', verbose_name='mesa'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='usu_id',
            field=models.ForeignKey(db_column='usu_id', on_delete=django.db.models.deletion.RESTRICT, related_name='PedidoUsuario', to=settings.AUTH_USER_MODEL, verbose_name='usuario'),
        ),
        migrations.DeleteModel(
            name='PedidoPlatos',
        ),
        migrations.AddField(
            model_name='pedidoplato',
            name='pedido_id',
            field=models.ForeignKey(db_column='pedido_id', on_delete=django.db.models.deletion.RESTRICT, related_name='PlatoPedido', to='api.pedido', verbose_name='pedido'),
        ),
        migrations.AddField(
            model_name='pedidoplato',
            name='plato_id',
            field=models.ForeignKey(db_column='plato_id', on_delete=django.db.models.deletion.RESTRICT, related_name='PedidoPlato', to='api.plato', verbose_name='plato'),
        ),
    ]