# class Game:
#     def __init__(self):
#         self.rooms = self.create_rooms()
#         self.player = Player(self.rooms['Entrance Hall'])

#     def create_rooms(self):
#         # Create Rooms
#         entrance_hall = Room("Entrance Hall", "A large hall with doors to the north and east.")
#         library = Room("Library", "A dusty room filled with old books. There is a locked chest here.")
#         armory = Room("Armory", "An armory with a sword on the wall.")
#         secret_room = Room("Secret Room", "A hidden room filled with treasures.")

#         # Set exits
#         entrance_hall.exits = {'north': library, 'east': armory}
#         library.exits = {'south': entrance_hall, 'east': secret_room}
#         armory.exits = {'west': entrance_hall}
#         secret_room.exits = {'west': library}

#         # Place items
#         key = Item("Key", "A small rusty key.", usable_in_room="Library")
#         sword = Item("Sword", "A shiny sword with intricate designs.")
#         treasure=Item("Treasure","A chest filled with Golds and Jewels")
        
#         # Add items to rooms
#         library.add_item(key)
#         armory.add_item(sword)
#         secret_room.add_item(treasure)

#         # Return dictionary of rooms
#         return {
#             'Entrance Hall': entrance_hall,
#             'Library': library,
#             'Armory': armory,
#             'Secret Room': secret_room
#         }

#     def start_game(self):
#         print("Welcome to the Adventure Game!")
#         print("Type 'help' to see the list of commands.\n")
#         self.game_loop()

#     def game_loop(self):
#         while True:
#             print("\n" + self.player.current_room.describe())
#             command = input("What would you like to do? ").strip().lower()
#             if command == "quit":
#                 print("Thank you for playing!")
#                 break
#             else:
#                 self.handle_input(command)

#     def handle_input(self, command):
#         words = command.split()
#         if not words:
#             return
        
#         action = words[0]
#         if action == "move" and len(words) == 2:
#             self.player.move(words[1])
#         elif action == "take" and len(words) == 2:
#             self.player.take_item(words[1])
#         elif action == "use" and len(words) == 2:
#             self.player.use_item(words[1])
#         elif action == "inventory" and len(words) == 1:
#             self.player.show_inventory()
#         elif action == "help" and len(words) == 1:
#             self.show_help()
#         else:
#             print("Invalid command. Type 'help' for a list of commands.")

#     def show_help(self):
#         print("\nCommands:")
#         print("  move [direction] - Move to a room in the specified direction (north, south, east, west).")
#         print("  take [item] - Pick up an item in the current room.")
#         print("  use [item] - Use an item from your inventory.")
#         print("  inventory - Show your current inventory.")
#         print("  quit - Exit the game.")


# class Player:
#     def __init__(self, start_room):
#         self.current_room = start_room
#         self.inventory = []

#     def move(self, direction):
#         if direction in self.current_room.exits:
#             self.current_room = self.current_room.exits[direction]
#             print(f"You move {direction} to the {self.current_room.name}.")
#         else:
#             print("You can't go that way.")

#     def take_item(self, item_name):
#         item = self.current_room.get_item(item_name)
#         if item:
#             self.inventory.append(item)
#             self.current_room.remove_item(item)
#             print(f"You picked up the {item_name}.")
#         else:
#             print(f"There is no {item_name} here.")

#     def use_item(self, item_name):
#         item = next((i for i in self.inventory if i.name.lower() == item_name), None)
#         if item:
#             if item.usable_in_room == self.current_room.name:
#                 print(f"You used the {item_name} in the {self.current_room.name}.")
#                 if item_name == "key" and self.current_room.name == "Library":
#                     print("The key unlocks the chest! Inside, you find a treasure map!")
#             else:
#                 print(f"The {item_name} can't be used here.")
#         else:
#             print(f"You don't have a {item_name} in your inventory.")

#     def show_inventory(self):
#         if self.inventory:
#             print("Inventory:", ", ".join([item.name for item in self.inventory]))
#         else:
#             print("Your inventory is empty.")


# class Room:
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description
#         self.exits = {}
#         self.items = []

#     def add_item(self, item):
#         self.items.append(item)

#     def remove_item(self, item):
#         self.items.remove(item)

#     def get_item(self, item_name):
#         for item in self.items:
#             if item.name.lower() == item_name:
#                 return item
#         return None

#     def describe(self):
#         description = f"{self.name}\n{self.description}\nExits: {', '.join(self.exits.keys())}"
#         if self.items:
#             description += "\nItems: " + ", ".join([item.name for item in self.items])
#         return description


# class Item:
#     def __init__(self, name, description, usable_in_room=None):
#         self.name = name
#         self.description = description
#         self.usable_in_room = usable_in_room


# # Start the game
# if __name__ == "__main__":
#     game = Game()
#     game.start_game()


import tkinter as tk
from tkinter import messagebox

class Game:
    def __init__(self):
        self.rooms = self.create_rooms()
        self.player = Player(self.rooms['Entrance Hall'])
        self.window = self.create_window()
        self.update_room_display()

    def create_rooms(self):
        entrance_hall = Room("Entrance Hall", "A large hall with doors to the north and east.")
        library = Room("Library", "A dusty room filled with old books. There is a locked chest here.")
        armory = Room("Armory", "An armory with a sword on the wall.")
        secret_room = Room("Secret Room", "A hidden room filled with treasures.")

        entrance_hall.exits = {'north': library, 'east': armory}
        library.exits = {'south': entrance_hall, 'east': secret_room}
        armory.exits = {'west': entrance_hall}
        secret_room.exits = {'west': library}

        key = Item("Key", "A small rusty key.")
        sword = Item("Sword", "A shiny sword with intricate designs.")
        treasure = Item("Treasure", "A chest filled with gold and jewels.")

        library.add_item(key)
        armory.add_item(sword)
        secret_room.add_item(treasure)

        return {
            'Entrance Hall': entrance_hall,
            'Library': library,
            'Armory': armory,
            'Secret Room': secret_room
        }

    def create_window(self):
        window = tk.Tk()
        window.title("Text-Based Adventure Game")

        self.room_label = tk.Label(window, text="", wraplength=300)
        self.room_label.pack(pady=10)

        self.command_entry = tk.Entry(window)
        self.command_entry.pack(pady=5)

        self.submit_button = tk.Button(window, text="Submit", command=self.handle_input)
        self.submit_button.pack(pady=5)

        self.inventory_button = tk.Button(window, text="Show Inventory", command=self.player.show_inventory_gui)
        self.inventory_button.pack(pady=5)

        return window

    def update_room_display(self):
        self.room_label.config(text=self.player.current_room.describe())

    def handle_input(self):
        command = self.command_entry.get().strip().lower()
        self.command_entry.delete(0, tk.END)  # Clear the input field
        if command == "quit":
            self.window.quit()
        else:
            action_parts = command.split()
            if action_parts[0] == "move" and len(action_parts) == 2:
                self.player.move(action_parts[1])
            elif action_parts[0] == "take" and len(action_parts) == 2:
                self.player.take_item(action_parts[1])
            elif action_parts[0] == "use" and len(action_parts) == 2:
                self.player.use_item(action_parts[1])
            else:
                messagebox.showinfo("Invalid Command", "Type 'help' for a list of commands.")

            self.update_room_display()

    def start_game(self):
        self.window.mainloop()


class Player:
    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
        else:
            messagebox.showinfo("Invalid Move", "You can't go that way.")

    def take_item(self, item_name):
        item = self.current_room.get_item(item_name)
        if item:
            self.inventory.append(item)
            self.current_room.remove_item(item)
            messagebox.showinfo("Item Taken", f"You picked up the {item_name}.")
        else:
            messagebox.showinfo("Item Not Found", f"There is no {item_name} here.")

    def use_item(self, item_name):
        item = next((i for i in self.inventory if i.name.lower() == item_name), None)
        if item:
            messagebox.showinfo("Item Used", f"You used the {item_name}.")
        else:
            messagebox.showinfo("Item Not Found", f"You don't have a {item_name}.")

    def show_inventory_gui(self):
        if self.inventory:
            inventory_list = ", ".join([item.name for item in self.inventory])
            messagebox.showinfo("Inventory", f"Your inventory: {inventory_list}")
        else:
            messagebox.showinfo("Inventory", "Your inventory is empty.")


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name:
                return item
        return None

    def describe(self):
        description = f"{self.name}\n{self.description}\nExits: {', '.join(self.exits.keys())}"
        if self.items:
            description += "\nItems: " + ", ".join([item.name for item in self.items])
        return description


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


# Start the game
if __name__ == "__main__":
    game = Game()
    game.start_game()
