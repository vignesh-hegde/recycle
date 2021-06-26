from random import choice
list_of_quotes = [
                '"The environment is where we all meet; where all have a mutual interest; it is the one thing all of us share." -Lady Bird Johnson',
                '"The good man is the friend of all living things." -Gandhi',
                '"The earth is what we all have in common." - Wendell Berry',
                '"Nature is painting for us, day after day, pictures of infinite beauty." - John Ruskin',
                '"He that plants trees loves others beside himself." - Thomas Fuller',
                '"To leave the world better than you found it, sometimes you have to pick up other people\'s trash." - Bill Nye',
                '"Every day is Earth Day, and I vote we start investing in a secure climate future right now." -Jackie Speier'
            ]

def get_message(name):
    return f"""
Hello {name},

We have recived your request to pick up recyclable waste,Our agent will Call you soon and schedule a pick up time.
We hope to see you again!
Feel free to inbox us if you have any quires related to this.
            
Best Regards,

Team Recycle

{choice(list_of_quotes)}
"""

     