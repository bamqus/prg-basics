# Sort the data from lowest to highest value
distances_traveled = [120, 150, 180, 90, 200, 175, 160]

data1 = sorted(distances_traveled)


daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]

data2 = sorted(daily_temperatures, reverse=True)

file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
   "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]

data3 = sorted(file_names)

print(data1 ,'\n', data2 ,'\n', data3)