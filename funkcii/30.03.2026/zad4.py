def make_greeter(language):
    def greeter(name):
        if language == "bg":
            print(f"Здравей, {name}!")
        elif language=='en':
            print(f"Hello, {name}!")
    
    return greeter  


bggr = make_greeter('bg')
bggr('Иван') 
engr = make_greeter('en')
engr('Ivan') 
