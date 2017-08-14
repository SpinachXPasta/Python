headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Dicovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papper:bok Review: Totally Triffic"]

news_ticker = ""
for head in headlines:
    if len(news_ticker) + len(head) >= 140:
        n = 0
        while len(news_ticker) < 140:
            news_ticker += head[n]
            n = n + 1
    else:
        news_ticker += head + " "
    
print (news_ticker)
