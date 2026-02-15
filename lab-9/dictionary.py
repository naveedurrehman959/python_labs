# Step 1: Initialize a dictionary with a user's profile

user_profile={ "name": "alice", "age": 25, "city": "new york"}
    print(user_profile)


 # Step 1: Access the 'name' value from the dictionary
    print ("User's Name:" user_profile["name"])

 # Update the 'age' key with a new value
 user_profile["age"] = 31

 # Verify the updated value
    print("updated age :" , user_profile)


  # remove any thing from list
  user_profile.pop("city")
  print("after removing city:", user_profile)

  # how to print one key and value from given list
  # iterate over 
  for key, value in user_profile.items():
    print(f"{key}: {value}")

# Step 2: Iterate over dictionary keys
  for key in user_profile.keys():
    print(f"Key: {key}")
