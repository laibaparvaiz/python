hour = int(input("Enter starting hour (0-23): "))
minute = int(input("Enter starting minutes (0-59): "))
duration = int(input("Enter duration in minutes: "))

end_minute = minute + duration
end_hour = hour + (end_minute // 60)
end_minute = end_minute % 60
end_hour = end_hour % 24  

print(f"The show will end at {end_hour:02d}:{end_minute:02d}")
