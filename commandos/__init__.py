from commandos import Commandos

app = Commandos()

@app.command('action1')
def funkcja1():
    """Funkcja numer 1"""
    print(app.v)

@app.command('action2')
def funkcja2():
    """Funkcja numer 2"""
    print('funkcja2')
 
app.run()
