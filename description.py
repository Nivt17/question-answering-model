description = """
URFU_TextApp API поможет использовать ML для решения задач с текстами. 🚀

## Методы

Есть два основных метода:
* /prdict/ - позволяет отправить текст и вопрос к этому тексу. В ответ приходит пара вопрос|ответ.
* /predict_sequel/ - дополняет произвольный текст цитатми из "Преступления и наказания", наиболее подходящими по смыслу.

## Авторы

* Веселина Зацепина
* Цинцов Никита
* Констатин Кожемяков

Лицензия:
"""

tags_metadata = [
    {
        "name": "Вопрос|Ответ",
        "description": "Находит ответ в тексте",
        "externalDocs": {
            "description": "TF.HubModel",
            "url": "https://tfhub.dev/see--/bert-uncased-tf2-qa/1",
        },
    },
    {
        "name": "Преступление и наказание",
        "description": "Продолжает текст походящей цитатой из книги",
        "externalDocs": {
            "description": "HF.model",
            "url": "https://bit.ly/3Ilck7L",
        },
    },
    {
        "name": "Запрос на доступность",
        "description": "Выдает дефолтный ответ, если API доступно",

    },
]
