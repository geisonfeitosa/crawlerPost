from urllib.parse import urlencode
from urllib.request import Request, urlopen
import rescape

def consultaCep(cep):

    url = "http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm"
    param = {'relaxation': cep, 'tipoCEP': 'ALL'}

    request = Request(url, urlencode(param).encode())
    result = urlopen(request).read()
    result = str(result)

    result = rescape.unescapeString(result)
    result = bytes(result, "iso-8859-1").decode("unicode_escape")
    result = rescape.unescapeXml(result)

    find = 'CEP:</th>'
    posicao = int(result.index(find) + len(find))
    result = result[posicao : posicao + 200]

    # logradouro
    findInicio = '<td width="150">'
    posicaoInicio = int(result.index(findInicio) + len(findInicio))
    result = result[posicaoInicio : posicaoInicio + 200]
    findFim = '</td><td>'
    posicaoFim = int(result.index(findFim))
    logradouro = result[0 : posicaoFim]

    # setor
    findInicio = findFim
    posicaoInicio = int(result.index(findInicio) + len(findInicio))
    result = result[posicaoInicio : posicaoInicio + 200]
    findFim = '</td><td>'
    posicaoFim = int(result.index(findFim))
    setor = result[0 : posicaoFim]

    # municipio
    findInicio = findFim
    posicaoInicio = int(result.index(findInicio) + len(findInicio))
    result = result[posicaoInicio : posicaoInicio + 200]
    findFim = '</td><td width="55">'
    posicaoFim = int(result.index(findFim))
    municipio = result[0 : posicaoFim]

    # cep
    findInicio = findFim
    posicaoInicio = int(result.index(findInicio) + len(findInicio))
    result = result[posicaoInicio : posicaoInicio + 200]
    findFim = '</td>'
    posicaoFim = int(result.index(findFim))
    cep = result[0 : posicaoFim]

    print("\n\n\n>>>>>>>>>> CONSULTA CEP <<<<<<<<<<\n")
    print("CEP: " + cep)
    print("Logradouro: " + logradouro)
    print("Setor: " + setor)
    print("Municipio/UF: " + municipio)
    print("\n>>>>>>>>>> CONSULTA CEP <<<<<<<<<<\n")