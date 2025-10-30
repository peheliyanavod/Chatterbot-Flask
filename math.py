from chatterbot import ChatBot

mathbot = ChatBot("Math", logic_adapters=["chatterbot.logic.MathematicalEvaluation"])

print("------------ Math ChatBot ------------")

while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        break

    response = mathbot.get_response(user_input)
    print("MathBot:", response)
