import movie
import netclipz


# Instantiate movie objects to be displayed on the web page.

black_panther = movie.Movie("Black Panther",
                            "After the death of his father, T'Challa returns"
                            " home to the African nation of Wakanda to take"
                            " his rightful place as king. When a powerful enemy"
                            " suddenly reappears, T'Challa's mettle as king --"
                            " and as Black Panther -- gets tested when he's"
                            " drawn into a conflict that puts the fate of"
                            " Wakanda and the entire world at risk. Faced with"
                            " treachery and danger, the young king must rally"
                            " his allies and release the full power of Black"
                            " Panther to defeat his foes and secure the safety"
                            " of his people.",
                            "images/black_panther.jpeg",
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU")

infinity_war = movie.Movie("Avengers: Infinity War",
                           "Iron Man, Thor, the Hulk and the rest of the"
                           " Avengers unite to battle their most powerful"
                           " enemy yet -- the evil Thanos. On a mission to"
                           " collect all six Infinity Stones, Thanos plans to"
                           " use the artifacts to inflict his twisted will on"
                           " reality. The fate of the planet and existence"
                           " itself has never been more uncertain as"
                           " everything the Avengers have fought for has led"
                           " up to this moment.",
                           "images/avengers.jpeg",
                           "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

deadpool2 = movie.Movie("Deadpool 2",
                        "Wisecracking mercenary Deadpool joins forces with"
                        " three mutants -- Bedlam, Shatterstar and Domino --"
                        " to protect a boy from the all-powerful Cable.",
                        "images/deadpool2.jpeg",
                        "https://www.youtube.com/watch?time_continue=1&v=20bpjtCbCz0")

solo = movie.Movie("Solo: A Star Wars Story",
                   "Through a series of daring escapades, young Han Solo"
                   " meets his future co-pilot Chewbacca and encounters the"
                   " notorious gambler Lando Calrissian.",
                   "images/solo.jpg",
                   "https://www.youtube.com/watch?v=jPEYpryMp2s")

antman2 = movie.Movie("Ant-Man and The Wasp",
                      "Scott Lang is grappling with the consequences of his"
                      " choices as both a superhero and a father. Approached"
                      " by Hope van Dyne and Dr. Hank Pym, Lang must once"
                      " again don the Ant-Man suit and fight alongside the"
                      " Wasp. The urgent mission soon leads to secret"
                      " revelations from the past as the dynamic duo finds"
                      " itself in an epic battle against a powerful new enemy.",
                      "images/antman2.jpeg",
                      "https://www.youtube.com/watch?v=UUkn-enk2RU")

venom = movie.Movie("Venom",
                    "One of Marvel's most enigmatic, complex and badass"
                    " characters comes to the big screen, starring Academy"
                    " Award nominated actor Tom Hardy as the lethal protector"
                    " Venom.",
                    "images/venom.jpg",
                    "https://www.youtube.com/watch?v=u9Mv98Gr5pY")


# Add all movie instances to a list of all movies
all_movies = [black_panther, infinity_war, deadpool2, solo, antman2, venom]


# Display all of the movies on a web page.
netclipz.open_movies_page(all_movies)
