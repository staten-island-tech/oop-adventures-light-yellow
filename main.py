import random
inputRN = 0
truelove=False


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
    def confession(president):
        if president.__affection >= 100:
            print (president.name,"'s affection for y/n is now over 100 <3<3<3 and they confess")
            inputRN =input("1: accept or 2:nah")
            if inputRN == '1':
                print("you spend the rest of your life with",president.name,"but lowkey like syyukno you keep on cheating ig sonion")
            elif inputRN == '2':
                print("hell nah twin i see you as a brother")
                president.__affection -= 200
                


Trump = prezs(1,"Donald trump",-30,"tsundere",{"red caps", "tan spray","big arch"},{"learning"},"Trumpy-kun")
Biden = prezs(2,"Joe biden",0 ,"forgetful",{"icecream", "his cildhood blanket 'blanky'"}, {"alarms"}, "sleepy senpai")
Obama = prezs(3,"Barrack obama",20,"chill",{"beatboxxing","grillcheese"},{"talking loudly"}, "obama-san")
Lincoln = prezs(4,"Abraham lincoln",10,"boxing tomboy but also theater kid",{"voting booths","musicals","dupliKate"},{"extortion","mustaches","omni-man"},"abby")
Washington = prezs(5,"George washington",50,"wierd childhood friend",{"quarters","you <3","BL manga"},{"popcorn","the beatles"},"weirdo")
Jfk = prezs(6,"John F Kennedy",-30,"popular kid",{"joyrides","talking"}, {"nerds"},"kenny-chan")
Teddy = prezs(7,"Theodore Rossevelt",0,"baseball tomboy",{"baseball"},{"creepy crawlies","algebra"},"teddy bear")

Classmates = [
{"id":Trump,"name":"Donald trump","personality":"tsundere","likes":{"red caps", "tan spray","big arch"},"dislikes":{"learning"},"nicknames":"Trumpy-kun"},
{"id":Biden,"name":"Joe biden","personality":"forgetful","likes":{"icecream", "his cildhood blanket 'blanky'"}, "dislikes":{"alarms"}, "nicknames":"sleepy senpai"},
{"id":Obama,"name":"Barrack obama","personality":"chill","likes":{"beatboxxing","grillcheese"},"dislikes":{"talking loudly"}, "nicknames":"obama-san"},
{"id":Lincoln,"name":"Abraham lincoln","personality":"boxing tomboy but also theater kid","likes":{"voting booths","musicals","dupliKate"},"dislikes":{"bullies","mustaches","omni-man"},"nicknames":"abby"},
{"id":Washington,"name":"George washington","personality":"wierd childhood friend","likes":{"quarters","you <3","BL manga"},"dislikes":{"popcorn","the beatles"},"nicknames":"weirdo"},
{"id":Jfk,"name":"John F Kennedy","personality":"popular kid","likes":{"joyrides","talking"},"dislikes": {"nerds"},"nicknames":"kenny-chan"},
{"id":Teddy,"name":"Theodore Rossevelt","personality":"baseball tomboy","likes":{"baseball"},"dislikes":{"creepy crawlies","algebra"},"nicknames":"teddy bear"}
]

random_classmates = random.choice(Classmates)
while truelove == False:
    print ("you encountered",random_classmates['name'], "in the hallway")
    inputRN = input('say 1:hi or 2:ignore')
    if inputRN =='1':
        print ("Hiii~ im",random_classmates["name"],"[insert text and stuff]")
        inputRN = input("1:*Malicously frame mog*,2: say 'my exp bar is low (๑/////๑')',3:*talk about deepwoken lore*,4: *give chocoloate*")
        if inputRN =='1':
            prezs.affection_down(random_classmates["id"])
        elif inputRN == '2':
            prezs.affection_up(random_classmates["id"])
        elif inputRN == '3':
            prezs.affection_Cdown(random_classmates["id"])
        elif inputRN == '4':
            prezs.affection_Cup(random_classmates["id"])
        else:
            print ("you lowkirkuinely have a stroke and they walks away" )
    elif inputRN =='2':
        print ("you passed",random_classmates["name"])
    else:
        print ("error")
    prezs.confession(random_classmates["id"])
    random_classmates = random.choice(Classmates)
