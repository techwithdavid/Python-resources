# https://django-extensions.readthedocs.io/en/latest/create_template_tags.html
#create_template_tags

# Create templatetags directory for foobar app:
python3 manage.py create_template_tags foobar
#you can pass custom tags filename by providing --name argument:
python3 manage.py create_template_tags foobar --name custom_tags

#https://django-extensions.readthedocs.io/en/latest/delete_squashed_migrations.html
# delete_squashed_migrations

# Delete leftover migrations from the first squashed migration found in myapp
python3 manage.py delete_squashed_migrations myapp
# As above but non-interactive
python3 manage.py --noinput delete_squashed_migrations myapp
# Explicitly specify the squashed migration to clean up
python3 manage.py delete_squashed_migrations myapp 0001_squashed

# https://django-extensions.readthedocs.io/en/latest/dumpscript.html
# dumpscript

# https://django-extensions.readthedocs.io/en/latest/runscript.html#usage
# runscript

# https://django-extensions.readthedocs.io/en/latest/export_emails.html
# export_emails

#Export all the addresses in the '"First Last" <my@addr.com>;' format.
python3 manage.py export_emails > addresses.txt
# Export users from the group 'Attendees' in the linked in pre-approve Group csv format.
python3 manage.py export_emails -g Attendees -f linkedin pycon08.csv
# Create a csv file importable by Gmail or Google Docs
python3 manage.py export_emails --format=google google.csv

# https://django-extensions.readthedocs.io/en/latest/generate_password.html
# generate_password
python manage.py generate_password  [--length=<length>]

# https://django-extensions.readthedocs.io/en/latest/graph_models.html
# Graph models

#https://django-extensions.readthedocs.io/en/latest/list_model_info.html
#list_model_info

# Show each field's class
python manage.py list_model_info --field-class
# Show each field's database type representation
python3 manage.py list_model_info --db-type
# Show each method's signature
python3 manage.py list_model_info --signature
# Show all model methods, including private methods and django's default methods
python3 manage.py list_model_info --all-methods
# Output only information for a single model, specifying the app and model using dot notation
python3 manage.py list_model_info --model users.User
#You can combine arguments. for instance, to list all methods and show the method signatures for the User model within the users app:
python3 manage.py list_model_info --all --signature --model users.User

# https://django-extensions.readthedocs.io/en/latest/list_signals.html
#list_signals
python3 manage.py list_signals

# https://django-extensions.readthedocs.io/en/latest/merge_model_instances.html
# merge_model_instances
python3 merge_model_instances

# https://django-extensions.readthedocs.io/en/latest/print_settings.html
# print_settings
python3 manage.py print_settings
python3 manage.py print_settings --format=json
python3 manage.py print_settings --format=yaml    # Requires PyYAML
python3 manage.py print_settings --format=pprint
python3 manage.py print_settings --format=text
python3 manage.py print_settings --format=value

# https://django-extensions.readthedocs.io/en/latest/reset_db.html
# reset_db

# Reset the DB so that it contains no data and migrations can be run again
python3 manage.py reset_db mybucket
# Don't ask for a confirmation before doing the reset
python3 manage.py reset_db --noinput
# Use a different user and password than the one from settings.py
python3 manage.py reset_db --user db_root --password H4rd2Guess

#https://django-extensions.readthedocs.io/en/latest/runprofileserver.html
# runprofileserver

#https://django-extensions.readthedocs.io/en/latest/runserver_plus.html
# runserver_plus
python3 manage.py runserver_plus
python3 manage.py runserver_plus --cert-file cert.crt

#https://django-extensions.readthedocs.io/en/latest/sync_s3.html
#sync_s3
# Upload files to S3 into the bucket 'mybucket'
python3 manage.py sync_s3 mybucket
# Upload files to S3 into the bucket 'mybucket' and enable gzipping CSS/JS files and setting of a far future expires header
python3 manage.py sync_s3 mybucket --gzip --expires
# Upload only media files to S3 into the bucket 'mybucket'
python3 manage.py sync_s3 mybucket  --media-only  # or --static-only
# Upload only media files to a S3 compatible provider into the bucket 'mybucket' and set private file ACLs
python3 manage.py sync_s3 mybucket  --media-only  --s3host=cs.example.com --acl=private

# https://django-extensions.readthedocs.io/en/latest/syncdata.html
# syncdata
# Assuming that you’ve got sample.json under fixtures directory in one of your INSTALLED_APPS:
python3 manage.py syncdata sample.json

# If you want to keep old records use --skip-remove option:
python3 manage syncdata sample.xml --skip-remove

# You can provide full path to your fixtures file like:
python3 manage syncdata /var/fixtures/sample.json

#https://django-extensions.readthedocs.io/en/latest/sqldiff.html
# sqldiff

# View SQL differences for all installed applications
python3 manage.py sqldiff -a
# View SQL differences for all installed applications using text instead of SQL
python3 manage.py sqldiff -a -t

#https://django-extensions.readthedocs.io/en/latest/sqlcreate.html
# sqlcreate

python3 manage.py sqlcreate [–database=<databasename>] | <my_database_shell_command>
#postgresql
python3 manage.py sqlcreate [–database=<databasename>] | psql -U <db_administrator> -W
#mysql 
python3 manage.py sqlcreate [–database=<databasename>] | mysql -u <db_administrator> -p

#https://django-extensions.readthedocs.io/en/latest/sqldsn.html
# sqldsn

# Prints the DSN for the default database
python3 manage.py sqldsn
# Prints the DSN for all databases
python3 manage.py sqldsn --all
# Print the DSN for database named 'slave'
python3 manage.py sqldsn --database=slave
# Print all DSN styles available for the default database
python3 manage.py sqldsn --style=all
# Create .pgpass file for default database by using the quiet option
python3 manage.py sqldsn -q --style=pgpass > .pgpass

#https://django-extensions.readthedocs.io/en/latest/validate_templates.html
# validate_templates
python3 manage.py validate_templates

#https://django-extensions.readthedocs.io/en/latest/admin_generator.html
# admin_generator
python3 manage.py admin_generator <your_app_name>

#https://django-extensions.readthedocs.io/en/latest/jobs_scheduling.html
# jobs_scheduling
python3 manage.py create_jobs <django_application>

#https://django-extensions.readthedocs.io/en/latest/permissions.html
# permissions
