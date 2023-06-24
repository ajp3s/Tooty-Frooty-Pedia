from WebBasicsExam.profiles.models import Profile


def get_profile():
    profile = Profile.objects.all().first()
    if not profile:
        return None
    return profile
