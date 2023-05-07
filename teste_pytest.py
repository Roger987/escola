import requests

class TestCursos:
    headers = {'Authorization': 'Token 7aa806e53a563832f7f656c970a75c0c2d59482b'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200
    
    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}2/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso de Programação com Ruby 4",
            "url": "http://geekuniversity.com.br/cpr4"
        }

        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Novo Curso de Ruby 1",
            "url": "http://geekuniversity.com.br/cpr5"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}2/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200
        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}2/', headers=self.headers)

        assert resposta.status_code == 204
