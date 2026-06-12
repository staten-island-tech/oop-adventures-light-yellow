from characters import prezs, Trump, Classmates
import random
lovers=[]
rejected = []
inputRN = 0
end = False
print ("It's your first day at Eville High School. You walk through the doors for the first time, and the first thing you notice is that.. ALL THE STUDENTS ARE U.S PRESIDENTS AND THEY'RE SUPER DUPER KAWAII!!!! Your heart races as you see all the geriatric old men roaming the halls. YOU NEED TO DATE ONE OF THEM!!!")
print("Donald Trump is a yandere that seems pretty unfriendly at first.. Biden and Teddy Roosevelt seem indifferent towards you, while Obama and Lincoln make an effort to be friendly. Jfk, on the other hand, seems to dislike you at first.. George Washington is your childhood friend that you've known for a long time, so his affection starts out higher. Good luck!!")
previous_classmates = 0
choosing = []
talkitve =0
day_count = 0
while not end:
    day_count +=1
    print ("day",day_count)
    if end == False:
        if len(rejected) >= 3:
            print ("You walk into school on the", day_count, "day, and everyone lowrkikenuinely ignores you because you have a reputation for leading people on and then rejecting them. Everyone freaking hates you bro you suck.", "SINGLE FOREVER ENDING")
            end = True
            break
        for encounters in range(3):
            random_classmates = random.choice(Classmates)
            if random_classmates == previous_classmates:
                while random_classmates == previous_classmates:
                    random_classmates = random.choice(Classmates)
            print ("you encountered",random_classmates['name'], "in the hallway")
            # classmate appear code here
            inputRN = input('1:hi or 2:ignore')
            if inputRN =='1':
                randomchoices = {
                'good':["i like your shoes y/n-kun","do you want to talk about excuse me sir?","thanks for studying with me twin","Are you the White House? Because I'd like to spend all my time at your address."],
                'bad':["want to talk about deepwoken?","can i get your mom's number","on charlie kirk youre chopped","healthcare type shi"],
                'supergood':["100 million to isreal?",["i think youre awesome",random_classmates['name'],"-chan"],["i brought your favoritre",random_classmates['likes']],["Are you Air Force One",random_classmates["nicknames"],"? Because my heart takes off whenever you're around."]],
                'superbad':[["i brought your favoritre",random_classmates['dislikes']],"on blue judas imma slime you out","i-i-i-i th-think-nk i-im-m ii-in lov-ve wi-ith y-y-yo-your dad (⸝⸝¬`‸´ ¬⸝⸝)","67"]
                }
                talkitve +=1
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
            if prezs.confession(random_classmates["id"], rejected):
                end = True
                break
            previous_classmates = random_classmates
            choosing.clear()
    if end == False:
        print ("you head home from school")
        inputRN = input("1: go to sleep ,2: check stats")
        if inputRN == "2":
            for ppl in Classmates:
                prezs.stats(ppl["id"])
            print("youve talked",talkitve,"times in",day_count,"days")