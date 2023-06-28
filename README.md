# CutIt
## Описание
CutIt - это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

Удобнее использовать короткие ссылки. Например, ссылки http://yacut.ru/lesson и http://yacut.ru/12e07d воспринимаются лучше, чем https://www.google.com/url?sa=i&url=%3A%2F%2Fwww.theguardian.com%2Flifeandstyle&source=images

Описание API можно посмотреть в openapi.yml
## Как запустить проект
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:helhander/cutit.git
```

```
cd cutit
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Linux/macOS

    ```
    source venv/bin/activate
    ```

* Windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить проект:

```
export FLASK_APP=cutit
flask run
```