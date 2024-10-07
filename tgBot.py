import telebot
import rospy
from clover.srv import SetLEDEffect
from std_srvs.srv import Trigger
from clover import srv

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)
set_effect = rospy.ServiceProxy('led/set_effect', SetLEDEffect)

token = 'Token'
bot = telebot.TeleBot(token)

def takeoff():
    navigate(x=0, y=0, z=1, speed=0.5, frame_id='body', auto_arm=True)
    rospy.sleep(2)
    set_effect(r=255, g=255, b=0)
    rospy.sleep(2)
def base():
    
    navigate(x=0, y=0, z=1.5, speed=0.5, frame_id='body', auto_arm=True)
    rospy.sleep(5)
    set_effect(effect='flash', r=0, g=255, b=0)
    rospy.sleep(5)
    navigate(x=0, y=0, z=1.5, speed=0.5, frame_id='aruco_20')
    rospy.sleep(5)
    land()
def landoff():
    set_effect(r=0, g=255, b=0)
    rospy.sleep(2)
    set_effect(r=255, g=255, b=255)
    rospy.sleep(3)
    land()
    rospy.sleep(3)
    set_effect(effect='flash', r=255, g=255, b=0)
    rospy.sleep(3)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    
    set_effect(effect='flash', r=0, g=255, b=0)  # flash twice with red color
    rospy.sleep(5)
    a = message.text.split(';')
    #c = a[3].split('.')
    #v = c[0]*a[2]
    

    if a[0] == "Университетская, 10":       
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_14")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_14')
        rospy.sleep(7)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")       
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")
        # bot.send_message(message.from_user.id, "общая стоимость :" + v)
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")

    if a[0] == "Ангарская, 89":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_21")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_21')
        
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")       
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб") 
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")
        
    if a[0] == "Летняя, 14":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_22")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_22')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")        
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")
        
    if a[0] == "Каменная, 10":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_23")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_23')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")  
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")      
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")
        
    if a[0] == "Аэродромная, 1":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_16")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_16')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")      
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")  
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")
        
    if a[0] == "Аэродромная, 21":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_17")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_17')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")     
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")   
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")
        
    if a[0] == "Зимняя, 97":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_18")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_18')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")    
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")    
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")

    if a[0] == "Каменная, 12":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_19")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_19')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + " ед") 
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")       
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")

    if a[0] == "Школьная, 9":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_12")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_12')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")   
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")     
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")

    if a[0] == "Заречная, 35":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_13")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_13')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")       
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб") 
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")

    if a[0] == "БОЛЬНИЦА":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_15")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_15')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")   
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")     
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")

    if a[0] == "Бумажная, 114":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_8")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_8')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")  
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")      
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")

    if a[0] == "Заречная, 37":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_9")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_9')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")  
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")      
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")

    if a[0] == "Научная, 15":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_10")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_10')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")       
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб") 
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")

    if a[0] == "Научная, 14":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_11")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_11')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")  
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")      
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")
    
    if a[0] == "Кирова, 2":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_4")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_4')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")    
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")    
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")
    
    if a[0] == "ПОДВИЖНАЯ ПЛАТФОРМА":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_5")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_5')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")  
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")      
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")

    if a[0] == "Кирова, 6":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_6")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_6')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")  
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")      
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")

    if a[0] == "Кирова, 8":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_7")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_7')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")  
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")      
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")

    if a[0] == "Кирова, 1":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_0")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_0')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")  
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")      
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")

    if a[0] == "Кирова, 3":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_1")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_1')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")   
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")     
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")

    if a[0] == "Кирова, 5":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_2")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_2')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед") 
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")       
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")

    if a[0] == "Кирова, 7":
        bot.send_message(message.from_user.id, "Заказ принят в обработку")
        set_effect(r=0, g=255, b=0)
        takeoff()
        bot.send_message(message.from_user.id, "Заказ отправлен")
        print("aruco_3")
        set_effect(r=255, g=255, b=255)
        rospy.sleep(0.2)
        navigate(x=0, y=0, z=1, speed=0.5, frame_id='aruco_3')
        rospy.sleep(5)
        landoff()
        bot.send_message(message.from_user.id, "Заказ доставлен")
        bot.send_message(message.from_user.id, "=====чек===== \n ОПЛАЧЕНО, ДОСТАВЛЕНО \n Наименование товара:" + a[1] + a[2] + "ед")  
        bot.send_message(message.from_user.id, "Стоимость за штуку :" + a[3]  + " руб")      
        base()
        bot.send_message(message.from_user.id, "Дрон вернулся")

   

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Дрон вернулся")
    else:
        bot.send_message(message.from_user.id, "ОШИБКА")

bot.polling(none_stop=True, interval=0)