from django.utils.deprecation import MiddlewareMixin

class Row1(MiddlewareMixin):
    def process_request(self,request):
        print "666666666666"

    def process_response(self,request,response):
        print "222222222222222"
        return response

class Row2(MiddlewareMixin):
    def process_request(self,request):
        print "88888888888"

    def process_response(self,request,response):
        print "77777777777777"
        return response
