import subprocess
from django.conf import settings
from django.core.management import call_command
from django.contrib.auth.models import Permission
from django.core.management.base import BaseCommand
from core.models import Pages

class Command(BaseCommand):
    help = 'Runs both makemigrations and migrate commands at once and updates the db if there is anything to update'
        
    def delete_default_permissions(self):
        # Delete unnecessary permission objects 
        default_custom_apps = ["about_us","accounts","blogs","core","dashboard", "documents","news","suppliers", 'task_manager',"vacancies"]
        required_apps = getattr(settings,"CUSTOM_INSTALLED_APPS",default_custom_apps) 
        required_apps.append("auth")

        all_perms = Permission.objects.all() 
        # print(all_perms.count())
        for p in all_perms:
            app = str(p.content_type).split("|")[0].strip()
            if app not in required_apps:
                p.delete()
        # print(Permission.objects.count())
        
    def data_migrator(self):
        # check if pages are created
        if Pages.objects.first() is None:
            Pages.objects.create()
        
        # 

    def handle(self, *args, **options):
        self.stdout.write("Making migrations to all apps...")
        call_command('makemigrations', interactive=False)
        self.stdout.write(" \nMigrating...")
        call_command('migrate', interactive=False)
        # subprocess.run(['python', 'manage.py', 'migrate'], check=True)
        self.stdout.write(self.style.SUCCESS("\nMigration completed successfully"))
        self.delete_default_permissions()
        self.data_migrator()
        self.stdout.write("\nDB is updated.")


