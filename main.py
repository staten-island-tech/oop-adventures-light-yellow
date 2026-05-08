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
    def affection_Cup(president):
        president.__affection +=20
        print (president.name,"'s affection for y/n is now",president.__affection,"<3, the system starts blushing" )
    def affection_Cdown(president):
        president.__affection -=20
        print (president.name,"'s affection for y/n is now",president.__affection,"</3, i hope you get hit by a car" )

Trump = prezs(1,"Donald trump",-30,"tsundere",{"red caps", "tan spray","big arch"},{"learning"},"Trumpy-kun")
Biden = prezs(2,"Joe biden",0 ,"forgetful",{"icecream", "his cildhood blanket 'blanky'"}, {"alarms"}, "sleepy senpai")
Obama = prezs(3,"Barrack obama",20,"chill",{"beatboxxing","grillcheese"},{"talking loudly"}, "obama-san")
lincoln = prezs(4,"Abraham lincoln",10,"boxing tomboy but also theater kid",{"voting booths","musicals","dupliKate"},{"extortion","mustaches","omni-man"},"abby")
washington = prezs(5,"George washington",50,"wierd childhood friend",{"quarters","you <3","BL manga"},{"popcorn","the beatles"},"weirdo")
jfk = prezs(6,"John F Kennedy",-30,"popular kid",{"joyrides","talking"}, {"nerds"},"kenny-chan")
teddy = prezs(7,"Theodore Rossevelt",0,"baseball tomboy",{"baseball"},{"creepy crawlies","algebra"},"teddy bear")

Classmates = [
{id:1,"name":"Donald trump","personality":"tsundere","likes":{"red caps", "tan spray","big arch"},"dislikes":{"learning"},"nicknames":"Trumpy-kun"},
{id:2,"name":"Joe biden","personality":"forgetful","likes":{"icecream", "his cildhood blanket 'blanky'"}, "dislikes":{"alarms"}, "nicknames":"sleepy senpai"},
{id:3,"name":"Barrack obama","personality":"chill","likes":{"beatboxxing","grillcheese"},"dislikes":{"talking loudly"}, "nicknames":"obama-san"},
{id:4,"name":"Abraham lincoln","personality":"boxing tomboy but also theater kid","likes":{"voting booths","musicals","dupliKate"},"dislikes":{"bullies","mustaches","omni-man"},"nicknames":"abby"},
{id:5,"name":"George washington","personality":"wierd childhood friend","likes":{"quarters","you <3","BL manga"},"dislikes":{"popcorn","the beatles"},"nicknames":"weirdo"},
{id:6,"name":"John F Kennedy","personality":"popular kid","likes":{"joyrides","talking"},"dislikes": {"nerds"},"nicknames":"kenny-chan"},
{id:7,"name":"Theodore Rossevelt","personality":"baseball tomboy","likes":{"baseball"},"dislikes":{"creepy crawlies","algebra"},"nicknames":"teddy bear"}
]

import random
truelove=False
random_classmates = random.choice(Classmates)
print(random_classmates["name"])
while truelove == False:
    print ("you encountered",random_classmates['name'], "in the hallway")
    inputRN = input('say 1:hi or 2:ignore')
    if inputRN == 1:
        print ("Hiii~ im",random_classmates["name"],"[insert text and stuff]")
        input ("1:*Malicously frame mog*",random_classmates["name"],",2: say 'my exp bar is low (๑/////๑')'","3:*talk about deepwoken lore*,4: *give chocoloate*")
        if inputRN ==1:
            prezs.affection_down
        elif inputRN == 2:
            prezs.affection_up
        elif inputRN == 3:
            prezs.affection_Cdown
        elif inputRN == 4:
            prezs.affection_Cup
        else:
            print ("you lowkirkuinely have a stroke and",random_classmates["name"],"walks away" )
    else:
        print ("you pass",random_classmates["name"])

