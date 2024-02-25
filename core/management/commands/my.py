from django.core.management.commands import makemessages
from django.core.management.base import BaseCommand, CommandError
class Command(BaseCommand):
    def handle(self, *args, **options):
        print("mine is running")
    
        # xgettext_keywords = options.pop('xgettext_keywords')
        # if xgettext_keywords:
        #     self.xgettext_options = (
        #         makemessages.Command.xgettext_options[:] +
        #         ['--keyword=%s' % kwd for kwd in xgettext_keywords]
        #     )
        # super(Command, self).handle(*args, **options)
