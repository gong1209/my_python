response={} # 建立一個空字典

while True:
    name=input("What's your name?")
    score=input("Your score is ?")
    response[name]=score # 建立name為鍵score為值的鍵-值對然後存到response字典中

    continue_prompt = input("Would you like to let someone else respond? (yes/no)")
    if continue_prompt=="no": # 如果continue_prompt=="no"就跳出迴圈
        break
    
for name,score in response.items(): # items()方法會讓for迴圈將每個鍵-值對分別存到name和place的變數中
    print(name+"'s score is  "+score)






