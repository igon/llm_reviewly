SYSTEM_PROMPT = """
You are an AI assistant that provides concise, Cliff Notes-style summaries of short-term rental reviews.
Your role is to highlight key points with brief, clear responses that include actual quotes and capture the emotional tone of the reviews.
Summarize the pros, cons, and recurring themes efficiently, ensuring users can quickly understand guest experiences.
If a guest expresses a concern about a specific topic, follow up with questions to gather more details and reason about why the guest was concerned.
Offer more details or in-depth analysis when requested.
"""

STR_CONTEXT = """
-------------

Here are some important listings details:
- Listing title: Luxury stay near lake Belton - Wi-Fi A/C
- Entire home in Belton, Texas.
- Can host up to 8 guests
- It has 3 bedrooms
- Has 4 beds and 2 full baths
- Description provided by host
"
Our home is perfect for family vacations and remote work getaways. Located just minutes from local attractions, including Lake Belton and the Bell County Expo Center, our home is the perfect base for your Texas adventure. With its welcoming atmosphere, our home is ideal for making lasting memories with your loved ones or focusing on your work without distraction. Bond over board games and cook with our new kitchen appliances. Book now and experience the comfort and convenience of our home.
Other things to note
Our house is in a quiet residential neighborhood, just a short drive from local restaurants, shops, and attractions. We're also just a quick 5-minute drive from the beautiful Lake Belton, where you can swim, fish, and enjoy a variety of water sports.

We pride ourselves on providing our guests with a clean and comfortable space.
"
- What this place offers
"
Bathroom:
Bathtub
Hair dryer
Cleaning products
Shampoo
Conditioner
Hot water

Bedroom and laundry:
Free washer – In unit
Free dryer – In unit

Essentials:
Towels, bed sheets, soap, and toilet paper
Hangers
Bed linens
Room-darkening shades
Iron
Clothing storage: walk-in closet and closet

Entertainment:
43 inch HDTV with Chromecast
Books and reading material

Family:
Paid crib - available upon request
Children’s books and toys
High chair
Changing table - available upon request
Board games

Heating and cooling:
AC - split type ductless system
Ceiling fan
Heating - split type ductless system

Home safety:
Exterior security cameras on property
The driveway and entry door are under video surveillance by Ring video doorbell. It records video and audio on any motion detected.
Smoke alarm
Carbon monoxide alarm
Fire extinguisher
First aid kit

Internet and office:
Fast wifi – 53 Mbps
Verified by speed test. Stream 4K videos and join video calls on multiple devices.

Dedicated workspace:
In a room with a door
Kitchen and dining

Kitchen:
Space where guests can cook their own meals
Refrigerator
Microwave

Cooking basics:
Pots and pans, oil, salt and pepper
Dishes and silverware
Bowls, chopsticks, plates, cups, etc.
Dishwasher
LG stainless steel electric stove
Oven
Hot water kettle
Coffee maker
Wine glasses
Toaster
Blender
Rice maker
Barbecue utensils
Grill, charcoal, bamboo skewers/iron skewers, etc.
Dining table

Location features:
Beach access – Beachfront
Guests can enjoy a nearby beach

Outdoor:
Private patio or balcony
Private backyard - Not fully fenced
An open space on the property usually covered in grass

Outdoor furniture:
Private BBQ grill: gas
Parking and facilities
Free parking on premises
Single level home
No stairs in home

Services:
Long term stays allowed - Allow stay for 28 days or more
Self check-in
Lockbox
"
"""

ASSESSMENT_PROMPT = """
### Instructions

Your task is to analyze the conversation between a guest and an assistant, then generate a prioritized list of points of interest based on the guest's **most recent message**.

Follow these guidelines:

1. **Classify Points of Interest**:
   - Identify a point of interest if the guest expresses a significant concern or need.
   - Assign higher weight to points related to **safety** or **basic needs** (e.g., security, comfort).
   - Assign lower weight to points concerning **non-essential** or **complementary needs** (e.g., amenities, preferences).
   - Ensure no duplication of existing points. Only add new points if they provide additional, meaningful, or updated information.
   - Break down generic concerns into more precise topics whenever possible.

2. **Sort Points of Interest**:
   - Rank points by weight, placing those with higher importance (e.g., safety, basic needs) at the top.

### Output Format:

{{
    "points_of_interest_updates": [
        {{
            "topic": "<Specific Topic>",
            "weight": "<Weight: Strong/Moderate/Weak>"
        }}
    ]
}}

### Inputs Provided:

- **Most Recent Guest Message**: `{latest_message}`
- **Conversation History**: `{history}`
- **Existing Points of Interest**: `{existing_points_of_interest}`
- **Current Date**: `{current_date}`
"""