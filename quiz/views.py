from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .models import Quiz, PassedQuiz


def index(request: HttpRequest) -> HttpResponse:
    if request.user.is_anonymous:
        return render(request, "quiz/greeting.html")
    user = request.user
    questions = Quiz.objects.exclude(Q(passedquiz__user=user))
    if request.method == "POST":
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            if q.answer == request.POST.get(q.question):
                PassedQuiz.objects.create(quiz=q, user=user)
                score += 10
                correct += 1
            else:
                wrong += 1
        try:
            percent = score / (total * 10) * 100
        except ZeroDivisionError:
            percent = 0
        user.scores += score
        user.passed_tests += total
        user.save()
        context = {
            "score": score,
            "correct": correct,
            "wrong": wrong,
            "percent": percent,
            "total": total,
        }
        return render(request, "quiz/result.html", context)
    else:
        context = {"questions": questions}
        return render(request, "quiz/index.html", context)
