from flask import Flask, render_template, request, redirect
from rpsls_logic import *
from rpsls_dictionaries import *

images =["Rock.png", "Paper.png", "Scissors.png", "Lizard.png", "Spock.png"]

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/play', methods=["GET", "POST"])
def play():
   if request.method == 'POST':
      return render_template("play.html")
   else:
      return redirect('/')

@app.route('/winner', methods=["POST"])
def winner():
   user_input = request.form['user_input']
   computer_choice = get_computer_choice()
   if user_input == computer_choice:
      winneris = (f"You both choose {user_input}, tie!")
      messageis = "Draw!!!"
      
      
   else:   
      winneris = get_winner(user_input, computer_choice)
      messageis = get_message(user_input, computer_choice)
      
      
      
  
   return render_template("winner.html", user_input = user_input, computer_choice = computer_choice, winneris = winneris, messageis = messageis)

@app.route('/bye', methods=["POST"])
def bye():
   if request.form['play_again'] == "False":
      return render_template("bye.html")
   else:
      return render_template("play.html")



if __name__ == '__main__':
   app.run()


