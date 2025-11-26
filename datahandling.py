# 1️⃣ What is Data Handling?

# Data handling means how Python stores, reads, writes, and processes data.
# In backend development, we often handle:

# Data from users (forms, APIs)

# Data from files (CSV, JSON, text)

# Data from databases

# We usually need to:

# Read data → Process it → Save or send it

# 📦 2️⃣ What is JSON?

# JSON = JavaScript Object Notation
# It’s a lightweight format to exchange data between backend (Python, PHP) and frontend (JS).

# ✅ Example JSON:

{
  "name": "Regina",
  "age": 25,
  "city": "Chennai"
}


# Looks like a Python dictionary — that’s why it’s easy to use in Python!

# 🔁 3️⃣ Python JSON Handling (Using json module)

# Python provides a built-in library called json to handle JSON data.

# Let’s see the 4 main operations 👇

# 🔹 A. Convert Python → JSON (Serialization / Encoding)
import json

data = {"name": "Regina", "age": 25, "city": "Chennai"}

json_data = json.dumps(data)   # Convert dict → JSON string
print(json_data)


# Output:

# {"name": "Regina", "age": 25, "city": "Chennai"}


# 🧠 json.dumps() = dump string
# Used when you want to send data to frontend or API.

# 🔹 B. Convert JSON → Python (Deserialization / Decoding)
import json

json_data = '{"name": "Regina", "age": 25, "city": "Chennai"}'
python_dict = json.loads(json_data)

print(python_dict)
print(python_dict["name"])


# Output:

# {'name': 'Regina', 'age': 25, 'city': 'Chennai'}
# Regina


# 🧠 json.loads() = load string
# Used when you receive JSON from an API or frontend.

# 🔹 C. Read JSON from File
import json

with open("data.json", "r") as file:
    data = json.load(file)   # Read JSON → dict
print(data)


# 🧠 json.load() reads JSON data from a file directly.

# 🔹 D. Write JSON to File
import json

data = {"project": "Turbo Trader", "version": 1.0}

with open("project.json", "w") as file:
    json.dump(data, file)   # dict → JSON file

print("JSON file created successfully!")


# 🧠 json.dump() writes a Python dictionary into a JSON file.

# 💡 4️⃣ Real Backend Example (API-style)

# Imagine you receive user data from frontend:

import json

# JSON coming from frontend (like API)
user_json = '{"name":"Regina", "email":"regina@gmail.com"}'

# Convert JSON → Python dictionary
user = json.loads(user_json)

# Process data
print("Welcome,", user["name"])
print("Email:", user["email"])

# Send response back as JSON
response = {"status": "success", "message": "User added!"}
print(json.dumps(response))

# 🧾 5️⃣ Summary
# Action	Function	Description
# dict → JSON string	json.dumps()	For API responses
# JSON string → dict	json.loads()	For received data
# dict → JSON file	json.dump()	Save to file
# JSON file → dict	json.load()	Read from file




# 2️⃣ Python JSON Module

# Python provides the json module to handle JSON:

# json.dumps() → Python object → JSON string

# json.loads() → JSON string → Python object (dict/list)
