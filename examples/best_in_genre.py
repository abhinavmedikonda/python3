import requests

class best_in_genre:
    def get_best_from_api(self, genre):
        response = requests.get('https://jsonmock.hackerrank.com/api/tvseries')
        total_pages = response.json().get('total_pages')
        # print(total_pages)

        best = ''
        score = 0
        for i in range(1, total_pages+1):
            response = requests.get(f'https://jsonmock.hackerrank.com/api/tvseries?page={i}')
            # print(f'https://jsonmock.hackerrank.com/api/tvseries?page={i}')
            json = response.json()
            # print(json)
            for item in json.get('data'):
                # print(item)
                if genre in item.get('genre') and item.get('imdb_rating') > score:
                    best = item.get('name')
                    score = item.get('imdb_rating')
        
        return best

def main():
    cls = best_in_genre()
    print(cls.get_best_from_api('Action'))

if __name__ == '__main__':
    main()