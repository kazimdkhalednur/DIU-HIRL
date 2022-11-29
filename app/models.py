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
    image = models.ImageField(upload_to="testimonial/%y",null=True)

    def __str__(self):
        return self.name

class Achievement(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class Research_Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="research/%y",null=True)
    def __str__(self):
        return self.name



class Research(models.Model):
    
    category = models.ForeignKey(Research_Category,on_delete=models.CASCADE, default=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
   

    def __str__(self):
        return str(self.category)



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

class Year_of_Publication(models.Model):
    published_year = models.CharField(max_length=5)

    def __str__(self):
        return str(self.published_year)


class Journal(models.Model):

    paper_type = models.CharField(max_length=10,default="Journal")
    category = models.ForeignKey(Year_of_Publication,on_delete=models.CASCADE, default=True)
    reference = models.TextField(max_length=500, default=True)
    paper_link = models.URLField(max_length=300,blank=True)

    def __str__(self):
        return str(self.paper_type)


class Conference(models.Model):

    paper_type = models.CharField(max_length=10,default="Conference")
    category = models.ForeignKey(Year_of_Publication,on_delete=models.CASCADE, default=True)
    reference = models.TextField(max_length=500, default=True)
    paper_link = models.URLField(max_length=300,blank=True)

    def __str__(self):
        return str(self.paper_type)



class Event(models.Model):
    title = models.CharField(max_length=250)
    image = models.FileField(upload_to = 'event/%y')
    drive_link = models.URLField(max_length=300,blank=True)
 
    def __str__(self):
        return self.title

# class EventImage(models.Model):
#     event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
#     images = models.FileField(upload_to = 'event/%y')
 
#     def __str__(self):
#         return self.event.title


    