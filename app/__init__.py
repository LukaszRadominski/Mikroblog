# Najczęściej init   jest pusty, informują jednak Pythona, że to nie jest zwykły katalog, ale właśnie paczka (package) - tu jest to app, 
# i że mogą się w niej znajdować moduły. 
# Te moduły dostępne są przy pomocy kropki. Dodatkową zaletą paczki jest to, że może być zaimportowana. 
# W czasie importu wykonywany jest kod, który znajduje się w pliku __init__.py.


from flask import Flask    # 1
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)      # 2 Nazwa __name__ to predefiniowana w Pythonie zmienna, której wartością może być "__main__", gdy moduł wykonywany jest bezpośrednio. Jeśli moduł uruchamiany jest jako zależność, to w __name__ będzie znajdowała się jego nazwa.
app.config.from_object(Config) # Dodaję tu odczyt konfiguracji z obiektu Config
db = SQLAlchemy(app)  # wprowadzimy instancję bazy danych 
migrate = Migrate(app, db) # dodaję migrację


from app import routes     # 3  Import dopiero w tym wierszu to z kolei pewna sztuczka, która pomoże nam zabezpieczyć się przed problemem cyklicznych importów.  tworzymy tu po prostu instancję aplikacji i importujemy moduł routes.py. #  import pochodzi  paczki app, czyli czegoś zdefiniowanego przez nazwę folderu app oraz pliku __init__.py. Zmienna app, będąca instancją Flask, jest zawarta w tej paczce. Za chwilę to zobaczymy.
