
def poker(file):
    infile = open(file,'r')
    player1 = []
    player2 = []
    score_1 = []
    score_2 = []
    for lines in infile:
        player1.append(lines[0:14].split())
        player2.append(lines[14:].split())
    for plays1 in player1:
        score_1.append(card_safety(plays1))
    for plays2 in player2:
        score_2.append(card_safety(plays2))
    #print(omega(howmany(converted(sep(player1[1]))),howmany(converted(sep(player2[1])))))
                
        
    the_game1 = 0
    the_game2 = 0
    draw = 0
    dracu = 0

    #for other in range(1000):
#        if score_1[other][0] == "RF" or score_1[other][0] == "RF":
#            print (player1[other],score_1[other]," ", player2[other],score_2[other])

    for C in range(len(player1)):
        dracu += 1
        if game(score_1[C]) == game(score_2[C]):
            if pairs(sep(player1[C])) == "True" and pairs(sep(player2[C])) == "True":
                if int(draw_decider(converted(sep(player1[C])))) > int(draw_decider(converted(sep(player2[C])))):
                    the_game1 += 1
                elif int(draw_decider(converted(sep(player1[C])))) == int(draw_decider(converted(sep(player2[C])))):
                    if int(mini(howmany(converted(sep(player1[C]))))) > int(mini(howmany(converted(sep(player2[C]))))):
                        the_game1 += 1
                    else:
                        the_game2 += 1                
                else:
                    the_game2 += 1
            elif score_1[C][0] == "1P" and score_2[C][0] == "1P":
                if int(mini(howmany(converted(sep(player1[C]))))) == int(mini(howmany(draw_decider(converted(sep(player2[C])))))):
                    if omega(howmany(converted(sep(player1[C]))),howmany(converted(sep(player2[C]))))[0] > omega(howmany(converted(sep(player1[C]))),howmany(converted(sep(player2[C]))))[1]:
                        the_game1 += 1
                    else:
                        the_game2 += 1
                elif int(mini(howmany(converted(sep(player1[C]))))) > int(mini(howmany(converted(sep(player2[C]))))):
                    the_game1 += 1
                else:
                    the_game2 += 1
            elif score_1[C][0] == "Weak" and score_2[C][0] == "Weak":
                print ("Hell yea")
                if omega(howmany(converted(sep(player1[C]))),howmany(converted(sep(player2[C]))))[0] > omega(howmany(converted(sep(player1[C]))),howmany(converted(sep(player2[C]))))[1]:
                    the_game1 += 1
                else:
                    the_game2 += 1
        elif game(score_1[C]) > game(score_2[C]):
                the_game1 += 1
        else:
            the_game2 += 1

        
       
          
    print (the_game1,the_game2)
    infile.close()


def omega(micro1,micro2):
    outega = []
    box1 = []
    box2 = []
    for m1 in micro1:
        if micro1[m1] == 1:
            box1.append(int(m1))
    for m2 in micro2:
        if micro2[m2] == 1:
            box2.append(int(m2))
    for last in box1:
        if last in box2:
            box2.pop(box2.index(last))
            box1.pop(box1.index(last))
    outega.append(max(box1))
    outega.append(max(box2))
    return outega


    
    
def mini(mi):
    print ("Config mini")
    yt = 0
    for yth in mi:
        if mi[yth] == 1 and int(yth) > yt:
            yt = int(yth)
            
    return str(yt)
            

def mini(mi):
    print ("Config mini")
    yt = 0
    for yth in mi:
        if mi[yth] == 1 and int(yth) > yt:
            yt = int(yth)
            
    return str(yt)
            
    
def game(gl):
    game_point = 0
    if gl[0] == 'RF':
        game_point = int(gl[1]) + 145
    elif gl[0] == 'CStr8':
        game_point = int(gl[1]) + 130
    elif gl[0] == '4OK':
        game_point = int(gl[1]) + 114
    elif gl[0] == 'FulH':
        game_point = int(gl[1]) + 98
    elif gl[0] == 'flush':
        game_point = int(gl[1]) + 82
    elif gl[0] == 'Str8':
        game_point = int(gl[1]) + 66
    elif gl[0] == '3oK':
        game_point = int(gl[1]) + 49
    elif gl[0] == '2P':
        game_point = int(gl[1]) + 32
    elif gl[0] == '1P':
        game_point = int(gl[1]) + 15
    else:
        game_point = int(gl[1]) + 0
    return game_point

def sep(listr):
    work = []
    for iy in listr:
        work.append(iy[0])
    return work

def draw_decider(bank):
    out_decider = ""
    compare2 = max_dic(howmany(bank))[1]
    bad_count = 0
    versus = {}
    if pairs(bank) == "True":
        print ("here i was")
        versus = howmany(bank)
        for obc in versus:
            if versus[obc] == 2 and int(obc) < int(compare2):
                compare2 = versus[obc]
                out_decider = obc
    elif max_dic(howmany(bank))[0] == 2 and pairs(bank) != True:
        out_decider = mini(howmany(bank))
        
            
        
    '''
    if max_dic(versus)[0] == 2:
        print ("Hola")
        for obc in versus:
            if versus[obc] == 2 and int(obc) < int(compare2):
                compare2 = versus[obc]
                out_decider = obc
                break
            elif versus[obc] == 2 and bad_count == 0:
                compare2 = versus[obc]
                out_decider = obc
                bad_count += 1
            elif versus[obc] == 1 and int(obc) > int(compare2):
                compare2 = versus[obc]
                out_decider = obc
    '''
                
            
    return out_decider
    

def card_safety(list_cards_main):
    if len(list_cards_main) == 5:
        return splitter(hand(list_cards_main))

def hand(cards):
    letters1 = ""
    numbers1 = []
    counter1 = 0
    for luck in cards:
        numbers1.append(luck[0])
        letters1 += luck[1]
    numbers1 = converted(numbers1)
    '''
        else:
            for l in luck:                
                if counter1 == 0:
                    numbers1.append(l)
                    counter1 += 1
                else:
                    letters1 += l
                    counter1 = 0
    '''

    return ([letters1,numbers1])

def splitter(cardeck):
    out_put = []
    hand = ""
    power = ""
    letters = cardeck[0]
    numbers = []
    for iyu in cardeck[1]:
        numbers.append(iyu)
    '''
    counter1 = 0
    for luck in cards:
        if '10' in luck:
            numbers.append(luck[0:2])
            letters += luck[2:]
        else:
            for l in luck:                
                if counter1 == 0:
                    numbers.append(l)
                    counter1 += 1
                else:
                    letters += l
                    counter1 = 0
    '''
    #print(bubbleSort(['8', '4', '5', '6', '7']))
    #print(extra(howmany(converted(numbers))),"sex")
 


    if max_dic2(howmany(letters))[0] == 5  and (bubbleSort(converted(numbers)) == ['10','11','12','13','14']):
        #print("I reached here",max_dic(howmany(numbers))[0],numbers)
        hand = "RF"
        power = "14"
    elif max_dic2(howmany(letters))[0] == 5 and (is_sequence(numbers)[0] == "True"):
        #print("I reached here",max_dic(howmany(numbers))[0],numbers)
        hand = "CStr8"
        power = str(is_sequence(numbers)[1])
    elif max_dic(howmany(numbers))[0] == 4:
        #print("I reached here",max_dic(howmany(numbers))[0],numbers)
        hand = "4OK"
        power = max_dic(howmany(converted(numbers)))[1]
    
    elif max_dic2(howmany(letters))[0] == 5:
        #print("I reached here",max_dic(howmany(numbers))[0],numbers)
        hand = "flush"
        power = str(greates(cardeck[1]))
    
    elif full(numbers) == "True":
        #print("I reached here",max_dic(howmany(numbers))[0],numbers)
        hand = "FulH"
        power = max_dic(howmany(converted(numbers)))[1]

    elif is_sequence(numbers)[0] == "True":
        #print("I reached here",max_dic(howmany(numbers))[0],numbers)'
        hand = "Str8"
        power = is_sequence(numbers)[1]
    elif max_dic(howmany(numbers))[0] == 3:
        #print("I reached here",max_dic(howmany(numbers))[0],numbers)
        hand = "3oK"
        power = max_dic(howmany(converted(numbers)))[1] 
    elif pairs(numbers) == "True":
        #print("I reached here",max_dic(howmany(numbers))[0],numbers)
        hand = "2P"
        power = str(extra(howmany(converted(numbers))))
    elif max_dic(howmany(numbers))[0] == 2:
        #print("I reached here",max_dic(howmany(numbers))[0],numbers)
        hand = "1P"
        power = max_dic(howmany(converted(numbers)))[1] 
    else:
        #print("I reached here",max_dic(howmany(numbers))[0],numbers)
        hand = "Weak"
        power = greates(numbers)
    
    out_put.append(hand)
    out_put.append(power)
    return (out_put)
                      
def extra(dic2):
    extra_out = ""
    compare = 0
    for qwe in dic2:
        if dic2[qwe] == 2 and int(qwe) > compare:
            extra_out = qwe
            compare = dic2[qwe]
    return extra_out
            
        
           

def full(house):
    cycle = 0
    for xyzu in howmany(house):
        if howmany(house)[xyzu] == 2:
            cycle += 0.5
        elif howmany(house)[xyzu] == 3:
            cycle += 1
        if cycle == 1.5:
            return "True"
            cycle = 0
            
def pairs(pairs):
    cycle2 = 0
    for xyzu in howmany(pairs):
        if howmany(pairs)[xyzu] == 2:
            cycle2 += 1
    if cycle2 == 2:
        return "True"
        cycle2 = 0  
        
            
    
   
    
    
def is_sequence(what_seq):
    main_seq = ['2','3','4','5','6','7','8','9','10','11','12','13','14']
    sub_seq = []
    start_seq = 0
    your_seq = []
    while start_seq + 5 < 13:
        sub_seq.append(main_seq[start_seq:start_seq+5])
        start_seq += 1
        
    what_seq = card_order(what_seq)
    
    if what_seq in sub_seq:
        your_seq.append("True")
        your_seq.append(greates(what_seq))
    elif what_seq == (['2','3','4','5','14']):
        your_seq.append("True")
        your_seq.append('5')
    else:
        your_seq.append("F")
    return your_seq

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for g in range(passnum):
            if int(alist[g])>int(alist[g+1]):
                temp = alist[g]
                alist[g] = alist[g+1]
                alist[g+1] = temp
    return alist




def card_order(list_of_cards):
    '''
    order_cards = []
    while list_of_cards != []:
        order_cards.append(greates(list_of_cards))
        pop_val = list_of_cards.index(greates(list_of_cards))
        list_of_cards.pop(pop_val)
    '''
    return bubbleSort(converted(list_of_cards))
'''
def bottom_up(list_extra):
    bottom_Up = []
    for jak in reversed(list_extra):
        bottom_Up.append(jak)
    return(bottom_Up)
'''
    
def howmany(howmany):
    bucket1 = {}
    loop = 0
    for isp in howmany:
        if isp not in bucket1:
            bucket1[isp]= howmany.count(isp)
    return bucket1

def max_dic(dic):
    largest = 0
    type_suite = ""
    for kings in dic:
        if dic[kings] > largest:
            largest = dic[kings]
            type_suite = kings
        elif dic[kings] == largest and int(kings) > int(type_suite):
            largest = dic[kings]
            type_suite = kings
    return [largest, type_suite]

def max_dic2(dic5):
    largest2 = 0
    type_suite2 = ""
    for kings2 in dic5:
        if dic5[kings2] > largest2:
            largest2 = dic5[kings2]
            type_suite2 = kings2
        #elif dic[kings] == largest and int(kings) > int(type_suite):
#            largest = dic[kings]
#            type_suite = kings
    return [largest2, type_suite2]
    
        
def converted(conv):
    ixn = 0
    while ixn < 5:
        if conv[ixn] == "A":
            conv[ixn] = "14"
            ixn += 1
        elif conv[ixn] == "K":
            conv[ixn] = "13"
            ixn += 1
        elif conv[ixn] == "Q":
            conv[ixn] = "12"
            ixn += 1
        elif conv[ixn] == "J":
            conv[ixn] = "11"
        elif conv[ixn] == "T":
            conv[ixn] = "10"
            ixn += 1
        else:
            ixn += 1
    return conv
        
def greates(numh):
    great = 0
    if 'A' in numh or ('K' in numh) or ('Q' in numh) or ('J' in numh) or ('T' in numh):
        numh = converted(numh)
             
    for ixb in numh:
        if int(ixb) > great:
            great = int(ixb)
    return (str(great))


#print(is_sequence(['A','3','4','2','5']))
#print (greates(['A','J','5','6','7']))        
#card_safety(['4D','3D','5D','6D','7D'])
#card_safety(['JD','AD','10D','QD','KD'])
#card_safety(['10D','10H','10C','KS','KD'])
#card_safety(['10D','10S','10C','10H','KD'])
#card_safety(['AD','2D','3D','10D','KD'])
#card_safety(['AD','2D','3D','4C','5D'])
#card_safety(['AD','AC','AH','QC','5D'])
#card_safety(['AD','AC','2H','2C','5D'])
#print(card_safety(['AD','AC','2H','QC','5D']))
#print(draw_decider(howmany(converted(sep(['5D','6C','AH','QC','AD'])))))
#print(card_order(['A','A','A','3','4']))
#print(mini(howmany(converted(sep(['6D', '7C', '5D', '5H', '3S'])))))

poker('/Users/Siddhartha/Desktop/python/Python/csv repo/p054_poker.txt') 
