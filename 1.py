import re
def simple_chatbot(user_input):
  user_input = user_input.lower()
  rules = {
      'hello': 'Hi there! How can I help you?',
      'how are you': 'I am bot and I don\'t have feelings, thanks for asking',
      'bye': 'Goodbye! Have a nice day',
      'name': 'I am a simple chatbot, you can call me as a chatbot',
      'default': 'I am not sure how to respond. Ask me something else!'
  }
  for pattern, response in rules.items():
    if re.search(pattern, user_input):
      return response
  return rules['default']
while True:
  user_input = input('you: ')
  if user_input.lower() == 'exit':
    print('Chatbot: Goodbye!')
    break
  response = simple_chatbot(user_input)
  print('Chatbot:',response)
