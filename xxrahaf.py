import tambotapi, random, requests
token = "thWEVw3sYHDnOJDUEU1GFrswxOJ2MORHhyYzGlSo3vM"
bot = tambotapi.TamBot(token)
def subs(channel_id, token, user_id):
  response = requests.get(f'https://botapi.tamtam.chat/chats/{channel_id}/members?access_token={token}&user_ids={user_id}').text
  return response
channel_id = -74010778708972
def main():
    chat_id = bot.get_chat_id()  
    while True:
      try:
        last_update = bot.get_updates() 
        if last_update: 
            chat_id = bot.get_chat_id(last_update) 
            user_id = bot.get_user_id(last_update) 
            username = bot.get_username(last_update)
            type = bot.get_update_type(last_update)
            admins = bot.get_chat_admins(chat_id)
            callback_id = bot.get_callback_id(last_update)
            text = bot.get_text(last_update)
            mid = bot.get_message_id(last_update)
            chatt = bot.get_chat_type(last_update)
            if "/all" in text:
                if username=="cooo" or username=="boss" or username=="sssn":
                  mess = str(text).replace('/all','')
                  if mess != "":
                    chats= bot.get_all_chats(100)["chats"]
                    numc = 0
                    for ccat in chats:
                       ch=  ccat["chat_id"]
                       if int(ch) != chat_id:
                        numc +=1
                        bot.send_message(f"{str(mess)}", int(ch))
                    bot.send_message(f"تم ارسال رسالتك للكل.. ✅ :: {str(numc)}", chat_id)
                  else:
                    chats= bot.get_all_chats(100)["chats"]
                    numac =0
                    numc = 0
                    for ccat in chats:
                       ch=  ccat["chat_id"]
                       if int(ch) != chat_id and str("-") in str(ccat):
                         numc +=1
                       elif int(ch) != chat_id and str("-") not in str(ccat):
                         numac +=1
                       
                    bot.send_message(f"عدد كروبات البوت.. ✅ :: {str(numc)}" +"\n" +f"عدد مشتركين البوت.. ✅ :: {str(numac)}", chat_id)
            elif chatt == "chat":
              if 'is_admin' not in subs(channel_id, token, user_id):
                 bot.delete_message(mid)
                 bot.send_message(text= f"""عزيزي [{bot.get_name(last_update)}](tamtam://user/{user_id}) 𓃠 ,
يجب عليك الاشتراك في القناة اولا
لتستطيع التحدث في المجموعة 
القناة : http://tt.me/nnann""", chat_id=chat_id, format= "markdown")
              

                
            else:
            	pass
				
      except:
        print(Exception)
        continue


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
