import datetime


CLASS_DAYS = ['Monday', 'Wednesday', 'Thursday']
DISPLAY_DAYS = CLASS_DAYS
#DISPLAY_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']


SPECIAL_DATES = [
    (datetime.datetime(2026, 1, 19), 'Martin Luther King Jr. Day: no classes'),
    (datetime.datetime(2026, 2, 16), 'President\'s Day: no classes'),
    (datetime.datetime(2026, 2, 17), 'Substitute Day: Monday Schedule'),
    (datetime.datetime(2026, 3, 16), 'Spring Break: no classes'),
    (datetime.datetime(2026, 3, 17), 'Spring Break: no classes'),
    (datetime.datetime(2026, 3, 18), 'Spring Break: no classes'),
    (datetime.datetime(2026, 3, 19), 'Spring Break: no classes'),
    (datetime.datetime(2026, 3, 20), 'Spring Break: no classes'),
    (datetime.datetime(2026, 4, 15), 'Ruhlman Conference: no classes'),
    (datetime.datetime(2026, 4, 20), 'Patriot\'s Day: no classes'),
    (datetime.datetime(2026, 4, 30), 'Substitute Day: Monday Schedule'),
    (datetime.datetime(2025, 5, 1), 'Reading Period Begins.'),
    (datetime.datetime(2025, 5, 5), 'Final Exam Period Begins.'),
]


READING_PERIOD_START = datetime.datetime(2026, 5, 1)


def is_date_special(current):
    for d, desc in SPECIAL_DATES:
        if d == current:
            return desc

    return None


def generate_yml_calendar():
    course_start = datetime.datetime(2026, 1, 19)
    course_end = datetime.datetime(2026, 5, 8)

    start = course_start - datetime.timedelta(days=course_start.weekday())
    end = course_end + datetime.timedelta(days=6 - course_end.weekday())

    print('events:')

    current = start
    while current <= end:
        day = current.strftime('%A')

        if day in DISPLAY_DAYS:        
            print('  - month: "{}"'.format(current.strftime('%B')))
            print('    day: "{}"'.format(current.strftime('%d')))
            print('    day-of-week: "{}"'.format(day))

            desc = is_date_special(current)
            if desc is not None:
                print('    special: "{}"'.format(desc))

            if day in CLASS_DAYS:
                print('    topic:')

            print('    due:')
            print('    released:')
            print('    pre-class:')

            if current >= READING_PERIOD_START:
                print('    class-meetings-over: true')
                
            print('')

        current = current + datetime.timedelta(days=1)



def main():    
    generate_yml_calendar()

    
if __name__ == '__main__':
    main()
