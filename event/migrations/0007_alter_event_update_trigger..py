from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_update_event_availability_improved'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                DROP TRIGGER event_update_after ON event_event;
                
                -- Create a new trigger for handling insert or update operations
                -- To avoid recursion issues, only 2 columns are used in trigger
                CREATE OR REPLACE TRIGGER event_after_insert_or_update
                AFTER INSERT OR UPDATE OF date, available_places
                ON event_event
                FOR EACH ROW
                EXECUTE FUNCTION update_event_availability();
            """
        ),
    ]
