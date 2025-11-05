class MyName:
    """Опис класу / Документація
    """
    total_names = 0 #Class Variable

    def __init__(self, name=None, domain="itcollege.lviv.ua") -> None:
 
        self.name = (name if name is not None else self.anonymous_user().name).capitalize()
        self.domain = domain  
        MyName.total_names += 1 #modify class variable
        self.my_id = self.total_names

    @property
    def whoami(self) -> str: 

        return f"My name is {self.name}"
    
    @property
    def name_length(self) -> int:
        return len(self.name)
    
    @property
    def my_email(self) -> str:
 
        return self.create_email()
    
    def create_email(self) -> str:

        return f"{self.name}@{self.domain}"

    @classmethod
    def anonymous_user(cls):

        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:

        return f"You say: {message}"
    
    @property
    def full_name(self) -> str:
        
        return f"User #{self.my_id}: {self.name} ({self.my_email})"
    

def save_to_file(self, filename="users.txt") -> None:
    with open(filename, "a", encoding="utf-8") as file:
        file.write(self.full_name + "\n")


print("Розпочинаємо створювати обєкти!")

names = ("bohdan", "marta", None)
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
print(f"Length of name: {me.name_length} letters")
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
{"<*>"*20}""")

print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")

new_message = "Я стомився :("
print(f"Нове привітання: {MyName.say_hello(new_message)}")