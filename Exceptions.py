class InvalidPassword(Exception):
    pass


class TooShortPassword(InvalidPassword):
    pass


class TooLongPassword(InvalidPassword):
    pass


class IncorrectLengthPassword(InvalidPassword):
    pass


class InvalidSymbols(InvalidPassword):
    pass


class AlreadyExist(Exception):
    pass


class EmailAlreadyExist(AlreadyExist):
    pass


class UsernameAlreadyExist(AlreadyExist):
    pass


class VacuumCleanerCrash(Exception):
    pass


class LowBattery(VacuumCleanerCrash):
    pass


class DeadBattery(VacuumCleanerCrash):
    pass


class EmptyWater(VacuumCleanerCrash):
    pass


class FullTrash(VacuumCleanerCrash):
    pass


class WrongInboundData(VacuumCleanerCrash):
    pass
