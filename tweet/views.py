from django.shortcuts import render,redirect
from tweet.models import tweet as Tweetmodel
from django.shortcuts import get_object_or_404
from tweet.forms import TweetForm,userregister
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def tweet_list(request):
        tweets=Tweetmodel.objects.all()
        return render(request, 'tweet/tweet_list.html',{'tweets':tweets})


@login_required
def tweet_create(request):
    if request.method=="POST":
        form=TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweets=form.save(commit=False)
            tweets.user=request.user
            tweets.save()
            return redirect('tweet_list')
    else:
        form=TweetForm()
    return render(request,'tweet/tweet_form.html',{'form':form})

@login_required
def tweet_edit(request,tweet_id):
    tweet=get_object_or_404(Tweetmodel,id=tweet_id)
    if request.method=="POST":
        form=TweetForm(request.POST,request.FILES, instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request,"tweet/tweet_form.html",{'form':form})

@login_required
def tweet_delete(request,tweet_id):
    tweet=get_object_or_404(Tweetmodel,id=tweet_id)
    if request.method=="POST":
        tweet.delete()
        return redirect ('tweet_list')
    return render(request,'tweet/tweet_delete.html')


def user_register(request):
    if request.method=="POST":
        form=userregister(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('user_login')
    else:
        form=userregister()
    return render(request,'tweet/user_register.html',{'form':form})

# def user_login(request):
#     if request.method=="POST":
#         username=request.POST['username']
#         password=request.POST.get('password')
#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('tweet_list')
#     else:
#         return render(request,'user_login.html')
#     return render(request,'user_login.html')

def user_login(request): 
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('tweet_list')
    else:
        form=AuthenticationForm()   
    return render(request, 'tweet/user_login.html', {'form': form})

def user_logout(request):
    logout(request,)
    return redirect('user_login')