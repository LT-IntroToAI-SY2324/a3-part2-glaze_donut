games_db: List[Tuple[str, str, str, int, List[str]]] = [
    (
        "4-2",  # final score
        "Uruguay",  # winning team
        "Argentina",  # losing team
        1930,  # year
        [
            "Nasazzi",  # winning team captain
            "Manuel Ferreira"  # losing team captain
        ]  # captains, winning team first
    ),
    (
        "2-1",
        "Italy",
        "Czechoslovakia",
        1934,
        [
            "Combi",
            "Planicka"
        ]
    ),
    (
        "4-2",
        "Italy",
        "Hungary",
        1938,
        [
            "Ferrari",
            "Szalay"
        ]
    ),
    (
        "4-2",
        "Uruguay",
        "Brazil",
        1950,
        [
            "Nasazzi",
            "Augusto"
        ]
    ),
    (
        "3-2",
        "West Germany",
        "Hungary",
        1954,
        [
            "Fritz Walter",
            "Bozsik"
        ]
    ),
    (
        "5-2",
        "Brazil",
        "Sweden",
        1958,
        [
            "Bellini",
            "Nils Liedholm"
        ]
    ),
    (
        "3-2",
        "Brazil",
        "Czechoslovakia",
        1962,
        [
            "Mauro Ramos",
            "Karol Dobias"
        ]
    ),
    (
        "4-2",
        "England",
        "West Germany",
        1966,
        [
            "Bobby Moore",
            "Uwe Seeler"
        ]
    ),
    (
        "4-1",
        "Brazil",
        "Italy",
        1970,
        [
            "Carlos Alberto",
            "Giacinto Facchetti"
        ]
    ),
    (
        "2-1",
        "West Germany",
        "Netherlands",
        1974,
        [
            "Franz Beckenbauer",
            "Wim Suurbier"
        ]
    ),
    (
        "3-1",
        "Argentina",
        "Netherlands",
        1978,
        [
            "Daniel Passarella",
            "Ruud Krol"
        ]
    ),
    (
        "3-2",
        "Italy",
        "West Germany",
        1982,
        [
            "Dino Zoff",
            "Karl-Heinz Rummenigge"
        ]
    ),
    (
        "3-0",
        "Argentina",
        "West Germany",
        1986,
        [
            "Diego Maradona",
            "Karl-Heinz Rummenigge"
        ]
    ),
    (
        "0-0 (a.e.t., 3-2 pens)",
        "West Germany",
        "Argentina",
        1990,
        [
            "Lothar Matthäus",
            "Diego Maradona"
        ]
    ),
    (
        "3-0",
        "Brazil",
        "Italy",
        1994,
        [
            "Dunga",
            "Paolo Maldini"
        ]
    ),
    (
        "3-0",
        "France",
        "Brazil",
        1998,
        [
            "Didier Deschamps",
            "Cafu"
        ]
    ),
    (
        "2-0",
        "Brazil",
        "Germany",
        2002,
        [
            "Cafu",
            "Oliver Kahn"
        ]
    ),
    (
        "1-1 (a.e.t., 5-3 pens)",
        "Italy",
        "France",
        2006,
        [
            "Fabio Cannavaro",
            "Lilian Thuram"
        ]
    ),
    (
        "1-0 (a.e.t.)",
        "Spain",
        "Netherlands",
        2010,
        [
            "Iker Casillas",
            "Giovanni van Bronckhorst"
        ]
    ),
    (
        "1-0",
        "Germany",
        "Argentina",
        2014,
        [
            "Philipp Lahm",
            "Lionel Messi"
        ]
    ),
    (
        "4-2",
        "France",
        "Croatia",
        2018,
        [
            "Hugo Lloris",
            "Luka Modric"
        ]
    ),
    (
        "1-0 (a.e.t.)",
        "Italy",
        "England",
        2021,
        [
            "Giorgio Chiellini",
            "Harry Kane"
        ]
    )
]

# Example of accessing the data for the 1930 World Cup final
print("Final score:", games_db[0][0])
print("Winning team:", games_db[0][1])
print("Losing team:", games_db[0][2])
print("Year:", games_db[0][3])
print("Captains:", games_db[0][4])