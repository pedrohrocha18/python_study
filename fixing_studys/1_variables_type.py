global_var = "Complete Course of Python"

def type_text():
    global global_var
    global_var = "Apenas um teste"
    local_var = "Pedro H."
    print("Global Var:", global_var)
    print("Local Var:", local_var)

if __name__ == "__main__":
    print("Execute funcion Type Text")
    type_text()
    
    print("Try to execute variable directly")
    print("Global Var", global_var)