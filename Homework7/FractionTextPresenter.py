from SimpleFraction import SimpleFraction


class FractionTextPresenter:
    def __init__(self, fraction):
        self.fraction = fraction

    def draw(self):
        print(self.fraction)

    def update_model(self, fraction):
        self.fraction = fraction
        self.update()

    def update(self):
        self.draw()
