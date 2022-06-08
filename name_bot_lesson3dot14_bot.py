
        
def start_prog (user_id,namebot,message_in,status,message_id,name_file_picture,telefon_nome):
    import iz_func
    import iz_telegram 
    
    if message_in.find ('/start') != -1:
        status = ''
        iz_telegram.save_variable (user_id,namebot,"status",'')  
        reting = iz_func.load_variable(user_id,'Рейтинг продукта',namebot)
        if reting == '':
            reting = 1  
            
        list_lesson = iz_func.get_lesson(user_id,namebot,reting)
            
        print ('[+] list_lesson:',list_lesson)    
        message_out,menu = iz_telegram.get_message (user_id,'Список уроков',namebot)
        
        #list = []
        
        #for line in list_lesson:
        #    list.append([line,line])
        
        markup = iz_telegram.simple_menu_main (user_id,namebot,list_lesson,1) 
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)
        
        
    if message_in.find ('add_') != -1:
        message_out,menu = iz_telegram.get_message (user_id,'Урок номер 1',namebot)
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)
   