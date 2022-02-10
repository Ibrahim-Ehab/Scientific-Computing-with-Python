
def get_days_later(days):
  """ Helper function to format days later"""
  if days == 1:
      return "(next day)"
  elif days > 1:
      return f"({days} days later)"
  return ""


def add_time(start, duration, day=False):
    week_days =  [
        'monday', 'tuesday',
        'wednesday', 'thursday',
        'friday', 'saturday',
        'sunday'
      ]

    days_later = 0
    one_day = 24
    half_day = 12
    start_hour, start_minutes = start.split(":")
    start_minutes, period = start_minutes.split(" ")
    duration_hours, duration_minutes = duration.split(":")

    #CLEAN DATA
    start_hour = int(start_hour)  
    start_minutes = int(start_minutes)  
    duration_hours = int(duration_hours)  
    duration_minutes = int(duration_minutes)  
    period = period.strip().lower()  # AM or PM"

    total_minuts = start_minutes + duration_minutes
    total_hours = start_hour + duration_hours

    if total_minuts >= 60:
        total_hours += int(total_minuts / 60)
        total_minuts = int(total_minuts % 60)

    if duration_hours or duration_minutes:  
        if period == "pm" and total_hours > half_day:
            if total_hours % one_day >= 1.0:
                days_later += 1  

        if total_hours >= half_day:
            hours_left = total_hours / one_day
            days_later += int(hours_left)
            
        tth = total_hours
        while True:
            # constantly reverse period untils
            # total_hours are less than half a day
            if tth < half_day:
                break
            if tth >= half_day:
                if period == "am":
                    period = "pm"
                elif period == "pm":
                    period = "am"
                tth -= half_day

   
    remaining_hours = int(total_hours % half_day) or start_hour + 1
    remaining_mins = int(total_minuts % 60)

    results = f'{remaining_hours}:{remaining_mins:02} {period.upper()}'
    if day: 
        day = day.strip().lower()
        selected_day = int((week_days.index(day) + days_later) % 7)
        current_day = week_days[selected_day]
        results += f', {current_day.title()} {get_days_later(days_later)}'

    else: # add days later
        results = " ".join((results, get_days_later(days_later)))

    return results.strip()