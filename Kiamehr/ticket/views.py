import random
import string
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import get_user_model
from .form import CreateTicketForm, AssignTicketForm
from .models import Ticket 

User = get_user_model()

def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.customer = request.user
            while not var.ticket_id :
                id = ''.join(random.choices(string.digits, k=6))
                try:
                    var.ticket_id = id
                    var.save()
                    # send email function
                    subject = f'{var.ticket_title} #{var.ticket_id}'
                    message = 'تیکت شما ثبت شد به زودی منتور به شما  پاسخ میدهد'
                    email_form = 'mentor@email.com'
                    recipient_list = [request.user.email, ]
                    send_mail(subject, message, email_form, recipient_list)
                    messages.success(request, 'your ticket has been submitted.')
                    return redirect('customer-active-tickets')
                    # break 
                except IntegrityError:
                    continue
        else:
            messages.warning(request, 'something went wrong')
            return redirect('create-ticket')
    else:
        form = CreateTicketForm()
        context = {'form':form}
        return render(request, 'ticket/create_ticket.html', context)
    



def customer_active_tickets(request):
    tickets = Ticket.objects.filter(customer=request.user, is_resolved=False).order_by('-created_on')
    context = {'tickets':tickets}
    return render(request, 'ticket/customer_active_tickets.html', context)



def customer_resolved_tickets(request):
    tickets = Ticket.objects.filter(customer=request.user, is_resolved=True).order_by('-created_on')
    context = {'tickets':tickets}
    return render(request, 'ticket/customer_resolved_tickets.html', context)

 
 # engineer can see all her/his active tickets
def engineer_active_tickets(request):
    tickets = Ticket.objects.filter(engineer=request.user, is_resolved=False).order_by('-created_on')
    context = {'tickets':tickets}
    return render(request, 'ticket/engineer_active_tickets.html', context)


 # engineer can see all her/his resolved tickets
def engineerr_resolved_tickets(request):
    tickets = Ticket.objects.filter(engineer=request.user, is_resolved=True).order_by('-created_on')
    context = {'tickets':tickets}
    return render(request, 'ticket/engineer_resolved_tickets.html', context)


def assign_ticket(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    if request.method == 'POST':
        form = AssignTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_assigend_to_engineer = True
            var.status = 'Active'
            var.save()
            messages.success(request, f'ticket has been assigned to {var.engineer}' )
            return redirect('ticket-queue')
        else:
            messages.warning(request, 'something went wrong.')
            return redirect('assign-ticket')
    else:
        form = AssignTicketForm(instance=ticket)
        form.fields['engineer'].queryset = User.objects.filter(is_engineer = True)
        context = {'form':form, 'ticket':ticket}
        return render(request, 'ticket/assign_ticket.html', context)
    


def ticket_details(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    context = {'ticket':ticket}
    return render(request, 'ticket/ticket_details.html', context)



def ticket_queue(request):
    tickets = Ticket.objects.filter(is_assigend_to_engineer=False)
    context = {'tickets':tickets}
    return render(request, 'ticket/ticket_queue.html', context)



def resolve_ticket(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    if request.method == 'POST':
        rs = request.POST.get('rs')
    ticket.resolution_steps = rs
    ticket.is_resolved = True
    ticket.status = 'Resolved'
    ticket.save()
    messages.success(request, 'ticket is now resolved and closed')
    return redirect('dashboard')



def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    ticket.delete()
    return redirect('dashboard')



def update_ticket(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    if request.method == 'POST':
        rs = request.POST.get('rs')
    ticket.resolution_steps = rs
    ticket.is_resolved = True
    ticket.status = 'Resolved'
    ticket.save()
    messages.success(request, 'ticket is now resolved and closed')
    return redirect('dashboard')
