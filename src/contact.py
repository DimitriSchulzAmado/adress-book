class Contact:
    def __init__(self):
        self.contact_list = []
    
    @classmethod
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


    @classmethod
    def show_contacts(self):
        if not self.contact_list:
            print("Nenhum contato encontrado.")
            return
        
        for index, contact in enumerate(self.contact_list, start=1):
            favorite_mark = "★" if contact["favorite"] else "☆"
            print(f"{index}. {contact['name']} {favorite_mark}")
    
    
    @classmethod
    def contact_detail(self, contact_id: int):
        index = contact_id - 1
        contact = self.contact_list[index]
        
        print(f'\nNome: {contact['name']} \
                \nPhone: {contact['phone']} \
                \nE-mail: {contact['email']} \
                \nFavorito: {"★" if contact['favorite'] else "☆"}')
    
    
    def edit_contact():
        pass
    
    
    def set_contact_to_favorite():
        pass
    
    
    def show_favorite_contacts():
        pass
    
    
    def delete_contact():
        pass
    
    
contact = Contact()
