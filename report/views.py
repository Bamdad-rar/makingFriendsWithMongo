from django.shortcuts import render


def report_generator_page(request):
    return render(request,'report.html')



