import fresh_tomatoes
import media


# Here are some of my favourite movies
interstellar = media.Movie(
    "Interstellar",
    "8.6",
    "In Earth's future, a global crop blight and second "
    "Dust Bowl are slowly rendering the planet "
    "uninhabitable. Professor Brand (Michael Caine), "
    "a brilliant NASA physicist, is working on plans to "
    "save mankind by transporting Earth's population to a "
    "new home via a wormhole. But first, Brand must send "
    "former NASA pilot Cooper (Matthew McConaughey) and a "
    "team of researchers through the wormhole and across "
    "the galaxy to find out which of three planets could "
    "be mankind's new home.",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",  # NOQA
    "https://youtu.be/0vxOhd4qlnA",
    "2014",
    "2h 48m")

inception = media.Movie(
    "Inception",
    "8.8",
    "Dom Cobb (Leonardo DiCaprio) is a thief with the "
    "rare ability to enter people's dreams and steal "
    "their secrets from their subconscious. His skill "
    "has made him a hot commodity in the world of "
    "corporate espionage but has also cost him everything "
    "he loves. Cobb gets a chance at redemption when he "
    "is offered a seemingly impossible task: Plant an idea "
    "in someone's mind. If he succeeds, it will be the "
    "perfect crime, but a dangerous enemy anticipates "
    "Cobb's every move.",
    "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",  # NOQA
    "https://youtu.be/YoHD9XEInc0",
    "2010",
    "2h 48m")

fight_club = media.Movie(
    "Fight Club",
    "8.8",
    "A depressed man (Edward Norton) suffering from "
    "insomnia meets a strange soap salesman named Tyler "
    "Durden (Brad Pitt) and soon finds himself living in "
    "his squalid house after his perfect apartment is "
    "destroyed. The two bored men form an underground club "
    "with strict rules and fight other men who are fed "
    "up with their mundane lives. Their perfect "
    "partnership frays when Marla (Helena Bonham Carter), "
    "a fellow support group crasher, attracts Tyler's "
    "attention.",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
    "https://youtu.be/SUXWAEX2jlg",
    "1999",
    "2h 31m")

spirited_away = media.Movie(
    "Spirited Away",
    "8.6",
    "In this animated feature by noted Japanese director "
    "Hayao Miyazaki, 10-year-old Chihiro (Rumi Hiiragi) "
    "and her parents (Takashi Naito, Yasuko Sawaguchi) "
    "stumble upon a seemingly abandoned amusement park. "
    "After her mother and father are turned into giant "
    "pigs, Chihiro meets the mysterious Haku (Miyu Irino), "
    "who explains that the park is a resort for "
    "supernatural beings who need a break from their "
    "time spent in the earthly realm, and that she must "
    "work there to free herself and her parents.",
    "https://upload.wikimedia.org/wikipedia/en/d/db/Spirited_Away_Japanese_poster.png",
    "https://youtu.be/ByXuk9QqQkk",
    "2001",
    "2h 20m")

three_idiots = media.Movie(
    "3 Idiots",
    "8.4",
    "Two friends looking for a lost buddy deal with "
    "a forgotten bet, a wedding they are forced to crash "
    "and an out of control funeral.",
    "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
    "https://youtu.be/xvszmNXdM4w",
    "2009",
    "2h 51m")

shutter_island = media.Movie(
    "Shutter Island",
    "8.1",
    "The implausible escape of a brilliant murderess "
    "brings U.S. Marshal Teddy Daniels (Leonardo DiCaprio) "
    "and his new partner (Mark Ruffalo) to Ashecliffe "
    "Hospital, a fortress-like insane asylum located on "
    "a remote, windswept island. The woman appears to have "
    "vanished from a locked room, and there are hints of "
    "terrible deeds committed within the hospital walls. "
    "As the investigation deepens, Teddy realizes he will "
    "have to confront his own dark fears if he hopes to "
    "make it off the island alive.",
    "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
    "https://youtu.be/5iaYLCiq5RM",
    "2010",
    "2h 18m")

# here are some tv shows I like
friends = media.TvShow(
    "Friends",
    "8.9",
    "Three young men and three young women - of the BFF "
    "kind - live in the same apartment complex and face "
    "life and love in New York. They're not above "
    "sticking their noses into one another's businesses "
    "and swapping romantic partners, which always leads "
    "to the kind of hilarity average people will never "
    "experience - especially during breakups.",
    "http://www.gstatic.com/tv/thumb/tvbanners/183931/p183931_b_v8_ac.jpg",
    "https://youtu.be/Yp0kth7-zsM",
    "10",
    "NBC")

friends.tv_episodes = [
    "The One After Joey and Rachel Kiss",
    "The One Where Ross is Fine",
    "The One with Ross's Tan",
    "The One with the Cake",
    "The One Where Rachel's Sister Babysits",
    "The One with Ross's Grant",
    "The One with the Home Study",
    "The One with the Late Thanksgiving",
    "The One with the Birth Mother",
    "The One Where Chandler Gets Caught",
    "The One Where the Stripper Cries",
    "The One with Phoebe's Wedding",
    "The One Where Joey Speaks French",
    "The One with Princess Consuela",
    "The One Where Estelle Dies",
    "The One with Rachel's Going Away Party",
    "The Last One"]

game_of_thrones = media.TvShow(
    "Game of Thrones",
    "9.5",
    "George R.R. Martin's best-selling book series \"A "
    "Song of Ice and Fire\" is brought to the screen as "
    "HBO sinks its considerable storytelling teeth into "
    "the medieval fantasy epic. It's the depiction of "
    "two powerful families -- kings and queens, knights "
    "and renegades, liars and honest men -- playing a "
    "deadly game for control of the Seven Kingdoms of "
    "Westeros, and to sit atop the Iron Throne.",
    "https://upload.wikimedia.org/wikipedia/en/9/92/Game_of_Thrones_Season_7.png",  # NOQA
    "https://youtu.be/-5xdTlgaaaw",
    "7",
    "HBO")

game_of_thrones.tv_episodes = [
    "Dragonstone", "Stormborn", "Queen of Justice",
    "The Spoils of War", "Eastwatch",
    "Beyond the Wall", "The Dragon and the Wolf"]

the_big_bang = media.TvShow(
    "The Big Bang Theory",
    "8.3",
    "Mensa-fied best friends and roommates Leonard and "
    "Sheldon, physicists who work at the California "
    "Institute of Technology, may be able to tell "
    "everybody more than they want to know about quantum "
    "physics, but getting through most basic social "
    "situations, especially ones involving women, totally "
    "baffles them. How lucky, then, that babe-alicious "
    "waitress/aspiring actress Penny moves in next door. "
    "Frequently seen hanging out with Leonard and Sheldon "
    "are friends and fellow Caltech scientists "
    "Wolowitz and Koothrappali. Will worlds collide? "
    "Does Einstein theorize in the woods?",
    "http://www.gstatic.com/tv/thumb/tvbanners/12912842/p12912842_b_v8_aa.jpg",  # NOQA
    "https://youtu.be/PAm8PV47jMM",
    "1",
    "CBS")

the_big_bang.tv_episodes = [
    "Pilot", "The Big Bran Hypothesis",
    "The Fuzzy Boots Corollary",
    "The Luminous Fish Effect",
    "The Hamburger Postulate",
    "The Middle-Earth Paradigm",
    "The Dumpling Paradox",
    "The Grasshopper Experiment",
    "The Cooper-Hofstadter Polarization",
    "The Loobenfeld Decay",
    "The Pancake Batter Anomaly",
    "The Jerusalem Duality",
    "The Bat Jar Conjecture",
    "The Nerdvana Annihilation",
    "The Shiksa Indeterminacy",
    "The Peanut Reaction",
    "The Tangerine Factor"]

videos = [
    interstellar, inception, fight_club, spirited_away, shutter_island,
    game_of_thrones, the_big_bang, friends, three_idiots]

fresh_tomatoes.open_videos_page(videos)
