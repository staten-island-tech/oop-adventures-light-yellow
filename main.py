class prezs:
    def __init__(president,name,affection,personality,likes,dislikes,nickname):
        president.name = name
        president.__affection = affection
        president.personality = personality
        president.likes = likes
        president.dislikes = dislikes
        president.nickname = nickname
    def affection_up(president):
        president.__affection +=10
        print (president.name,"'s affection for y/n is now",president.__affection,"<3" )
Trump = prezs("Donald trump",-30,"tsundere",{"red caps", "tan spray","big arch"},{"learning"},"Trumpy-kun")
Biden = prezs("Joe biden",0 ,"forgetful",{"icecream", "his cildhood blanekt 'donkey'"}, {"alarms"}, "sleepy senpai")
Obama = prezs("Barrack obama",20,"chill",{"beatboxxing","grillcheese"},{"talking loudly"}, "obama-san")
lincoln = prezs("Abraham lincoln",10,"boxing tomboy but also theater kid",{"voting booths","musicals","dupliKate"},{"extortion","mustaches","omni-man"},"abby")
washington = prezs("George washington",20,"wierd childhood friend",{"quarters","you <3","BL manga"},{"popcorn","the beatles"},"weirdo")
jfk = prezs("John F Kennedy",-30,"popular kid",{"joyrides","talking"}, {"nerds"},"kenny-chan")
teddy = prezs("Theodore Rossevelt",0,"baseball tomboy",{"baseball"},{"creepy crawlies","algebra"},"teddy bear")
prezs.affection_up(Trump)