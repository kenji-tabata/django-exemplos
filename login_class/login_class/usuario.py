from django.contrib.auth import authenticate, login

class Usuario(object):

    def auth_user(self, request, username, password):    

        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                self.set_user_session(request, user)
                login(request, user)
                return True
            else:
                status = "O usuário não está ativo."
        else:
            status = "O nome de usuário ou senha está incorreto."
         
        return status

    def set_user_session(self, request, user_data):
        request.session['nome_usuario'] = user_data.first_name
        request.session['usuario'] = user_data.username

    def get_user_session(self, request, dados):
        context = {}

        for list in dados:
            if request.session.__contains__(list):
                context[list] = request.session[list]
            else:
                context[list] = ""

        return context