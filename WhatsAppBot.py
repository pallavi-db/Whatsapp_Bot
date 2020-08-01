from selenium import webdriver
import time
web_Driver=webdriver.Chrome(executable_path=r'C:\Users\palla\Desktop\chromedriver')
web_Driver.get(r'https://web.whatsapp.com/')

print("Please scan the QR code.")
print("Do you wish to send text message or Image/Video?")
print("Type 'text' to send text messages or type 'iv' to send picture: ")
data = input()

if data == 'text':
    contact = input("Enter the name of the person or group you want to send message: ")
    message = input("Enter the message you want to send: ")
    time.sleep(3)

    new_chat = web_Driver.find_element_by_xpath('//div[@title = "New chat"]')
    new_chat.click()
    time.sleep(2)

    search_contact = web_Driver.find_element_by_xpath('//div[@class = "_3FRCZ copyable-text selectable-text"]')
    search_contact.send_keys(contact)
    time.sleep(2)


    contact_name = web_Driver.find_element_by_xpath('//span[@title = "{}"]'.format(contact))
    contact_name.click()
    time.sleep(2)

    type_message = web_Driver.find_element_by_class_name("_3uMse")
    type_message.send_keys(message)
    time.sleep(1)

    button_send = web_Driver.find_element_by_class_name("_1U1xa")
    button_send.click()

elif data == 'iv':
    contact = input("Enter the name of the person or group you want to send image: ")
    file = input("Enter the filepath of image or video: ")
    time.sleep(3)

    new_chat = web_Driver.find_element_by_xpath('//div[@title = "New chat"]')
    new_chat.click()
    time.sleep(2)

    search_contact = web_Driver.find_element_by_xpath('//div[@class = "_3FRCZ copyable-text selectable-text"]')
    search_contact.send_keys(contact)
    time.sleep(2)

    contact_name = web_Driver.find_element_by_xpath('//span[@title = "{}"]'.format(contact))
    contact_name.click()
    time.sleep(2)

    data_attach = web_Driver.find_element_by_xpath('//div[@title="Attach"]')
    data_attach.click()

    data_box = web_Driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    data_box.send_keys(file)
    time.sleep(2)

    send_arrow = web_Driver.find_element_by_xpath('//div[@class="_3y5oW _3qMYG"]')
    send_arrow.click()
