from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render


def contact(request):
    if request.method == "POST":
        try:
            c_name = request.POST.get("c_name")
            c_email = request.POST.get("c_email")
            c_subject = request.POST.get("c_subject")
            c_message = request.POST.get("c_message")
            e_msg = {
                "name": c_name,
                "email": c_email,
                "subject": c_subject,
                "message": c_message,
            }
            print(e_msg)
            message = """
            New Message: {}

            From: {}
            """.format(
                e_msg["message"], e_msg["email"]
            )

            send_mail(e_msg["subject"], message, "", ["badshahdon41@gmail.com"])
        except:
            return HttpResponse("ERROR")
        return redirect("/")

    return render(request, "contact.html")
