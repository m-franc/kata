#https://www.codewars.com/kata/58298e19c983caf4ba000c8d/train/python

def min_umbrellas(weather):
    where_are_umb = {"home" : 0,
                     "work" : 0}
    nb_umbrellas = 0
    conditions = {"clear" : 0,
                  "sunny" : 0,
                  "cloudy" : 0,
                  "overcast" : 0,
                  "windy" : 0,
                  "rainy" : 1,
                  "thunderstorms" : 1}
    for i, hd_weather in enumerate(weather):
        if conditions[hd_weather] == 1:
            if i % 2 == 0:
                if where_are_umb["home"] == 1:
                    where_are_umb["home"] = 0
                    where_are_umb["work"] = 1
                else:
                    nb_umbrellas += 1
                    where_are_umb["work"] = 1
            else:
                if where_are_umb["work"] == 1:
                    where_are_umb["work"] = 0
                    where_are_umb["home"] = 1
                else:
                    nb_umbrellas += 1
                    where_are_umb["home"] = 1
    return nb_umbrellas
print(min_umbrellas(['thunderstorms', 'thunderstorms', 'windy', 'rainy', 'thunderstorms', 'windy', 'rainy', 'thunderstorms', 'windy', 'thunderstorms', 'rainy', 'thunderstorms', 'rainy', 'windy', 'thunderstorms', 'thunderstorms', 'sunny', 'sunny', 'thunderstorms', 'rainy', 'windy', 'cloudy', 'rainy', 'windy', 'cloudy', 'thunderstorms', 'sunny', 'rainy', 'rainy', 'thunderstorms', 'thunderstorms', 'thunderstorms', 'rainy', 'thunderstorms', 'rainy', 'sunny', 'thunderstorms', 'thunderstorms', 'thunderstorms', 'sunny', 'thunderstorms', 'windy', 'cloudy', 'windy', 'thunderstorms', 'thunderstorms', 'rainy', 'windy', 'windy', 'windy', 'sunny', 'windy', 'windy', 'windy', 'thunderstorms', 'rainy', 'thunderstorms', 'sunny', 'cloudy', 'thunderstorms', 'cloudy', 'thunderstorms', 'windy', 'windy', 'thunderstorms', 'thunderstorms', 'thunderstorms', 'thunderstorms', 'rainy', 'rainy', 'cloudy', 'windy', 'cloudy', 'rainy', 'windy', 'windy', 'rainy', 'thunderstorms', 'windy', 'thunderstorms', 'thunderstorms', 'rainy', 'windy', 'thunderstorms', 'rainy', 'windy', 'thunderstorms', 'thunderstorms', 'thunderstorms', 'windy', 'sunny', 'windy', 'windy', 'rainy', 'thunderstorms', 'rainy', 'thunderstorms', 'cloudy', 'thunderstorms', 'rainy']))