# Builder Pattern in Python

## 🔹 What is the Builder Pattern?
The **Builder Pattern** is a **creational design pattern** that allows you to construct complex objects step by step.  
Instead of passing all parameters at once into a constructor, you build the object by setting only the fields you need.  

This makes object creation:
- **Readable** – each step clearly shows what is being set.  
- **Flexible** – you can add only what you need, skipping optional fields.  
- **Maintainable** – adding new fields does not break existing code.  

---

## 🔹 The Problem (Telescoping Constructor)
When an object has many parameters, using a constructor quickly becomes unreadable and error-prone.  

For example:
- You must remember the exact **order** of parameters.  
- Adding or removing a field requires changing the constructor everywhere.  
- Creating a simple object may still require passing many unnecessary values.  

This issue is known as the **Telescoping Constructor Problem**.  

### Example of Telescoping Constructor
url = URL("https", "example.com", 443, "search", {"q": "builder pattern", "lang": "python"}, "section1")

---

## 🔹 The Solution (Builder Pattern)
The **Builder Pattern** solves this by separating the **construction** of an object from its **representation**.  

Instead of stuffing everything into one constructor, the builder pattern lets you:
- Construct the object **step by step**.  
- Use **method chaining** (fluent style) for readability.  
- Build different **representations** of the same object.  

The final object can also be made **immutable**, since all modifications happen during the build process.  


---

## 🔹 Returning `self`

Every setter returns the builder itself (`return self`).  

This enables **method chaining** so multiple methods can be called in one fluent line.  

### Example
URLBuilder().set_scheme("https").set_host("example.com").add_param("q", "python")

---

## 🔹 Benefits of Builder Pattern
- **Improved readability** – no more confusing parameter order.  
- **Flexibility** – optional fields can be skipped easily.  
- **Easier maintenance** – adding a new field just means adding a new method.  
- **Consistency** – object creation is centralized, avoiding errors.  

---

## 🔹 Real-World Analogies
- **Burger Shop** 🍔 → choose bun, patty, sauce, toppings step by step, then get the final burger.  
- **URL Builder** 🌐 → add scheme, host, path, parameters, fragment step by step, then get the final URL.  
- **SQL Query Builder** 🗄️ → add select, from, where clauses step by step, then get the final query.  
