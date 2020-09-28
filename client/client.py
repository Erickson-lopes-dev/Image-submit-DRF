import requests


def search_pk(pk):
    """
        Busca na base de dados o pk requerido, e caso seja encontrado, pergunta ao usuário
        se deseja fazer o download
    """
    result = requests.get(f'https://saulo-img.herokuapp.com/images/{pk}')
    try:
        if result.json()['detail']:
            print(result.json())
    except KeyError:
        imgs = [result.json()['image_one'], result.json()['image_two']]

        print(f'Sucesso na busca, duas imagens encontrada no id {pk}!')
        quest = input('Deseja baixar as imagens ?[Y/N]')

        if quest in ['Y', 'y']:
            for image in imgs:
                y = ''
                for caractere in image[::-1]:
                    y += caractere
                    if caractere == '/':
                        break

                with open(f'{y[::-1][1:]}', 'wb') as save:
                    save.write(requests.get(image).content)
        print('Download concluido!')


def send(img1, img2):
    """
        Envia as imagens, apenas especifique o caminho e nome da imagem.
        Exemplo: send('imagem.jpg', 'pasta/imagem.jpg')
    """
    try:
        json = {
            "image_one": open(img1, 'rb'),
            "image_two": open(img2, 'rb')
        }

        post = requests.post('https://saulo-img.herokuapp.com/images/', files=json)
    except Exception as error:
        print("Erro ao enviar as imagens, Verifique o tipo de arquivo que deseja enviar. \n", error)
    else:
        print(post.text)
        print('Fotos Enviadas com sucesso')


send('0.jpg', '43468_index_p.jpg')
# search_pk(1)
