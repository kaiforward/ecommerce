from django.apps import AppConfig


class PaymentConfig(AppConfig):
    name = 'payment'
    verbose_name = 'Payment'

    #import signal in app ready method
    def ready(self):
    	# import signal.handlers
    	import payment.signals
