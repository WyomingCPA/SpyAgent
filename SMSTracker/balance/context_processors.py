from balance.models import UserBalanceChange

def balance(request):
    try:
        user_balance = UserBalanceChange.objects.get(user=request.user)
        balance = int(user_balance.amount)
    except:
        balance = 0
    return {"balance": balance}