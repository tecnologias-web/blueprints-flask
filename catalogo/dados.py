CURSOS = [{ 
    'nome': 'Desenvolvimento Web',
    'tipo': 'Programação',
    'desc': 'Aprendar a criar lindas páginas na web',
    'ativo': True,
    'slug': 'desenvolvimento-web'
},{ 
    'nome': 'Introdução à Pyton',
    'tipo': 'Programação',
    'desc': 'Aprendar a programar em Python em poucas aulas',
    'ativo': True,
    'slug': 'introducao-a-python'
},{ 
    'nome': 'Fundamentos UX',
    'tipo': 'UX',
    'desc': 'Entenda os funcadmentos da disciplina de User Experience',
    'ativo': True,
    'slug': 'fundamentos-ux'
},{ 
    'nome': 'Identidade Visual',
    'tipo': 'Design',
    'desc': 'Criando um sistema visual para a sua aplicação web',
    'ativo': True,
    'slug': 'identidade-visual'
}]

def listar_cursos_ativos():
    resultado = []
    for curso in CURSOS:
        if curso['ativo']:
            resultado.append(curso)

    return resultado

def obter_curso(slug=''):
    for curso in CURSOS:
        if slug == curso['slug']:
            return curso
