from django.conf import settings
from apps.main.models import UserExtend





def systemstarterkit(request): 
	try:
	    extuser = UserExtend.objects.get(user__id=request.user.id)
	    return {'extuser':extuser}
	except:
		return {}
