from django.shortcuts import render

def home(request):
	title = 'Welcome'
	if request.user.is_authenticated():
		title="My title %s" %(request.user)

	context={
		"template_title":title,
	}
	return render(request, "home.html", context)