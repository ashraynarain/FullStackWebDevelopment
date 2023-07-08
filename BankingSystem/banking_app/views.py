from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import User, Transaction
import json

# Create your views here.
@csrf_exempt
def get_all_users(request):
    users = User.objects.all().values()
    return JsonResponse(list(users),safe=False)

@csrf_exempt
def get_user_by_username(request, username):
    try:
        user = User.objects.get(username = username)
        return JsonResponse(model_to_dict(user))
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"})

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User(username = data['username'],password = data['password'], email = data['email'], balance = data['balance'])
        user.save()
        return JsonResponse(model_to_dict(user))
    else :
        return JsonResponse({"error":"Invalid Request"})
@csrf_exempt
def delete_all_users(request):
    User.objects.all().delete()
    return JsonResponse({"message": "All users deleted"})

@csrf_exempt
def delete_user_by_username(request, username):
    try:
        user = User.objects.get(username=username)
        user.delete()
        return JsonResponse({"message": "User deleted"})
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
    
@csrf_exempt
def update_user(request, username):
    if request.method == 'PUT':
        try:
            user = User.objects.get(username=username)
            data = json.loads(request.body)
            user.password = data['password']
            user.email = data['email']
            user.balance = data['balance']
            user.save()
            return JsonResponse(model_to_dict(user))
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
    else:
        return JsonResponse({"error": "Invalid request"}, status=400)
@csrf_exempt
def get_all_transactions(request):
    transactions = Transaction.objects.all().values()
    return JsonResponse(list(transactions), safe=False)

@csrf_exempt
def get_transaction_by_id(request, transaction_id):
    try:
        transaction = Transaction.objects.get(transaction_id=transaction_id)
        return JsonResponse(model_to_dict(transaction))
    except Transaction.DoesNotExist:
        return JsonResponse({"error": "Transaction not found"}, status=404)

@csrf_exempt
def create_transaction(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        from_username = data['from_username']
        to_username = data['to_username']
        amount = data['amount']

        try:
            from_user = User.objects.get(username=from_username)
            to_user = User.objects.get(username=to_username)
            if from_user.balance < amount:
                return JsonResponse({"error": "Insufficient balance"}, status=400)
            else:
                transaction = Transaction(from_username=from_username, to_username=to_username, amount=amount)
                transaction.save()
                from_user.balance -= amount
                to_user.balance += amount
                from_user.save()
                to_user.save()
                return JsonResponse(model_to_dict(transaction))
        except User.DoesNotExist:
            return JsonResponse({"error": "Invalid users"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request"}, status=400)