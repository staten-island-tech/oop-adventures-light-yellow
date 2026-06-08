import random
lovers=[]
inputRN = 0
end = False
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
    def confession(president):
        if president.__affection >= 100:
            print (president.name,"'s affection for y/n is now over 100 <3<3<3 and they confess")
            inputRN =input("1: accept or 2:nah")
            if inputRN == '1':
                print("you spend the rest of your life with",president.name)
                global end
                end = True
            elif inputRN == '2':
                president.__affection -= 200
                print("hell nah twin i see you as a brother")
            else:
                print ("you lowkey just die brochacho")








previous_classmates = 0


               




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
random_classmates = random.choice(Classmates)


choosing = []
talkitve =0
day_count = 0
while not end:
    day_count +=1
    print ("day",day_count)
    if end == False:
        for encounters in range(3):
            random_classmates = random.choice(Classmates)
            if random_classmates == previous_classmates:
                while random_classmates == previous_classmates:
                    random_classmates = random.choice(Classmates)
            print ("you encountered",random_classmates['name'], "in the hallway")
            inputRN = input('1:hi or 2:ignore')
            if inputRN =='1':
                randomchoices = {
                'good':["i like your shoes y/n-kun","do you want to talk about excuse me sir?","thanks for studying with me twin","Are you the White House? Because I'd like to spend all my time at your address."],
                'bad':["want to talk about deepwoken?","can i get your mom's number","on charlie kirk youre chopped","healthcare type shi"],
                'supergood':["100 million to isreal?",["i think youre awesome",random_classmates['name'],"-chan"],["i brought your favoritre",random_classmates['likes']],["Are you Air Force One",random_classmates["nicknames"],"? Because my heart takes off whenever you're around."]],
                'superbad':[["i brought your favoritre",random_classmates['dislikes']],"on blue judas imma slime you out","i-i-i-i th-think-nk i-im-m ii-in lov-ve wi-ith y-y-yo-your dad (⸝⸝¬`‸´ ¬⸝⸝)","67"]
                }
                talkitve =+1
                print ("Hiii~ im",random_classmates['name'],"[insert text and stuff]")
                for catergories in randomchoices:
                    chosen_text = random.choice(randomchoices[catergories])
                    choosing.append(chosen_text)
                print("\n".join(
                    f"{i}: {item}"
                    for i, item in enumerate(choosing, start=1)
                ))
                inputRN = input("what shall you do?")
                if inputRN =='1':
                    prezs.affection_up(random_classmates["id"])
                elif inputRN == '2':
                    prezs.affection_down(random_classmates["id"])
                elif inputRN == '3':
                    prezs.affection_Cup(random_classmates["id"])
                elif inputRN == '4':
                    prezs.affection_Cdown(random_classmates["id"])
                else:
                    print ("you lowkirkuinely have a stroke and they walks away" )
            elif inputRN =='2':
                print ("you passed",random_classmates["name"])
            else:
                print ("error")
            prezs.confession(random_classmates["id"])
            if end == True:
                break
            previous_classmates = random_classmates
            choosing.clear()
    if end == False:
        print ("you head home from school and sleep")
        inputRN = input("1: go to sleep ,2: check stats")
        if inputRN == "2":
            for ppl in Classmates:
                prezs.stats(ppl["id"])
            print("youve talked",talkitve,"times in",day_count,"days")
