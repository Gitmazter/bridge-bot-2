list_of_uuids = [
  "a37292ee-6748-11ee-8c99-0242ac120002",
  "aad85744-6748-11ee-8c99-0242ac120002",
  "ae5c82aa-6748-11ee-8c99-0242ac120002",
  "b200cb3c-6748-11ee-8c99-0242ac120002",
  "b48ffb8e-6748-11ee-8c99-0242ac120002",
]

def sample_responses(input_text: str) -> str:
  user_message = str(input_text).lower()

  if user_message in ['hello', 'hello ser', 'hi', 'sup', 'hey']:
    return "Hey! How's it going?"
  
  if user_message in ['bye', 'goodbye', 'good bye', 'see ya']:
    return "Goodbye... friend."
  
  if user_message in ['ok', 'sure', 'yeah', 'yup']:
    return "We are in agreement"
  
  if 'find' in user_message:
    new_message: str = user_message.replace('find', '').strip()
    return new_message
  
  if 'address' in user_message:
    new_message: str = user_message.replace('find', '').strip()
    return list_of_uuids
  
  return "whaaaaat?"