# Reflections

1. Share one aspect of building this project you found challenging and how you
   overcame it.

The most challenging aspect of building this project is practicing separation of concerns. At first my code was not that modular, because I was constantly changing existing functions in order to make them work with new features. For example, I had to separate the function that was asking for an input and modifying the data at the same time in order to be able to reuse the modifying part of the function.
I overcame this challenge by making a new habit of separating a feature into 2 functions: Taking an input, and using that input to modify the data. This is useful because if I want to use that new feature without user input, I can skip the middle man and modify the data directly.


2. Share one technical concept that you gained a deeper understanding of
   through building this project. Explain that concept in simple terms and
   explain how it is used in your project.

A technical concept that I gained a deeper understanding through building this project is dictionaries. In my project my main data was stored in a list of dictionaries, which stores data as key-value pairs, making it possible to look up data by key. The most useful tool that I learned about dictionaries is the `.update()` method which allows me to merge 2 dictionaries without deleting the entire dictionary. For example if I had a dictionary `person_info={'name':"Jason", 'age':20, 'job':None}` and the user wanted to update their age and job with this dictionary: `new_info={'age':21, 'job':'Firefighter'}`, instead of writing a line of code that reassigns each key one by one, I can use the `.update()` method. My project uses this method to create a way to update/edit old recipe's, it creates a new dictionary asking the user for the changes they want to make, and then updates the main recipe with the `.update()` method.

```python
person_info={'name':"Jason", 'age':20, 'job':None}
new_info={'age':21, 'job':'Firefighter'}
person_info.update(new_info)
print(person_info)
# output: {'name':"Jason", 'age':21, 'job':'Firefighter'} 
```