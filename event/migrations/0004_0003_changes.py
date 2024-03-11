from django.db import migrations
from django.db import models

class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_adding_constraints'),
    ]

    operations = [
        migrations.RunSQL(
            # Forward SQL for applying the migration
            sql="""
                -- Removes the 'available_places' column, if present, losing any existing data in the column
                ALTER TABLE event_event
                DROP COLUMN IF EXISTS available_places;
                
                -- Adds 'available_places' column again but allows NULL values this time
                ALTER TABLE event_event
                ADD COLUMN available_places INTEGER DEFAULT NULL;
            """,

            # Reverse SQL for reverting the migration
            reverse_sql="""
                -- Drop the modified 'available_places' column to revert changes
                ALTER TABLE event_event
                DROP COLUMN available_places;
                
                -- Re-add 'available_places' column with original settings if applicable
                ALTER TABLE event_event
                ADD COLUMN available_places INTEGER NOT NULL DEFAULT 0;
            """,

            # Provide a state_operations list to describe the state change in Django's migration system
            state_operations=[
                migrations.AlterField(
                    model_name='event',
                    name='available_places',
                    field=models.IntegerField(null=True, default=None),
                ),
            ]
        ),
    ]
