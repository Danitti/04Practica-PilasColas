from collections import deque


def equilibrados(texto: str) -> bool:
    if (texto == ""):
        return True
    pila_cierres = deque()
    for elemento in texto:
        if elemento == "(" or elemento == "{" or elemento == "[":
            pila_cierres.appendleft(elemento)
            continue
        
        if elemento == ")" or elemento == "}" or elemento == "]":
            if (pila_cierres == deque([])):
                return False
            elemento_pila = pila_cierres[0]
            if (elemento_pila == "(" and elemento != ")"):
                return False
            elif (elemento_pila == "{" and elemento != "}"):
                return False
            elif (elemento_pila == "[" and elemento != "]"):
                return False
            
            pila_cierres.popleft()
    
    if (pila_cierres == deque([])):
        return True
    
    return False


def procesar_turnos(ordenes: list[tuple[str, str]]) -> list[str]:
    lista_secuencia = []
    cola_ordenes = deque()

    for instruccion, persona in ordenes:
        if instruccion == "llega":
            cola_ordenes.append(persona)
            continue
        
        if instruccion == "siguiente":
            if cola_ordenes != deque([]):
                lista_secuencia.append(cola_ordenes[0])
            else:
                lista_secuencia.append("VACIA")        
            
            continue
        
        if instruccion == "atiende":
            if cola_ordenes != deque([]):
                lista_secuencia.append(cola_ordenes[0])
                cola_ordenes.popleft()
            else:
                lista_secuencia.append("VACIA")
        
        
    return lista_secuencia
    


def probar_ejercicios() -> None:
    casos_parentesis = [
        ('', True),
        ('texto sin símbolos', True),
        ('a*(b+[c])', True),
        ('{[()]}', True),
        ('([)]', False),
        ('((', False),
        (']', False),
        ('(]', False),
    ]
    for texto, esperado in casos_parentesis:
        obtenido = equilibrados(texto)
        assert obtenido == esperado, (
            f'equilibrados({texto!r}): esperado {esperado}, obtenido {obtenido}'
        )

    casos_turnos = [
        ([], []),
        ([('siguiente', ''), ('atiende', '')], ['VACIA', 'VACIA']),
        ([('llega', 'Ana'), ('llega', 'Luis'), ('siguiente', ''),
          ('atiende', ''), ('atiende', ''), ('atiende', '')],
         ['Ana', 'Ana', 'Luis', 'VACIA']),
        ([('llega', 'Ana'), ('llega', 'Luis'), ('siguiente', ''),
          ('llega', 'Eva'), ('atiende', ''), ('siguiente', ''),
          ('atiende', ''), ('llega', 'Paco'), ('atiende', ''),
          ('atiende', ''), ('atiende', '')],
         ['Ana', 'Ana', 'Luis', 'Luis', 'Eva', 'Paco', 'VACIA']),
    ]
    for ordenes, esperado in casos_turnos:
        obtenido = procesar_turnos(ordenes)
        assert obtenido == esperado, (
            f'procesar_turnos({ordenes!r}): esperado {esperado}, obtenido {obtenido}'
        )
    print('12 casos superados')


if __name__ == '__main__':
    probar_ejercicios()
