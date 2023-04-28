import datetime

comentarios = []
comentario = None

while comentario!="":
    comentario = input('Insira seu comentário: ')
    data_public = datetime.datetime.now()
    data_public_str = data_public.strftime("%d/%m/%Y %H:%M")
    comentarios.append((comentario, data_public_str))
    
for comentario in comentarios:
    print(comentario)