import myfitnesspal

client = myfitnesspal.Client()

day = client.get_date(2024, 4, 12)

print(day)
print(day.totals)
print(day.keys())
