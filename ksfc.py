from pynput import keyboard
key_frequencies = {}
frequency_limit = 5
print("Enter the Key Strokes to count their Frequency")   
def on_press(key):
     try:
         key_str = key.char
     except AttributeError:
         key_str = str(key)
     key_frequencies[key_str] = key_frequencies.get(key_str, 0) + 1
     if key_frequencies[key_str] >= frequency_limit:
         print(f"Key '{key_str}' exceeds the frequency limit of {frequency_limit}!, Counting Stopped.")
         return
     print("Key Frequencies: ",key_frequencies)
     
with keyboard.Listener(on_press=on_press)as listener:
    listener.join()                 
