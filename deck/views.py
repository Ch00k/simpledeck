from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django_tables2 import SingleTableView

from .forms import CreateForm, DeleteForm
from .models import Deck
from .tables import DeckTable


class DeckListView(LoginRequiredMixin, SingleTableView):
    model = Deck
    table_class = DeckTable
    template_name = "deck/list.html"
    login_url = "/accounts/login/"

    def get_queryset(self) -> QuerySet:
        self.queryset = self.model._default_manager.filter(user=self.request.user)
        return super().get_queryset()


@login_required
def show_create_update(request: HttpRequest, pk: int = None) -> HttpResponse:
    if request.method == "POST":
        form = CreateForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            text = form.cleaned_data["text"]
            theme = form.cleaned_data["theme"]

            if pk is None:
                p = Deck(title=title, text=text, theme=theme, user=request.user)
                p.save()
                return redirect("show", pk=p.pk)
            else:
                p = get_object_or_404(Deck, pk=pk, user=request.user)
                p.title = title
                p.text = text
                p.theme = theme
                p.save()
                form = CreateForm(initial={"title": p.title})
                return render(
                    request,
                    "deck/edit.html",
                    {
                        "title": p.title,
                        "text": p.text,
                        "theme": p.theme,
                        "form": form,
                    },
                )
        else:
            return render(request, "deck/edit.html", {"form": form})
    else:
        if pk is None:
            title = "New deck"
            text = ""
            theme = "simple"
        else:
            p = get_object_or_404(Deck, pk=pk, user=request.user)
            title = p.title
            text = p.text
            theme = p.theme
        form = CreateForm(initial={"title": title})
        return render(
            request,
            "deck/edit.html",
            {
                "title": title,
                "text": text,
                "theme": theme,
                "form": form,
            },
        )


@login_required
def present(request: HttpRequest, pk: int) -> HttpResponse:
    p = get_object_or_404(Deck, pk=pk, user=request.user)
    return render(request, "deck/present.html", {"title": p.title, "text": p.text})


@login_required
def delete(request: HttpRequest, pk: int) -> HttpResponse:
    p = get_object_or_404(Deck, pk=pk, user=request.user)

    if request.method == "POST":
        form = DeleteForm(request.POST, instance=p)
        if form.is_valid():
            p.delete()
            return redirect("list")
        else:
            return render(request, "deck/list.html")

    else:
        return redirect("list")
