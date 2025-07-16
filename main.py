from src.contact import contact

def main():
    print("-----------------------------------")
    print("Agenda de Contatos")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Ver Contato específico")
    print("4. Editar Contato")
    print("5. Marcar/Desmarcar contato como favorito")
    print("6. Ver lista de contatos favoritos")
    print("7. Remover Contato")
    print("0. Sair")
    print("-----------------------------------")
    
    
    while True:
        choice = input("Escolha uma opção: ")
        
        match choice:
            case "1":
                name = input("Digite o nome do contato: ")
                phone = input("Digite o telefone do contato: ")
                email = input("Digite o email do contato: ")
                favorite = input("É favorito? (s/n): ").lower() == 's'
                contact.add_contact(name, phone, email, favorite)
                
            case "2":
                contact.show_contacts()
                
            case "3":
                contact_id = int(input('Numero do contato:')) 
                contact.contact_detail(contact_id)
                
            case "4":
                pass
                
            case "5":
                pass
                
            case "6":
                pass
                
            case "7":
                pass
                
            case "0":
                print("Saindo...")
                break
            
            case _:
                print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()