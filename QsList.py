from craigslist import CraigslistHousing
from datetime import datetime, date, timedelta

# "apa" is craigslist's url key for "apartments / housing for rent"
sgv_rooms = CraigslistHousing(site="losangeles", area="sgv", category="roo")
# post = next(sgv_rooms.get_results())
current_date_time = datetime.now()

for post in sgv_rooms.get_results():
    # get post_date
    post_date_time = datetime.strptime(post.get("datetime"), '%Y-%m-%d %H:%M')
    
    # compare post_date with current_date
    if current_date_time-timedelta(hours=2) <= post_date_time <= current_date_time:
        print(post)