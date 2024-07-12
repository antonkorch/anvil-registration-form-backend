from db_commands import create_db, drop_db, add_client
from sqlalchemy import create_engine
import anvil.server
import configparser


config = configparser.ConfigParser()
config.read('settings.ini')
token = config['General']['token']

engine = create_engine('sqlite:///clients.db')
drop_db(engine)
create_db(engine)

@anvil.server.callable
def add_client_to_db(name, company, city, phone, email):
    print (name, company, city, phone, email)
    add_client(engine, name, company, city, phone, email)
    return True


if __name__ == "__main__":
  anvil.server.connect(token)
  anvil.server.wait_forever()