from chatterbot import ChatBot

chatbot = ChatBot("units", logic_adapters=["chatterbot.logic.UnitConversion"])


while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    response = chatbot.get_response(user_input)

    print("Units Converter Bot: ", response)