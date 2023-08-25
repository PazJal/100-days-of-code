def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return ""
  return f"Result: {f_name.title()} {l_name.title()}"
print(format_name(input("What is your first name? \n"), input("What is your last name? \n")))