import requests

API_URL = "http://www.omdbapi.com/?apikey=505480d7&s="


def search_movies(title):
    try:
        response = requests.get(API_URL + title)
        response.raise_for_status()
        data = response.json()

        if data["Response"] == "True":
            return data["Search"]
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при обращении к API: {e}")
        return None


def print_results(results):
    if results:
        for movie in results:
            print(f"Название: {movie['Title']}, Год: {movie['Year']}, Тип: {movie['Type']}")
    else:
        print("Ничего не найдено по вашему запросу.")


def main():
    while True:
        title = input("Введите название фильма (или напишите 'выход' чтобы завершить работу): ")

        if title.lower() == "выход":
            print("Завершение работы...")
            break

        results = search_movies(title)

        if results is not None:
            print_results(results)
        else:
            print("Произошла ошибка при поиске. Пожалуйста, попробуйте еще раз.")


if __name__ == "__main__":
    main()