

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import facebook
from .models import Details
# from django.template.context import RequestContext
def new(request):
	access_token="CAADsYnnLvmgBADaeFGw2zEOW7vZB6ZA1RI4CDIPsgTnVQFjVQxSn7vhWQm57AXTR8gZCnXU69BK72p81hAsU9sKyHvSnyNZAVtoXjH4RMLPHFyaZCuzcvLIrYXwrhJe8dI7ZBqT3UOdHRVfX3twpVdWJG9fUnlA47TjwJrdTPzahQn9hCeR7jScx4b0jeod6Gxx5ZCov20o7wZDZD"
	graph = facebook.GraphAPI(access_token=access_token, version='2.2')
	details=graph.get_object('/me?fields=id,first_name,birthday,last_name,age_range,email')

	Details.email=details['email']
	Details.uid=details['id']
	Details.first_name=details['first_name']
	Details.birthday=details['birthday']
	Details.last_name=details['last_name']
	Details.age_range=details['age_range']
	context={'email':Details.email,'uid': Details.uid,'birthday': Details.birthday,'lastname':Details.last_name,'firstname':Details.first_name,'agerange':Details.age_range}
	return render(request,'detail.html',context)


def name(request):
	context=dict()
	return render(request,'name.html',context)
def login(request):
	#social=request.user.social_auth.get(provider='facebook').first()
	# if social_user:
	# 	url = u'<a href="https://graph.facebook.com/{0}/'">https://graph.facebook.com/{0}/'</a> \
	# 	u'friends?fields=id,name,location,picture' \
	# 	u'&access_token={1}'.format(

 #        social_user.uid,
 #        social_user.extra_data['access_token'],
 #    	)
 #    request = urllib2.Request(url)
 #    friends = json.loads(urllib2.urlopen(request).read()).get('data')
 #    new=list()
 #    for friend in friends:
 #        location = friend.get('location')
 #        new.append(location)
 	graph = facebook.GraphAPI(access_token='your_token', version='2.2')

    
	context = RequestContext(request, {
    	'request': request, 'user': request.user,

    	})

    	
	return render_to_response('login.html', context_instance=context)
    #return render(request, 'login.html')


@login_required(login_url='/')
def home(request):
    return render_to_response('home.html')


def logout(request):
    auth_logout(request)
    return redirect('/fblogin')
