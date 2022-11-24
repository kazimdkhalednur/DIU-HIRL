from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import  Team, Publication, Event,EventImage,Research,About,WE_DO,Achievement, Client, Testimonial
from django.core.mail import send_mail
# Create your views here.



def index(request):
    
    if request.method == 'POST':
        try:
            member = Team()
            member.name = request.POST.get('name')
            member.designation = request.POST.get('designation')
            member.institution = request.POST.get('institution')
            member.email = request.POST.get('email')
            member.google_scholor = request.POST.get('gs')
            member.research_gate = request.POST.get('rg')
            member.orcid = request.POST.get('oc')
            member.linkedin = request.POST.get('ln')

            if len(request.FILES) !=0:
                member.img = request.FILES['upload']

            member.save()
        except:
            c_name = request.POST.get('c_name')
            c_email = request.POST.get('c_email')
            c_subject = request.POST.get('c_subject')
            c_message = request.POST.get('c_message')
            e_msg = {
                'name': c_name,
                'email': c_email,
                'subject': c_subject,
                'message': c_message,
            }
            print(e_msg)
            message = '''
            New Message: {}

            From: {}
            '''.format(e_msg['message'],e_msg['email'])

            send_mail(e_msg['subject'],message,'',['badshahdon41@gmail.com'])
        return redirect('/')

    

    research = Research.objects.all()
    director_data = Team.objects.filter(m_post='LD')
    advisor_data = Team.objects.filter(m_post='LA')
    coordinator_data = Team.objects.filter(m_post='RC')
    researcher_data = Team.objects.filter(m_post='R')
    member_data = Team.objects.filter(m_post='LM')
    event_data = Event.objects.all()
    about_data = About.objects.all()
    do_data = WE_DO.objects.all()
    total_members = Team.objects.all()
    count_member = len(total_members)
    total_publication = Publication.objects.all()
    count_publication = len(total_publication)
    total_achievement = Achievement.objects.all()
    count_achievement = len(total_achievement)
    client_data = Client.objects.all()
    testimonial_data = Testimonial.objects.all()
    # for i in do_data:
    #     print(i.we_do)
    data = {'research': research,'director_data':director_data,
    'advisor_data':advisor_data,'coordinator_data':coordinator_data,
    'researcher_data':researcher_data,'member_data':member_data,
    'event_data':event_data,'about_data':about_data,
    'do_data':do_data,'count_member':count_member,
    'count_publication':count_publication,
    'count_achievement':count_achievement,
    'client_data':client_data,'testimonial_data':testimonial_data,}

    # for i in count_member:
    #     print(i)

    return render(request, 'index.html',data)


def blog(request):
    research_blog = Research.objects.all()
    re_data_blog = {'research_blog': research_blog}
    return render(request, 'blog.html',re_data_blog)

def publication(request):

    publication = Publication.objects.all()
    journal = Publication.objects.filter(publication_type='J')
    conference = Publication.objects.filter(publication_type='C')
    # print("*****")
    # for i in journal:
    #     print(i)

    pub_data = {'publication': publication,'journal': journal,'conference': conference}

    # for i in pub_data['journal']:
    #     print(i)
    
    return render(request, 'publication.html',pub_data)


def event(request):
    event_data = Event.objects.all()
    event_img = EventImage.objects.all()
    # for i in event_data:
    #     print(i.title,i.image)
    # print("******")
    # for i in event_img:
    #     print(i.event,i.images)

    data = {'event_data': event_data,'event_img': event_img}
    return render(request, 'event.html',data)