from django.db import models


# Create your models here.
class About(models.Model):
    mission = models.TextField(max_length=1000)
    vision = models.TextField(max_length=1000)


class WE_DO(models.Model):
    we_do = models.TextField(max_length=1000)


class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=30)
    feedback = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="testimonial/%y", null=True)

    def __str__(self):
        return self.name


class Achievement(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Research_Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="research/%y", null=True)

    def __str__(self):
        return self.name


class Research(models.Model):

    category = models.ForeignKey(
        Research_Category, on_delete=models.CASCADE, default=True
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="active_research/%y", null=True)

    def __str__(self):
        return str(self.category)


class Team(models.Model):

    LAB_DIRECTOR = "LD"
    LAB_ADVISOR = "LA"
    INTER_COLLABORATOR = "IC"
    RESEARCHER_STD = "RS"
    RESEARCHER_ALUMNI = "RA"
    RESEARCHER_FACULTY = "RF"
    POST_CHOICES = [
        (LAB_DIRECTOR, "LAB_DIRECTOR"),
        (LAB_ADVISOR, "LAB_ADVISOR"),
        (INTER_COLLABORATOR, "INTER_COLLABORATOR"),
        (RESEARCHER_STD, "RESEARCHER_STD"),
        (RESEARCHER_ALUMNI, "RESEARCHER_ALUMNI"),
        (RESEARCHER_FACULTY, "RESEARCHER_FACULTY"),
    ]
    m_post = models.CharField(
        max_length=2, choices=POST_CHOICES, default=RESEARCHER_STD
    )
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=20)
    institution = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    google_scholor = models.URLField(max_length=200, blank=True)
    research_gate = models.URLField(max_length=200, blank=True)
    orcid = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    img = models.ImageField(upload_to="img/%y")
    position = models.PositiveIntegerField(default=0, blank=False, null=False)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["position"]


class Year_of_Publication(models.Model):
    published_year = models.CharField(max_length=5)

    def __str__(self):
        return str(self.published_year)


class Journal(models.Model):

    paper_type = models.CharField(max_length=10, default="Journal")
    category = models.ForeignKey(
        Year_of_Publication, on_delete=models.CASCADE, default=True
    )
    reference = models.TextField(max_length=500, default=True)
    paper_link = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return str(self.paper_type)


class Conference(models.Model):

    paper_type = models.CharField(max_length=10, default="Conference")
    category = models.ForeignKey(
        Year_of_Publication, on_delete=models.CASCADE, default=True
    )
    reference = models.TextField(max_length=500, default=True)
    paper_link = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return str(self.paper_type)


class Event(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=1000, blank=True)
    image = models.FileField(upload_to="event/%y")
    drive_link = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return self.title


class Dataset(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    image = models.FileField(upload_to="dataset/%y")
    dataset_link = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return self.title


class Github(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    image = models.FileField(upload_to="github/%y")
    github_link = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return self.title


# class EventImage(models.Model):
#     event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
#     images = models.FileField(upload_to = 'event/%y')

#     def __str__(self):
#         return self.event.title


class Footer(models.Model):
    twitter = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    youtube = models.URLField(max_length=200, blank=True)
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()

    def __str__(self):
        return str(self.id)


class Carousel(models.Model):
    image = models.ImageField(upload_to="carousel/")
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.image.url


class MemberCarousel(models.Model):
    image = models.ImageField(upload_to="member_carousel/")
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.image.url
