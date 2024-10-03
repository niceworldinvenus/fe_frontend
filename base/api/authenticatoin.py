from tastypie.authentication import Authentication

class customApiKeyAuthentication(Authentication):
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True
        
        return super().is_authenticated(request, **kwargs)

        