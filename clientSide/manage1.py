#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import threading
import vintagecorner.sL as sL
import signal


# class WsConexao(threading.Thread):

def run():
    sL.iniciar()
# class Aplicacao(threading.Thread):
#
#     def run(self):
def main():
        """Run administrative tasks."""
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        print('--------- ',sys.argv)


        signal.signal(signal.SIGINT, run)
        signal.signal(signal.SIGTERM, run)
        execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # ws=WsConexao()
    # app=Aplicacao()
    # ws.start()
    # app.start()
    main()

