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


def get_approved_message(name,coupon,amount):
    return f"""
Hola! {name} Congrajulations,

We have recived your recyclabel waste. We highly appriciate your effors in saving our nature.

Reward Summary:

Amount   : Rs {amount}
Coupon no: {coupon}

We hope to see you again!
Feel free to inbox us if you have any quires related to this.
            
Best Regards,

Team Recycle

{choice(list_of_quotes)}
"""

def get_rejected_message(name):
    return f"""
Hello {name},
We Thank you for using our service.
We highly appriciate your effors in saving our nature. But We regreat to inform you that we are unable to process your request,We will consider this request Cancelled.

We hope to see you again!
Feel free to inbox us if you have any quires related to this.
            
Best Regards,

Team Recycle

{choice(list_of_quotes)}
"""
     