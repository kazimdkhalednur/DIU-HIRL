from django.db import models

# Create your models here.
class About(models.Model):
    mission = models.TextField(max_length=1000)
    vision = models.TextField(max_length=1000)

class WE_DO(models.Model):
    we_do = models.TextField(max_length=1000)



class Client(models.Model):
    image = models.ImageField(upload_to="clients/%y",null=True)



class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=30)
    feedback = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="testimonial/%y",null=True)

    def __str__(self):
        return self.name

class Achievement(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Research(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="research/%y",null=True)

    def __str__(self):
        return self.name



class Team(models.Model):

    LAB_DIRECTOR = "LD"
    LAB_ADVISOR = "LA"
    RESEARCH_COORDINATOR = "RC"
    RESEARCHER = "R"
    LAB_MEMBER = "LM"
    POST_CHOICES = [
        (LAB_DIRECTOR, "LAB_DIRECTOR"),
        (LAB_ADVISOR, "LAB_ADVISOR"),
        (RESEARCH_COORDINATOR,"RESEARCH_COORDINATOR"),
        (RESEARCHER,"RESEARCHER"),
        (LAB_MEMBER,"LAB_MEMBER"), 
    ]
    m_post = models.CharField(max_length=2,choices=POST_CHOICES, default=LAB_MEMBER)
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=20)
    institution = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    google_scholor = models.URLField(max_length=200,blank=True)
    research_gate = models.URLField(max_length=200,blank=True)
    orcid = models.URLField(max_length=200,blank=True)
    linkedin = models.URLField(max_length=200,blank=True)
    img = models.ImageField(upload_to="img/%y")
    


    def __str__(self):
        return self.name



class Publication(models.Model):

    JOURNAL_PUBLICATION = "J"
    CONFERENCE_PUBLICATION = "C"

    JOURNAL_CHOICES = [
        (JOURNAL_PUBLICATION, "JOURNAL_PUBLICATION"),
        (CONFERENCE_PUBLICATION, "CONFERENCE_PUBLICATION"),
    ]

    publication_type = models.CharField(max_length=1,choices=JOURNAL_CHOICES, default=JOURNAL_PUBLICATION)
    publisher_name = models.CharField(max_length=30)
    research_title = models.CharField(max_length=100)
    paper_link = models.URLField(max_length=300,blank=True)

    def __str__(self):
        return self.publisher_name



class Event(models.Model):
    title = models.CharField(max_length=250)
    # image = models.FileField(blank=True)
 
    def __str__(self):
        return self.title

class EventImage(models.Model):
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'event/%y')
 
    def __str__(self):
        return self.event.title


    