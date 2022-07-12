from flask import Flask
import sys
from customer_personality.logger import logging
from customer_personality.exception import Customer_PersonalityException

app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        customer_personality = Customer_PersonalityException(e, sys)
        logging.info(customer_personality.error_message)
        logging.info("We are testing logging module")
    return "CI CD pipeline has been established."

if __name__=="__main__":
    app.run(debug=True)
