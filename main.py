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
                contact.show_contacts()
                contact_id = int(input('Numero do contato:')) 
                contact.contact_detail(contact_id)
                
            case "4":
                contact.show_contacts()
                contact_id = int(input('Numero do contato:')) 
                contact.edit_contact(contact_id)
                
            case "5":
                contact.show_contacts()
                contact_id = int(input('Numero do contato:')) 
                contact.change_state_from_favorite_contact(contact_id)
                
            case "6":
                contact.show_favorite_contacts()
                
            case "7":
                contact.show_contacts()
                contact_id = int(input('Numero do contato para remoção: ')) 
                contact.delete_contact(contact_id)
                
            case "0":
                print("Saindo...")
                break
            
            case _:
                print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()