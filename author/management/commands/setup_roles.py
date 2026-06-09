from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from author.models import UserProfile


class Command(BaseCommand):
    help = 'Create default Super Admin and Moderator users'

    def handle(self, *args, **options):
        # Create Super Admin
        superadmin_user, created = User.objects.get_or_create(
            username='superadmin',
            defaults={
                'email': 'superadmin@blog.com',
                'first_name': 'Super',
                'last_name': 'Admin',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            superadmin_user.set_password('superadmin123')
            superadmin_user.save()
            self.stdout.write(self.style.SUCCESS(
                '[OK] Super Admin created: username="superadmin", password="superadmin123"'
            ))
        else:
            self.stdout.write(self.style.WARNING(
                '[!] Super Admin user "superadmin" already exists.'
            ))

        # Ensure profile has super_admin role
        profile, _ = UserProfile.objects.get_or_create(user=superadmin_user)
        profile.role = 'super_admin'
        profile.save()
        self.stdout.write(self.style.SUCCESS(
            '   -> Role set to: Super Admin'
        ))

        self.stdout.write('')  # blank line

        # Create Moderator
        moderator_user, created = User.objects.get_or_create(
            username='moderator',
            defaults={
                'email': 'moderator@blog.com',
                'first_name': 'Blog',
                'last_name': 'Moderator',
                'is_staff': True,
            }
        )
        if created:
            moderator_user.set_password('moderator123')
            moderator_user.save()
            self.stdout.write(self.style.SUCCESS(
                '[OK] Moderator created: username="moderator", password="moderator123"'
            ))
        else:
            self.stdout.write(self.style.WARNING(
                '[!] Moderator user "moderator" already exists.'
            ))

        # Ensure profile has moderator role
        profile, _ = UserProfile.objects.get_or_create(user=moderator_user)
        profile.role = 'moderator'
        profile.save()
        self.stdout.write(self.style.SUCCESS(
            '   -> Role set to: Moderator'
        ))

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('Done! Role-based users are ready.'))
        self.stdout.write('')
        self.stdout.write('  Permissions Summary:')
        self.stdout.write('  +-------------------+--------------------------------------------------+')
        self.stdout.write('  | Super Admin       | Full access - delete any post, comment, or user  |')
        self.stdout.write('  | Moderator         | Delete any post or comment, cannot manage users  |')
        self.stdout.write('  | Author (default)  | Delete only own posts and comments               |')
        self.stdout.write('  +-------------------+--------------------------------------------------+')
