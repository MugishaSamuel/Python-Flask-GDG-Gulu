
w = """   An Internet search engine.
    Web email.
    A news aggregator.
    Calendar software.
    A suite of productivity applications, including spreadsheet, word-processing, and photo-editing software.
    Cloud storage for consumers
    Cloud storage for businesses.
    Cloud computing for businesses.
    A website for watching Internet videos.
    A web browser.
    A smartphone/tablet operating system.
    A thermostat. 
    Unknown life-extending technologies.
    Computerized contact lenses
    Robot assistants
    Self-driving cars
    A home video monitoring system.
    High-speed Internet service.
    Laptop computers.
    Desktop computers.
    A dongle that puts Internet video on your TV.
    Balloons that broadcast Internet signal.
    Drones that deliver goods to homes.
    Computers you wear like glasses.
    Airborne wind turbines.
    A digital collection of all the world's books.
    A map of the world.
    A collection of photographs of every street in the world.
    A social network.
    Software for creating and maintaining blogs.
    An online video rental store.
    An online software store.
    A live-updating database of equities and financial news.
    A service that allows you to pay for things with your phone.
    A language translation service.
    A phone number replacement service.
    Video-conferencing software."""

l = []

r = w.strip()
p = r.split(".")

for i in p:    
    e = i.strip()

    l.append(e)


print(l)


products = ['An Internet search engine', 'Web email', 'A news aggregator', 'Calendar software', 'A suite of productivity applications, including spreadsheet, word-processing, and photo-editing software', 'Cloud storage for consumers','Cloud storage for businesses', 'Cloud computing for businesses', 'A website for watching Internet videos', 'A web browser', 'A smartphone/tablet operating system', 'A thermostat', 'Unknown life-extending technologies', 'Computerized contact lenses','Robot assistants','Self-driving cars','A home video monitoring system', 'High-speed Internet service', 'Laptop computers', 'Desktop computers', 'A dongle that puts Internet video on your TV', 'Balloons that broadcast Internet signal', 'Drones that deliver goods to homes', 'Computers you wear like glasses', 'Airborne wind turbines', "A digital collection of all the world's books", 'A map of the world', 'A collection of photographs of every street in the world', 'A social network', 'Software for creating and maintaining blogs', 'An online video rental store', 'An online software store', 'A live-updating database of equities and financial news', 'A service that allows you to pay for things with your phone', 'A language translation service', 'A phone number replacement service', 'Video-conferencing software']
