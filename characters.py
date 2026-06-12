class prezs: #3
    def __init__(president,id,name,affection,personality,likes,dislikes,nickname):
        president.name = name
        president.id =id
        president.__affection = affection
        president.personality = personality
        president.likes = likes
        president.dislikes = dislikes
        president.nickname = nickname
    def stats(president):
        print("Name:", president.name,",Affection:", president.__affection,",Personality:", president.personality,",Likes:", president.likes,",Dislikes:", president.dislikes,",Nickname:", president.nickname)
    def affection_up(president):
        president.__affection +=10
        print (president.name,"'s affection for y/n is now",president.__affection,"<3" )
    def affection_down(president):
        president.__affection -=10
        print (president.name,"'s affection for y/n is now",president.__affection,"</3, No-ot tha-hat i care hmph" )
    def affection_Cdown(president):
        president.__affection -=20
        print (president.name,"'s affection for y/n is now",president.__affection,"</3, i hope you get hit by a car" )
    def affection_Cup(president):
        president.__affection +=20
        print (president.name,"'s affection for y/n is now",president.__affection,"<3, the system starts blushing" )
    def confession(president, rejected):
        if president.__affection >= 100:
            print (president.name,"'s affection for y/n is now over 100 <3<3<3 and they confess")
            inputRN =input("1: accept or 2:nah")
            if inputRN == '1':
                if Trump.__affection >= 50:
                    print ("you accept and hold hands and skip home with",president.name)
                    print ("...")
                    print ("a pair of eyes stares at you from the darkness, as the moonlight fills the room, their silhouette is illuminated... its trump...")
                    print ("he whispers, 'youre mine y/n chan...' and lowkirkenuinely slimes you out")
                    print ("yandere trump ending😈🔪🩸")
                    return True
                else:
                    print("you spend the rest of your life with",president.name, "HAPPY ENDING!!:D")
                    return True
            elif inputRN == '2':
                president.__affection -= 200
                print("hell nah twin i see you as a brother")
                rejected.append(president.name)
            else:
                print ("you lowkey just die brochacho")
                return


Trump = prezs(1,"Donald trump",-30,"tsundere","tan spray","learning","Trumpy-kun")
Biden = prezs(2,"Joe biden",0 ,"forgetful","icecream", "alarms", "sleepy senpai")
Obama = prezs(3,"Barrack obama",20,"chill","grillcheese","talking loudly", "obama-san")
Lincoln = prezs(4,"Abraham lincoln",10,"boxing tomboy but also theater kid","musicals","omni-man","abby")
Washington = prezs(5,"George washington",50,"wierd childhood friend","BL manga","the beatles","weirdo")
Jfk = prezs(6,"John F Kennedy",-30,"popular kid","convertible","nerds","kenny-chan")
Teddy = prezs(7,"Theodore Rossevelt",0,"baseball tomboy","triple T","creepy crawlies","teddy bear")

Classmates = [
{"id":Trump,"name":"Donald trump","personality":"tsundere","likes":"tan spray","dislikes":"learning","nicknames":"Trumpy-kun"},
{"id":Biden,"name":"Joe biden","personality":"forgetful","likes":"icecream", "dislikes":"alarms", "nicknames":"sleepy senpai"},
{"id":Obama,"name":"Barrack obama","personality":"chill","likes":"grillcheese","dislikes":"talking loudly", "nicknames":"obama-san"},
{"id":Lincoln,"name":"Abraham lincoln","personality":"boxing tomboy but also theater kid","likes":"musicals","dislikes":"omni-man","nicknames":"abby"},
{"id":Washington,"name":"George washington","personality":"wierd childhood friend","likes":"BL manga","dislikes":"the beatles","nicknames":"weirdo"},
{"id":Jfk,"name":"John F Kennedy","personality":"popular kid","likes":"covertibles","dislikes": "airports","nicknames":"kenny-chan"},
{"id":Teddy,"name":"Theodore Rossevelt","personality":"baseball tomboy","likes":"triple T","dislikes":"creepy crawlies","nicknames":"teddy bear"}
]