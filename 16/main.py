#from turtle import Turtle, Screen
#my_turt = Turtle()
#my_turt.shape("turtle")
#my_turt.color("cyan")
#my_turt.forward(100)

#my_screen = Screen()
#my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
