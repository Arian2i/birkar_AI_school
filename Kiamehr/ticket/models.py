
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Ticket(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    engineer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='engineer', null=True, blank=True)
    ticket_id = models.CharField(max_length=15, unique=True)
    ticket_title = models.CharField(max_length=50)
    ticket_description = models.TextField()
    status = models.CharField(max_length=20, choices=(('Active', 'Active'), ('Pending', 'Pending'), ('Resolved', 'Resolved')), default='Pending')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)
    severity = models.CharField(max_length=5, choices=(('A', 'A'), ('B', 'B')), default='B')
    is_assigend_to_engineer = models.BooleanField(default=False)
    resolution_steps = models.TextField(blank=True, null=True)
    assign_ticket = models.ForeignKey(User, related_name='assign_ticket', on_delete=models.CASCADE, null=True)


