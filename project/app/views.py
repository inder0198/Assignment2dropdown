from django.shortcuts import render
from string import ascii_letters

from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = 'home.html'

def mainpage(request):
    var = request.POST['dropdown']
    print(var)

    if request.POST['dropdown'] == 'Type_1':
        str1 = request.POST['str1']
        sr = 1
        first = ""
        vowels = ['a', 'e', 'i', 'o', 'u']
        for j in range(sr):
            for i in str1:
                if i in vowels:
                    first = first + i.upper()
                else:
                    first = first + i
        else:
            return render(request, "home.html", {"result": first})


    elif request.POST['dropdown'] == 'Type_2':
        str1 = request.POST['str1']
        words = str1.split(" ")
        newWords = [word[::-1] for word in words]
        newSentence = " ".join(newWords)
        return render(request, "home.html", {"result": newSentence})


    elif request.POST['dropdown'] == 'Type_3':
        str1 = request.POST['str1']
        se = 1
        third=""
        words = str1.split()
        for j in range(se):
            for i in words:
                a = i
                res = ''.join(sorted(a))
                third = third + str(res) + " "
        else:
            return render(request, "home.html", {"result": third})


    elif request.POST['dropdown'] == 'Type_4':

        str1 = request.POST['str1']
        a = "".join(dict.fromkeys(str1))
        return render(request, "home.html", {"result": a})


    elif request.POST['dropdown'] == 'Type_5':

        str1 = request.POST['str1']
        sw = 1
        fifth = ""
        for j in range(sw):
            for c in str1:
                if c == " ":
                    fifth = fifth + " "
                elif c in ascii_letters:
                    fifth = fifth + ascii_letters[(ascii_letters.index(c) + 2) % len(ascii_letters)]
        else:
            return render(request, "home.html", {"result": fifth})