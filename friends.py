import requests

def counting_points(string_date):
    count = 0
    for char in string_date:
        if char == '.':
            count += 1
    return count

def splitting_year(string_date):
    new_string = ''
    count = 0
    for char in string_date:
        if char == '.':
            count += 1
            continue
        if count == 2:
            new_string += char
    return new_string

def calc_age(uid):
    ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'
    url = 'https://api.vk.com/method/users.get'
    params = {'user_ids': uid,
              'access_token': '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711', 'v': '5.71'}
    r = requests.get(url=url, params=params).json()
    id = r['response'][0]['id']
    url = 'https://api.vk.com/method/friends.get'
    params = {'user_id': id,
              'access_token': '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711', 'v': '5.71',
              'fields': 'bdate'}
    r = requests.get(url, params=params).json()
    date_list = []
    for elem in r['response']['items']:
        if 'bdate' in elem:
            if counting_points(elem['bdate']) > 1:
                date_list.append(2020 - int(splitting_year(elem['bdate'])))

    date_map = {}
    for elem in date_list:
        if elem not in date_map:
            date_map[elem] = date_list.count(elem)

    tmp = sorted(date_map.items(), key=lambda para: para[0])
    tmp = sorted(tmp, key=lambda para: para[1], reverse=True)
    return tmp

if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)