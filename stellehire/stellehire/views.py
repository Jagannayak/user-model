from bson.json_util import dumps, loads
from .settings import *
from django.http import HttpResponse
from django.views import View


class Login(View):
    def get(self,request):
        try:
            response={"message":"GET Method Not Allowed","status":"failed","code":405}
        except Exception as e:
            response.update({"message":str(e)})	
        return HttpResponse(dumps(response))	
    def post(self,request):
        response={"message":"","status":"failed","code":400,"callBack":"Login"}
        try:
            response.update({"message":"Please enter User Name"})
            if 'userName' in request.POST and  request.POST['userName']!='':
                response.update({"message":"Please enter Password"})
                if 'password' in request.POST and request.POST['password']!='':
                   
                    response= loginDef(request.POST['userName'],request.POST['password'],response)
        except Exception as e:
            response.update({"message":str(e),"status": "failed"})
        return HttpResponse(dumps(response))
def loginDef(userName,password,response):
    #dbCursor.UserLogin.insert({"userName":"test_user","password":"correcthorsebatterystaple"})
    dbCursor.user1.insert({"userName":"test_user;","password":"correcthorsebatterystaple"})

    userRoleCheck = loads(dumps(dbCursor.user1.find({"userName":userName.lower()+";","password":password}, {'_id': 0}))) # check the token in db
	# print('userRoleCheck',userRoleCheck)
   # response = {'message': 'Unauthorized User.','status':'failed'}
    if userRoleCheck:  # if token find
        response.update({
        'message':'Successfully Login ', 
        'status': 'success', 
       }) # return response with role,userId and user name
    return response

