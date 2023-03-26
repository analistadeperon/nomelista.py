$nome -like '*empl*'
...
def pesquisar(nome):
    import re
    print""
    if (len(nomes)< 1):
        print 'Não há nomes na lista para pesquisar'
    else:
        print 'Pesquisar:'
        pesquisar = raw_input()
        print""
        result = ""
        for nome in nomes:
            if (pesquisar.lower()in nome.lower()):
                result.append(nome)
                if len(result)> 0:
                    print'Resumtados para "%s":'%(pesquisar)
                    print""
                    for r in result:
                        print r
                    else:
                        print 'Se ocorrencias para "%s".'%(pesquisar)
                        print""
                        for r in result:
                            print r
                        else:
                            print'Se Se ocorrencias para "%s".'%(pesquisar)
                            print""
                        
                    
