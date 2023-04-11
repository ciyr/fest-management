# Generated by Django 4.2 on 2023-04-10 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('club_id', models.IntegerField(primary_key=True, serialize=False)),
                ('club_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_email', models.CharField(max_length=50)),
                ('customer_phone', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.IntegerField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('event_venue', models.CharField(max_length=50)),
                ('total_tickets', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('performer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('performer_name', models.CharField(max_length=50)),
                ('performer_genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('sponsor_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sponsor_name', models.CharField(max_length=50)),
                ('sponsor_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_id', models.IntegerField(primary_key=True, serialize=False)),
                ('vendor_name', models.CharField(max_length=50)),
                ('vendor_location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_price', models.IntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fests.customer')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fests.event')),
            ],
        ),
        migrations.CreateModel(
            name='Organizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fests.club')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fests.event')),
            ],
        ),
        migrations.CreateModel(
            name='EventVendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fests.event')),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='fests.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='EventSponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fests.event')),
                ('sponsor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='fests.sponsor')),
            ],
        ),
        migrations.CreateModel(
            name='EventPerformer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fests.event')),
                ('performer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='fests.performer')),
            ],
        ),
    ]
