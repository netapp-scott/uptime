# ctypes required for using GetTickCount64()
import ctypes
 
# getting the library in which GetTickCount64() resides
lib = ctypes.windll.kernel32
 
# calling the function and storing the return value
t = lib.GetTickCount64()
 
# since the time is in milliseconds i.e. 1000 * seconds
# therefore truncating the value
t = int(str(t)[:-3])
 
# extracting hours, minutes, seconds & days from t
# variable (which stores total time in seconds)
mins, sec = divmod(t, 60)
hour, mins = divmod(mins, 60)
days, hour = divmod(hour, 24)
 
# formatting the time in readable form
# (format = x days, HH:MM:SS)

print("\n")
print(f"  System Uptime: {days} days, {hour:02}:{mins:02}:{sec:02}")
print("\n")
input("  Press Enter to continue...")