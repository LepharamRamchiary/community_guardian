import os
import django
from django.conf import settings

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'community_guardian.settings')
django.setup()

from issue.models import Issue
import cloudinary.uploader

def migrate_images_to_cloudinary():
    """Migrate existing local images to Cloudinary"""
    issues = Issue.objects.all()
    for issue in issues:
        # Check if the image is a local file path
        if hasattr(issue.image, 'url') and not str(issue.image).startswith('http'):
            try:
                # Build the local path to the image
                local_path = os.path.join(settings.MEDIA_ROOT, str(issue.image))
                if os.path.exists(local_path):
                    print(f"Uploading {local_path} to Cloudinary...")
                    
                    # Upload to Cloudinary
                    upload_result = cloudinary.uploader.upload(local_path, folder="issue_images")
                    
                    # Update the issue with the new Cloudinary image
                    issue.image = upload_result['public_id']
                    issue.save()
                    
                    print(f"Successfully migrated image for issue '{issue.title}'")
                else:
                    print(f"Warning: Image file not found for issue '{issue.title}': {local_path}")
            except Exception as e:
                print(f"Error migrating image for issue '{issue.title}': {str(e)}")

if __name__ == "__main__":
    print("Starting migration of images to Cloudinary...")
    migrate_images_to_cloudinary()
    print("Migration complete!")