# Randomly_Generate_69420

I was scrolling Reddit and saw a project where Python generate random 5-digit numbers until 69420 is generated(`https://www.reddit.com/r/Python/comments/hvq628/randomly_generate_69420_generate_random_5digit/`).

So,i decided to do some research.

# How it works

 1. Number contains 5 digits(from 0-9,except first, it's form 1-9), every digit randomly generates using `randint` from `random` module, those digits are recording into variable(`number`).
2. That tuple converts into int-number.
3. While loop comes in, program repeating step **1** and **2**  until our number appears

# Additional instruments
After the main script works perfectly, we need to somehow analyze information.
What i decided to do:

 - Outer loop with `count` variable to count loops
 - `info` variable with list  that contains contains dictionaries with **loop**(number of script generation) and **tries**(how many guesses program done to guess the number), this list updates every time script found the number
 - `CSV` module helped me to save and structure information
 - `pandas` and `matplotlib` modules helped me to create **barchart**
 
 # Results
 - **10** Loops
 
 First generation:
 
 ![Ten_loops](/bars/Bars_10_1.png)
  
  **Average = 91949,7 tries**
  
  Second generation:
  
  ![Ten_loops](/bars/Bars_10_2.png)
  
  **Average = 74049,8 tries**
  
  Third generation:
  
  ![Ten_loops](/bars/Bars_10_3.png)
  
   **Average = 154052,6 tries**
   
   **Average of all generations = 106 684,033 tries**
   
 - **50** Loops
 
 First generation:
 
 ![Ten_loops](/bars/Bars_50_1.png)
  
  **Average = 96550,12 tries**
  
  Second generation:
  
  ![Ten_loops](/bars/Bars_50_2.png)
  
  **Average = 108650 tries**
  
  Third generation:
  
  ![Ten_loops](/bars/Bars_50_3.png)
  
   **Average = 84903,92 tries**
   
   **Average of all generations = 96 701,3467 tries**
   
  - **100** Loops
 
 First generation:
 
 ![Ten_loops](/bars/Bars_100_1.png)
  
  **Average = 84957,95 tries**
  
  Second generation:
  
  ![Ten_loops](/bars/Bars_100_2.png)
  
  **Average = 78325,72 tries**
  
  Third generation:
  
  ![Ten_loops](/bars/Bars_100_3.png)
  
   **Average = 87850,73 tries**
   
   **Average of all generations = 83711,4667 tries**
