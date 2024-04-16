# visibilidade de uma variável dentro do código
# LOCAL -> dentro de uma função, rotina
# existe somente dentro dessa função onde ela foi declarada
# é inicializada toda vez que a função é chamada
# não conseguimos utilizar ela fora
# GLOBAL -> é declarada fora das funções
# pode ser acessada em qualquer parte do código

var_global = "Estudos de Python"

def escreve_na_tela():
    global var_global
    var_global = "Python é muito legal!"
    var_local = "Pedro H. Rocha"
    
    print("Var GLOBAL:", var_global)
    print("Var LOCAL:", var_local)
    
if __name__ == "__main__":
    escreve_na_tela()
    
    print("Var GLOBAL FORA:", var_global)
    
    #5:48
    