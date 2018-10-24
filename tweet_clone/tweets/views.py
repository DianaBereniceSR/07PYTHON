from django.shortcuts import render
from .models import Tweet
from .forms import FormCreate
from django.views import generic
# Create your views here.

def index(request):
	context={"message":"Este es un mensaje desde la vista index","numerico":6578,"array":[1,2,3,4],
	"dic":{"a":12,"b":23}
	}
	return render(request, "tweets/index.html",context)


class ListTweets(generic.ListView):
	template_name="tweets/list_tweets.html"
	model=Tweet






def list_tweets(request):

	contex={"tweets":Tweet.objects.all()}
	return render(request,"tweets/list_tweets.html",contex)	



class DetailTweet(generic.DetailView):
	template_name="tweets/detail.html"
	model=Tweet



def detail_tweet(request,id=1):
	queryset=Tweet.objects.get(id=id)
	contex={"tweet_object":queryset}
	return render(request,"tweets/detail.html",contex)



class Create(generic.CreateView):
	template_name="tweets/create.html"
	model=Tweet
	fields=["content"]
	success_url="/list_tweet/"

	

def create(request):
	form=FormCreate(request.POST or None)
	if request.POST:
		if form.is_valid():
			form.save()	
	else:
		form=FormCreate(request.POST or None)	

	contex={"form":form}
	return render(request,"tweets/create.html",contex)	




class UpdateTweet(generic.UpdateView):
	template_name="tweets/update.html"
	model=Tweet
	fields=["content"]
	success_url="/list_tweet/"


class DeleteTweet(generic.DeleteView):
	template_name="tweets/delete.html"
	model=Tweet
	success_url="/list_tweet/"