# potrzebne są ustawienia konfiguracyjne na poziomie aplikacji. 
# Umieścimy je tym razem w osobnym module (config.py)

import os




BASE_DIR = os.path.abspath(os.path.dirname(__file__))    # 1 o często spotykany sposób na to, by ustawić folder, który będzie punktem odniesienia dla innych operacji. Po prostu otrzymujemy ścieżkę do katalogu, w którym znajduje się nasz plik. To w nim możemy chcieć utworzyć bazę danych.

class Config:
   SECRET_KEY = os.environ.get("SECRET_KEY") or "remember-to-add-secret-key"    # 2 SECRET_KEY jest używany wszędzie tam, gdzie aplikacja będzie coś szyfrować.
   SQLALCHEMY_DATABASE_URI = (                           # 3  Na początku szukamy tam konfiguracji, a jeśli jej nie znajdziemy, to ustawiamy schemat SQLite dla pliku mikroblog.db.
           os.environ.get('DATABASE_URL') or
           'sqlite:///' + os.path.join(BASE_DIR, 'mikroblog.db')
   )
   SQLALCHEMY_TRACK_MODIFICATIONS = False  # Wyłączy to funkcjonalność SQLAlchemy, polegającą na śledzeniu zmian w obiektach i emitowaniu sygnałów, gdy takie zmiany występują. To obciążające, więc powinno być wyłączane, jeśli nie jest potrzebne.