class prezs:
    def __init__(president,id,name,affection,personality,likes,dislikes,nickname):
        president.name = name
        president.id =id
        president.__affection = affection
        president.personality = personality
        president.likes = likes
        president.dislikes = dislikes
        president.nickname = nickname
    def affection_up(president):
        president.__affection +=10
        print (president.name,"'s affection for y/n is now",president.__affection,"<3" )
    def affection_down(president):
        president.__affection -=10
        print (president.name,"'s affection for y/n is now",president.__affection,"</3, No-ot tha-hat i care hmph" )

Trump = prezs(1,"Donald trump",-30,"tsundere",{"red caps", "tan spray","big arch"},{"learning"},"Trumpy-kun")
Biden = prezs(2,"Joe biden",0 ,"forgetful",{"icecream", "his cildhood blanket 'blanky'"}, {"alarms"}, "sleepy senpai")
Obama = prezs(3,"Barrack obama",20,"chill",{"beatboxxing","grillcheese"},{"talking loudly"}, "obama-san")
lincoln = prezs(4,"Abraham lincoln",10,"boxing tomboy but also theater kid",{"voting booths","musicals","dupliKate"},{"extortion","mustaches","omni-man"},"abby")
washington = prezs(5,"George washington",50,"wierd childhood friend",{"quarters","you <3","BL manga"},{"popcorn","the beatles"},"weirdo")
jfk = prezs(6,"John F Kennedy",-30,"popular kid",{"joyrides","talking"}, {"nerds"},"kenny-chan")
teddy = prezs(7,"Theodore Rossevelt",0,"baseball tomboy",{"baseball"},{"creepy crawlies","algebra"},"teddy bear")

Classmates = [
{id:1,"name":"Donald trump","affection":-30,"personality":"tsundere","likes":{"red caps", "tan spray","big arch"},"dislikes":{"learning"},"nicknames":"Trumpy-kun"},
{id:2,"name":"Joe biden","affection":0 ,"personality":"forgetful","likes":{"icecream", "his cildhood blanket 'blanky'"}, "dislikes":{"alarms"}, "nicknames":"sleepy senpai"},
{id:3,"name":"Barrack obama","affection":20,"personality":"chill","likes":{"beatboxxing","grillcheese"},"dislikes":{"talking loudly"}, "nicknames":"obama-san"},
{id:4,"name":"Abraham lincoln","affection":10,"personality":"boxing tomboy but also theater kid","likes":{"voting booths","musicals","dupliKate"},"dislikes":{"bullies","mustaches","omni-man"},"nicknames":"abby"},
{id:5,"name":"George washington","affection":50,"personality":"wierd childhood friend","likes":{"quarters","you <3","BL manga"},"dislikes":{"popcorn","the beatles"},"nicknames":"weirdo"},
{id:6,"name":"John F Kennedy","affection":-30,"personality":"popular kid","likes":{"joyrides","talking"},"dislikes": {"nerds"},"nicknames":"kenny-chan"},
]

import random
truelove=False
random_mates = random.choice(Classmates)
print(random_mates["name"])