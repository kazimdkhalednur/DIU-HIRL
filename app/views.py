from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import  *
from django.core.mail import send_mail
# Create your views here.



def index(request):
    event_data = Event.objects.all()
    about_data = About.objects.all()
    do_data = WE_DO.objects.all()
    total_members = Team.objects.all()
    count_member = len(total_members)
    total_journal = Journal.objects.all()
    total_conference = Conference.objects.all()
    count_publication = len(total_journal)+len(total_conference)
    total_achievement = Achievement.objects.all()
    count_achievement = len(total_achievement)
    testimonial_data = Testimonial.objects.all()
    
    data = {'event_data':event_data,'about_data':about_data,
    'do_data':do_data,'count_member':count_member,
    'count_publication':count_publication,
    'count_achievement':count_achievement,
    'testimonial_data':testimonial_data,}

   

    return render(request, 'index.html',data)


def blog(request):

    category = request.GET.get('category')
    research_category = Research_Category.objects.all()
    if category == None:
        research_blog = Research.objects.all()
    else:
        research_blog = Research.objects.filter(category__name=category)

    
    re_data_blog = {'research_category': research_category,
    'research_blog': research_blog}
    return render(request, 'blog.html',re_data_blog)

def dataset(request):
    all_dataset_data = Dataset.objects.all()
    return render(request, 'dataset.html', {'dataset_data': all_dataset_data})

def github(request):

    all_github_data = Github.objects.all()
    return render(request, 'github.html',{'all_github_data': all_github_data})
    
def research(request):

    research_category = Research_Category.objects.all()
    

   
    re_data = {'research_category': research_category,}
    return render(request, 'research.html',re_data)

def join(request):
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
            return HttpResponse("ERROR")
        return redirect('/')

    return render(request, 'join.html')

def contact(request):
    if request.method == 'POST':
        try:
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
        except:
            return HttpResponse("ERROR")
        return redirect('/')

    return render(request, 'contact.html')
    


def researchers(request):
    director_data = Team.objects.filter(m_post='LD')
    faculty_researcher_data = Team.objects.filter(m_post='RF')
    student_researcher_data = Team.objects.filter(m_post='RS')
    alumni_researcher_data = Team.objects.filter(m_post='RA')
    team_data = {'director_data':director_data,
                 'faculty_researcher_data':faculty_researcher_data,
                 'student_researcher_data':student_researcher_data,
                 'alumni_researcher_data':alumni_researcher_data,
                 }
    return render(request, 'researchers.html',team_data)

def international_cola(request):
    international_colla_data = Team.objects.filter(m_post='IC')
    
    team_data = {'international_colla_data':international_colla_data,
   }
    return render(request, 'international_cola.html',team_data)

def advisor_committee(request):
    
    advisor_data = Team.objects.filter(m_post='LA')
   
    team_data = {'advisor_data':advisor_data,}
    return render(request, 'advisor_committee.html',team_data)

def journal(request):
    category = request.GET.get('category')
    categories = Year_of_Publication.objects.all()

    if category == None:
        journal = Journal.objects.all()
        
    else:
        journal = Journal.objects.filter(category__published_year=category)

    data = {'journal': journal,'categories': categories}

    return render(request, 'journal.html',data)

def conference(request):

    category = request.GET.get('category')
    categories = Year_of_Publication.objects.all()


    if category == None:
        conference = Conference.objects.all()
        
    else:
        conference = Conference.objects.filter(category__published_year=category)

    data = {'conference': conference,'categories': categories}
    
    return render(request, 'conference.html',data)



def event(request):

    event_data = Event.objects.all()
  
    data = {'event_data': event_data}
    return render(request, 'event.html',data)