#!/usr/bin/python

import logging.config
import cgi
import stripe
import traceback

logging.basicConfig(
    filename='stripe.log',
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


try:
    form = cgi.FieldStorage()

    logger.info(form)

    stripe_token = form['stripeToken'].value
    mail_address = form['stripeEmail'].value

    stripe.api_key = "sk_test_xxxxxxxxxxxxxxxxxxxxxxx"

    stripe.Charge.create(
        amount=2000,
        currency="jpy",
        description="Charge for {mail}".format(mail=mail_address),
        source=stripe_token
    )

except:
    logger.error(traceback.format_exc())
