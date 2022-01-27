from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            favourite_spell: str
    ):
        super().__init__(nickname, musical_instrument)
        self.__favourite_spell = favourite_spell

    def player_info(self):
        return f"Druid {self.nickname}." \
               f" {self.nickname} has a" \
               f" favourite spell: {self.__favourite_spell}"

    def get_rating(self):
        return len(self.__favourite_spell)
