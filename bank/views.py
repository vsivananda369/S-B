from django.shortcuts import render, redirect

from .forms import CustomerForm


def register(request):

    if request.method == "POST":

        form = CustomerForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    else:

        form = CustomerForm()

    return render(
        request,
        "bank/register.html",
        {
            "form": form
        }
    )


def login_view(request):

    if request.method == "POST":

        email = request.POST.get("email")

        from .models import Customer

        try:

            customer = Customer.objects.get(
                email=email
            )

            request.session["customer_id"] = customer.id

            return redirect("dashboard")

        except Customer.DoesNotExist:

            return render(
                request,
                "bank/login.html",
                {
                    "error": "Customer not found."
                }
            )

    return render(
        request,
        "bank/login.html"
    )


def dashboard(request):

    customer_id = request.session.get(
        "customer_id"
    )

    if not customer_id:

        return redirect("login")

    from .models import Customer

    customer = Customer.objects.get(
        id=customer_id
    )

    return render(
        request,
        "bank/dashboard.html",
        {
            "customer": customer
        }
    )


def home(request):

    return redirect("login")