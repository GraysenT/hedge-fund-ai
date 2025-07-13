class ExchangeProtocol:
    def __init__(self, federation):
        self.federation = federation

    def execute(self):
        for civilization in self.federation.civilizations:
            if civilization.population > 0:
                print(f'{civilization.name} survives with {civilization.population} population.')
            else:
                print(f'{civilization.name} has been eliminated.')
