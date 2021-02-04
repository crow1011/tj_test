# tj_test
Проект выполнен в качестве тестового задания, практической пользы не несет, go out

основной файл main.py

пример запуска 
```sh
python3 main.py data/ AAPL
```


### Для запуска тестов:
 - python -m unittest tests/full_test.py
 - pytest -s

*\*выполнять из корневой директории проекта*


___________________________________________________________

Замеры на 122к строк в одном из файлов
Без генераторов: Current memory usage is 0.01916MB; Peak was 162.234025MB
С генераторами: Current memory usage is 0.017957MB; Peak was 15.973011MB
