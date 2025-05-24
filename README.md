# Decode With Showrin Rahman



# 📚 Python Tutorials Code Repository  

Welcome to the **official repository** for the  tutorials from [Showrin Rahman](https://www.youtube.com/@showrin20).
## 📺 **YouTube Channel**  
Check out the tutorials on the YouTube channel: [Showrin Rahman](https://www.youtube.com/@showrin20). Subscribe for regular Python programming tips, tutorials and projects!  

🔥 **Decode with Shpwrin: Days of Soja Banglai** 🔥

Hey Showrin! Love your initiative to make Python, Machine Learning (ML), and Deep Learning (DL) accessible to beginners in Bangla. Here's a comprehensive script for your Facebook Shorts series, tailored for non-IT folks and starters. Each script is designed to be engaging, informative, and under 60 seconds.



## 🐍 Week 1–7: **Soja Banglai Python**


## 🎬 ভিডিও শিরোনাম: Soja Banglai Python – শুরু করি প্রোগ্রামিং একদম শুরু থেকে

### 🕒 0:00 – 0:30 | Intro

> "**আসসালামু আলাইকুম!** সবাইকে স্বাগতম আজকের ভিডিওতে – যেখানে আমরা শিখবো ‘Soja Banglai Python’। তুমি যদি একদম নতুন হও, কোডিং বুঝো না – চিন্তা কোরো না! আমরা একদম সহজ ভাষায় দেখবো কীভাবে Python দিয়ে প্রোগ্রাম লেখা যায়। তো চলো, দেরি না করে শুরু করি!"

---

### 🕒 0:30 – 2:00 | Variables & Data Types
 "Programming মানে কম্পিউটারকে কাজ শেখানো। যেমন তুমি বলো – পানি খাও, কম্পিউটারকে বলবে – `print('pani khao')`

 
> "Python-এ কোনো জিনিসকে মনে রাখার জন্য আমরা ব্যবহার করি ‘variable’। Variable মানে হচ্ছে একটা নাম দেয়া বক্স, যেটাতে কিছু রাখা যায়।"

```python
name = "Showrin"
age = 12
height = 5.4
isGraduated = False
```

> "**name** হচ্ছে string, **age** হচ্ছে number, **height** হচ্ছে decimal বা float, আর **isGraduated** হচ্ছে True/False – মানে boolean।"

```python
print(type(name))
print(type(age))
print(type(height))
print(type(isGraduated))
```

> "এইভাবে আমরা বুঝি কোনটা কেমন ধরনের ডেটা – যেটাকে বলে Data Type."

---

### 🕒 2:00 – 3:30 | Input-Output

> "চল এবার দেখি কীভাবে ইউজার থেকে ইনপুট নেয়া যায়।"

```python
user_name = input("তোমার নাম লিখো: ")
print("হ্যালো", user_name)
```

---

### 🕒 3:30 – 6:00 | Control Structures (if-else + loop)

> "**Control Structure** মানে হচ্ছে প্রোগ্রামের ভিতরে কীভাবে কাজ হবে – সেটা নিয়ন্ত্রণ করা।"

```python
temp = float(input("তাপমাত্রা দাও: "))
if temp < 0:
    print("একদম ঠাণ্ডা")
elif temp <= 10:
    print("ঠাণ্ডা")
elif temp < 18:
    print("গরম")
else:
    print("খুব গরম")
```

> "আর এখন আমরা শিখবো loop – মানে একই কাজ বারবার করানো।"

```python
for i in range(5):
    print("Python শিখছি")
```

---

### 🕒 6:00 – 8:30 | List + List Methods

> "List মানে একসাথে অনেক ডেটা রাখা যায় এমন একটা জিনিস। যেমন –"

```python
attendance = ["Arup", "Tayeeb", "Shoily"]
print(attendance)
attendance.append("Doha")
attendance.remove("Tayeeb")
print(attendance)
```

> "আরো কিছু গুরুত্বপূর্ণ মেথড দেখো:"

```python
attendance.insert(1, "Rahim")
attendance.pop()
print(attendance)
```

> "চলো দেখি কিভাবে লিস্টে ঘুরে ঘুরে দেখা যায়:"

```python
for student in attendance:
    print(student)
```

---

### 🕒 8:30 – 9:30 | Tuple

> "Tuple হচ্ছে লিস্টের মতই, কিন্তু একবার বানানোর পর বদলানো যায় না।"

```python
student_info = ("Showrin", 12, 5.4)
print(student_info[0])
print(len(student_info))
```

> "Tuple হচ্ছে 'fixed' – যেমন জাতীয় পরিচয়পত্র (NID)."

---

### 🕒 9:30 – 11:00 | Set

> "Set মানে এমন একটা list – যেটাতে একই item বারবার রাখা যায় না। আর এর কোন order নেই।"

```python
numbers = {1, 2, 3, 2, 1}
print(numbers)
numbers.add(4)
numbers.remove(2)
print(numbers)
```

---

### 🕒 11:00 – 13:30 | Function

> "Function মানে হচ্ছে বারবার ব্যবহার করার জন্য কিছু কোডের প্যাকেট।"

```python
def welcome(name):
    print("স্বাগতম", name)

welcome("Showrin")
```

> "আরো একটা function – যেটা বলে কোন সংখ্যা জোড় না বিজোড়:"

```python
def odd_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

odd_even(7)
odd_even(10)
```

---

### 🕒 13:30 – 15:30 | String Methods

> "String মানে লেখা – যেমন নাম।"

```python
name = "sHowRIN"
print(name.lower())
print(name.upper())
print("R" in name)
print(name.count("H"))
print(name.replace("R", "r"))
```

> "আরো কিছু powerful জিনিস:"

```python
sentence = "Python is fun"
print(sentence.startswith("Python"))
print(sentence.endswith("fun"))
print(sentence.split(" "))
```

---

### 🕒 15:30 – 17:30 | Practice Task

> "**চল একটা ছোট প্র্যাকটিস করি –** ইউজার নাম নিবো, বয়স নিবো, আর বলবো সে ভোট দিতে পারে কিনা।"

```python
name = input("নাম লেখো: ")
age = int(input("তোমার বয়স কতো? "))

if age >= 18:
    print(name, "ভোট দিতে পারবে")
else:
    print(name, "ভোট দিতে পারবে না")
```

---

### 🕒 17:30 – 20:00 | Recap + Next Steps

> "**আজ আমরা শিখলাম –**"

* Variable
* Data Types
* Input/Output
* if-else & loop
* List, Tuple, Set
* Functions
* String Methods


---

## 📈 Week 8–13: **Soja Banglai ML**

**Day 8: ML মানে কী? কী শিখে machine?**

🎥 **Script:**

> "তোমার মা যদি বলে – ৩ দিন পায়েস খাইলা, তুমি বুঝবা ঈদ আসতেছে। এটাও একধরনের learning!"

**Day 9: Data মানে fuel, না থাকলে ML বন্ধ**

🎥 **Script:**

> "ডেটা মানে fact। যেমন – বৃষ্টি হলে কাদা হয়। Machine ঐ ডেটার pattern শিখে।"

**Day 10: Supervised vs Unsupervised – ক্লাস আছে নাকি নাই?**

🎥 **Script:**

> "Supervised মানে শিক্ষক আছেন (লেবেলড ডেটা)। Unsupervised মানে machine নিজেই group বানায়।"

**Day 11: Train করা মানে কী? খাইয়ে দিচ্ছি data?**

🎥 **Script:**

> "Train করা মানে machine কে data দিয়ে pattern শিখানো। ঠিক যেমন পড়ার পর exam দাও।"

**Day 12: Predict মানে আন্দাজ, কিন্তু বুদ্ধি দিয়ে**

🎥 **Script:**

> "আজকে এই weather data দিয়ে machine বলে দিবে – বৃষ্টি হবে নাকি না!"

**Day 13: Linear Regression মানে সোজা equation**

🎥 **Script:**

> "Math লাগবে না। শুধু মনে রাখো – price বেশি হলে size ও বাড়ে, এই relation বুঝায় linear regression."

---

## 🧠 Week 14–19: **Soja Banglai DL**

**Day 14: Deep Learning মানে brain mimic করা**

🎥 **Script:**

> "তোমার মাথায় neuron কাজ করে, computer-এর মাথায়ও neuron আছে – artificial neuron!"

**Day 15: Neural Network মানে node এর জাল**

🎥 **Script:**

> "একটা node মানে mini decision maker। অনেকগুলো মিলায় একটা বড় decision!"

**Day 16: Activation Function মানে switch on/off**

🎥 **Script:**

> "এই function decide করে – signal pass হবে নাকি না। ঠিক যেমন switch on করলেই বাত্তি জ্বলে।"

**Day 17: Image চিনে কিভাবে? CNN**

🎥 **Script:**

> "Cat চিনতে machine প্রথমে দেখে ear, তারপর eyes, তারপর shape। এটাকেই বলে Convolutional Neural Network."

**Day 18: Voice চিনে কিভাবে? RNN**

🎥 **Script:**

> "তুমি বলো – আমি ভালো আছি। RNN বুঝে – আগের শব্দের সাথে মিলায়, pattern ধরে।"

**Day 19: Final Showdown – DL নিয়ে কী শিখলা?**

🎥 **Script:**

> "Challenge: একটা হাতের লেখা image দেখে digit predict করো! দেখাই দিব কিভাবে কাজ করে।"

---
