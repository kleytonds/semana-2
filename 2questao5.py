def preco():
    preco = int(input(""))
    vista = preco - ((preco/100) * 9)
    cinco_vezes = preco / 5
    dez_vezes = (preco + ((preco/100) * 17))/10
    print(f'{vista:.2f}')
    print(f'{cinco_vezes:.2f}')
    print(f'{dez_vezes:.2f}')

def main():
    preco()
    
if __name__ == '__main__' :
    main()
