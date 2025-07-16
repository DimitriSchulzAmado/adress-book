class Contact:
    def __init__(self):
        self.contact_list = []
    
    def add_contact(self, name: str, phone: str, email: str, favorite: bool = False):
        contact = {
            "id": len(self.contact_list) + 1,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite,
        }
        self.contact_list.append(contact)
        print(f"Contato de '{name}' adicionado com sucesso.")


    def show_contacts(self):
        if not self.contact_list:
            print("Nenhum contato encontrado.")
            return
        
        for index, contact in enumerate(self.contact_list, start=1):
            favorite_mark = "★" if contact["favorite"] else "☆"
            print(f"{index}. {contact['name']} {favorite_mark}")
    
    
    def contact_detail(self, contact_id: int):
        index = contact_id - 1
        contact = self.contact_list[index]
        
        print(f'------------------------- \
                \nNome: {contact['name']} \
                \nPhone: {contact['phone']} \
                \nE-mail: {contact['email']} \
                \nFavorito: {"★" if contact['favorite'] else "☆"} \
                \n-------------------------')
    
    
    def edit_contact(self, contact_id: int):
        index = contact_id - 1
        contact = self.contact_list[index]
        
        print(f"Editando contato: {contact['name']}")
        name = input("Novo nome (deixe em branco para manter): ") or contact['name']
        phone = input("Novo telefone (deixe em branco para manter): ") or contact['phone']
        email = input("Novo email (deixe em branco para manter): ") or contact['email']
        favorite = input("É favorito? (s/n): ").lower()
        
        self.contact_list[index] = {
            "id": contact_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite,
        }
        print(f"Contato '{name}' atualizado com sucesso.")
    
    
    def change_state_from_favorite_contact(self, contact_id: int):
        index = contact_id - 1
        contact = self.contact_list[index]
        contact['favorite'] = not contact['favorite']
        
        print(f"Contato '{contact['name']}' {'favoritado' if contact['favorite'] else 'desfavoritado'} com sucesso.")
    
    
    def show_favorite_contacts(self):
        print("Lista de contatos favoritos:")
        for contact in self.contact_list:
            if contact['favorite']:
                print(f"- {contact['name']}")
    
    
    def delete_contact(self, contact_id: int):
        contact = self.contact_list[contact_id - 1]
        self.contact_list.remove(contact)
        
        print(f"Contato '{contact['name']}' removido com sucesso.")
    
    
contact = Contact()
