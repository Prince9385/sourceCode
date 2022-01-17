from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration1
from .forms import StudentRegistration2
from .models import StudentInfo ,StudentAcademics

# Create your views here.
################### Create Student Form ###########################################################3
def students(request):
    if request.method=='POST':
        student_details1=StudentRegistration1(request.POST)
        student_details2=StudentRegistration2(request.POST)
        print(student_details2.is_valid())
        if student_details2.is_valid() and student_details1.is_valid():
            sturollno=student_details2.cleaned_data['Rollno']
            stuname=student_details2.cleaned_data['Name']
            stuclass=student_details2.cleaned_data['Class']
            stuschool=student_details2.cleaned_data['School']
            stumobile=student_details2.cleaned_data['Mobile']
            stuaddress=student_details2.cleaned_data['Address']
            stu_maths_marks=student_details1.cleaned_data['Maths']
            stu_phyics_marks=student_details1.cleaned_data['Physics']
            stu_chemistry_marks=student_details1.cleaned_data['Chemistry']
            stu_biology_marks=student_details1.cleaned_data['Biology']
            stu_english_marks=student_details1.cleaned_data['English']
            reg=StudentInfo(Rollno=sturollno,Name=stuname,Class=stuclass,School=stuschool,Mobile=stumobile,Address=stuaddress)
            reg.save()
            sturollno1=StudentInfo.objects.get(Rollno=sturollno)
            
            reg1=StudentAcademics(Rollno=sturollno1,Maths=stu_maths_marks,Physics=stu_phyics_marks,Chemistry=stu_chemistry_marks,Biology=stu_biology_marks,English=stu_english_marks)
            reg1.save()
      
    else:
        student_details1=StudentRegistration1()
        student_details2=StudentRegistration2()
    return render(request,'inner.html',{'form2':student_details2,'form1':student_details1})
##################### Create Stutent Table & Serach Box ################################################
def StudentTable(request):
    if request.method=='POST':
        name=request.POST.get('q')
        if(len(name)>0):
            try:
                studentstables=StudentInfo.objects.get(Name=name)
                
                print(studentstables)
                print("heyyyyyyyyyyyyyyyyyyyyyyyyyy")
                return render(request,'studentinformation.html',{'stutable':studentstables})
            except:
                studentstables=StudentInfo.objects.all()
                return render(request,'studentinformation.html',{'stutables':studentstables})
            
        else:
             return render(request,'studentinformation.html')
    else:
        studentstables=StudentInfo.objects.all()
        # print(studentstables)
    return render(request,'studentinformation.html',{'stutables':studentstables})
###################### Student Delete Form ######################################################
def delete_data(request,Rollno):
    if request.method=='POST':
        pi=StudentInfo.objects.get(pk=Rollno)
        pi.delete()
        return HttpResponseRedirect('/stu')

######################### Student Update Form #########################################################
def update_data(request,Rollno):
    if request.method=='POST':
        student_update=StudentInfo.objects.get(pk=Rollno)
        # print(student_update.Maths)
        student_update1=StudentAcademics.objects.get(Rollno=student_update)
        student_data=StudentRegistration2(request.POST, instance=student_update)
        student_data1=StudentRegistration1(request.POST,instance=student_update1)
        if student_data.is_valid() and student_data1.is_valid():
            # sturollno=student_data.cleaned_data['Rollno']
            stuname=student_data.cleaned_data['Name']
            stuclass=student_data.cleaned_data['Class']
            stuschool=student_data.cleaned_data['School']
            stumobile=student_data.cleaned_data['Mobile']
            stuaddress=student_data.cleaned_data['Address']
            stu_maths_marks=student_data1.cleaned_data['Maths']
            stu_phyics_marks=student_data1.cleaned_data['Physics']
            stu_chemistry_marks=student_data1.cleaned_data['Chemistry']
            stu_biology_marks=student_data1.cleaned_data['Biology']
            stu_english_marks=student_data1.cleaned_data['English']
            # print(stuschool)
            reg=StudentInfo(Rollno=Rollno,Name=stuname,Class=stuclass,School=stuschool,Mobile=stumobile,Address=stuaddress)
            reg.save()
            reg1=StudentAcademics(Rollno=student_update,Maths=stu_maths_marks,Physics=stu_phyics_marks,Chemistry=stu_chemistry_marks,Biology=stu_biology_marks,English=stu_english_marks)
            reg1.save()
            return HttpResponseRedirect('/stu')

            # student_data1.save()
    else:
        student_update=StudentInfo.objects.get(pk=Rollno)
        # print(student_update)
        student_update1=StudentAcademics.objects.get(Rollno=student_update)
        print(student_update1)
        print(student_update1.Maths)
        # maths=student_update1.Maths
        student_data=StudentRegistration2(instance=student_update)
        # print(StudentRegistration2(instance=student_update))
        student_data1=StudentRegistration1(initial={"Maths":student_update1.Maths,"Physics":student_update1.Physics,"Chemistry":student_update1.Chemistry,"Biology":student_update1.Biology,"English":student_update1.English})
        # print(StudentRegistration1(value=maths))
    return render(request,'updatedata.html',{'form':student_data,'form1':student_data1})


###################### Student Mark ###########################################


def student_information(request,Rollno):
    stu=StudentInfo.objects.get(pk=Rollno)
    stu1=StudentAcademics.objects.get(Rollno=stu)
    print(stu1.Maths)
    return render(request,"stuinfo.html",{"forms":stu1})


######################## Home Page #################################################
def StudentTable1(request):

    return render(request,"search.html")



