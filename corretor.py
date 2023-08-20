def main():
    # Solicitar input das duas listas de 10 strings
    lista1 = []
    lista2 = []

    for i in range(10):
        string1 = input(f"Digite a {i + 1}ª resposta: ")
        lista1.append(string1)

    print("\nAgora, insira as alternativas corretas da lista:")
    for i in range(10):
        string2 = input(f"{i+1}ª questão. Você respondeu [{lista1[i]}], a resposta esta [C]orreta ou [E]rrada? ")
        lista2.append(string2)

    # Mostrar as duas listas lado a lado
    print("\nListas lado a lado:")
    for str1, str2 in zip(lista1, lista2):
        print(f"{str1:20s} | {str2}")

if __name__ == "__main__":
    main()
