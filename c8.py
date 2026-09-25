#sets
dict={
    "bangalore":"besi bele bath",
    "mangalore":"fish",
    "davangere":"bene dosa"
}
print(dict)

dict["sira"]="mutton"
print(dict)

dict["bangalore"]="Ragi muddhe"
print(dict)

mang=dict.pop("mangalore")
print(mang)

#del dict["mangalore"]
print(dict)

print(dict.keys())
print(dict.values())
print(dict.items())



two_frnds={
    "friend_1":{
        "name":"sangeetha",
        "fav_sub":"maths",
        "fav_food":"biriyani"
    },
    "friend_2":{
        "name":"keerthana",
        "fav_sub":"maths",
        "fav_food":"fish"
    }
    
    }
a=two_frnds["friend_2"]["fav_food"]
print(f"Keerthana's fav food is {a}.")



