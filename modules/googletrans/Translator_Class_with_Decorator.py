'https://medium.com/@tomisinabiodun/understanding-decorators-in-python-b6d7adbd1ea1'


from googletrans import Translator

translator = Translator()

APP_LANGUAGE = 'fr'


def translate(func):
    def replacement_func(*args, **kwargs):
        result = func(*args, **kwargs)
        return translator.translate(result, dest=APP_LANGUAGE).text

    return replacement_func


@translate
def greet_someone(name: str):
    return f"Hello and welcome, {name}!"

print(greet_someone("Pierre"))