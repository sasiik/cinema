# Generated by Django 5.0.2 on 2024-03-10 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_alter_event_available_places'),
    ]

    operations = [
        migrations.RunSQL(
            # To set the initial value of available_places to places_count of event.location
            sql=
            """
            CREATE OR REPLACE FUNCTION available_places_initial_set()
            RETURNS TRIGGER AS $$
            BEGIN
                IF NEW.available_places IS NULL THEN
                    NEW.available_places := (SELECT places_count FROM event_eventlocation WHERE event_eventlocation.id = NEW.location_id);
                END IF;
                RETURN NEW;
            END;
            $$ LANGUAGE plpgsql;
            
            CREATE TRIGGER update_available_places_initial
            BEFORE INSERT ON event_event
            FOR EACH ROW EXECUTE FUNCTION available_places_initial_set();

            """
            )
    ]
